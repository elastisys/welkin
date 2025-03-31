# Welkin Infrastructure Requirements

> [!NOTE]
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).

This page lists infrastructure requirements to run Welkin in production.
For setting up a development environment, see [this guide](https://github.com/elastisys/compliantkubernetes-apps/blob/main/DEVELOPMENT.md) instead.

You should always perform a [provider audit](provider-audit.md) to get a stable and secure Welkin environment.
This page serve primarily as an initial assessment -- to determine whether it's even worth getting started.
This ensures that the fundamental conditions are met before investing further effort.

## How much infrastructure capacity does Welkin need?

The required capacity depends on the performance of your infrastructure.
This, in turn, is strongly influenced by the CPU model, memory bandwidth, network bandwidth, disk bandwidth, etc. that you invested in.

We found the following to be a good starting point:

* Management Cluster:
  * 3x 2 CPUs, 4 GB RAM, 60 GB local disk for control plane Nodes
  * 5x 2 CPUs, 8 GB RAM, 80 GB local disk for worker Nodes
* Workload Cluster:
  * 3x 2 CPUs, 4 GB RAM, 60 GB local disk for control plane Nodes
  * 2x 2 CPUs, 6 GB RAM, 60 GB local disk for Welkin worker Nodes
  * Add additional capacity as required by your application and Additional Managed Services.

Before going live, you should adjust capacity as needed to preserve stability and security.
See the [Go-Live Checklist](../user-guide/go-live.md).

## What infrastructure capabilities do I need?

This depends a lot on your goals.
For example:

* If you want to tolerate one datacenter failure, then you MUST have three datacenters, due to Kubernetes quorum requirements ([further reading](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)).
* If you want to tolerate one Node failure, then you MUST have a load-balancer with health-checks which can route traffic away from the failed Node.

Ideally, your infrastructure SHOULD provide:

* VMs or physical servers running Ubuntu 24.04 LTS
* Firewall to protect the VMs
* Two private networks, one for the Management Cluster and one for the Workload Cluster
* Two load-balancers
* [CSI-compatible](https://kubernetes-csi.github.io/docs/drivers.html) block storage
* [S3-compatible](https://www.techtarget.com/searchstorage/tip/How-to-use-S3-compatible-storage#:~:text=Top%20S3%2Dcompatible%20products%20and%20vendors) object storage
* An [OpenTofu](https://opentofu.org/) or [Terraform Provider](https://registry.terraform.io/browse/providers) to configure all above via an API

Furthermore, your infrastructure SHOULD not block:

* Internal traffic between the VMs
* Access to the [Swedish NTP servers](https://www.netnod.se/swedish-distributed-time-service) (outgoing packets on UDP port 123). Note that the Swedish NTP servers are mandated by MSBFS 2020:7 “Myndigheten för samhällsskydd och beredskaps föreskrifter om säkerhetsåtgärder i informationssystem för statliga myndigheter“ 3 kap § 13\.
* Access to [LetsEncrypt](https://letsencrypt.org/) (outgoing and incoming packets on TCP port 80)

For initial setup, platform administrators need SSH access to the VMs.
This can be done in a few ways:

* Expose the VMs on the public Internet and allowlist the platform administrators' VPNs.
* Expose a Bastion Host running Ubuntu on the public Internet and allowlist the platform administrators' VPNs.
* Provide the platform administrators with a Linux-compatible VPN client to access the VMs via SSH.

## What if I lack ...?

* ... a policy which allows SSH access to the VMs:
Platform administrators needs to be empowered to use the tools which make them most efficient.
Doing initial setup via "desktop share", such as [VNC](https://www.realvnc.com/en/connect/download/viewer/), [Remote Desktop](https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c) or [Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/overview.html), is tedious and error-prone.
Let us help you by reading your Exception Policy, fill out your Exception Request Form and provide you with detailed Compensating Controls to mitigate risk associated with the exception.
* ... an API to configure my infrastructure:
Platform administrators will communicate with your infrastructure team via email or service tickets.
In fact, we recommend that initial setup includes a detailed architecture diagram of the infrastructure, both to reduce misunderstandings, but also to serve as documentation, as required by ISO 27001 Annex A 5.37 Documented Operating Procedures.
* ... access to the Swedish NTP servers:
Welkin can be configured with alternative NTP servers.
This will ensure you conform with ISO 27001 Annex A 8.17 Clock Synchronization.
* ... access to LetsEncrypt:
[This page](air-gapped.md) discusses alternative strategy for certificate provisioning.
Note that this may reduce automation, hence is more human time intensive and error prone.
* ... an S3-compatible object storage:
Consider using a public cloud-based fully-managed S3-compatible object storage.
* ... CSI-compatible block storage:
If you have Rook/Ceph experts, then you can set up a Rook/Ceph cluster.
Note that this will increase infrastructure footprint and the skills needed for troubleshooting from your team.
Always prefer using your existing block storage solution, such as your existing NFS server.
* ... load-balancers:
If Welkin may speak BGP with your routers, then you may use [kube-vip](https://kube-vip.io/) -- currently not part of Welkin.
If not, then this will make it significantly harder to tolerate Node failures. We could potentially compensate by using DNS with health-checks, as provided by [AWS Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html), however fail-over times become a lot larger, e.g., up to 5 minutes. If DNS failover is unsuitable for you, then we recommend a manual failover process.
* ... private networks:
You can use public IP addresses for the VMs and protect them using your firewall.
* ... three datacenters:
To tolerate one datacenter failure, you need three datacentres.
This requirement is due to Kubernetes needing a quorum.
Some Additional Managed Services also need quorom for tolerating failure.
You also need to have a load-balancer which is "stretched" across all datacenters.
This means that if one datacenter goes down, your load balancer needs to be able to direct traffic to the healthy datacenters.
This is usually achieved via [BGP Anycast](https://en.wikipedia.org/wiki/Anycast).
* ... Internet access:
See [air-gapped](air-gapped.md).
