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
- provide some technical documentation (Annex VII CRA);
- fulfill essential cybersecurity requirements (Annex I CRA).

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

3. Name and type of any additional additional information enabling the unique identification of Welkin: Both the Grafana and OpenSearch Service Endpoints feature a welcome dashboards which show the version of Welkin you are currently running.

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
        - [Platform Administrator: Understand Welin](../../operator-manual/understand-welkin.md).
    - Welkin needs a compliant and secure infrastructure. See:
        - [Infrastructure Requirements](../../operator-manual/infrastructure-requirements.md);
        - [Provider Audit](../../operator-manual/provider-audit.md).

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
    - For more information, see [Self-Managed Welkin](https://elastisys.com/self-managed/).

<!--
8. detailed instructions or an internet address referring to such detailed instructions and information on:

(a) the necessary measures during initial commissioning and throughout the lifetime of the product with digital elements to ensure its secure use;

(b) how changes to the product with digital elements can affect the security of data;

(c) how security-relevant updates can be installed;

(d) the secure decommissioning of the product with digital elements, including information on how user data can be securely removed;

(e) how the default setting enabling the automatic installation of security updates, as required by Part I, point (2)(c), of Annex I, can be turned off;

(f) where the product with digital elements is intended for integration into other products with digital elements, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Annex I and the documentation requirements set out in Annex VII.

9. If the manufacturer decides to make available the software bill of materials to the user, information on where the software bill of materials can be accessed.
-->

TBD

## Technical Documentation (Annex VII CRA)

<!--
The technical documentation referred to in Article 31 shall contain at least the following information, as applicable to the relevant product with digital elements:

1. a general description of the product with digital elements, including:

(a) its intended purpose;

(b) versions of software affecting compliance with essential cybersecurity requirements;

(c) where the product with digital elements is a hardware product, photographs or illustrations showing external features, marking and internal layout;

(d) user information and instructions as set out in Annex II;

2. a description of the design, development and production of the product with digital elements and vulnerability handling processes, including:

(a) necessary information on the design and development of the product with digital elements, including, where applicable, drawings and schemes and a description of the system architecture explaining how software components build on or feed into each other and integrate into the overall processing;

(b) necessary information and specifications of the vulnerability handling processes put in place by the manufacturer, including the software bill of materials, the coordinated vulnerability disclosure policy, evidence of the provision of a contact address for the reporting of the vulnerabilities and a description of the technical solutions chosen for the secure distribution of updates;

(c) necessary information and specifications of the production and monitoring processes of the product with digital elements and the validation of those processes;

3. an assessment of the cybersecurity risks against which the product with digital elements is designed, developed, produced, delivered and maintained pursuant to Article 13, including how the essential cybersecurity requirements set out in Part I of Annex I are applicable;

4. relevant information that was taken into account to determine the support period pursuant to Article 13(8) of the product with digital elements;

5. a list of the harmonised standards applied in full or in part the references of which have been published in the Official Journal of the European Union, common specifications as set out in Article 27 of this Regulation or European cybersecurity certification schemes adopted pursuant to Regulation (EU) 2019/881 pursuant to Article 27(8) of this Regulation, and, where those harmonised standards, common specifications or European cybersecurity certification schemes have not been applied, descriptions of the solutions adopted to meet the essential cybersecurity requirements set out in Parts I and II of Annex I, including a list of other relevant technical specifications applied. In the event of partly applied harmonised standards, common specifications or European cybersecurity certification schemes, the technical documentation shall specify the parts which have been applied;

6. reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability handling processes with the applicable essential cybersecurity requirements as set out in Parts I and II of Annex I;

7. a copy of the EU declaration of conformity;

8. where applicable, the software bill of materials, further to a reasoned request from a market surveillance authority provided that it is necessary in order for that authority to be able to check compliance with the essential cybersecurity requirements set out in Annex I.
-->

TBD

## Essential Cybersecurity Requirements (Annex I CRA)

A detailed analysis on how Elastisys ensures Welkin complies with essential cybersecurity requirements, including evidence, is documented internally.
Feel free to get in touch with Elastisys and we'd be happy to walk you through it.

## Further Reading

- [EU Cyber Resilience Act (CRA)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847)
