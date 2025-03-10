# Release Notes

## Welkin Cluster API

<!-- BEGIN TOC -->

- [v0.5.0](#v050) - 2025-02-05
- [v0.4.0](#v040) - 2024-11-28
- [v0.3.0](#v030) - 2024-08-23
- [v0.2.0](#v020) - 2024-06-28
- [v0.1.0](#v010) - 2024-01-24
<!-- END TOC -->

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
