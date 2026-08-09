# Tools and Automation

> Covers SBOM generation, management, and scanning tools, and where automation ends and human responsibility begins.

---

LLMS index: [llms.txt](/llms.txt)

---

An SBOM workflow is not completed by a single tool. The three capabilities of generation,
vulnerability matching, and lifecycle management are split across different tools, and the
common conclusion of recent tool comparison analyses is that no single tool covers all three
areas completely. It is more accurate to think of it as assembling a pipeline from a combination
of tools.

## The Division of Labor Among Generation, Management, and Scanning

![Three categories of SBOM tools — generation, management, and matching — divide roles, with management and matching exchanging data on every new vulnerability](./tool-roles-en.png)

**Figure 1.** The three roles of SBOM tools *(source: compiled from tool comparison analyses,
2026-01. Retrieved 2026-06-14)*

In the generation space, Anchore's Syft is regarded as "the dedicated tool that does SBOM
generation, and only that, best." Its attestation workflow, combined with the signing tool
cosign, is mature. OWASP CycloneDX's cdxgen is distinguished by broad support for multiple
languages and container images, and by a dedicated AI BOM mode.

In the management space, OWASP Dependency-Track has established itself as a platform for
monitoring component usage and security/license compliance across an organization's entire
application portfolio. Eclipse SW360 is another option centered on license compliance.

In the scanning space, Grype takes an SBOM as input and matches it against vulnerabilities,
while Aqua Security's Trivy is both a scanner and an SBOM generator.

| Role | Representative open source tools | Characteristics |
|---|---|---|
| Generation | Syft, cdxgen | Syft is generation-only with mature attestation; cdxgen offers multi-language support and an AI BOM mode |
| Management | Dependency-Track, SW360 | Portfolio monitoring, license and vulnerability tracking |
| Matching/Scanning | Grype, Trivy | Matches an SBOM against a vulnerability database |

**Table 1.** Classification of SBOM tools by role *(source: compiled from tool comparison
analyses, 2026-01. Retrieved 2026-06-14)*

## How Far Does Automation Go

It is important to honestly distinguish between areas where automation works well and areas that
people must fill in.

| Task | Automation maturity |
|---|---|
| Code/dependency SBOM generation | Mature |
| Container image component identification | Mature |
| SBOM storage and vulnerability monitoring | Mature |
| Automated license identifier extraction | Partial (requires review) |
| Interpreting non-standard licenses and tracking compliance | Immature (people/policy) |

**Table 2.** Automation maturity of SBOM tasks *(source: compiled from tool comparison analyses.
Retrieved 2026-06-14)*

Tools do generation well. Put Syft or cdxgen into the build pipeline, and the component list
fills in automatically. But whether the license field of a generated SBOM is accurate, whether
the obligations of a non-standard license are met, and whether obligations propagate downstream
without omission are things no tool guarantees automatically. This area is filled by policy and
human review.

## The Tool Itself Is an Attack Surface

Before trusting an automation tool, its own integrity must be verified. In January 2026, a case
was reported in which an SBOM tool was implicated in two supply chain attacks within a short
period, with the damage spreading to downstream projects. On this basis, some pipeline operators
removed the tool in question.

The fact that an SBOM generation tool can itself become a target of supply chain risk requires
combining hashes, signatures, and attestations at the generation and verification stages. This
same concern lies behind CISA's 2025 minimum elements draft adding Tool Name, Generation Context,
and Component Hash as new fields. Avoiding the paradox that "an SBOM made by an untrustworthy
tool cannot be trusted" requires pinning tool versions, verifying provenance, and signing the
output.

## Sources

Anchore. *Syft* <https://github.com/anchore/syft>, *Grype* <https://github.com/anchore/grype>.
OWASP. *cdxgen* <https://github.com/CycloneDX/cdxgen>, *Dependency-Track*
<https://dependencytrack.org/>. Aqua Security. *Trivy*
<https://github.com/aquasecurity/trivy>. Eclipse *SW360* <https://www.eclipse.org/sw360/>.
(All retrieved: 2026-06-14)
