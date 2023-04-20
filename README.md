Demo:

<img width="203" alt="image" src="https://user-images.githubusercontent.com/46434871/233369891-56dba6f1-529b-4248-a922-6cb9928e65c5.png">

**Full Changelog**: https://github.com/kogekiplay/ClashMetaForWindows_Mini/compare/1.1...1.31

### 1.3变化：

- 添加了更多不同情况下的错误提示，更好引导首次配置
- 覆写 `external-ui` 目录防止因yacd目录不正确导致启动失败
- 支持更新 yacd-meta 面板
- 支持更新到最新 CLash Meta Alpha 核心
- 现在tun/代理切换将读取配置文件中的值，请配置`mixed-port`
- 支持调用默认浏览器打开yacd面板
- 修复uac弹窗3次的问题
- Geosite和Geoip请手动下载，内置foo/bin/resources为自用lite版本

### 配置说明：
- 将 `config.yaml.example` 重命名为 `config.yaml `
- 修改成你自己的配置文件再启动
- Geosite和Geoip请手动下载，并放到 `foo/bin/resources `目录
- 推荐的Geo资源下载地址：

geoip.dat:
- https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geoip.dat

country.mmdb:
- https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/country.mmdb

eosite.dat
- https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geosite.dat


下载链接：
https://github.com/kogekiplay/ClashMetaForWindows_Mini/releases
