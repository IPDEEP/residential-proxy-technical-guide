# 07. A Practical IP Quality Check

“IP quality” is not one universal score. It is a collection of observations that should be evaluated against a specific, authorized workload.

## Useful dimensions

| Dimension | What to inspect | Limitation |
|---|---|---|
| Reachability | Can the endpoint establish a connection? | A successful test does not guarantee future availability |
| Latency | Round-trip time to a chosen destination | Changes by route, time, and destination |
| Packet loss | Whether test packets are lost | Short tests may miss intermittent loss |
| ASN / organization | Announced network and organization labels | Does not prove access technology |
| Geolocation | Country/region estimate | Databases can disagree |
| DNS behavior | Which resolver handles lookups | Browser and OS may use separate DNS paths |
| Reputation indicators | Results from IP intelligence sources | Scores are proprietary and may be stale |
| Stability | Repeated measurements over time | A single snapshot is insufficient |

## Suggested procedure

1. Define the destination and performance requirements.
2. Record the IP address observed by the test service.
3. Capture timestamp, ASN, organization, and geolocation estimate.
4. Measure latency to the actual business endpoint, not only a generic speed-test host.
5. Repeat tests at different times.
6. Compare multiple intelligence sources where classification matters.
7. Record errors and provider-side incident information.

## Avoid misleading conclusions

- A high reputation score does not guarantee access to a third-party service.
- A low latency result to one host does not predict latency to every destination.
- “Residential” is not synonymous with “clean,” “exclusive,” or “risk-free.”
- A DNS leak test is meaningful only when interpreted in the context of the application's DNS architecture.
- Do not test systems without authorization or attempt to bypass access controls.

You may use [ToDetect IP lookup](https://www.todetect.net/ip/) as one input to an inspection workflow. Document the source and timestamp when sharing results.
