---
description: Learn how to deploy your application on Welkin, the Kubernetes platform for software critical to our society
search:
  boost: 2
---

# Step 2: Deploy

Hello again, Application Developer! In this step, we will walk you through what is needed to deploy your application on Welkin.

## Demo Application Available

In case you are just reading along, or do not already have a [containerized application prepared](prepare.md), we have developed a demo application which allows you to quickly explore the benefits of Welkin.

The provided artifacts, including Dockerfile and Helm Chart, allow you to quickly get started on your journey to become an agile organization with zero compromise on compliance with data protection regulations.

We have versions of it for [Node JS](https://github.com/elastisys/welkin/tree/main/user-demo) and [.NET](https://github.com/elastisys/welkin/tree/main/user-demo-dotnet) available. You will note that once built and containerized, they deploy exactly the same.

## Push Your Container Images

{%
    include "./registry.md"
    start="<!--user-demo-registry-start-->"
    end="<!--user-demo-registry-end-->"
%}

## Deploy Your Application

<!-- markdownlint-disable MD044 -->
{%
    include "./kubernetes-api.md"
    start="<!--user-demo-kubernetes-api-start-->"
    end="<!--user-demo-kubernetes-api-end-->"
%}
<!-- markdownlint-enable MD044 -->

## View Application Logs

{%
    include "./logs.md"
    start="<!--user-demo-logs-start-->"
    end="<!--user-demo-logs-end-->"
%}

## Next step? Operating!

Now that you have deployed your containerized application and know how to look at its logs, what's next? Head over to the next step, where you learn how to [operate](operate.md) and monitor it!
