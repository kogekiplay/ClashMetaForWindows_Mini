import os
import yaml
from foo.test.cmd import cmdnoadmin

file='config.yaml'

# 检查config.yaml是否存在
def checkexist():
    if os.path.exists(file):
        return True
    else:
        return False

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

# 替换externel-ui目录
def externaluimod():
    yaml_data=loadyaml()
    #print(yaml_data)
    yaml_data.setdefault('external-ui','../dashboard')
    yaml_data.setdefault('external-controller','0.0.0.0:9090')
    yaml_data['external-ui']='../dashboard'
    try:
        with open(file, "w",encoding='utf-8') as f:
            yaml.dump(yaml_data, f,default_flow_style=False,encoding='utf-8',allow_unicode=True)
        return True
    except:
        return False

#获取代理端口
def getproxyport():
    yaml_data=loadyaml()
    proxyport=yaml_data["mixed-port"]
    return proxyport

#获取面板端口
def getuiport():
    yaml_data=loadyaml()
    uiport=yaml_data["external-controller"].split(':')[1]
    return uiport

# 读取yaml文件并返回字典
def loadyaml():
    with open(file,'rb') as f:
        data = yaml.safe_load(f)
    return data