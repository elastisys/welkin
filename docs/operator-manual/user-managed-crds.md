# Self-managed Cluster resources (Preview)

Adding certain Cluster-wide resources, such as CustomResourceDefinitions, are Cluster-wide settings that are prohibited by Welkin [for security purposes](../user-guide/demarcation.md).
However, many popular applications, in particular ones with Operators, require Cluster-wide resources to be installed.
This preview feature enables application developers to self-manage a **predefined** set of such Cluster-wide resources.
This trade-off means that application developers get the ability to install and manage such popular applications, but without compromising the security posture of the Cluster.
By enabling this feature, a predefined set of Cluster-wide resources is allowed to be installed.
In addition to CustomResourceDefinitions, other Cluster-wide resources, such as the required ClusterRoles and ServiceAccounts are installed.
The list of currently supported applications for self-management is:

- SealedSecrets
- MongoDB
- Flux
- Kafka

## Limitations

Welkin does not allow application developers to install ClusterRoles and ClusterRoleBindings.
For pre-approved operators that require ClusterRoles and ClusterRoleBindings.
They are installed during enabling of self-managed-CRDs feature.
The installation of self-managed Cluster resources can be limited to a pre-defined Namespace. For example, Sealed Secrets is required to be installed in the namespace `sealed-secrets`. This to correctly bind a Cluster role to the service account.

## Enable self-managed Cluster-wide resources

By default, this feature is disabled.
To enable it, add the following snippet to the environments `wc-config.yaml` file

```yaml
user:
  # Enable Sealed Secrets
  sealedSecrets:
    enabled: true
  # Enable MongoDB
  mongodb:
    enabled: true
  # Enable Flux
  fluxv2:
    enabled: true
  # Enable Kafka
  kafka:
    enabled: true

gatekeeper:
  allowUserCRDs:
    # Enable feature
    enabled: true
    enforcement: deny
    # Add extra allowed CRDs
    extraCRDs: []
    # - names:
    #     - sealedsecrets.bitnami.com
    #   group: "bitnami.com"

    # Add extra service accounts that needs access to CRDs
    extraServiceAccounts: []
    #  - namespace: "gatekeeper-system"
    #    name: "gatekeeper-admin-upgrade-crds"
```
