# Release Notes

## Welkin Cluster API

<!-- BEGIN TOC -->

- [v0.7.0](#v070) - 2025-06-23
- [v0.6.2](#v062) - 2025-05-21
- [v0.6.1](#v061) - 2025-04-24
- [v0.6.0](#v060) - 2025-04-04
- [v0.5.1](#v051) - 2025-03-28
- [v0.5.0](#v050) - 2025-02-05
- [v0.4.0](#v040) - 2024-11-28
- [v0.3.0](#v030) - 2024-08-23
- [v0.2.0](#v020) - 2024-06-28
- [v0.1.0](#v010) - 2024-01-24
<!-- END TOC -->

## v0.7.0

Released 2025-06-23

### Feature(s)

- Added templating for using local volumes
- Opened SSH access to Nodes
- Added OpenStack floatingIP pool for stable egress
- Added ability to configure custom NTP servers
- Implemented Kubespray -> ClusterAPI NTP settings migration

### Improvement(s)

- Upgraded cert-manager chart to v1.17.1
- Reconfigured the containerd registry mirror authentication method
- Implemented marketplace solution for Azure
- Unified registry mirror configuration for OpenStack and Azure
- Upgraded to CAPI v1.10 and CAPO v1.12
- Allowed skipping health monitor creation for OpenStack Load Balancers
- Added support for migrating local volumes from Kubespray to capi
- Added default NTP servers
- Azure: added configuration options to set disk type and size

### Other(s)

- Removed all internal references from configuration and docs
- Cleanup: purged all references to yq3
- Cleanup: exposed affinity configuration for the local volume provisioner
- Docs: added DR section for broken API server load balancer
- Upgraded openstack-cloud-controller-manager to v2.32.0
- Upgraded openstack-cinder-csi to v2.32.0
- Fix: labeled CoreDNS PDB Helm release with type=application

## v0.6.2

Released 2025-05-21

### Others(s)

- Remove all internal refs in the repository

## v0.6.1

Released 2025-04-24

### Improvement(s)

- update VMs images with containerd v1.7.27

## v0.6.0

Released 2025-04-04

### Feature(s)

- Added support for load balancers to use predefined floating IP addresses.
- Added local volume provisioner chart.

### Improvement(s)

- Improved migration documentation to allow for less disruptive upgrades.
- Images built for Elastx now uses VirtIO-SCSI, allowing for more than 25 volumes to be attached to a Node.

### Upgraded

- Bumped default Kubernetes version to v1.31.7.

## v0.5.1

Released 2025-03-28

### Improvement(s)

- Improved migration documentation to allow for less disruptive upgrades

## v0.5.0

Released 2025-02-05

### Upgraded

- Upgraded Ubuntu images to 24.04
- Bumped default Kubernetes version to v1.30.9

## v0.4.0

Released 2024-11-28

### Features(s)

- Azure environments now only use one resource group.

### Improvement(s)

- `kube-system` Pods are now prevented from scheduling on autoscaled Nodes, to ensure that the Nodes can be automatically scaled down again.

## v0.3.0

Released 2024-08-23

### Features(s)

- Azure now has support for `ReadWriteMany` volumes. Use the StorageClass `azurefile-nfs-premium-lrs`.
- Enabled unattended upgrades for security patching.

## v0.2.0

Released 2024-06-28

### Feature(s)

- Add Azure Cloud as a infrastructure provider

## v0.1.0

Released 2024-01-24

First stable release!

!!! warning "Compatibility Notice(s)"

    - This version of Welkin Cluster API only supports Cleura and Elastx as infrastructure providers.
