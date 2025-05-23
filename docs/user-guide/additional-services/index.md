---
search:
  boost: 2
tags:
  - BSI IT-Grundschutz APP.4.4.A16
---

# Additional Services

!!! welkin-managed "For Welkin Managed Customers"

    You can order Managed Additional Services by filing a [service ticket](https://elastisys.atlassian.net/servicedesk/).

    For more information, please read [ToS Appendix 3 Managed Additional Service Specification](https://elastisys.com/legal/terms-of-service/#appendix-3-managed-additional-service-specification-managed-services-only).

![Illustration of Welkin as the hourglass waist](img/additional-services.drawio.svg)

Welkin simplifies usage of a complex and diverse infrastructure. By exposing simple and uniform concepts, it allows you to focus on application development.

However, your application needs more than just running stateless containers. At the very least, you will need a database -- such as PostgreSQL -- to persist data. More complex applications will require a distributed cache -- such as Redis -- to store session information or offload the database. Finally, background tasks are best handled by separate containers, connected to your user-facing backend code via a message queue -- such as RabbitMQ.

These additional services need to be delivered as securely as the rest of the platform. Access control, business continuity, disaster recovery, security patching and maintenance need to be core features, not afterthoughts.

It turns out, the same simple and uniform concepts that benefit your application can also be used to simplify hosting additional services. And thanks to security-hardening included in Welkin, the burden of delivering additional services with the security you need is also reduced.

Welkin is the "hourglass waist" of the platform. Think of it like HTTPS being the "hourglass waist" of the Internet: It unites the sprawl of wired and wireless network technologies to offer a uniform concept on which various web, gaming, chat and video streaming protocols can run.

In the end, you win by having a feature-full platform to host your application. Not just VMs, but useful services. Administrators win by avoiding to re-invent the wheel and focus on the specifics of each additional service.

This section of the user guide will help you benefit the most from the additional services hosted within Welkin.
