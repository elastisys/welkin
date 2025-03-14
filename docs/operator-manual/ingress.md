# Ingress

Welkin uses the Ingress NGINX Controller to route external traffic to the correct Service inside the Cluster. Welkin can configure the Ingress Controller in two different ways depending on the underlying infrastructure.

## Using a Service of type LoadBalancer

When using a Infrastructure Provider with a Kubernetes cloud integration such as AWS, Azure and Google cloud the Ingress
controller can be exposed with a Service of type LoadBalancer. This will create an external load balancer in the cloud
provider with an external ip-address. Any DNS records should be pointed to the IP address of the load balancer.

!!!note

    This is only currently supported in Welkin for AWS. It is however possible to configure this for Azure and Google cloud as well but it's not done by default

## Using the host network

For any Infrastructure Provider (or bare metal) not supporting these kind of public load balancers the Ingress Controller
uses the host network instead. This is done by configuring the Ingress Controller as a DaemonSet so one Pod
is created on each Node. The Pods are configured to use the host network, so all traffic received on the Node
on port 80 and 443 will be intercepted by the Ingress Controller Pod and then routed to the desired Service.

On some Infrastructure Providers there is load balancing available for the worker Nodes. For example Exoscale uses an "elastic IP"
which provides one external IP which load balances to the available worker Nodes. For these Infrastructure Providers this external IP
of the load balancers should be used as the entry point in the DNS.

For the Infrastructure Providers where this is not available the easiest option is to just point the DNS to the IP of any, or all, of
the worker Nodes. This is of course not a optimal solution because it adds a single point of failure on the worker Node which
is selected by the DNS. Another option is to use any existing load balancer service if this is available.

## Installation

The Ingress NGINX Controller is currently configured and installed by the
[compliantkubernetes-apps](https://github.com/elastisys/compliantkubernetes-apps) repository.
The configuration is set in
[sc-config.yaml](https://github.com/elastisys/compliantkubernetes-apps/blob/main/config/sc-config.yaml#L526-L530)
and [wc-config.yaml](https://github.com/elastisys/compliantkubernetes-apps/blob/main/config/wc-config.yaml#L322-L334) under:

```yaml
ingressNginx:
  useHostPort: ""
  service:
    enabled: ""
    type: ""
```

If the apps repository is initiated with the correct Infrastructure Provider these configuration options will get the
correct defaults.

For more ways to install the Ingress NGINX Controller see [the upstream documentation](https://kubernetes.github.io/ingress-nginx/deploy/).

## Ingress resource

The Ingress resource is used to later route traffic to the desired Service. For more information about this
see the official [documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/).
