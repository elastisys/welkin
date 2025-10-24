# Software Bill of Materials (SBOM)
Modern software generally consists of multiple discrete components, many of which are built on-top of already existing software.
Heavy use of layers upon layers of third party dependency is the rule, not the exception. These dependencies
quickly create such a high level of complexity that when some critical vulnerability emerges, just knowing *if* you are
affected or not becomes a challenge.

A common remedy for this issue is the inclusion of a **Software Bill of Materials (SBOM)**. A SBOM is a formal, machine-readable
inventory of all components in a software artifact. It takes every library, every dependancy, every version, and catalogues it
in a standardized fashion. This way, SBOMs make the opaque transparent. They are generated during the software build process by
scanning components. For securoty-conscious organizations SBOMs are not just good practice. They are increasingly mandatory.
