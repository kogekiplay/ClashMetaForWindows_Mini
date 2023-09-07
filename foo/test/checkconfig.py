import os
import yaml
from foo.test.cmd import cmdnoadmin

file = 'config.yaml'

# 检查config.yaml是否存在


def checkexist():
    if os.path.exists(file):
        return True
    else:
        return False

# 校验yaml


def is_valid_yaml(yaml_content):
    try:
        # 尝试加载 YAML 内容
        yaml.safe_load(yaml_content)
        return True
    except yaml.YAMLError as e:
        # 如果出现错误，说明 YAML 内容无效
        return "YAML 校验错误:" + str(e)

# 检查配置文件合法性


def checkyaml():
    command = "cd foo/bin && clash.exe -d ./resources/ -f ../../config.yaml -t"
    output = cmdnoadmin(command)
    output1 = output.find("successful")
    if output1 > 0:
        return True
    else:
        lines = output.split('\n')
        last_lines = lines[-5:]
        output = '\n'.join(last_lines)
        return output

# 替换externel-ui目录,添加tun模式配置


def yaml_mod():
    yaml_data = loadyaml()
    yaml_key_to_remove = [
        'tun', 'external-controller', 'external-ui', 'secret']
    for key in yaml_key_to_remove:
        yaml_data.pop(key, None)
    yaml_data['external-ui'] = '../dashboard'
    tun_data = {'auto-detect-interface': True, 'auto-route': True,
                'dns-hijack': ['0.0.0.0:53'], 'enable': True, 'stack': 'system'}
    yaml_data['tun'] = tun_data
    yaml_data['external-controller'] = '0.0.0.0:9090'
    yaml_data['external-ui'] = '../dashboard'
    try:
        with open(file, "w", encoding='utf-8') as f:
            yaml.dump(yaml_data, f, default_flow_style=False,
                      encoding='utf-8', allow_unicode=True)
        return True
    except:
        return False

# tun模式切换覆写配置


def tun_yaml_mod(status: str):
    yaml_data = loadyaml()
    # print(yaml_data)
    if status == "open":
        tun_open_data = {'auto-detect-interface': True, 'auto-route': True,
                         'dns-hijack': ['0.0.0.0:53'], 'enable': True, 'stack': 'system'}
        yaml_data['tun'] = tun_open_data
    elif status == "close":
        tun_close_data = {'auto-detect-interface': True, 'auto-route': True,
                          'dns-hijack': ['0.0.0.0:53'], 'enable': False, 'stack': 'system'}
        yaml_data['tun'] = tun_close_data
    else:
        return
    try:
        with open(file, "w", encoding='utf-8') as f:
            yaml.dump(yaml_data, f, default_flow_style=False,
                      encoding='utf-8', allow_unicode=True)
        return True
    except:
        return False

# 获取代理端口


def getproxyport():
    yaml_data = loadyaml()
    proxyport = yaml_data["mixed-port"]
    return proxyport

# 获取面板端口


def getuiport():
    yaml_data = loadyaml()
    uiport = yaml_data["external-controller"].split(':')[1]
    return uiport

# 读取yaml文件并返回字典


def loadyaml():
    with open(file, 'rb') as f:
        data = yaml.safe_load(f)
    return data

# if __name__== "__main__" :
#    tun_yaml_mod("close")
