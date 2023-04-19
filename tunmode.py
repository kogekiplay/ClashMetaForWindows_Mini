import urllib
import requests
import json
import winreg
import ctypes

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
    set_key('ProxyEnable', 1)  # 启用
    set_key('ProxyOverride', u'*.local;<local>')  # 绕过本地
    set_key('ProxyServer', u'127.0.0.1:7890')  # 代理IP及端口，将此代理修改为自己的代理IP
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    print('系统代理已开启')


def stop():
    # 停用代理
    set_key('ProxyEnable', 0)  # 停用
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

def proxyswitch():
    url = "http://127.0.0.1:9090/configs"
    response = urllib.request.urlopen(url)
    config =  json.loads(response.read())
    tunstatus = config["tun"]["enable"]
    if tunstatus == False:
        paramdata = json.dumps({
            "tun": {
                "enable": True
            }
        })
        response = requests.patch(url,data=paramdata)
        result = response.status_code
        if result == 204:
            stop()
            print("操作成功，tun模式已开启,系统代理已关闭")
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
            print("操作成功，tun模式已关闭，系统代理已开启")
            return False

    

