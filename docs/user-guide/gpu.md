---
search:
  boost: 2
---

# Using GPU Workload in Welkin

!!! elastisys "For Elastisys Managed Services Customers"
    You can order a new Environment with GPU support by filing a [service ticket](https://elastisys.atlassian.net/servicedesk/).
    Make sure to specify the need for GPU Nodes in "Additional information or comments".
    If you are unsure, get in touch with your account manager.

As the demand for AI, machine learning, and data science workloads grows, Kubernetes provides a flexible and scalable platform to manage these applications.
In this guide, we'll focus on how to use GPU in the Welkin platform.

> [!NOTE]
> Not all infrastructure providers have support for GPU.
> Check with the platform administrator to find out if your environment has support for GPU workload.

## Deployment

To use GPU resources in your cluster, you need to create a deployment that is using the resource `nvidia.com/gpu`.
Here's an example of how to configure GPU resources for a Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-vectoradd
spec:
  restartPolicy: OnFailure
  containers:
  - name: cuda-vectoradd
    image: "nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04"
    resources:
      limits:
        nvidia.com/gpu: 1
```

### Managing Node Types for GPU Workloads

GPU nodes are essential for certain high-performance workloads, such as machine learning or data processing.
Clusters often host a variety of workloads, some of which require GPU nodes, while others can run on standard CPU nodes.
To optimize resource usage and prevent unnecessary costs—since GPU nodes are significantly more expensive than CPU nodes—we have introduced multiple node types with corresponding labels and taints.
This ensures workloads are deployed on appropriate node types based on their requirements.

#### Node Labels and Taints

To enforce resource-specific scheduling, nodes have been configured with the following labels and taints:

- **CPU Nodes**:
    - **Label**: `elastisys.io/node-group=worker`
    - **Taint**: None
    - These nodes serve as the default option for general workloads and require no additional configuration in Pod specifications.

- **GPU Nodes**:
    - **Labels**:
        - `elastisys.io/node-type=gpu`
        - `elastisys.io/node-group=gpu-worker`
    - **Taint**: `elastisys.io/node-type=gpu:NoSchedule`
    - These nodes are reserved exclusively for workloads requiring GPU resources. To schedule pods on GPU nodes, specific **node affinity** and **toleration** must be configured in the Pod definition.

By using these labels and taints, we ensure that:

1. General workloads remain on CPU nodes by default.
1. Only workloads explicitly configured to use `GPUs` are scheduled on GPU nodes.

##### Recommendations for Self-Managed Environments

If you are managing the environment yourself, we recommend applying the above labels and taints to your nodes. This prevents workloads from unintentionally consuming GPU resources, thereby avoiding unnecessary expenses.

###### How to Configure GPU Workloads

Application developers who need to deploy workloads on GPU nodes must include the appropriate affinity and toleration settings in the Pod specification. Below is an example configuration:

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
            - key: elastisys.io/node-type
              operator: In
              values:
              - gpu
  tolerations:
    - effect: NoSchedule
      key: elastisys.io/node-type
      operator: Equal
      value: gpu
```

This configuration ensures the workload is scheduled only on GPU nodes.

###### Advanced example Scenario

Let’s imagine you have a workload that specifically requires a GPU flavor called `Standard_B2s`.
You want to ensure this workload is scheduled exclusively on nodes with this GPU type. Here’s how you can achieve this:

1. File a [service ticket](https://elastisys.atlassian.net/servicedesk/) and ask to add a new GPU flavor `Standard_B2s` and a label to that GPU node like `node.kubernetes.io/instance-type=Standard_B2s`
1. Modify the workload manifest file to include the additional label. The updated manifest would look like this:

  ```yaml
  spec:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
              - key: elastisys.io/node-type
                operator: In
                values:
                - gpu
              - key: node.kubernetes.io/instance-type
                operator: In
                values:
                - Standard_B2s
    tolerations:
      - effect: NoSchedule
        key: elastisys.io/node-type
        operator: Equal
        value: gpu
  ```

This configuration ensures that the workload is only scheduled on GPU nodes labeled with both Elastisys.io/node-type=gpu and node.Kubernetes.io/instance-type=Standard_B2s.

> [!NOTE]
> If your cluster is using the cluster autoscaling feature and there's currently not enough resources, the autoscaler will create one for you.
> It might take a couple of minutes for the new node to join the cluster and to install all the pre-requisites.

###### Further Reading

- [Kubernetes Schedule GPU Documentation](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
- [Kubernetes Cluster Autoscaler Documentation](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)
- [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
