from foo.test.checkconfig import checkexist, checkyaml, yaml_mod
from foo.test.cmd import cmdnoadmin
from foo.test.tunmode import enable_default_proxy, disable_proxy

# 启动服务


def startservice():
    fileexist = checkexist()
    # 检查config.yaml 是否存在
    if fileexist == True:
        # 修改externel-ui部分
        yamlmod = yaml_mod()
        if yamlmod == True:
            yamloutput = checkyaml()
            # 检查配置文件合法性
            if yamloutput == True:
                command = "cd foo/bin && WinSW.exe install ./Clash-meta.xml && WinSW.exe start ./Clash-meta.xml"
                output = cmdnoadmin(command)
                output1 = output.find("started")
                output2 = output.find("exists")
                if output1 > 0 or output2 > 0:
                    enable_default_proxy()
                    return True
                else:
                    return False
            else:
                return yamloutput

        else:
            return "no permission"
    elif fileexist == False:
        return "not exist"
    else:
        return "error"

# 停止服务并卸载


def stopservice():
    command = "cd foo/bin && WinSW.exe stop ./Clash-meta.xml && WinSW.exe uninstall ./Clash-meta.xml"
    output = cmdnoadmin(command)
    output1 = output.find("stopped")
    output2 = output.find("exist")
    if output1 > 0 or output2 > 0:
        disable_proxy()
        return True
    else:
        return False

# 仅停止服务


def stopserviceonly():
    command = "cd foo/bin && WinSW.exe stop ./Clash-meta.xml"
    output = cmdnoadmin(command)
    output1 = output.find("stopped")
    if output1 > 0:
        disable_proxy()
        return True
    else:
        return False

# 仅启动服务


def startserviceonly():
    fileexist = checkexist()
    # 检查config.yaml 是否存在
    if fileexist == True:
        # 修改externel-ui部分
        yamlmod = yaml_mod()
        if yamlmod == True:
            yamloutput = checkyaml()
            # 检查配置文件合法性
            if yamloutput == True:
                command = "cd foo/bin && WinSW.exe start ./Clash-meta.xml"
                output = cmdnoadmin(command)
                output1 = output.find("started")
                if output1 > 0:
                    enable_default_proxy()
                    return True
                else:
                    return False
            else:
                return yamloutput
        else:
            return "no permission"
    elif fileexist == False:
        return "not exist"
    else:
        return "error"


# if __name__== "__main__" :
#    startservice()
