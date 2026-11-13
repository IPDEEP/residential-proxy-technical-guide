# 03. Static vs. Dynamic Residential Proxies

## Definitions

A **static residential proxy** provides a persistent or long-lived exit IP for the period and conditions defined by the provider. The address may remain assigned to a customer or session for an extended time, but exact retention and replacement rules vary.

A **dynamic residential proxy** selects an exit IP from a pool. The address may change between requests, sessions, or after a configured interval, depending on the provider's rotation model.

The terms describe allocation behavior. They do not independently define speed, anonymity, geographic accuracy, or quality.

## Comparison

| Dimension | Static residential | Dynamic residential |
|---|---|---|
| Exit IP | Intended to remain stable | Selected from a rotating pool |
| Continuity | Useful when a workflow requires a consistent endpoint | Useful when a workflow legitimately requires multiple exit addresses |
| Billing | May be per IP and time period | May be traffic-based or another provider-defined model |
| Operational concern | Address replacement and long-term health | Rotation rules, session duration, and traffic consumption |
| Best evaluation method | Test persistence and connection quality over time | Test pool behavior, session controls, and consumption |

## How to choose

Consider static allocation when an authorized application requires a stable network endpoint, predictable allowlisting, or continuity during a long-running workflow.

Consider dynamic allocation when authorized testing requires sampling multiple network exits or when the provider's traffic-based model better matches variable usage.

Neither model is universally better. Measure the workload rather than relying on labels.

## Cost calculation

For a per-IP monthly plan:

```text
Monthly cost = Number of IPs × Monthly price per IP
```

For a traffic-based plan:

```text
Estimated cost = Billable traffic (GB) × Price per GB
```

Check whether the provider bills uploaded and downloaded traffic, rounds usage, applies minimum charges, or has separate session and bandwidth limits. Do not assume a quoted starting price applies to every region or plan.

## Questions to ask a provider

- How long can an IP remain assigned?
- Can a session be kept stable, and what ends the session?
- What causes an IP to be replaced?
- How is traffic measured and rounded?
- Which protocols and authentication methods are supported?
- What are the concurrency, bandwidth, and acceptable-use limits?
- How are service interruptions and replacement requests handled?

Product information and pricing change. Check the provider's current official documentation before purchasing. IPDEEP's registered product paths include [static residential IP](https://www.ipdeep.cn/static-residence) and [dynamic residential proxy](https://www.ipdeep.cn/dynamic-residence); verify that each page is live and current before using it as a purchase reference.
