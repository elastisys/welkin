# Software Bill of Materials (SBOM)

Modern software consists of multiple discrete components, many of which are built on-top of already existing software.
Heavy use of layers upon layers of third party dependency is the rule, not the exception. These dependencies
quickly create such a high level of complexity that when some critical vulnerability emerges, just knowing _if_ you are
affected or not becomes a challenge.

A common remedy for this issue is the inclusion of a **Software Bill of Materials (SBOM)**. An SBOM is a formal, machine-readable
inventory of all components in a software artifact. It takes every library, every dependency, every version, and catalogues it
in a standardized fashion. This way, SBOMs make the opaque transparent. They are generated during the software build process by
scanning components. For security-conscious organizations SBOMs are not just good practice. They are increasingly mandatory.

## Our SBOM Approach

Welkin generates SBOMs using the **CycloneDX** format, an industry-standard specification designed specifically for software supply chain
transparency. Our SBOMs are generated at release time, ensuring they accurately reflect the exact components shipped in each version.
Our SBOM generation captures components from Helm charts and container images. For each release, we inventory:

- All Helm charts (both custom charts and upstream charts from external repositories)
- All container images referenced in deployments
- Version information and source repositories for each component
- License information

To learn even more about our approach, you can view our most recently updated
[SBOM for Welkin Apps](https://github.com/elastisys/compliantkubernetes-apps/blob/main/sbom/sbom.cdx.json)
