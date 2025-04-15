# Run Ingress-NGINX as a DaemonSet

- Status: accepted
- Deciders: arch meeting
- Date: 2023-03-16

## Context and Problem Statement

Currently we run Ingress-NGINX as a DaemonSet.
This can potentially feel like a waste of resources in large environments.
Running the Ingress Controller as a Deployment with at least two replicas is a possibility.

Should we run Ingress-NGINX as a Deployment or as a DaemonSet?
What do we do for Infra Providers that do not have Service type LoadBalancer?

## Decision Drivers

- We want to deliver a stable and secure platform.
- We want to keep application Nodes "light", so the application team knows what capacity is available for their application.
- We want to find a solution which is scalable and minimizes administrator burden.
- We don't want to waste infrastructure.
- We want to keep things simple.

## Considered Options

1. Keep running the Ingress-NGINX as a DaemonSet.
1. Run Ingress-NGINX as a Deployment with 2 or more replicas depending on the environment size and requirements.
1. Do not run Ingress-NGINX on the AMS Nodes.
1. For Infra Providers without Service type LoadBalancer continue using host network as decided in adr0008
1. For Infra Providers without Service type LoadBalancer start using Service type NodePort for NGINX and also use the external load balancer to route traffic from ports 80/443 to Node ports 30080/30443.

## Decision Outcome

Chosen options: 1 & 3 & 5

- "Keep running Ingress-NGINX as a DaemonSet."
- "Do not run Ingress-NGINX on the AMS Nodes."
- "For Infra Providers without Service type LoadBalancer start using Service type NodePort for NGINX and also use the external load balancer to route traffic from ports 80/443 to Node ports 30080/30443" -> This supersedes adr0008.

### Positive Consequences

- We keep things simple and have the same solution on all Infrastructure Providers.
- We keep the platform stable and secure, and don't risk dropping traffic when we replace Nodes or Nodes become unavailable.
- No changes are needed.
- More resources are available on the AMS Nodes.
- Reduce complexity.
- We will now use `externalTrafficPolicy: local` and with this we will reduce latency and preserve the client’s source IP address, which is essential for some applications that rely on knowing the client's IP, such as for logging, security, or geolocation services.

### Negative Consequences

- Feels like some resources are wasted on very large environments with many Nodes.

## Recommendation to Platform Administrators

- Do not run the Ingress-NGINX on the AMS Nodes.
- For Infra Providers without Service type LoadBalancer start using Service type NodePort for NGINX and also use the external load balancer to route traffic from ports 80/443 to Node ports 30080/30443

## Links

- [Issue using host network](https://github.com/kubernetes-sigs/kubespray/blob/master/contrib/terraform/exoscale/modules/kubernetes-cluster/templates/cloud-init.tmpl#L34-L44)
