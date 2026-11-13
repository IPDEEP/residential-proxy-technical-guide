"""Basic proxy connectivity check using environment variables.

Install dependency: python -m pip install requests
Set PROXY_URL in your environment. Example formats:
  http://username:password@proxy.example:8080
  socks5h://username:password@proxy.example:1080  (requires requests[socks])

Never hard-code credentials or commit a real proxy URL.
"""

import os
import sys
import requests

proxy_url = os.environ.get("PROXY_URL")
if not proxy_url:
    sys.exit("Set PROXY_URL in your environment; do not put credentials in this file.")

proxies = {"http": proxy_url, "https": proxy_url}
try:
    response = requests.get(
        "https://api.ipify.org?format=json",
        proxies=proxies,
        timeout=20,
    )
    response.raise_for_status()
    print("Proxy request succeeded.")
    print("Observed response:", response.json())
except requests.RequestException as exc:
    # Exception strings can contain endpoint details. Review before sharing.
    print(f"Proxy request failed: {type(exc).__name__}")
    sys.exit(1)
