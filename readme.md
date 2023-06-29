# GSAPI
### 本文档由ApiFox复制而来,完整文档请前往[ApiFox](https://mo-genstar.apifox.cn)查看
本API还处于开发阶段，请留意 [状态监视页面](https://service.moyanjdc.top/status/ms)。和[ApiFox](https://mo-genstar.apifox.cn)上的文档
## 请求限制
每ip每秒最多10次
### 封禁ip列表
| ip          | 原因         |
| ----------- | ----------- |
| 192.168.1.1 | 测试         |
| 127.0.01    | 不允许调用自己 |
### 不允许做的事
1. 不允许DDOS
2. 枚举 UID 或大量查询来填充数据库

enka不能做的我们也不能做
## SDK
我们提供了快捷请求本API的SDK
| 平台      | 链接 |
| ----------- | ----------- |
| Python      | [链接](https://service.moyanjdc.top/status/ms)       |
| JavaScript   | [链接](https://service.moyanjdc.top/status/ms)|
| 结绳      | [链接](https://service.moyanjdc.top/status/ms) |
| GO | [链接](https://service.moyanjdc.top/status/ms) |
| Java      | [链接](https://service.moyanjdc.top/status/ms)|

## HTTP 响应状态码

请确保您的应用对此有适当的处理。
```
201 = UID 格式错误
202 = 后端服务器错误
404 = API不存在
503 = 请求频率限制（被我的或者ENKA的服务器）
500 = 服务器错误
```
## 数据结构
参见[ENKA文档](https://api.enka.network/#/api_chs?id=数据结构)