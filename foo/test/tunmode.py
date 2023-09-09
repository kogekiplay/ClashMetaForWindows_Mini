import urllib
import requests
import json
import configparser
from sys import argv
from winreg import OpenKey, QueryValueEx, SetValueEx
from winreg import HKEY_CURRENT_USER, KEY_ALL_ACCESS
import ctypes
import os
from foo.test.firmware import FirewallManager
from foo.test.checkconfig import getproxyport, getuiport, tun_yaml_mod

PROXIES = {
    'default': {
        'enable': 1,
        'override': f'127.0.0.1;localhost;<local>',
        'server': '127.0.0.1:7891'
    },
    'off': {
        'enable': 0,
        'override': f'-',
        'server': f'-'
    },
}

INTERNET_SETTINGS = OpenKey(HKEY_CURRENT_USER,
                            r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                            0, KEY_ALL_ACCESS)


def set_key(name, value):
    SetValueEx(INTERNET_SETTINGS, name, 0,
               QueryValueEx(INTERNET_SETTINGS, name)[1], value)


def set_proxy(proxy_name):
    try:
        set_key('ProxyEnable', PROXIES[proxy_name]['enable'])
        set_key('ProxyOverride', PROXIES[proxy_name]['override'])
        set_key('ProxyServer', PROXIES[proxy_name]['server'])

        # granting the system refresh for settings take effect
        internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
        internet_set_option(0, 37, 0, 0)  # refresh
        internet_set_option(0, 39, 0, 0)  # settings changed
        return True
    except KeyError:
        return False


def enable_default_proxy():
    proxyport = getproxyport()
    PROXIES['default']['server'] = f'127.0.0.1:{proxyport}'
    return set_proxy('default')


def disable_proxy():
    return set_proxy('off')


# 修改配置文件的函数，将startup、proxy和tun的值写入config/config.ini
def parse_config_file(mode="write", proxy=True, tun=False):
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    if mode == "write":
        if 'General' not in config:
            config['General'] = {}  # 如果General部分不存在，创建它
        config['General']['proxy'] = str(proxy)
        config['General']['tun'] = str(tun)
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
    elif mode == "read":
        if 'General' in config and 'proxy' in config['General'] and 'tun' in config['General']:
            return config.getboolean('General', 'proxy'), config.getboolean('General', 'tun')
        else:
            # 如果proxy和tun不存在，返回默认值 False
            return False, False
    else:
        return False


# tun/系统代理模式切换
def proxyswitch():
    uiport = getuiport()
    url = f"http://127.0.0.1:{uiport}/configs"
    response = urllib.request.urlopen(url)
    config = json.loads(response.read())
    tunstatus = config["tun"]["enable"]
    if tunstatus == False:
        firewall_manager = FirewallManager()
        enable_firmware = True  # Change this to True or False as needed
        firewall_manager.control_firmware(
            enable=enable_firmware)
        switch_tun_mode(True)
        disable_proxy()
        tun_yaml_mod("open")
        parse_config_file(mode="write", proxy=False, tun=True)
        return True
    elif tunstatus == True:
        switch_tun_mode(False)
        enable_default_proxy()
        tun_yaml_mod("close")
        parse_config_file(mode="write", proxy=True, tun=False)
        return False

    #     paramdata = json.dumps({
    #         "tun": {
    #             "enable": True
    #         }
    #     })
    #     response = requests.patch(url, data=paramdata)
    #     result = response.status_code
    #     if result == 204:
    #         disable_proxy()
    #         tun_yaml_mod("open")
    #         return True
    # elif tunstatus == True:
    #     paramdata = json.dumps({
    #         "tun": {
    #             "enable": False
    #         }
    #     })
    #     response = requests.patch(url, data=paramdata)
    #     result = response.status_code
    #     if result == 204:
    #         enable_default_proxy()
    #         tun_yaml_mod("close")
    #         return False


# 开关tun模式
def switch_tun_mode(tun_enable: False):
    uiport = getuiport()
    uiport = getuiport()
    url = f"http://127.0.0.1:{uiport}/configs"
    paramdata = json.dumps({
        "tun": {
            "enable": tun_enable
        }
    })
    response = requests.patch(url, data=paramdata)
    result = response.status_code
    if result == 204:
        disable_proxy()
        tun_yaml_mod("open")
        return True


def getclashpath():
    # get the exe file path
    clash_path = os.path.normpath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../bin/clash.exe'))
    return clash_path

# if __name__ == "__main__":
