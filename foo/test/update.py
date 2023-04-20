# 导入requests和zipfile模块
import requests
import zipfile
import os
import shutil

# 更新yacd-meta
def updateyacd():
    try:
        # 定义压缩包的URL和保存路径
        zip_file_url = "https://github.com/kogekiplay/Yacd-meta/archive/refs/heads/gh-pages.zip"
        save_path = "yacd.zip"
        # 使用requests模块下载压缩包
        r = requests.get(zip_file_url)
        with open(save_path, "wb") as f:
            f.write(r.content)
        # 使用zipfile模块解压压缩包到新建文件夹
        with zipfile.ZipFile(save_path, "r") as z:
            z.extractall("tmp")
        # 删除压缩包
        os.remove(save_path)
        # 定义源文件夹和目标文件夹的路径
        src_dir = "tmp/Yacd-meta-gh-pages/"
        dst_dir = "foo/bin/dashboard/"
        shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
        shutil.rmtree("tmp")
        return True
    except:
        return False

# 更新Clash Meta Alpha核心
def updatecore():
    try:
        download_url = "https://github.com/MetaCubeX/Clash.Meta/releases/download"
        response = requests.get("https://api.github.com/repos/MetaCubeX/Clash.Meta/releases/tags/Prerelease-Alpha")
        download_version = response.json()["assets"][0]["name"].split("arm64-")[1].split(".gz")[0]
        os.makedirs("./tmp", exist_ok=True)
        file_name = f"clash.meta-windows-amd64-{download_version}.zip"
        file_path = os.path.join("./tmp", file_name)
        r = requests.get(f"{download_url}/Prerelease-Alpha/{file_name}", stream=True)
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("tmp")
        return True
    except:
        return False

def replacecore():
    try:
        shutil.move("tmp/clash.meta-windows-amd64.exe","tmp/clash.exe")
        shutil.move("tmp/clash.exe","foo/bin/clash.exe")
        shutil.rmtree("tmp")
        return True
    except:
        return False