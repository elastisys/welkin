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

# Avoid cluster autoscaler failing to scale down nodes due to local storage emptydir usage

!!!important

    This guardrail is enabled by default and will deny violations, but only on clusters with where cluster autoscaling is available. As a result, resources that violate this policy will not be created. TODO - default not determined yet, update once that is done

## Problem

The cluster autoscaler can manage the amount of nodes in the cluster by creating or removing nodes based on resources requested by pods. It will scale down nodes once there is a node that is not needed anymore. However, there are [some scenarios](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node) where the autoscaler will not remove certain nodes. One such scenario is if there is a Pod running on the node that is not backed by a controller object (such as a Deployment or StatefulSet).

A Pod that is running without any controller object backing it is also not resilient, since if that Pod is deleted, it will not be re-created. This could be ok for temporary Pods, but in general it should be avoided.

## Solution

There are a few different solutions to avoid the scenario stated above:

1. Create pods using some sort of [controller](https://kubernetes.io/docs/concepts/workloads/pods/#pods-and-controllers). Such as Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, or CronJob.
1. If it is ok that the Pod is deleted by the autoscaler even though it is not backed by a controller. Then you can annotate the Pod with `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` to note that the Pod is safe to evict in general, this also allows the autoscaler to delete the Pod even if it is also violating some of the other rules that normally prevent the autoscaler from deleting pods.

## How Does Welkin Help?

To make sure you don't create pods that prevent the autoscaler from deleting nodes, the administrator can configure Welkin to deny creation of Pods that would prevent the autoscaler.

If you get the following error:

```error
Error: UPGRADE FAILED: failed to create resource: admission webhook "validation.gatekeeper.sh" denied the request: [denied by elastisys-reject-pod-without-controller] The Pod "Pod-without-controller" does not have any ownerReferences. This can prevent autoscaler from scaling down a node where this is running. Read more about this and possible solutions at <link-to-public-documentation>
```

Then your Pod does not have a backing controller, which would prevent the autoscaler from scaling down a node.

Note that this is only a problem if the Pod will be scheduled on a node that is subject to autoscaling. However, this policy does not know where the Pod would be scheduled, so it will trigger even if the Pod would not be scheduled on an node subject to autoscaling. If you are certain that the Pod will not be scheduled on a node subject to autoscaling, then you can safely add the annotation mentioned in the solutions above.

If your administrator has not enforced this policy yet, you can view current violations of the policy by running:

```bash
kubectl get k8srejectpodwithoutcontroller.constraints.gatekeeper.sh elastisys-reject-pod-without-controller -ojson | jq .status.violations
```
