# Run Cluster API controllers on Management Cluster

- Status: accepted
- Deciders: Cluster API management and Tekton meeting
- Date: 2023-03-15

## Context and Problem Statement

With Cluster API there are multiple different ways to organise the management hierarchy that have different impacts on the environment in regard to cost, availability, security and ease of Deployment and maintainability.

Where should we run the Cluster API controller?

## Decision Drivers <!-- optional -->

- We want to minimise the impact it has on resources
- We want to ease the Deployment and maintenance process
- We want to be able to tolerate faults in management and Workload Clusters
- We want to maintain good security posture

## Considered Options

- Independent Clusters
    - All Clusters run the Cluster API controllers and all Clusters manage themselves independently.
- Controller Cluster
    - A new separate Controller Cluster runs the Cluster API controllers and manages all Clusters in the environment.
- Management Cluster
    - The Management Cluster runs the Cluster API controllers and manages all Clusters in the environment.

## Decision Outcome

Chosen option: "Management Cluster", because it strikes the balance between security, as it has relatively good availability properties and no Kubernetes admin credentials have to be stored in the Workload Cluster, and maintainability, as Clusters can be managed centralised.

### Positive Consequences <!-- optional -->

- Requires no additional resources
- Requires single instance of Cluster API controllers per environment
- Requires less Deployment and maintenance efforts to manage
- Management Cluster already provides services to allow backups, monitoring, and logging
- Workload Cluster will not have Kubernetes admin credentials

### Negative Consequences <!-- optional -->

- Cluster API controllers availability relies on Management Cluster
    - Main consideration is control plane, since Management Cluster has sufficient Nodes for the controller to reschedule
    - Workload Cluster will still function but it will lose auto heal and auto scaling functions
- Management Cluster will have Kubernetes admin credentials for the Workload Cluster

## Pros and Cons of the Options <!-- optional -->

### Independent Cluster

- Good, no additional resource requirements
- Good, all Clusters have required supporting services
- Good, all Clusters are independently impacted by failures
- Good, all Clusters are independently impacted by configuration mistakes, although...
- Bad, it is easier to do configuration mistakes
- Bad, it requires more effort to manage for each Cluster
- Bad, all Clusters have to be bootstrapped
- Bad, will contain Kubernetes admin credentials in Workload Cluster

### Controller Cluster

- Bad, requires additional resources
- Bad, requires additional supporting services
- Bad, Management and Workload Cluster lose management (auto healing and auto scaling) on Controller Cluster failure, although...
- Good, Management and Workload Cluster state can be backed up and restored
- Good, environment can be managed as a group or individually if needed, although...
- Bad, all Cluster can be impacted by configuration mistakes, although...
- Good, it is harder for configuration mistakes
- Good, it requires less effort to manage each Cluster
- Good, single Cluster has to be bootstrapped
- Good, will not contain Kubernetes admin credentials in Workload Cluster

### Management Cluster

- Good, no additional resource requirements
- Good, Management Cluster has required supporting services
- Bad, Workload Cluster loses management (auto healing and auto scaling) on Management Cluster failure, although...
- Good, Workload Cluster state can be backed up and restored
- Good, environment can be managed as a group or individually if needed, although...
- Bad, all Cluster can be impacted by configuration mistakes, although...
- Good, it is harder for configuration mistakes
- Good, it requires less effort to manage each Cluster
- Good, single Cluster has to be bootstrapped
- Good, will not contain Kubernetes admin credentials in Workload Cluster
