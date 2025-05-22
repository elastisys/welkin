---
search:
    boost: 2
---

# Valkey™

!!! elastisys "For Elastisys Managed Services Customers"

    You can order Managed Ephemeral Valkey™ by filing a [service ticket](https://elastisys.atlassian.net/servicedesk/). Here are the highlights:

    * **Business continuity**: Replicated across three dedicated Nodes.
    * **Disaster recovery**: none -- we recommend against using Valkey as a primary database.
    * **Monitoring, security patching and incident management**: included.

    For more information, please read [ToS Appendix 3 Managed Additional Service Specification](https://elastisys.com/legal/terms-of-service/#appendix-3-managed-additional-service-specification-managed-services-only).

<figure>
    <img alt="Valkey Deployment Model" src="../img/valkey.drawio.svg" >
    <figcaption>
        <strong>Valkey on Welkin Deployment Model</strong>
        <br>
        This help you build a mental model on how to access Valkey as an Application Developer and how to connect your application to Valkey.
    </figcaption>
</figure>

This page will help you succeed in connecting your application to a low-latency in-memory cache Valkey which meets your security and compliance requirements.

!!!important "Important: Access Control with NetworkPolicies"

    Please note the follow information about [Valkey access control](https://valkey.io/topics/security/) from the upstream documentation:

    > Valkey is designed to be accessed by trusted clients inside trusted environments.

    Valkey access is protected by [NetworkPolicies](../safeguards/enforce-networkpolicies.md). To allow your applications access to a Valkey cluster the Pods need to be labeled with `elastisys.io/valkey-<cluster_name>-access: allow`.

!!!important "Important: No Disaster Recovery"

    We do not recommend using Valkey as primary database. Valkey should be used to store:

    * Cached data: If this is lost, this data can be quickly retrieved from the primary database, such as the PostgreSQL cluster.
    * Session state: If this is lost, the user experience might be impacted -- e.g., the user needs to re-login -- but no data should be lost.

!!!important "Important: Sentinel support"

    We recommend a highly available setup with at minimum three instances. The Valkey client library that you use in your application needs to support [Valkey Sentinel](https://valkey.io/topics/sentinel/). Notice that clients with Sentinel support need [extra steps to discover the Valkey primary](https://valkey.io/topics/sentinel-clients/).

## Install Prerequisites

Before continuing, make sure you have access to the Kubernetes API, as describe [here](../prepare.md).

Make sure to install the Valkey client on your workstation. On Ubuntu, this can be achieved as follows:

```bash
sudo apt install redis-tools
```

## Getting Access

Your administrator will set up a ConfigMap inside Welkin, which contains all information you need to access your Valkey Cluster.
The ConfigMap has the following shape:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
    name: $CONFIG_MAP
    namespace: $NAMESPACE
data:
    # VALKEY is the name of the Valkey Cluster. You need to know the name to label your Pods correctly for network access.
    VALKEY_CLUSTER_NAME: $VALKEY_CLUSTER_NAME

    # VALKEY_SENTINEL_HOST represents a cluster-scoped Valkey Sentinel host, which only makes sense inside the Kubernetes cluster.
    # E.g., rfs-valkey-cluster.valkey-system
    VALKEY_SENTINEL_HOST: $VALKEY_SENTINEL_HOST

    # VALKEY_SENTINEL_PORT represents a cluster-scoped Valkey Sentinel port, which only makes sense inside the Kubernetes cluster.
    # E.g., 26379
    VALKEY_SENTINEL_PORT: "$VALKEY_SENTINEL_PORT"
```

To extract this information, proceed as follows:

```bash
export CONFIG_MAP=            # Get this from your administrator
export NAMESPACE=         # Get this from your administrator

export VALKEY_SENTINEL_HOST=$(kubectl -n $NAMESPACE get configmap $CONFIG_MAP -o 'jsonpath={.data.VALKEY_SENTINEL_HOST}')
export VALKEY_SENTINEL_PORT=$(kubectl -n $NAMESPACE get configmap $CONFIG_MAP -o 'jsonpath={.data.VALKEY_SENTINEL_PORT}')
```

> [!IMPORTANT]
> At the time of this writing, we do not recommend to use a Valkey Cluster in a multi-tenant fashion. One Valkey Cluster should have only one purpose.

## Create a ConfigMap

First, check that you are on the right Welkin Cluster, in the right **application** namespace:

```bash
kubectl get nodes
kubectl config view --minify --output 'jsonpath={..namespace}'; echo
```

Now, create a Kubernetes ConfigMap in your application namespace to store the Valkey Sentinel connection parameters:

```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
    name: app-valkey-config
data:
    VALKEY_SENTINEL_HOST: $VALKEY_SENTINEL_HOST
    VALKEY_SENTINEL_PORT: "$VALKEY_SENTINEL_PORT"
EOF
```

## Allow your Pods to communicate with the Valkey Cluster

The Valkey Cluster is protected by Network Policies. Add the following label to your Pods: `elastisys.io/valkey-<cluster_name>-access: allow`

`cluster_name` can be retrieved from the ConfigMap provided by your administrator:

```bash
kubectl -n $NAMESPACE get configmap $CONFIG_MAP -o 'jsonpath={.data.VALKEY_CLUSTER_NAME}'
```

## Expose Valkey Connection Parameters to Your Application

To expose the Valkey Cluster to your application, follow one of the following upstream documentation:

- [Create a Pod that has access to the ConfigMap data through a Volume](https://kubernetes.io/docs/concepts/configuration/configmap/#using-configmaps-as-files-from-a-pod)
- [Define container environment variables using ConfigMap data](https://kubernetes.io/docs/concepts/configuration/configmap/#configmaps-and-pods)

> [!IMPORTANT]
> Make sure to use a Valkey client library with Sentinel support. For example:
>
> - [Django-Valkey Client that supports Sentinel Cluster HA](https://github.com/danigosa/django-redis-sentinel-redux#how-to-use-it)
>   If the linked code example doesn't work, try `LOCATION: redis://mymaster/db`.
>
> If your library doesn't support sentinel you could use this project - [Redis sentinel proxy](https://github.com/anubhavmishra/redis-sentinel-proxy).
> Note that the default configuration in this repository will not ensure HA for Valkey.
> For this you'll either need to use multiple replicas or use it as a sidecar for your applications.

## Follow the Go-Live Checklist

You should be all set.
Before going into production, don't forget to go through the [go-live checklist](../go-live.md).

## Welkin Valkey Release Notes

Check out the [release notes](../../release-notes/valkey.md) for the Valkey Cluster that runs in Welkin environments!

## Best Practices Recommended

- **Eviction Policy**: Choose the [eviction policy](https://valkey.io/topics/lru-cache/) that works for your application. The `default` eviction policy for our Managed Valkey is `allkeys-lru`, which means any key can be evicted under memory pressure irrespective of whether the key is expired or not. It will keep the most recently used keys and remove the least recently used (LRU) key.

    > [!NOTE]
    > Since this is a server setting, it cannot be set by the user itself, but needs to be set by the administrators. Please send a support ticket with the values you would like to set.

- **Set TTL**: If possible, take the advantage of expiring keys, such as temporary OAuth authentication keys. When you set the key, set it with some expiration and Valkey will clean up for you. Refer to [TTL](https://valkey.io/commands/ttl/)
- **Avoid expensive or blocking operations**: Since Valkey command processing is single-threaded, operations like the [KEYS](https://valkey.io/commands/keys/) command are expensive and should be avoided. You can avoid `KEYS` by using [SCAN](https://valkey.io/commands/scan/) to reduce CPU spikes.
- **Monitor memory usage**: Monitor the usage in Grafana dashboard to ensure that you don't run out of memory and have the chance to scale your cache before seeing issues.
- **Manage idle connection**: The number of connections to Valkey increases if connections are not properly terminated. This can lead to bad performance. Therefore, we recommend to setting `timeout` which allows you to set the number of seconds before idle client connections are automatically terminated.
  The default `timeout` for our Managed Valkey is set to `0`, which means the idle clients do not timeout and remain connected until the client issues the termination.

    > [!NOTE]
    > Since this is a server setting, it cannot be set by the user itself, but needs to be set by the administrators. Please send a support ticket with the values you would like to set.

- **Cache-hit ratio**: You should regularly monitor your `cache-hit` ratio so that you know what percentage of key lookups are successfully returned by keys in your Valkey instance.
  `info stats` command provides `keyspace_hits` & `keyspace_misses` metric data to further calculate cache hit ratio for a running Valkey instance.

## Further Reading

- [Valkey Sentinel](https://valkey.io/topics/sentinel/)
- [Sentinel client spec](https://valkey.io/topics/sentinel-clients/)
- [Valkey Commands](https://valkey.io/commands/)
- [Kubernetes ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
