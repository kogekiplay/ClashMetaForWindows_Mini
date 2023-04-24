import requests
import re

def downlaodconfig(url):
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
            f.write(r.content)
            f.flush()
        return True
    else:
        return False

#if __name__== "__main__" :
#    downlaodconfig()