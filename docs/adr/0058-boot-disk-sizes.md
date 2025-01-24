# Boot disk size on nodes

- Status: Accepted
- Deciders: Product Team
- Date: 2024-12-19

## Context and Problem Statement

This ADR supersedes [adr-0032](0032-boot-disk-size.md) which previously established that all nodes should have boot disk of size 100GB irrespective of node size and that control plane Nodes should have 100GB local disk.

After running like this for over 1 year we have discovered that for small and medium environments this is too much and can be lowered for some of the nodes to reduce the infrastructure cost for our customers.

Should we use different boot disk sizes for nodes than we set before?

## Decision Drivers

- We want to best serve the Application Developer needs.
- We want to find a solution which is scalable and minimizes administrator burden.
- We don't want to waste infrastructure.

## Considered Options

- Do nothing and keep decision from adr-0032
- Change boot disk size to 50GB for all nodes irrespective of size and type.
- Keep boot disk size to minimum 100GB for all WC worker nodes
- Keep boot disk size to minimum 100GB for all WC Elastisys nodes
- Keep boot disk size to minimum 100GB for all control plane nodes in both MC and WC
- Keep boot disk size to minimum 100GB for all control plane nodes in WC
- Change boot disk size to minimum 50GB for all nodes irrespective of size and type in MC cluster and leave all WC cluster nodes with 100GB boot disk size.
- Keep boot disk size to minimum 100GB as recommended size for all nodes irrespective of size and type and on request change MC nodes and some WC nodes to use 50GB
- Do not change the default values

## Decision Outcome

Chosen option: 1 + 3 + 4 + 9

### Positive Consequences

- Improved Reliability for application nodes by choosing option 3
- Reduce the number of alerts and ops time from option 3 and 4
- Improve platform stability and scalability
- Reduce the infrastructure cost for small and medium environments.
- By not changing default configurations, no existing clusters will be impacted, reducing the risk of unintentional disruption.

### Negative Consequences

- Some alerts might appear for nodes that will use 50GB volumes
- More ops time would be needed to scale up the 50GB volumes

## Recommendation to Platform Administrators

- Try to use same VM flavors on all environments
- Use VM flavor with local disk of minimum 50GB, recommended 100GB or whichever is closest to this size depending on Infrastructure Provider for control plane Nodes.
- For worker nodes use 100GB boot disk size on Infrastructure Providers that allow it and on the ones that we can't use the VM flavor with the closest disk size.

## Links

- [Some recommendations](https://serverfault.com/questions/977871/recommended-disk-size-for-gke-nodes)
