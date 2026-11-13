# 05. ASN and ISP: What Do They Mean?

## ASN

An Autonomous System Number (ASN) identifies an autonomous system that participates in internet routing. An autonomous system is a network or group of networks managed under a common routing policy. ASNs are used in inter-domain routing, especially BGP.

An IP prefix is announced into the global routing system by an autonomous system. Looking up the ASN can help identify the network responsible for announcing the route, but it does not by itself reveal the physical device, access medium, or exact user location.

## ISP

An Internet Service Provider (ISP) provides internet connectivity or related network services. An IP intelligence database may display an ISP, organization, network owner, or hosting company. These fields may differ because the address can be registered to one entity, announced by another, and used by a downstream customer.

## ASN and ISP are not interchangeable

| Term | What it represents | What it does not prove |
|---|---|---|
| ASN | Routing identity of an autonomous system | Exact device type or user location |
| ISP | Connectivity provider or network organization label | That a particular IP is a residential line |
| Geolocation | Estimated geographic association | Precise physical location |
| Reverse DNS | Published hostname mapping, if any | Definitive network category |

## How to interpret results

Use ASN and ISP as clues. Compare them with registry information, reverse DNS, provider documentation, and more than one IP intelligence source. Be careful with reseller networks, leased address space, mobile carrier networks, and organizations that operate both access and hosting infrastructure.

## Practical notes

- Keep the lookup timestamp with your result.
- Do not infer a user's identity from an ASN.
- Do not treat a commercial “residential” or “datacenter” label as an authoritative registry fact.
- For incident response, use authoritative routing and registry sources and preserve evidence appropriately.
