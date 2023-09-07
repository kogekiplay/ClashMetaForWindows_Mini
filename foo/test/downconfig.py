import requests
import re
import subprocess
from foo.test.checkconfig import is_valid_yaml


def download_config(url):
    # 定义一个正则表达式，匹配http或https开头的url
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(url):
        headers = {
            "User-Agent": "Clash Meta For Windows Mini/1.0 (Prefer ClashMeta Format)"
        }
        try:
            r = requests.get(url=url, headers=headers)
            r.raise_for_status()  # 检查是否有HTTP错误
        except requests.exceptions.RequestException as e:
            return f"无法下载配置文件，请检查你的网络信息！\n错误信息:\n{e}"
        file_path = "config.yaml"
        with open(file_path, "wb") as f:
            yaml_content = r.content
            status = is_valid_yaml(yaml_content)
            if status == True:
                f.write(yaml_content)
                f.flush()
            else:
                return status

        return True
    else:
        return False


def open_config():
    # 使用默认应用打开 config.yaml
    try:
        subprocess.Popen(
            ["start", "config.yaml"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except Exception as e:
        print("无法打开文件:", e)

# if __name__== "__main__" :
#    download_config()
