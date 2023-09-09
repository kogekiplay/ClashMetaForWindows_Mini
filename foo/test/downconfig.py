import requests
import re
import os
import yaml
import subprocess
from foo.test.checkconfig import is_valid_yaml, loadyaml

headers = {
    "User-Agent": "Clash Meta For Windows Mini/1.0 (Prefer ClashMeta Format)"
}


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


def download_provider(url, name):
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()  # 检查是否有HTTP错误
    except requests.exceptions.RequestException as e:
        return f"无法下载你的proxy provider，请检查你的网络信息！\n错误信息:\n{e}"
    base_directory = "./foo/bin/resources"
    providers_directory = os.path.join(base_directory, "proxy-providers")
    file_name = f"{name}.yaml"
    file_path = os.path.join(providers_directory, file_name)
    os.makedirs(providers_directory, exist_ok=True)
    with open(file_path, "wb") as f:
        yaml_content = r.content
        status = is_valid_yaml(yaml_content)
        if status == True:
            f.write(yaml_content)
            f.flush()
            return True
        else:
            return status


def download_all_providers():
    yaml_data = loadyaml()
    if 'proxy-providers' in yaml_data:
        # 遍历所有键名并调用download_provider函数
        provider_names = yaml_data["proxy-providers"].keys()
        for name in provider_names:
            url = yaml_data["proxy-providers"][name]["url"]
            result = download_provider(url, name)
            if result:
                yaml_data["proxy-providers"][name]["path"] = f"./proxy-providers/{name}.yaml"
                try:
                    with open('config.yaml', "w", encoding='utf-8') as f:
                        yaml.dump(yaml_data, f, default_flow_style=False,
                                  encoding='utf-8', allow_unicode=True)
                except:
                    return False
                continue
            else:
                return False
    return True


def open_config():
    # 使用默认应用打开 config.yaml
    try:
        subprocess.Popen(
            ["start", "config.yaml"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except Exception as e:
        pass
# if __name__== "__main__" :
#    download_config()
