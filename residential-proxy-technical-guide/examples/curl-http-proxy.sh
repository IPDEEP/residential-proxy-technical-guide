#!/usr/bin/env bash
set -euo pipefail

: "${PROXY_HOST:?Set PROXY_HOST to your provider endpoint}"
: "${PROXY_PORT:?Set PROXY_PORT to your provider port}"
: "${PROXY_USER:?Set PROXY_USER to your proxy username}"
: "${PROXY_PASS:?Set PROXY_PASS to your proxy password}"

# Generic HTTP proxy test. Replace example.com with an endpoint you are
# authorized to test. Avoid enabling shell tracing when handling credentials.
curl --fail --show-error --silent \
  --proxy "http://${PROXY_HOST}:${PROXY_PORT}" \
  --proxy-user "${PROXY_USER}:${PROXY_PASS}" \
  --head "https://example.com/"
