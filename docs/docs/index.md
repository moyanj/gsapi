# 主页

!!! warning "警告"
    本API还处于开发阶段，请留意 [状态监视页面](https://service.moyanjdc.top/status/ms),以及官方QQ群(群号:769016444)
## 服务器地址
   
| 名称 | URL | HTTPS | 状态 |
|: ----------- |: ----------- |: ----------- |: -------- :
| 官方 | gsapi.moyanjdc.top | 是 | 失败 |

## 限制
1.每ip每秒最多50次
<br>
2. 不允许DDOS
<br>
3. 枚举 UID 或大量查询来填充数据库

## HTTP 响应状态码

请确保您的应用对此有适当的处理。
```
201 = UID 格式错误(崩坏:星穹铁道没有该错误码)
202 = 后端服务器错误
404 = API不存在
503 = 请求频率限制（被我的或者后端服务器）
500 = 服务器错误
```

## SDK
我们提供了快捷请求本API的SDK

平台      | 链接 |
: ----------- |: ----------- :
 Python      | [链接](https://service.moyanjdc.top/status/ms)       
 JavaScript   | [链接](https://service.moyanjdc.top/status/ms)
 结绳      | [链接](https://service.moyanjdc.top/status/ms) 
 GO | [链接](https://service.moyanjdc.top/status/ms) 
 Java      | [链接](https://service.moyanjdc.top/status/ms)
 
 
## License

```
1.该软件可以用于任何目的，包括商业用途。
2.该软件可以不受任何限制地修改和分发。
3.源代码必须包括在软件的任何分发中。
4.软件的任何分发都必须包括一份许可证的副本。
5.软件的任何分发都必须包括免责声明。
```