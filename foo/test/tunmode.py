import urllib
import requests
import json
from sys import argv
from winreg import OpenKey, QueryValueEx, SetValueEx
from winreg import HKEY_CURRENT_USER, KEY_ALL_ACCESS
import ctypes
import os,sys,subprocess
from foo.test.checkconfig import getproxyport,getuiport,tun_yaml_mod

proxyport=getproxyport()
PROXIES = {
    'default': {
        'enable': 1,
        'override': f'127.0.0.1;localhost;<local>',
        'server': f'127.0.0.1:{proxyport}'
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
        print(PROXIES[proxy_name]['override'])
        set_key('ProxyOverride', PROXIES[proxy_name]['override'])
        set_key('ProxyServer', PROXIES[proxy_name]['server'])

        # granting the system refresh for settings take effect
        internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
        internet_set_option(0, 37, 0, 0)  # refresh
        internet_set_option(0, 39, 0, 0)  # settings changed
        return True
    except KeyError:
        print(f'Proxy {proxy_name} is not registered in PROXIES')
        return False

def enable_default_proxy():
    return set_proxy('default')

def disable_proxy():
    return set_proxy('off')

# tun/系统代理模式切换
def proxyswitch():
    uiport=getuiport()
    url = f"http://127.0.0.1:{uiport}/configs"
    response = urllib.request.urlopen(url)
    config =  json.loads(response.read())
    tunstatus = config["tun"]["enable"]
    if tunstatus == False:
        paramdata = json.dumps({
            "tun": {
                "enable": True
            }
        })
        controlfirmware() #允许通过Windows防火墙
        response = requests.patch(url,data=paramdata)
        result = response.status_code
        if result == 204:
            disable_proxy()
            tun_yaml_mod("open")
            return True
    elif tunstatus == True:
        paramdata = json.dumps({
            "tun": {
                "enable": False
            }
        })
        response = requests.patch(url,data=paramdata)
        result = response.status_code
        if result == 204:
            enable_default_proxy()
            tun_yaml_mod("close")
            return False


def getclashpath():
    # get the exe file path
    clash_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../bin/clash.exe'))
    return clash_path

# Clash.exe 放行windows防火墙
def controlfirmware():
    clash_path=getclashpath()
    rule_name = "Clash Meta For Windows Mini"
    output = subprocess.check_output(["netsh", "advfirewall", "firewall", "show", "rule", "name="f"{rule_name}"""])
    if b"No rules match the specified criteria." in output:
        addrule(clash_path)
    else:
        # print(f"Rule {rule_name} already exists，将重新添加")
        subprocess.call(["netsh", "advfirewall", "firewall", "delete", "rule", "name=""Clash Meta For Windows Mini"""],stdout=subprocess.DEVNULL)
        addrule(clash_path)

def addrule(clash_path:str):
    if is_admin():
        subprocess.call(["netsh", "advfirewall", "firewall", "add", "rule", "name=""Clash Meta For Windows Mini""", "dir=in", "action=allow", f"program="f"{clash_path}""", "enable=yes", "description=""1"""],stdout=subprocess.DEVNULL)
        #subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule", "name=\"Clash\""])
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# if __name__== "__main__" :
#    enable_default_proxy()