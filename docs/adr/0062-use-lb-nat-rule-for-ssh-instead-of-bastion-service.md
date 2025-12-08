# Use Load Balancer NAT Rule for SSH Access instead of Azure Bastion Service

- Status: Accepted
- Deciders: Product Team
- Date: 2025-04-10

## Context and Problem Statement

When deploying a Welkin Cluster using Cluster API Provider Azure (CAPZ), the existing configuration for creating a bastion Node defaults to provisioning the costly and operationally rigid Azure Bastion Service.

This service presents significant drawbacks for operational efficiency and cost management:

- The Azure Bastion Service, when provisioned by CAPZ, cannot be easily paused, stopped, or deleted without terminating the entire Cluster. Furthermore, CAPZ attempts to reconcile and reinstate the service, resulting in continuous, high charges for the customer.

- SSH access via the Azure Bastion Service is complicated, requiring lengthy and non-standard Azure CLI commands, which hinders rapid troubleshooting on Cluster Nodes.

- The incurred cost is prohibitive for development and unnecessarily high for production Clusters, as the service runs perpetually.

We require a method for reliable, secure, and cost-effective SSH access to Welkin Cluster Nodes on Azure, specifically to facilitate essential troubleshooting commands on the underlying virtual machines.

## Decision Drivers

- Cost Efficiency: Achieve significant infrastructure cost reduction by eliminating the persistent charge of the Azure Bastion Service.

- Operational Simplicity: Streamline the process of obtaining SSH access for development and operations staff (Ops), moving away from the complex Azure Bastion workflow and the time-consuming manual VM creation/deletion workaround (which takes approx. 40 minutes per cycle).

- Troubleshooting Capability: Ensure quick and easy SSH access is available when necessary to run direct commands on Cluster Nodes.

## Considered Options

1. Customize CAPI Cluster Chart for a Normal VM Bastion: Modify the CAPI chart to provision a standard VM with a fixed public IP and necessary security rules to serve as a traditional bastion host.

1. Use LB NAT Rule to Access a Control Plane/Cluster VM (The Chosen Path): Configure a Network Address Translation (NAT) rule on the existing Azure Load Balancer (LB) to expose SSH port 22 on a designated Node (typically a control plane Node). This Node then serves as the jump host to access the rest of the Cluster VMs, aligning with documented CAPZ patterns.

1. Manual Bastion Creation/Deletion: Continue using the operational workaround of manually creating a temporary VM via the Azure CLI/UI when SSH access is needed, and then manually deleting it afterward.

1. Do Nothing: Accept the high cost and operational overhead imposed by the default CAPZ configuration utilizing the Azure Bastion Service.

## Decision Outcome

Option 2: Use LB NAT Rule to Access a Control Plane/Cluster VM.

The selected approach is to Enable port 22 on the Load Balancer and use that as a jump host to SSH to the Nodes.

This utilizes the existing Azure Load Balancer associated with the Welkin Cluster to provide secure, controlled Ingress for SSH access. This strategy avoids the limitations and high cost of the Azure Bastion Service while fulfilling the need for troubleshooting access.

The implementation will rely on the observed behavior that CAPI/CAPZ generally restricts external SSH access via the LB NAT rule to only one Node (the jump host), with other Nodes being accessible via that jump host.

### Positive Consequences

- Major Cost Savings: Eliminates the continuous, recurring cost associated with the dedicated Azure Bastion Service.

- Improved Operations: Provides a simpler, faster, and more standard method for Ops to gain shell access for diagnostics and troubleshooting.

- Cluster Consistency: Leverages existing Cluster resources (the LB) rather than relying on external or time-consuming manual workarounds.

### Negative Consequences

- Investigation Required: The default behavior of CAPI/CAPZ regarding the single-Node SSH restriction must be confirmed to ensure security standards are met before Deployment.

- Documentation Overhead: Existing documentation on SSH procedures for Welkin Clusters must be updated to clearly detail this new Load Balancer jump-host method for Azure infrastructure.
