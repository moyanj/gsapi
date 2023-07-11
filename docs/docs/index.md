# 主页

!!! warning "警告"
    本API还处于开发阶段，请留意 [状态监视页面](https://service.moyanjdc.top/status/ms),以及官方QQ群(群号:769016444)
    
## 服务器地址
   
| 名称 | URL | HTTPS |
|: ----------- |: ----------- |: ----------- :
| 官方 | gsapi.moyanjdc.top/api | 是 |

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
1.该软件可以用于任何目的，不包括商业用途。
2.该软件可以不受任何限制地修改和分发。
3.源代码必须包括在软件的任何分发中。
4.软件的任何分发都必须包括一份许可证的副本。
5.软件的任何分发都必须包括免责声明。
```


<a class="mo-feedback-button" href="/feed">
    <svg width="24" height="24" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M24 44C29.5228 44 34.5228 41.7614 38.1421 38.1421C41.7614 34.5228 44 29.5228 44 24C44 18.4772 41.7614 13.4772 38.1421 9.85786C34.5228 6.23858 29.5228 4 24 4C18.4772 4 13.4772 6.23858 9.85786 9.85786C6.23858 13.4772 4 18.4772 4 24C4 29.5228 6.23858 34.5228 9.85786 38.1421C13.4772 41.7614 18.4772 44 24 44Z" fill="none" stroke="#333" stroke-width="4" stroke-linejoin="round"/>
        <path d="M24 28.6248V24.6248C27.3137 24.6248 30 21.9385 30 18.6248C30 15.3111 27.3137 12.6248 24 12.6248C20.6863 12.6248 18 15.3111 18 18.6248" stroke="#333" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M24 37.6248C25.3807 37.6248 26.5 36.5055 26.5 35.1248C26.5 33.7441 25.3807 32.6248 24 32.6248C22.6193 32.6248 21.5 33.7441 21.5 35.1248C21.5 36.5055 22.6193 37.6248 24 37.6248Z" fill="#333"/>
    </svg>
        提供反馈
</a>