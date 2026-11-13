# 06｜HTTP、HTTPS 与 SOCKS5 代理有什么区别？

代理协议决定客户端如何与代理服务建立连接、传递请求以及进行认证。配置前必须确认服务端和客户端支持的协议。

## 1. HTTP 代理

HTTP 代理能够理解 HTTP 请求。访问普通 HTTP 目标时，客户端通常通过代理发送请求；访问 HTTPS 目标时，常见方式是使用 `CONNECT` 建立隧道。

示例形式：

```text
http://proxy.example.net:10000
```

这里的 `http://` 表示客户端到代理端点的连接协议，不代表目标网站只能使用 HTTP。

## 2. HTTPS 代理

部分代理端点支持客户端先与代理建立 TLS 连接。客户端是否支持 HTTPS proxy URL，需要查看对应工具或库的文档。

不能默认所有 HTTP 代理端点都支持 TLS 到代理端的连接。

## 3. SOCKS5

SOCKS5 是通用代理协议，常用于转发 TCP 连接。它本身不负责理解 HTTP 请求内容。

常见形式：

```text
socks5://proxy.example.net:10000
socks5h://proxy.example.net:10000
```

在支持这两种写法的客户端中，通常：

- `socks5://`：由本地客户端解析目标域名；
- `socks5h://`：将目标域名交由代理侧解析。

具体行为取决于客户端实现。

## 4. 对比表

| 维度 | HTTP 代理 | HTTPS 代理 | SOCKS5 |
|---|---|---|---|
| 理解 HTTP 请求 | 是 | 是 | 否 |
| 转发 HTTPS 目标 | 常见方式为 CONNECT | 常见方式为 CONNECT | 可转发 TCP |
| 客户端到代理的 TLS | 不代表支持 | 支持时可建立 | SOCKS5 本身不提供 |
| DNS 行为 | 取决于客户端 | 取决于客户端 | 取决于客户端模式 |
| 应用支持 | 视应用而定 | 视应用而定 | 视应用而定 |

## 5. 如何选择？

1. 查看服务提供方给出的协议类型。
2. 查看目标软件是否支持对应协议。
3. 确认认证方式和 DNS 行为。
4. 用非敏感请求测试。
5. 记录客户端版本和测试结果。

## 相关文档

- [curl 代理测试示例](../examples/curl-http-proxy.sh)
- [网络连接诊断](08-network-diagnostics.md)
- [IPDEEP 代理配置资源](https://www.ipdeep.cn/integrations?extendid=zXY2LS)
