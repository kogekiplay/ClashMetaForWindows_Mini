import os,sys
import subprocess
import win32com.shell.shell as shell

# 此函数使用管理员权限运行cmd指令
def cmdadmin(command: str):
    # 请求管理员权限
    ASADMIN = 'asadmin'
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    output=cmdnoadmin(command)
    return output

# 在cmd中运行命令
def cmdnoadmin(command: str):
    # 获取当前目录的完整路径
    current_dir = os.path.abspath(".")
    cmd_command = command
    cmd = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
    cmd.stdin.write(bytes(f'cd /d "{current_dir}" && {cmd_command}\n', 'utf-8'))
    cmd.stdin.close()
    output = cmd.stdout.read().decode(encoding='utf-8',errors='ignore')
    return output

#if __name__== "__main__" :
#    cmdnoadmin("cd foo/bin && clash.exe -d ./resources/ -f ../../config.yaml -t")
