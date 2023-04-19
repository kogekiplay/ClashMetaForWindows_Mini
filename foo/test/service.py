import os,sys
import subprocess
import win32com.shell.shell as shell


def startservice():
    command = "cd foo/bin && WinSW.exe install ./Clash-meta.xml && WinSW.exe start ./Clash-meta.xml"
    output = cmdadmin(command)
    output1 = output.find("started")
    output2 = output.find("exists")
    if output1 > 0 or output2 > 0:
        return True
    else:
        return False
    
def stopservice():
    command = "cd foo/bin && WinSW.exe stop ./Clash-meta.xml && WinSW.exe uninstall ./Clash-meta.xml"
    output = cmdadmin(command)
    output1 = output.find("stopped")
    output2 = output.find("exist")
    print(output)
    if output1 > 0 or output2 > 0:
        return True
    else:
        return False

def cmdadmin(command: str):
    # 获取当前目录的完整路径
    current_dir = os.path.abspath(".")

    # 请求管理员权限
    ASADMIN = 'asadmin'
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

    # 在cmd中运行命令
    cmd_command = command
    cmd = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    cmd.stdin.write(bytes(f'cd /d "{current_dir}" && {cmd_command}\n', 'utf-8'))
    cmd.stdin.close()
    output = cmd.stdout.read().decode(encoding='utf-8',errors='ignore')
    errors = cmd.stderr.read().decode(encoding='utf-8',errors='ignore')
    print(output)
    print(errors)
    return output
