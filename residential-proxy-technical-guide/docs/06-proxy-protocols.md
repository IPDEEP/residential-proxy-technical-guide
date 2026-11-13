# 06. HTTP, HTTPS, and SOCKS5 Proxy Protocols

## HTTP proxy

An HTTP proxy understands HTTP request semantics. For an ordinary HTTP request, the client can send an absolute-form request target to the proxy. For an HTTPS destination, clients commonly use the HTTP `CONNECT` method to establish a tunnel through the proxy, after which TLS is negotiated with the destination.

## HTTPS proxy endpoint

The term “HTTPS proxy” commonly means that the client-to-proxy connection itself is protected with TLS. This is distinct from using an HTTP proxy to tunnel an HTTPS connection to a destination. Confirm the provider's exact terminology and supported endpoint scheme.

## SOCKS5

SOCKS5 is a proxy protocol that can relay TCP connections and, where supported, UDP traffic. It is not limited to HTTP application traffic. Authentication methods and DNS handling depend on the client and server configuration.

## Comparison

| Feature | HTTP proxy | HTTPS proxy endpoint | SOCKS5 |
|---|---|---|---|
| Protocol awareness | HTTP-aware | HTTP-aware over TLS to proxy | Lower-level proxy negotiation |
| Typical use | Web requests | Protected client-to-proxy connection | Applications supporting SOCKS |
| HTTPS destination | Commonly via CONNECT | Commonly via CONNECT over TLS-to-proxy | Relays the TCP connection |
| DNS behavior | Client-dependent | Client-dependent | Client-dependent; remote resolution must be supported and selected |

## Generic curl examples

HTTP proxy:

```bash
curl --proxy "http://${PROXY_HOST}:${PROXY_PORT}" \
  --proxy-user "${PROXY_USER}:${PROXY_PASS}" \
  https://example.com/ -I
```

SOCKS5 with hostname resolution through the proxy, when supported:

```bash
curl --socks5-hostname "${PROXY_HOST}:${PROXY_PORT}" \
  --proxy-user "${PROXY_USER}:${PROXY_PASS}" \
  https://example.com/ -I
```

Set the variables in your shell or secret manager. Do not paste real credentials into source files, screenshots, public issues, or shell history. For a runnable template, see the `examples/` directory.

## Troubleshooting checklist

- Confirm the endpoint hostname and port.
- Confirm whether the endpoint expects HTTP, HTTPS, or SOCKS5.
- Verify username/password format and IP allowlisting requirements.
- Check whether the client supports the selected authentication method.
- Test DNS behavior separately.
- Compare the result with a direct connection where policy permits.
