---
description: Learn how to prepare for Welkin, the Kubernetes platform for software critical to our society
search:
  boost: 2
---

<!-- markdownlint-disable-file first-line-h1 -->

!!! welkin-managed "For Welkin Managed Customers"

    You can ask questions, get additional information, set up a call with our experts or order a managed service environment by emailing **sales@elastisys.com**.

    The highlights of ordering a managed service environment are:

    * **Infrastructure provider**: You choose it, among the Elastisys Partners.
    * **Business Continuity**: Kubernetes Cluster always feature 3 control plane Nodes.
    * **Retention**: by default 30 days for logs, 90 days for metrics.
    * **Backup**:
        * Scope: most Kubernetes resources and Persistent Volume Claims.
        * RPO: daily, 3 backups
    * **Monitoring, security patching and incident management**: included.

    For more information, please read [ToS Appendix 2 Managed Welkin Service Specification](https://elastisys.com/legal/terms-of-service/#appendix-2-managed-welkin-service-specification-managed-services-only).

# Step 1: Prepare

Hi there, Application Developer! Happy to have you on board with Welkin!

In this part, you will learn about the things you should do to prepare to get started with the platform.

<!--prerequisites-start-->

Your administrator has already set up the platform for you. You will therefore have received:

- URLs for the Service Endpoints: OpenSearch Dashboards, Grafana, and Harbor;
- a [kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) file for configuring `kubectl` or Lens access to the Workload Cluster; and
- (optionally and rarely) a static username and password. Note that normally, you should log in via a username and a password of your organization's Identity Provider, such as LDAP, Azure Active Directory, or Google Identity.

## Install Prerequisite Software

Required software:

- [oidc-login](https://github.com/int128/kubelogin), which helps you log into your Kubernetes Cluster via OpenID Connect integration with your Identity Provider of choice

Your Cluster management software of choice, of which you can choose either or both:

- [kubectl](https://kubernetes.io/docs/tasks/tools/), a command-line tool to help manage your Kubernetes resources
- [OpenLens](https://github.com/MuhammedKalkan/OpenLens/releases), a graphical user interface to help manage your Kubernetes resources (see also our [dedicated page on Lens integration](kubernetes-ui.md))

Optional, but very useful, tools for developers and DevOps engineers:

- [docker](https://docs.docker.com/get-docker/), if you want to build (Docker) container images locally
- [Helm](https://helm.sh/docs/intro/install/), if you want to manage your application with the Helm package manager

??? tip "You can verify that configuration is correct by issuing the following simple commands"

    Make sure you have configured your tools properly:

    ```
    export KUBECONFIG=path/of/kubeconfig.yaml  # leave empty if you use the default of ~/.kube/config
    export DOMAIN=  # the domain you received from the administrator
    ```

    To verify if the required tools are installed and work as expected, type:

    ```bash
    docker version
    kubectl version  --client
    helm version
    # You should see the version number of installed tools and no errors.
    ```

    To verify the received KUBECONFIG, type:

    ```bash
    # Notice that you will be asked to complete browser-based single sign-on
    kubectl get nodes
    # You should see the Nodes of your Kubernetes cluster
    ```

    To verify the received URLs, type:

    ```bash
    curl --head https://dex.$DOMAIN/healthz
    curl --head https://harbor.$DOMAIN/healthz
    curl --head https://grafana.$DOMAIN/healthz
    curl --head https://opensearch.$DOMAIN/api/status
    curl --insecure --head https://app.$DOMAIN/healthz  # Ingress Controller
    # All commands above should return 'HTTP/2 200'
    ```

 <!--prerequisites-end-->

## Access Your Web Portals

<!--endpoint-access-start-->

Those URLs that your Welkin administrator gave you all have a `$DOMAIN`, which will typically include your company name and perhaps the environment name.

Your web portals are available at:

- `harbor.$DOMAIN` -- the Harbor container image registry, which will be the home to all your container images
- `opensearch.$DOMAIN` -- the OpenSearch Dashboards portal, where you will view your application and audit logs
- `grafana.$DOMAIN` -- the Grafana portal, where you will view your monitoring metrics for both the platform, as such, and your application-specific metrics

Additional endpoints are also available, depending on if your platform has these additional managed services (AMS) or not:

- `jaeger.$DOMAIN` -- the [Jaeger](./additional-services/jaeger.md) distributed tracing observability tool
- `argocd.$DOMAIN` -- the [Argo CD](./additional-services/argocd.md) continuous Deployment GitOps tool

<!--endpoint-access-end-->

## Containerize Your Application

Welkin runs containerized applications in a Kubernetes platform. It is a Certified Kubernetes distribution, which means that if an application is possible to deploy on a standard Kubernetes environment, it can be deployed on Welkin.

However, there are some restrictions in place for security reasons. In particular, **containers cannot be run as root**. Following this [best practice](https://docs.docker.com/develop/develop-images/instructions/#user) is a simple way to ensure additional security for your containerized applications deployed in Kubernetes.

There are additional guardrails in place that reflect the security posture of Welkin that impact your application. These prevent users from doing potentially unsafe things. In particular, users are not allowed to:

{%
    include "./demarcation.md"
    start="<!--guardrails-start-->"
    end="<!--guardrails-end-->"
%}

## Next step? Deploying!

Ready with a containerized application? Head over to the next step, where you learn how to [deploy](deploy.md) it!
