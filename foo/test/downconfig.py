import requests
import re
import subprocess
from foo.test.checkconfig import is_valid_yaml

def download_config(url):
    # 定义一个正则表达式，匹配http或https开头的url
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(url):
        headers = {
            "User-Agent": "Clash Meta For Windows Mini/1.0 (Prefer ClashMeta Format)"
        }
        r = requests.get(url=url, headers=headers)
        file_path="config.yaml"
        with open(file_path, "wb") as f:
            yaml_content= r.content
            status = is_valid_yaml(yaml_content)
            if status == True:
                f.write(yaml_content)
                f.flush()
            else:
                return status
        # 打开文件使用系统默认程序
        try:
            subprocess.Popen(["start", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        except Exception as e:
            print("Error opening file:", e)
        return True
    else:
        return False

#if __name__== "__main__" :
#    download_config()