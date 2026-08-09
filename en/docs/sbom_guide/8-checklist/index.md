# Recommendations and Checklist

> Collects the key recommendations from the preceding sections and provides a checklist for reviewing SBOM adoption.

---

LLMS index: [llms.txt](/llms.txt)

---

This section organizes the content covered in the preceding sections into practical
recommendations and a checklist. Organizations adopting SBOM for the first time can follow the
checklist in order, while organizations already operating one can use it to check for missing
items.

## Key Recommendations

### Procurement and Generation

- When procuring software, specify the SBOM provision requirement in contracts and purchase terms.
  Specify which elements are to be provided, in what format, and when.
- Generate SBOMs in the SPDX or CycloneDX format, choosing based on your counterparty's
  requirements and your own toolchain.
- Automatically generate SBOMs at build time within the SSDLC and CI/CD pipeline to ensure
  accuracy and timeliness.
- Put in place a workflow to regenerate the SBOM whenever a new component is introduced or an
  existing component is updated.

### Data Quality

- Include complete metadata such as component name, version, license, and unique identifier.
  Because the minimum elements are only a floor, add fields to fit your own use case.
- Pin components with [PURL or CPE](../2-standards/2-identifiers/) so that traceability is not lost
  even when names or versions change.
- Pin the version of the generation tool, verify its provenance, and attach hashes and signatures
  to the output to ensure integrity.

### Vulnerabilities and Licenses

- Link the SBOM to vulnerability databases and advisories to maintain continuous visibility into
  security posture.
- Reflect any applied patches or mitigations in your own SBOM.
- Exchange vulnerability exploitability status using VEX and CSAF, and prioritize response based on
  risk.
- Analyze the license compatibility of all components to identify conflicts that may arise from
  combining them, in advance.

### Storage and Operations

- Store and transmit SBOMs securely using encryption and access control, and clearly distinguish
  between public and private scope.
- Check the accuracy and completeness of SBOMs through regular audits.
- Run training and awareness programs on the role of SBOM, from developers to the security team.

## Adoption Checklist

A checklist for reviewing what has been done at each stage.

| Stage | Checklist Item |
|---|---|
| Foundational | Identify critical assets and establish an adoption plan |
| Foundational | Decide on the SBOM format (SPDX/CycloneDX) and minimum data requirements |
| Foundational | Select a secure repository and tools |
| Foundational | Reflect the SBOM provision requirement in procurement contracts |
| Developing | Assign unique identifiers to components |
| Developing | Map supplier SBOMs to internal SBOMs |
| Developing | Integrate automatic SBOM generation into the build pipeline (CI/CD) |
| Developing | Apply secure configuration management, including access control and encryption |
| Scaling | Track SBOM linked with vulnerability databases |
| Scaling | Integrate VEX/CSAF-based exploitability management with incident response |
| Scaling | Run regular review, audits, and awareness programs |

## Next Steps

If you develop AI systems or exchange them across the supply chain, you need to add an AI-specific
layer — models, datasets, and training compute — on top of the SBOM capabilities covered in this
guide. The component, license, and vulnerability management practices of a general SBOM carry over
directly into the software layer of an AI BOM. This is covered in detail in the separate
[AI SBOM Compliance Guide](../../ai-sbom_guide/).

## Sources

NTIA (2021). *The Minimum Elements For a Software Bill of Materials (SBOM)*. CISA (2024). *Framing
Software Component Transparency*, Third Edition. CERT-In. *Technical Guidelines on Software Bill of
Materials (SBOM)*. Regulation (EU) 2024/2847 — Cyber Resilience Act. (all accessed:
June 14, 2026)
