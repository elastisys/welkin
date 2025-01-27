# Boot disk size on Nodes

- Status: Accepted
- Deciders: Product Team
- Date: 2024-12-19

## Context and Problem Statement

This ADR supersedes [ADR-0032](0032-boot-disk-size.md) which previously established that all Nodes should have boot disk of size 100GB irrespective of Node size and that control plane Nodes should have 100GB local disk.

After running like this for over 1 year we have discovered that for small and medium environments this is too much and can be lowered for some of the Nodes to reduce the infrastructure footprint.

Should we use different boot disk sizes for Nodes than we set before?

## Decision Drivers

- We want to best serve the Application Developer needs.
- We want to find a solution which is scalable and minimizes administrator burden.
- We don't want to waste infrastructure.

## Considered Options

1. Do nothing and keep decision from ADR-0032
1. Change boot disk size to 50GB for all Nodes irrespective of size and type.
1. Keep boot disk size to minimum 100GB for all WC worker Nodes
1. Keep boot disk size to minimum 100GB for all WC Elastisys Nodes
1. Keep boot disk size to minimum 100GB for all control plane Nodes in both MC and WC
1. Keep boot disk size to minimum 100GB for all control plane Nodes in WC
1. Change boot disk size to minimum 50GB for all Nodes irrespective of size and type in MC cluster and leave all WC cluster Nodes with 100GB boot disk size.
1. Keep the recommended boot disk size to minimum 100GB for all Nodes irrespective of size and type, however allow on request to change MC Nodes and some WC Nodes to use 50GB.
1. Do not change the default values

## Decision Outcome

Chosen option: 8 + 9. This means we will keep the recommended boot disk size to minimum 100GB for all Nodes irrespective of size and type, however allow on request to change MC Nodes and some WC Nodes to use 50GB. The default value stays at 100 GB.

### Positive Consequences

- Improved Reliability for application Nodes
- Reduce the number of alerts and ops time
- Improve platform stability and scalability
- Reduce the infrastructure cost for small and medium environments.
- By not changing default configurations, no existing clusters will be impacted, reducing the risk of unintentional disruption.

### Negative Consequences

- Some alerts might appear for Nodes that will use 50GB volumes
- More ops time would be needed to scale up the 50GB volumes

## Recommendation to Platform Administrators

- Try to use same VM flavors on all environments
- Use VM flavor with local disk of minimum 50GB, recommended 100GB or whichever is closest to this size depending on Infrastructure Provider for control plane Nodes.
- For worker Node use 100GB boot disk size on Infrastructure Providers that allow it and on the ones that we can't use the VM flavor with the closest disk size.

## Links

- [Discussion on boot disk size](https://serverfault.com/questions/977871/recommended-disk-size-for-gke-nodes)
