# Run managed services in Workload Cluster

<!-- vale off -->
- Status: proposed. **This ADR did not reach consensus, with strong arguments on both sides.** However, due to needing a decision in a timely manner, this ADR is actually followed. Therefore, this ADR serves both for visibility and to document a _[fait accompli](https://en.wikipedia.org/wiki/Glossary_of_French_expressions_in_English#F)_.
<!-- vale on -->
- Deciders: Cristian
- Date: 2021-04-29

## Context and Problem Statement

To truly offer our users an option to run containerized workloads in EU jurisdiction, they also need additional managed services, like databases, message queues, caches, etc.

Where should these run?

## Decision Drivers

- Some of these services are chatty and need low latency.
- Some of these services might assume trusted clients over a trusted network.
- We want to make it easy to run these services with regulatory compliance in mind, e.g., we should be able to reuse Welkin features around monitoring, logging, access control and network segregation.
- We want to make it difficult for Welkin users to negatively affect managed services.
- We want to keep support for multiple Workload Cluster, i.e., application multi-tenancy.
- Many Infrastructure Providers do not support Service type LoadBalancer, which complicates exposing non-HTTP services outside a Kubernetes Cluster.
- Management Cluster might not exist in a future packaging of Welkin.

## Considered Options

- Run managed services in Workload Cluster
- Run managed services in Management Cluster
- Run managed services in yet another Cluster

## Decision Outcome

Chosen option: "run managed services in Workload Cluster".

## Positive Consequences

- Latency is minimized: The application consuming the managed service is close to the managed service, without needing to go through intermediate software components, such as a TCP Ingress Controller.
- NetworkPolicies can be reused for communication segregation.
- OpenID and RBAC in the Workload Cluster can be reused for user access control.
- Kubernetes audit log can be re-used for auditing user access managed services. Such access is required, e.g., for manual database migrations and "rare" operations like GDPR data correction requests.
- Ease of exposition: No need for Service type LoadBalancer, which is not supported on all Infrastructure Providers.

## Negative Consequences

- Blurs separation of responsibilities between user and administrator.
- The managed service is easier impacted by user misusage, e.g., bringing a Node into OOM.
- Workload Cluster can no longer be deployed with “free for all” security. Platform Administrators need to push and fight back against loose access control.

## Links

- [Service type LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
- [Exposing TCP and UDP services with Ingress-NGINX](https://kubernetes.github.io/ingress-nginx/user-guide/exposing-tcp-udp-services/)
- [Redis Security](https://redis.io/topics/security/)
