# 部署
## 运行
### 使用Docker
如果您使用 Docker 部署 GSAPI 那将会十分的简单，您可以使用我们提供的一键脚本。

!!! warning "注意"
    您需要先确定自己已经安装了 Docker 和 cURL

一键脚本：

```bash
bash <(curl -s -L https://doc.gsapi.moyanjdc.top/src/ins.sh)
```
它将运行在8080端口，您就可以使用自己的 GSAPI 了。
### 使用真机部署

您首先需要获取GSAPI的源码，您可以选择下载最新的开发版源码，但我们更建议您下载正式版，因为它的bug会更少，会更稳定。

- 下载正式版

```bash
git clone --branch v1.1.0 https://github.com/moyanj/gsapi.git
```

- 下载开发版

```bash
git clone https://github.com/moyanj/gsapi.git
```

您下载完 GSAPI 源码后，您需要运行以下这条命令以进行安装依赖包。
```bash
pip install -r requirements.txt
```

一切都完毕后，你就可以运行此条命令来运行 GSAPI。
!!! warning "注意"
    您需要在源码根目录下运行

```bash
gunicorn app:app
```
它将在6475端口开启服务
## 配置
您可以使用我们提供的命令来配置，当然您也可以使用 SQLiteStudio 等软件直接修改 GSAPI 的数据库，在[开发](development.md)一章里，您可以找到方法。

### 命令格式
```bash
flask conf [项] [值]
```

 项 | 可选的值 | 意义 |
: ----------- |: ----------- |: ----------- :
 port | 1~65535 | 运行端口 |      
 host | IP | 监听IP |
 CDN | 任何字符 | 获取真实IP的header |
 chat.maxBit | 0~16384 | AI对话最大长度(bit) (暂无用)|
 log.level | INFO,DEBUG,ERROR | 日志等级 |
 cache.ttl | 任何数 | 缓存时间 |
 
### port
- 作用：修改程序运行端口
- 示例：
```bash
flask conf port 1145
```
### host
- 作用：更改程序监听地址，若想监听公网，则设为0.0.0.0
- 示例；
```bash
flask conf host 127.0.0.1
```
### CDN
!!! warning "警告⚠"
    本项即将变换作用！
    
- 作用：当您使用了CDN，程序获取用户真实IP的请求头
- 示例：
```bash
flask conf CDN X-Forwarded-For
```
### log.level
- 作用：日志等级，可以设为DEBUG, INFO, WARNING, ERROR或CRITICAL。
- 示例：
```bash
flask conf log.level ERROR
```
### cache.ttl
- 作用：设置数据缓存时间(秒)
- 示例
```bash
flask conf cache.ttl 1
```


<a class="mo-feedback-button" href="/feed">
    <svg width="24" height="24" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M24 44C29.5228 44 34.5228 41.7614 38.1421 38.1421C41.7614 34.5228 44 29.5228 44 24C44 18.4772 41.7614 13.4772 38.1421 9.85786C34.5228 6.23858 29.5228 4 24 4C18.4772 4 13.4772 6.23858 9.85786 9.85786C6.23858 13.4772 4 18.4772 4 24C4 29.5228 6.23858 34.5228 9.85786 38.1421C13.4772 41.7614 18.4772 44 24 44Z" fill="none" stroke="#333" stroke-width="4" stroke-linejoin="round"/>
        <path d="M24 28.6248V24.6248C27.3137 24.6248 30 21.9385 30 18.6248C30 15.3111 27.3137 12.6248 24 12.6248C20.6863 12.6248 18 15.3111 18 18.6248" stroke="#333" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M24 37.6248C25.3807 37.6248 26.5 36.5055 26.5 35.1248C26.5 33.7441 25.3807 32.6248 24 32.6248C22.6193 32.6248 21.5 33.7441 21.5 35.1248C21.5 36.5055 22.6193 37.6248 24 37.6248Z" fill="#333"/>
    </svg>
        提供反馈
</a>