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

# Avoid Cluster autoscaler failing to scale down Nodes due to usage of Pods without any backing controller

!!!important

    This guardrail is enabled by default and will warn on violations, but only on clusters with cluster autoscaling.
    As a result, resources that violate this policy will generate warning messages, but will still be created.

## Problem

The Cluster autoscaler can manage the amount of Nodes in the Cluster by creating or removing Nodes based on resources requested by Pods.
It will scale down Nodes once there is a Node that is not needed anymore.
However, there are [some scenarios](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node) where the autoscaler will not remove certain Nodes.
One such scenario is if there is a Pod running on the Node that is not backed by a controller object (such as a Deployment or StatefulSet).

A Pod that is running without any controller object backing it is also not resilient, since if that Pod is deleted, it will not be re-created.
This could be ok for temporary Pods, but in general it should be avoided.

## Solution

There are a few different solutions to avoid the scenario stated above:

1. Create Pods using some sort of [controller](https://kubernetes.io/docs/concepts/workloads/pods/#pods-and-controllers). Such as Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, or CronJob.
1. If it is ok that the Pod is deleted by the autoscaler even though it is not backed by a controller.
    Then you can annotate the Pod with `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` to note that the Pod is safe to evict in general, this also allows the autoscaler to delete the Pod even if it is also violating some of the other rules that normally prevent the autoscaler from deleting Pods.

## How Does Welkin Help?

To make sure you don't create Pods that prevent the autoscaler from deleting Nodes, the administrator can configure Welkin to deny creation of Pods that would prevent the autoscaler.

If you get the following error:

```error
Error: UPGRADE FAILED: failed to create resource: admission webhook "validation.gatekeeper.sh" denied the request: [denied by elastisys-reject-pod-without-controller] The Pod "Pod-without-controller" does not have any ownerReferences. This can prevent autoscaler from scaling down a node where this is running. Read more about this and possible solutions at <link-to-public-documentation>
```

Then your Pod does not have a backing controller, which would prevent the autoscaler from scaling down a Node.

Note that this is only a problem if the Pod will be scheduled on a Node that is subject to autoscaling.
However, this policy does not know where the Pod would be scheduled, so it will trigger even if the Pod would not be scheduled on an Node subject to autoscaling.
If you are certain that the Pod will not be scheduled on a Node subject to autoscaling, then you can safely add the annotation mentioned in the solutions above.

If your administrator has not enforced this policy yet, you can view current violations of the policy by running:

```bash
kubectl get k8srejectpodwithoutcontroller.constraints.gatekeeper.sh elastisys-reject-pod-without-controller -ojson | jq .status.violations
```
