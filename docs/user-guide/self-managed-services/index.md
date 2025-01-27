# Self-Managed Service

We designed Welkin with [guardrails by default](../safeguards/index.md).
Also, application developers have rather [limited permissions](../demarcation.md).
Together, these help your organization comply with various regulations and information security standards, such as:

<!-- vale off -->
- [BDEW Whitepaper Anforderungen an sichere Steuerungs- und Telekommunikationssysteme v3.0](https://www.bdew.de/media/documents/BDEW-OE-VSE-Whitepaper-3.0.pdf) Requirement 4.1.1 Minimal-Need-To-Know-Prinzip.
<!-- vale on -->

However, Welkin also empathises with application developers who need to "get things done".
Indeed, application developer may need to leverage the [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) pattern for increased productivity and may perceive Welkin to be too restrictive.

To fulfill the needs of application developers, Welkin introduces the concept of self-managed services.
Each self-managed service is a Welkin feature which provides just enough permissions to install an Operator, while at the same time complying with the principle of least privilege.
Self-managed services are disabled by default and need to be enabled by the platform administrator to comply with secure-by-default principles.

Check out the other pages in this section to discover which self-managed services are already supported by Welkin.

## Requesting a New Self-Managed Service

Each self-managed service is treated by Welkin like a feature to ensure it gets the needed attention in terms of quality assurance and security assessment.

If the self-managed service is not yet supported by Welkin, feel free to [Request a Feature](../../request-a-feature.md)

## Contributing a New Self-Managed Service

If you have the needed expertise to add a new self-managed service yourself, we welcome your contribution.

Please issue a PR against [Welkin Apps](https://github.com/elastisys/compliantkubernetes-apps) and we'll duly review it.
To get started, we recommend you [check out this PR](https://github.com/elastisys/compliantkubernetes-apps/pull/1886/files) which shows how we added the Kafka self-managed service.

## Further Reading

- [Kubernetes Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [ISO 27019:2024](https://www.iso.org/standard/85056.html)
<!-- vale off -->
- [BDEW Whitepaper Anforderungen an sichere Steuerungs- und Telekommunikationssysteme v3.0](https://www.bdew.de/media/documents/BDEW-OE-VSE-Whitepaper-3.0.pdf)
<!-- vale on -->
