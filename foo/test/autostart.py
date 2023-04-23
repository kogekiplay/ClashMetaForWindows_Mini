import os
import winshell


def getexepath():
        # get the exe file path
        exe_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../CMFW_mini.exe'))
        #兼容测试环境
        # check if the exe file exists
        if not os.path.exists(exe_path):
            # use the py file instead
            exe_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../run.pyw'))
        return exe_path

def add_to_startup(exe_path):
    # get the startup folder path
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    # get the exe file name
    exe_name = os.path.basename(exe_path)
    # get the shortcut file name
    shortcut_name = exe_name + '.lnk'
    # check if the shortcut file already exists in the startup folder
    if not os.path.exists(os.path.join(startup_folder, shortcut_name)):
        # create a shortcut object
        shortcut = winshell.shortcut(exe_path)
        # get the exe folder
        exe_folder = os.path.dirname(exe_path)
        # set the working directory
        shortcut.working_directory = exe_folder
        # save the shortcut to the startup folder
        shortcut.write(os.path.join(startup_folder, shortcut_name))

def remove_from_startup(exe_path):
    # get the startup folder path
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    # get the exe file name
    exe_name = os.path.basename(exe_path)
    # get the shortcut file name
    shortcut_name = exe_name + '.lnk'
    # check if the shortcut file exists in the startup folder
    if os.path.exists(os.path.join(startup_folder, shortcut_name)):
        # remove the shortcut file from the startup folder
        os.remove(os.path.join(startup_folder, shortcut_name))