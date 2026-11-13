#!/usr/bin/env bash
set -euo pipefail

: "${PROXY_HOST:?Set PROXY_HOST to your provider endpoint}"
: "${PROXY_PORT:?Set PROXY_PORT to your provider port}"
: "${PROXY_USER:?Set PROXY_USER to your proxy username}"
: "${PROXY_PASS:?Set PROXY_PASS to your proxy password}"

# --socks5-hostname asks curl to resolve the destination hostname through
# the SOCKS5 proxy. Support depends on the proxy and client configuration.
curl --fail --show-error --silent \
  --socks5-hostname "${PROXY_HOST}:${PROXY_PORT}" \
  --proxy-user "${PROXY_USER}:${PROXY_PASS}" \
  --head "https://example.com/"
