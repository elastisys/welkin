# Software Bill of Materials (SBOM)
Modern software generally consists of multiple discrete components, many of which are built on-top of already existing software. Heavy use of layers upon layers of third party dependency is the rule, not the exception. These dependencies













## Software Bill of Materials (SBOM)

Modern software is built from components—open-source libraries, third-party dependencies, and internal modules stacked layer upon layer.
When a critical vulnerability like Log4Shell emerges, the question becomes urgent: *Are we affected?*
Without visibility into your software's components, answering that question means scrambling through codebases, hoping your inventory is complete.

A **Software Bill of Materials (SBOM)** is a formal, machine-readable inventory of all components in a software artifact. Think of it as an ingredients list for software: every library, every dependency, every version, catalogued in a standardized format. SBOMs make the opaque transparent.

### How SBOMs work

SBOMs are generated during the build process by scanning your artifacts—container images, binaries, or source repositories. The output follows standardized formats like SPDX or CycloneDX, listing each component's name, version, supplier, and relationships to other components.

When a new CVE drops, you can query your SBOMs instantly: "Do we run the vulnerable version of this library?" No archaeology required. Better yet, automated tooling can continuously monitor SBOMs against vulnerability databases, alerting you the moment a component in your supply chain is compromised.

For security-conscious organizations—especially those bound by frameworks like NIS2 or Executive Order 14028—SBOMs aren't just good practice. They're increasingly mandatory.
