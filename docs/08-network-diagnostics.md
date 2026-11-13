# 08. Proxy Network Diagnostics

## 1. Separate endpoint, authentication, and destination failures

A proxy connection can fail because of an invalid hostname, unreachable port, authentication error, IP allowlist mismatch, unsupported protocol, DNS issue, TLS issue, or destination-side failure. Change one variable at a time so that the cause remains identifiable.

## 2. Basic checks

- Confirm the provider endpoint and port from the current account dashboard.
- Confirm the selected protocol.
- Check system clock and TLS certificate validation.
- Confirm that the account is active and within its usage limits.
- Check whether the provider requires source-IP allowlisting.
- Test a known, authorized HTTPS endpoint.

## 3. Use curl for a controlled test

```bash
curl -v --proxy "http://${PROXY_HOST}:${PROXY_PORT}" \
  --proxy-user "${PROXY_USER}:${PROXY_PASS}" \
  https://example.com/ -o /dev/null
```

Verbose output can contain sensitive headers or endpoint details. Redact it before sharing logs.

## 4. Check the observed public IP

Request a public-IP inspection endpoint through the configured proxy and compare it with the direct network path, if direct testing is permitted. The result should show the exit address used for that particular request. Different applications may follow different proxy and DNS settings.

## 5. DNS considerations

DNS resolution may occur locally or remotely depending on the protocol, client, and configuration. For SOCKS5, some clients offer a remote-resolution mode; others resolve hostnames locally. Browser DNS-over-HTTPS, operating-system resolvers, and application-specific networking can further change the result.

## 6. Common symptoms

| Symptom | Possible cause | Next check |
|---|---|---|
| Connection refused | Wrong port or service unavailable | Confirm endpoint and provider status |
| Authentication failed | Incorrect credentials or auth mode | Recheck account credentials and syntax |
| Timeout | Routing, firewall, congestion, or endpoint issue | Test reachability and provider status |
| Name resolution error | DNS configuration or resolver issue | Compare local and remote DNS behavior |
| TLS error | Certificate, clock, interception, or protocol mismatch | Check system time and TLS configuration |
| Unexpected exit IP | Some traffic bypasses proxy or another proxy is active | Inspect application-level proxy settings |

## Safe handling of diagnostic output

Never publish real usernames, passwords, API tokens, customer IPs, or private endpoints. Remove cookies, authorization headers, and identifying data from logs before opening a public issue.
