#!/usr/bin/env python3
"""通过环境变量配置代理，并请求用户自行指定的公开 IP 信息接口。

默认目标为 example.com，仅用于演示连接请求。若要查询出口 IP，
请将 PROXY_TEST_URL 设置为你信任且获准使用的 IP 查询 API。
"""

import os
import sys
import requests


def main() -> int:
    target = os.environ.get("PROXY_TEST_URL", "https://example.com/")
    proxies = {}

    http_proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
    https_proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")

    if http_proxy:
        proxies["http"] = http_proxy
    if https_proxy:
        proxies["https"] = https_proxy

    if not proxies:
        print("请先设置 HTTP_PROXY 和/或 HTTPS_PROXY 环境变量。")
        return 2

    try:
        response = requests.get(target, proxies=proxies, timeout=(10, 30))
        print(f"请求完成，HTTP 状态码：{response.status_code}")
        print(f"最终 URL：{response.url}")
        print("未输出代理凭据或完整代理 URL。")
        return 0
    except requests.exceptions.ProxyError:
        print("代理连接或协议协商失败，请检查端点和认证配置。")
    except requests.exceptions.ConnectTimeout:
        print("连接超时，请检查网络、主机和端口。")
    except requests.exceptions.ReadTimeout:
        print("读取响应超时。")
    except requests.exceptions.RequestException:
        print("请求失败，请在本地安全环境中检查诊断信息。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
