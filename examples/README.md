# 示例文件说明

本目录提供基础代理连接示例：

- `curl-http-proxy.sh`：HTTP 代理请求测试。
- `curl-socks5-proxy.sh`：SOCKS5 代理请求测试。
- `python-ip-check.py`：Python Requests 代理请求示例。

## 运行前准备

1. 安装 curl；Python 示例需要 Python 3 和 `requests`。
2. 使用服务提供方明确支持的代理协议。
3. 在本地环境设置代理变量。
4. 不要把真实账号密码写进脚本或提交到 GitHub。

安装 Python 依赖：

```bash
python -m pip install requests
```

示例中的目标地址仅用于演示。若需查询出口 IP，请自行配置可信、获准使用的公开 IP 查询接口。
