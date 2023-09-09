import os
import subprocess
import ctypes
import sys


class FirewallManager:

    def __init__(self, rule_name="Clash Meta For Windows Mini"):
        self.clash_path = self.get_clash_path()
        self.rule_name = rule_name

    def get_clash_path(self):
        clash_path = os.path.normpath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '../bin/clash.exe'))
        return clash_path

    def check_firmware_status(self):
        command = ["netsh", "advfirewall", "firewall",
                   "show", "rule", "name="f"{self.rule_name}"""]
        try:
            subprocess.run(command, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False

    def control_firmware_rule(self, enable=True, status="add"):
        command = ["netsh", "advfirewall", "firewall", status, "rule",
                   "name="f"{self.rule_name}""", "dir=in", "action=allow",
                   "program="f"{self.clash_path}""", "enable=yes", "description=""1"""]

        if self.is_admin():
            try:
                subprocess.run(command, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
                return True
            except subprocess.CalledProcessError:
                return False
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, __file__, None, 1)

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def control_firmware(self, enable=True):
        status = self.check_firmware_status()
        if enable and not status:
            return self.control_firmware_rule(enable=True)
        elif not enable and status:
            return self.control_firmware_rule(enable=False, status="delete")
        return None
