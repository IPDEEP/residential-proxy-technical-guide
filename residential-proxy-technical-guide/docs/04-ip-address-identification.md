# 04. Understanding Public IP Address Information

## What can an IP lookup show?

Depending on the data source, an IP lookup may return:

- Public IPv4 or IPv6 address observed by the service.
- Autonomous System Number (ASN).
- Network or organization name.
- Country, region, or city estimate.
- Reverse DNS hostname, if published.
- Network category or risk indicators from a commercial database.

Not every field is available for every address, and values can be incomplete or outdated.

## Public and private addresses

Private addresses are used inside local networks and are not globally routed on the public internet. Common IPv4 private ranges are:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

Loopback (`127.0.0.0/8`) and link-local (`169.254.0.0/16`) ranges also have special purposes. IPv6 has its own special-use and unique-local ranges. A local device's private address is not the same as the public address observed by a remote service.

## Why geolocation is approximate

IP geolocation databases infer location from registration information, network observations, commercial datasets, and other signals. The result may point to an ISP's registered office, a regional gateway, or an approximate service area. It should not be used as proof of a person's precise physical location.

## A repeatable lookup process

1. Query the public IP from the same application path you want to inspect.
2. Record the time, network, and test endpoint.
3. Check ASN and organization.
4. Compare country and region estimates across sources.
5. Repeat after network changes or provider reassignment.
6. Avoid publishing personal IP addresses or other identifying details without authorization.

For a basic public-IP inspection, see [ToDetect IP lookup](https://www.todetect.net/ip/). Interpret its output together with other evidence and the service's own methodology.
