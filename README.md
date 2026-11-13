# 住宅代理 IP 技术知识库 | Residential Proxy Technical Guide

> 面向开发者、跨境业务团队、网络管理员与代理 IP 使用者的中文技术知识库，介绍住宅代理基础、IP 类型识别、静态与动态代理、ASN / ISP、代理协议、网络诊断和产品选型。

**English summary:** A practical knowledge base covering residential proxy concepts, IP classification, proxy protocols, network diagnostics and selection considerations.

本项目由 IPDEEP 整理维护，内容以技术科普和合法网络配置为主。项目不提供代理账号、密码或可直接使用的代理节点，也不保证任何代理 IP 在特定平台上的审核结果、可用性或匿名程度。

## 你可以在这里了解什么？

- 住宅 IP、数据中心 IP 的基本区别与判断边界
- 静态住宅 IP 与动态住宅代理的工作方式和适用场景
- IP 地址、ASN、ISP、地理位置等常见信息
- HTTP、HTTPS 代理与 SOCKS5 协议基础
- IP 质量评估时可以关注的指标
- 代理连接、DNS 和网络问题的基础排查方法
- 根据业务需求选择代理资源时需要考虑的因素

## 文档目录

| 文档 | 内容 |
|---|---|
| [01 代理 IP 基础知识](docs/01-proxy-basics.md) | 代理的基本概念、工作过程与常见术语 |
| [02 住宅 IP 与机房 IP 的区别](docs/02-residential-vs-datacenter.md) | 网络归属、识别方法与判断局限 |
| [03 静态住宅 IP 与动态住宅代理](docs/03-static-vs-dynamic.md) | 地址变化方式、会话与选型考虑 |
| [04 IP 地址识别基础](docs/04-ip-address-identification.md) | IPv4、IPv6、地理位置及数据库差异 |
| [05 ASN 与 ISP 是什么](docs/05-asn-and-isp.md) | 自治系统、运营商和网络归属 |
| [06 HTTP、HTTPS 与 SOCKS5](docs/06-proxy-protocols.md) | 常见代理协议及其差异 |
| [07 IP 质量检测看哪些指标](docs/07-ip-quality-check.md) | 可用性、延迟、归属、风险信号 |
| [08 网络连接诊断](docs/08-network-diagnostics.md) | 连通性、延迟、DNS 与故障排查 |
| [09 如何选择代理资源](docs/09-proxy-selection-guide.md) | 按业务需求评估资源与成本 |

## 快速理解：代理 IP 的基本工作过程

```text
本地应用
   |
   | 代理协议请求
   v
代理服务器 / 代理网络
   |
   | 向目标地址发起连接
   v
目标网站或服务
```

具体的数据路径、DNS 解析位置、认证方式和加密方式取决于代理协议、客户端实现及服务端配置。代理不等同于 VPN，也不会自动为所有应用提供端到端加密。

## 配套示例

`examples/` 目录提供基础命令与代码示例：

- `curl-http-proxy.sh`：通过 HTTP 代理发起测试请求
- `curl-socks5-proxy.sh`：通过 SOCKS5 代理发起测试请求
- `python-ip-check.py`：使用环境变量配置代理并请求公开 IP 信息接口（需要用户自行指定接口）
- `README.md`：示例运行说明

示例使用占位符或环境变量，不包含真实代理凭据。运行前请阅读代码，并替换为自己有权使用的服务配置。

## 常见问题

### 住宅 IP 是否一定比机房 IP 更快？

不一定。速度受线路、路由、带宽、负载、目标服务器位置、网络拥塞等因素影响。IP 类型不能单独决定速度。

### 静态住宅 IP 是否一定不会触发平台风控？

不能保证。平台判断可能涉及账号行为、设备环境、请求模式、IP 历史记录及平台自身策略。任何 IP 类型都不能保证审核通过。

### IP 检测网站的结果为什么不同？

不同检测服务使用的数据源、更新频率、识别规则和检测维度不同。单一网站的结果不能代表完整结论。

### 代理 IP 和 VPN 是一回事吗？

不是。两者在工作层级、客户端覆盖范围、路由方式和管理方式上可能不同，具体取决于产品实现。

## 相关资源

- [IPDEEP 中文官网](https://www.ipdeep.cn/?extendid=zXY2LS)
- [IPDEEP 静态住宅 IP](https://www.ipdeep.cn/static-residence?extendid=zXY2LS)
- [IPDEEP 动态住宅代理](https://www.ipdeep.cn/dynamic-residence?extendid=zXY2LS)
- [IPDEEP 代理配置资源](https://www.ipdeep.cn/integrations?extendid=zXY2LS)
- [ToDetect IP 地址查询](https://www.todetect.net/ip/)

以上链接来自项目 URL 登记库。产品详情页在正式发布前仍应实际检查可访问性、跳转和页面内容；若页面发生变化，请以官网实际地址为准。

## 使用与合规说明

本项目用于网络技术学习、合法业务配置、开发测试和网络质量诊断。请遵守所在地法律法规、网络服务提供方规则以及目标网站的使用条款。不得将本项目用于欺诈、未经授权访问、身份冒用或规避安全控制。

## 参与改进

欢迎提交文档修正、可复现的配置示例和技术问题。提交前请阅读 [贡献指南](CONTRIBUTING.md)，不得提交真实账号密码、API Key、客户信息或其他敏感数据。

## 版本

当前文档版本：**v1.1（中文优先版）**  
更新记录见 [CHANGELOG.md](CHANGELOG.md)。
