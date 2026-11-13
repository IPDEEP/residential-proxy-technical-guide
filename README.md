# Residential Proxy Technical Guide

A practical knowledge base covering residential proxy fundamentals, IP network identification, proxy protocols, connection diagnostics, and responsible proxy selection.

**Language:** The initial documentation is primarily in Chinese, with standard English technical terminology retained for searchability and consistency.

**Maintained by IPDEEP** · [Official website](https://www.ipdeep.cn/) · [ToDetect IP lookup](https://www.todetect.net/ip/)

> This repository is an educational and technical reference. It does not promise that any IP address will be classified identically by every database or accepted by any third-party service. Always follow applicable laws, service terms, and network policies.

## What you'll learn

- What a proxy server does and how a proxy connection is routed.
- How residential and datacenter IP addresses differ at a network-allocation level.
- How static and dynamic residential proxy models differ.
- How to interpret IP address, ASN, ISP, and geolocation data.
- When to use HTTP, HTTPS, and SOCKS5 proxy protocols.
- How to test connectivity, DNS behavior, latency, and common failures.
- How to select a proxy service based on workload, stability, cost, and operational requirements.

## Documentation

| Chapter | Topic | File |
|---|---|---|
| 01 | Proxy fundamentals | [01-proxy-basics.md](docs/01-proxy-basics.md) |
| 02 | Residential vs. datacenter IPs | [02-residential-vs-datacenter.md](docs/02-residential-vs-datacenter.md) |
| 03 | Static vs. dynamic residential proxies | [03-static-vs-dynamic.md](docs/03-static-vs-dynamic.md) |
| 04 | IP address identification | [04-ip-address-identification.md](docs/04-ip-address-identification.md) |
| 05 | ASN and ISP | [05-asn-and-isp.md](docs/05-asn-and-isp.md) |
| 06 | Proxy protocols | [06-proxy-protocols.md](docs/06-proxy-protocols.md) |
| 07 | IP quality checks | [07-ip-quality-check.md](docs/07-ip-quality-check.md) |
| 08 | Network diagnostics | [08-network-diagnostics.md](docs/08-network-diagnostics.md) |
| 09 | Proxy selection guide | [09-proxy-selection-guide.md](docs/09-proxy-selection-guide.md) |

## Practical examples

The `examples/` directory contains generic examples using environment variables. Replace the example host, port, username, and password with credentials supplied by your provider. Never commit real credentials, API keys, customer data, or private endpoints.

- [HTTP proxy with curl](examples/curl-http-proxy.sh)
- [SOCKS5 proxy with curl](examples/curl-socks5-proxy.sh)
- [Python connectivity check](examples/python-proxy-check.py)

## Quick start

1. Read [Proxy fundamentals](docs/01-proxy-basics.md).
2. Review [Residential vs. datacenter IPs](docs/02-residential-vs-datacenter.md).
3. Choose a connection protocol in [Proxy protocols](docs/06-proxy-protocols.md).
4. Run a connectivity test using a placeholder configuration.
5. Compare IP and DNS observations using more than one reputable source.

## Important limitations

- IP classification databases can disagree or contain stale records.
- Geolocation is an estimate, not proof of a device's physical location.
- An ASN identifies the network that announces an IP prefix; it does not by itself prove the device type or access technology.
- A residential-looking classification is not a guarantee of quality, exclusivity, anonymity, or acceptance by a website.
- Static does not automatically mean faster; dynamic does not automatically mean slower. Performance depends on routing, congestion, destination, and provider infrastructure.
- Proxy use does not replace application security, endpoint security, or legal review.

## Related resources

- [IPDEEP official website](https://www.ipdeep.cn/) — proxy and VPS service information.
- [IPDEEP English website](https://www.ipdeep.com/).
- [ToDetect IP lookup](https://www.todetect.net/ip/) — inspect publicly observable IP information.
- [ToDetect Chinese website](https://www.todetect.cn/).

Product availability, locations, specifications, prices, and service limits can change. Check the current official product page before making a purchase decision. The registered Chinese product paths for [static residential IP](https://www.ipdeep.cn/static-residence) and [dynamic residential proxy](https://www.ipdeep.cn/dynamic-residence) should be checked for current availability and page status before being used in promotional materials.

## Contributing

Corrections and practical improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Please do not submit private credentials, personal data, or instructions intended to evade law enforcement or platform security controls.

## License

Documentation and examples are released under the MIT License unless a file states otherwise. See [LICENSE](LICENSE).
