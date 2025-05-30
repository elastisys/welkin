# How to run multiple AMS packages of the same type in the same environment

- Status: accepted
- Deciders: arch meeting
- Date: 2023-03-23

## Context and Problem Statement

Some of the Application Developers request multiple AMS packages of the same size or different sizes, using 1 package per request or multiple packages in the same request (batch-order).
How should we add the second or n-th package? Should we scale the Nodes vertically or horizontally?
If we scale horizontally, then in some cases we need to add AMS packages of different sizes and this brings up the problem where we need to stick the package to a specific set of Nodes otherwise for example, after a maintenance that reboots the Nodes, a postgres-4 package might be scheduled on a Node that was intended for a postgres-8 package and the postgres-8 Pod will not be able to be scheduled anymore because it does not fit on the postgres-4 Node.
How can we overcome this issue? Should we add a `elastisys.io/ams-cluster-name` label/taint for the AMS with dedicated Nodes?

## Decision Drivers

- We want to deliver a stable and secure platform.
- We want to best serve the Application Developer needs.
- We want to find a solution which is scalable and minimizes administrator burden.
- We don't want to waste infrastructure.

## Considered Options

1. Always scale the Nodes vertically and fit multiple PostgreSQL packages on the same pair of Nodes.

    - but how many packages should we place on the same pair of Nodes? max 3 packages? max 5 packages?
    - up to what Node sizes?
    - what about resource waste? we will not find VM flavors that match exactly our sum of packages.

    On the other hand we reduce the resources allocated to our services(each Node is eating ~ 1 CPU and 2GB ram, by placing 3 packages on the same Node we reduce by 2CPU and 4GB RAM the resource waste)

1. Always scale horizontally and place each package on its own set of dedicated Nodes.

1. Scale the AMS dedicated Nodes vertically so that it fits all packages on the same set of Nodes.

    - but how many packages should we place on the same pair of Nodes? max 3 packages? max 5 packages?
    - up to what Node sizes?
    - what about resource waste? we will not find VM flavors that match exactly our sum of packages.

## Decision Outcome

Chosen options: 2

1. Always scale horizontally and place each package on its own set of dedicated Nodes.

    - "Add additional label `elastisys.io/ams-cluster-name` to a set of Nodes dedicated to a specific package"
    - "Do not taint the Nodes."

    Respect [ADR-0022](0022-use-dedicated-nodes-for-additional-services.md) and add the `elastisys.io/node-type` taint and label.

### Positive Consequences

- The platform stability and scalability is improved.
- We provide extra isolation of the AMS.
- Being able to choose from options of scaling the Nodes both vertically and horizontally shows that we are flexible, and we can satisfy more of the Application Developer needs.
- We can add more labels that will better describe and schedule our AMS services, like `local-disk` and others.
- With options 1 and 3 more resources are available to the Application Developer.

### Negative Consequences

- For option 2 we need to add the new label to the AMS repository and update documentation.
- The infrastructure footprint is increased for option 2.
- With options 1 and 3 the stability of the AMS package is reduced, because if 1 Node is unresponsive then it will affect not 1 AMS package, but multiple AMS packages.

## Recommendations to Platform Administrators

- Use label like: `elastisys.io/ams-cluster-name`
- Update the AMS repository and documentation with this label, and set it by default to automatically get picked up by kubectl
