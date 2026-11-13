# 01. Proxy Fundamentals

## What is a proxy?

A proxy is an intermediary that receives a request from a client and forwards it to another server. The destination generally sees the proxy's network address as the source of the forwarded connection, rather than the client's original public IP address. The exact information visible to the destination depends on the protocol, proxy configuration, application behavior, and any forwarding headers.

A simplified request path is:

```text
Client application -> Proxy endpoint -> Destination server
                         |
                    Authentication
                    and forwarding
```

A proxy does not automatically encrypt every part of a connection. Encryption depends on the protocol and the connection between each pair of endpoints. For example, HTTPS protects application traffic between the client and the HTTPS destination, while the proxy connection itself may use a separate transport and authentication mechanism.

## Common proxy categories

- **Forward proxy:** acts on behalf of clients accessing external services.
- **Reverse proxy:** sits in front of application servers and receives requests on their behalf.
- **Residential proxy:** uses IP addresses associated in network-registration or geolocation datasets with consumer access networks. Classification is database-dependent.
- **Datacenter proxy:** uses IP addresses allocated to hosting, cloud, or data-center networks.
- **Mobile proxy:** routes traffic through mobile network infrastructure.

These labels describe broad network characteristics, not a guarantee of performance or suitability.

## What a proxy does not do

A proxy is not automatically a VPN, firewall, antivirus product, or identity-protection system. It does not make a user anonymous, remove malware, secure a compromised device, or authorize access to restricted resources. Applications may also use direct connections for some traffic unless configured to use the proxy consistently.

## When a proxy may be useful

Legitimate use cases include testing a website from different network regions, validating localization, checking public-facing content delivery, debugging network routing, and managing authorized enterprise connectivity. Use only systems and data that you are authorized to access.

## Checklist before use

1. Confirm the business and legal purpose.
2. Check the provider's acceptable-use policy and service limits.
3. Confirm supported protocols and authentication methods.
4. Test DNS behavior and application compatibility.
5. Store credentials securely and rotate them when needed.
6. Monitor latency, errors, and availability over time.
