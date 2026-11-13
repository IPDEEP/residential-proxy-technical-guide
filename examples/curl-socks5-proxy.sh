#!/usr/bin/env bash
set -euo pipefail

: "${SOCKS_PROXY:?请先设置 SOCKS_PROXY 环境变量}"

# 若客户端和服务端支持，可使用 socks5h:// 由代理侧解析目标域名。
curl \
  --proxy "$SOCKS_PROXY" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
