import urllib
import requests
import json
import winreg
import ctypes
import os,sys
from foo.test.checkconfig import getproxyport,getuiport

# 如果从来没有开过代理 有可能健不存在 会报错
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                   r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                   0, winreg.KEY_ALL_ACCESS)
# 设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

def set_key(name, value):
    # 修改键值
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

# 启用代理
def start():
    stop()  # 先关闭代理,请求的代理一般来自api,如果前一个代理ip失效或者没加入白名单,会请求失败
    proxyport=getproxyport()
    set_key('ProxyEnable', 1)  # 启用
    set_key('ProxyOverride', u'*.local;<local>')  # 绕过本地
    set_key('ProxyServer', u'127.0.0.1:{0}'.format(proxyport))  # 代理IP及端口，将此代理修改为自己的代理IP
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)


def stop():
    # 停用代理
    set_key('ProxyEnable', 0)  # 停用
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

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
            stop()
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
            start()
            return False


def getclashpath():
    # get the exe file path
    clash_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../bin/clash.exe'))
    return clash_path

# Clash.exe 放行windows防火墙
def controlfirmware():
    clash_path=getclashpath()
    rule_name = "Clash Meta For Windows Mini"
    output = os.popen(f"netsh advfirewall firewall show rule name=\"{rule_name}\"").read()
    if "No rules match the specified criteria." in output:
        addrule(clash_path)
    else:
        # print(f"Rule {rule_name} already exists，将重新添加")
        os.system(f"netsh advfirewall firewall delete rule name=\"Clash Meta For Windows Mini\"")
        addrule(clash_path)

def addrule(clash_path:str):
    if is_admin():
        os.system(f"netsh advfirewall firewall add rule name=\"Clash Meta For Windows Mini\" dir=in action=allow program=\"{clash_path}\" enable=yes description=\"1\"")
        #os.system(f"netsh advfirewall firewall delete rule name=\"Clash\"")
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#if __name__== "__main__" :
#    controlfirmware()