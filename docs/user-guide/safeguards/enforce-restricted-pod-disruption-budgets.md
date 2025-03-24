---
search:
  boost: 2
---

<!--
Note to contributors: Aim for the following format.

* Title: Highlight benefit to Application Developer
* Context
* Problem
* Solution
* Error
* Resolution
-->

# Avoid Installing PodDisruptionBudgets which Prevent Maintenance and Security Patches

> [!IMPORTANT]
> This guardrail is enabled by default and will deny violations.
> As a result, resources that violate this policy will not be created.

## Problem

PodDisruptionBudgets is a tool that can ensure your application does not suffer from too much disruption during normal maintenance operations.
PodDisruptionBudgets work by limiting how many Pods in a given Deployment or other Pod controller (StatefulSet, ReplicaSet, or ReplicationController) can be evicted at the same time, when a platform administrator drains a Node.
Platform administrators typically drain Nodes for maintenance purposes like restarting and upgrading Nodes or for removing and replacing Nodes, some of these actions might be done automatically by different tools.

When configured correctly PodDisruptionBudgets can be a good tool to collaborate with your platform administrators.
But it is possible to misconfigure them in a way that prevents or hinders platform administrators from draining Nodes.
If you create a PodDisruptionBudget that does not allow for any disruptions, then draining Nodes with a matching Pod will fail unless the platform administrator manually kills the Pod.

## Solution

To solve this problem you need to ensure that all PodDisruptionBudgets allow for at least one Pod disruption at a time.

- For PodDisruptionBudgets with `maxUnavailable` you need to set that option to anything above `0` or `0%`.
- For PodDisruptionBudgets with `minAvailable` you need to set that option to anything lower than the number of replicas in the Pod controller.
    - For percentages the `minAvailable` is rounded up to nearest integer.
    E.g. if the number of replicas for a Deployment is `4`, then any percentage from `1%` to `25%`would evaluate to require at least 1 available replica.
    In the same example you would then not want to set the percentage to `76%` or higher, since that would require all 4 replicas to be available, i.e. it would not allow for any Pod disruptions.

## How Does Welkin Help?

To make sure you don't create PodDisruptionBudgets that does not allow for Pod disruptions, the administrator can configure Welkin to deny creation of PodDisruptionBudgets and Pod controllers that does not allow for Pod disruptions.
So you might have both PodDisruptionBudgets and Pod controllers be denied by this policy.

If you get the following error:

```error
Error from server (Forbidden): error when creating "pdb.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [elastisys-restrict-pod-disruption-budgets] PodDisruptionBudget rejected: Deployment <test-deployment> has 4 replica(s) but PodDisruptionBudget <test-pdb> has minAvailable of 4, minAvailable should always be lower than replica(s), and not used when replica(s) is set to 1. Read more about this and possible solutions at <link-to-public-documentation>
```

Then your PodDisruptionBudget and Pod controller does not allow for any Pod disruption.

If your administrator has not enforced this policy yet, you can view current violations of the policy by running:

```bash
kubectl get k8srestrictpoddisruptionbudgets.constraints.gatekeeper.sh elastisys-restrict-pod-disruption-budgets -ojson | jq .status.violations
```

## Further reading

You can read more about Pod disruption and PodDisruptionBudgets in the upstream documentation for Kubernetes.

- [Pod disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
- [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
