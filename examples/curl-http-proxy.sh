#!/usr/bin/env bash
set -euo pipefail

: "${HTTP_PROXY:?请先设置 HTTP_PROXY 环境变量}"

curl \
  --proxy "$HTTP_PROXY" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
