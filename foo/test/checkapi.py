import psutil
from foo.test.tunmode import parse_config_file


def checkinfo(info: str):
    try:
        found = False
        for process in psutil.process_iter():  # 遍历所有进程
            if process.name() == "clash.exe":  # 匹配程序名称
                found = True
                if info == "memory":
                    mem_info = process.memory_info()  # 获取进程的内存信息
                    # 打印物理内存占用（以MB为单位）并加上 "MB" 的单位
                    mem_info = (
                        str(round(mem_info.rss / 1024 / 1024, 2)) + " MB")
                    return mem_info
                elif info == "status":
                    proxy, tun = parse_config_file(mode="read")
                    if proxy == True and tun == False:
                        return "运行中：SysProxy"
                    elif proxy == False and tun == True:
                        return "运行中：Tun"
                    elif proxy == True and tun == True:
                        return "运行中：Multi"
                    else:
                        return "运行中"
                else:
                    return "NaN"
        if not found:
            if info == "memory":
                mem_info = "NaN"
                return mem_info
            elif info == "status":
                status = "已停止"
                return status
            else:
                return "NaN"

    except:
        return "NaN"

# if __name__== "__main__" :
#    checkinfo("memory")
