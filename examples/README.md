# 示例文件说明

本目录提供基础代理连接示例和本地 IP 列表检查工具：

- `curl-http-proxy.sh`：HTTP 代理请求测试；
- `curl-socks5-proxy.sh`：SOCKS5 代理请求测试；
- `python-ip-check.py`：Python Requests 代理请求示例；
- `ip-list-audit.py`：使用 Python 标准库检查 IP 列表格式、地址范围类别和重复项，并导出 CSV。

## IP 列表检查工具

无需安装第三方依赖，要求 Python 3.10 或更高版本：

```bash
python examples/ip-list-audit.py ips.txt
python examples/ip-list-audit.py ips.txt --output reports/ip-audit.csv
```

输入文件每行一个 IPv4 或 IPv6 地址，空行和 `#` 注释会被忽略。工具仅做本地地址解析和范围分类，不会联网查询，也不能判断住宅、移动、ISP 或数据中心属性。

详细说明见 [批量 IP 地址检查工具](../docs/10-ip-list-audit.md)。

## 运行代理请求示例前

1. 安装 curl；Python Requests 示例需要 Python 3 和 `requests`。
2. 使用服务提供方明确支持的代理协议。
3. 在本地环境设置代理变量。
4. 不要把真实账号密码写进脚本或提交到 GitHub。

安装 Python Requests 依赖：

```bash
python -m pip install requests
```

示例中的目标地址仅用于演示。若需查询出口 IP，请自行配置可信、获准使用的公开 IP 查询接口。
