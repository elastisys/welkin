# Microsegmentation

Welkin uses NetworkPolicies in order to ensure that components can only communicate with each other if absolutely necessary.
It does this by first using a policy that denies all communication and then using policies to open up the required communication paths.

Our Network Policies are created using a generic [generator chart](https://github.com/elastisys/compliantkubernetes-apps/tree/main/helmfile.d/charts/networkpolicy/generator) in which you define a set of rules and then a set of policies using those rules.

Take the [Velero values](https://github.com/elastisys/compliantkubernetes-apps/blob/main/helmfile.d/values/networkpolicies/common/velero.yaml.gotmpl) as an example.
Velero is configured to allow egress traffic to the Cluster DNS, the API server, and the object storage, and Ingress from Prometheus for metrics scraping, using common rules defined [here](https://github.com/elastisys/compliantkubernetes-apps/blob/main/helmfile.d/values/networkpolicies/common/common.yaml.gotmpl).

```yaml
velero:
    podSelectorLabels:
        app.kubernetes.io/name: velero
        name: velero
    egress:
    - rule: egress-rule-dns
    - rule: egress-rule-apiserver
    - rule: egress-rule-object-storage
    ingress:
    - rule: ingress-rule-prometheus
        ports:
        - tcp: 8085
```

Some of the rules in these Network Policies are configurable through the Apps configuration. The possible configuration keys are available in the [schema](schema/config.md/#networkpolicies).

Below is automatically generated documentation based on the Network Policy generator values found [here](https://github.com/elastisys/compliantkubernetes-apps/blob/main/helmfile.d/values/networkpolicies).

> [!note]
>
> This is where the auto-generated Network Policy documentation for Welkin Apps will be available when deployed!
>
> If you want to see this locally check out [the contribution guide](https://github.com/elastisys/welkin/blob/main/CONTRIBUTING.md)!
