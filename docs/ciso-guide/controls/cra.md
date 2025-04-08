# EU Cyber Resilience Act (CRA)

As explained [by the European Commission](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act):

> The Cyber Resilience Act (CRA) aims to safeguard consumers and businesses buying software or hardware products with a digital component.
> The Cyber Resilience Act  addresses the inadequate level of cybersecurity in many products, and the lack of timely security updates for products and software.
> It also tackles the challenges consumers and businesses currently face when trying to determining which products are cybersecure and in setting them up securely.
> The new requirements will make it easier to take cybersecurity into account when selecting and using products that contain digital elements.
> It will be more straightforward to identify hardware and software products with the proper cybersecurity features.

## Welkin and CRA

As a containerized application platform, Welkin is a CRA Important Product with Digital Elements in Class II, because it falls under "Hypervisors and container runtime systems that support virtualised execution of operating systems and similar environments" (see Annex III CRA).

As a result, Welkin needs to:

- provide certain information and instructions to the user (Annex II CRA);
- maintain technical documentation (Annex VII CRA) to, among others, demonstrate fulfilling essential cybersecurity requirements (Annex I CRA).

The following sections provide documentation as needed to fulfill requirements.

## Information and Instructions to the User (Annex II CRA)

<!--
At minimum, the product with digital elements shall be accompanied by:

1. the name, registered trade name or registered trademark of the manufacturer, and the postal address, the email address or other digital contact as well as, where available, the website at which the manufacturer can be contacted;
-->

1. Manufacturer contact information: See [Elastisys Contact](https://elastisys.com/contact/).

<!--
2. the single point of contact where information about vulnerabilities of the product with digital elements can be reported and received, and where the manufacturer’s policy on coordinated vulnerability disclosure can be found;
-->

2. Where to report and receive vulnerabilities: See [Reporting security issues](https://github.com/elastisys/compliantkubernetes-apps/blob/main/SECURITY.md).

<!--
3. name and type and any additional information enabling the unique identification of the product with digital elements;
-->

3. Name and type of any additional information enabling the unique identification of Welkin: Both the Grafana and OpenSearch Service Endpoints feature a welcome dashboards which show the version of Welkin you are currently running.

<!--
4. the intended purpose of the product with digital elements, including the security environment provided by the manufacturer, as well as the product’s essential functionalities and information about the security properties;
-->

4. Intended purpose of Welkin: See [Mission and Vision](../../mission-and-vision.md).

<!--
5. any known or foreseeable circumstance, related to the use of the product with digital elements in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to significant cybersecurity risks;
-->

5. Foreseeable misuse, which may lead to significant cybersecurity risks:
    - Welkin is a complex product and requires skilled people. See:
        - [Application Developers: Understand the Basics](../../user-guide/understand-the-basics.md);
        - [Platform Administrator: Understand the Basics](../../operator-manual/understand-the-basics.md);
        - [Platform Administrator: Understand Welkin](../../operator-manual/understand-welkin.md).
    - Welkin needs a compliant and secure infrastructure. See:
        - [Infrastructure Requirements](../../operator-manual/infrastructure-requirements.md);
        - [Provider Audit](../../operator-manual/provider-audit.md).
    - Welkin needs an application prepared to run on a containerized platform. See:
        - [Prepare Your Application](../../user-guide/prepare-application.md).
    - Welkin needs a correctly configured Identity Provider. See:
        - [Prepare Your Identify Provider](../../user-guide/prepare-idp.md).

<!--
6. where applicable, the internet address at which the EU declaration of conformity can be accessed;
-->

6. EU Declaration of Conformity: We are waiting for the European Commission to publish a list of notified bodies, as laid out in Article 44 CRA.

<!--
7. the type of technical security support offered by the manufacturer and the end-date of the support period during which users can expect vulnerabilities to be handled and to receive security updates;
-->

7. Type of technical security support:
    - Customers may migrate from one minor version of Welkin to the immediately next one, unless otherwise noted.
    - A minor Welkin version receives security support, until all Elastisys customers have stopped using that version.
    - For more information, see:
        - [Maintenance](../../operator-manual/maintenance.md);
        - [Self-Managed Welkin](https://elastisys.com/self-managed/).

<!--
8. detailed instructions or an internet address referring to such detailed instructions and information on:
-->

8. Detailed instructions and information on:
    - (a) the necessary measures during initial commissioning and throughout the lifetime of the product with digital elements to ensure its secure use:
        See point 5 above.
    - (b) how changes to the product with digital elements can affect the security of data:
        Welkin is designed to be secure-by-default.
        Among others it includes [guardrails](../../user-guide/safeguards/index.md) to make it hard to do things which may reduce the security of data.
        Such guardrails should only be disabled if the consequences are properly understood.
    - (c) how security-relevant updates can be installed:
        See [Maintenance](../../operator-manual/maintenance.md).
    - (d) the secure decommissioning of the product with digital elements, including information on how user data can be securely removed:
        User data is fully removed if the VMs, block storage volumes and object storage buckets are removed.
        Note that configuration data may still persist in your git repository.
        For details, see [Architecture](../../architecture.md) and [Understand Welkin](../../operator-manual/understand-welkin.md).
    - (e) how the default setting enabling the automatic installation of security updates can be turned off: Two components deal with automatic installation of security updates: Kured and Tekton. Tekton is not turned on by default. Kured is turned on by default and can be disabled by setting `kured.enabled` to `false`. See [Configuration Reference](../../operator-manual/schema/README.md).
    - (f) where the product with digital elements is intended for integration into other products with digital elements, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Annex I and the documentation requirements set out in Annex VII: See [Infrastructure Requirements](../../operator-manual/infrastructure-requirements.md), [Provider Audit](../../operator-manual/provider-audit.md) and [Prepare Identify Provider](../../user-guide/prepare-idp.md).

<!--
9. If the manufacturer decides to make available the software bill of materials to the user, information on where the software bill of materials can be accessed.
-->

9. Software bill of materials:
    An older version can be found [here](https://github.com/elastisys/compliantkubernetes-apps/blob/main/docs/sbom.md).
    If you need a newer version, please [contact Elastisys](https://elastisys.com/contact/).

## Technical Documentation (Annex VII CRA)

Elastisys maintains an internal document entitled "Technical Documentation (Annex VII CRA)", which lays out technical documentation, as required by Annex VII CRA.
This document contains extensive evidence to demonstrate that Welkin complies with essential cybersecurity requirements (Annex I CRA).

Feel free to [get in touch with Elastisys](https://elastisys.com/contact/) and we'd be happy to walk you through it.

## Further Reading

- [EU Cyber Resilience Act (CRA)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847)
