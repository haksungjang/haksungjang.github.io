---
title: "Standards and Formats"
linkTitle: "2. Standards and Formats"
weight: 20
type: docs
categories: ["guide"]
tags: ["SPDX", "CycloneDX", "Standards"]
description: >
  Compares SPDX and CycloneDX, the two standard formats for expressing an SBOM in a
  machine-readable form.
---

Since an SBOM requires machine readability, a standard format is necessary. Among the three
formats specified by the US NTIA minimum elements, SPDX and CycloneDX split practical use between
them. The third, the SWID tag, is used mainly in asset management; its role as an identifier is
covered in [Identifiers and Licenses](./2-identifiers/).

## SPDX

SPDX (System Package Data Exchange) is a project under the Linux Foundation. Version 2.2.1
became an international standard as ISO/IEC 5962:2021 in August 2021. It is worth noting that
the current ISO standard refers strictly to version 2.2.1.

The Linux Foundation released SPDX 3.0 on April 16, 2024, introducing a structure of
purpose-specific profiles. The approach layers Security, Build, Dataset, and AI profiles on top
of a core model. The AI profile carries model training and characterization information, the
Dataset profile carries data provenance and licensing, and the Security profile carries
vulnerability identification, severity, exploitability, and mitigation plans. A patch release,
3.0.1, followed in December of the same year. Whether SPDX 3.x is being re-standardized with ISO
had not been confirmed as of June 2026.

## CycloneDX

CycloneDX is a full-stack BOM standard that originated at OWASP (Open Worldwide Application
Security Project). Its distinguishing feature is native support for Vulnerability Exploitability
eXchange (VEX) within the format itself. International standardization proceeded through Ecma
International's technical committee TC54. Version 1.6 was published as ECMA-424 1st edition in
June 2024, adding a Cryptographic Bill of Materials (CBOM) and CycloneDX Attestations, and v1.7
was announced in October 2025 and standardized as ECMA-424 2nd edition in December 2025. v1.7
added post-quantum cryptography readiness, structured citations, and support for patent objects.

CycloneDX can express software (SBOM), hardware (HBOM), services (SaaSBOM), and machine learning
models (ML-BOM) all within a single format.

## Comparing the Two Formats

| | SPDX | CycloneDX |
|---|---|---|
| Steward | Linux Foundation | OWASP / Ecma TC54 |
| International standard | ISO/IEC 5962:2021 (based on v2.2.1) | ECMA-424 1st edition (v1.6, 2024-06), 2nd edition (v1.7, 2025-12) |
| Latest specification | 3.0 (2024-04), 3.0.1 (2024-12) | 1.7 (2025-10) |
| Extension mechanism | Purpose-specific profiles (Security, Build, Dataset, AI) | Component types and auxiliary objects, native VEX |
| Strengths | License expression and legal compliance history | Vulnerability/VEX integration, security-operations friendly |

**Table 1.** Comparison of the two major SBOM standard formats *(source: ISO/IEC 5962:2021,
Linux Foundation 2024, Ecma International ECMA-424. Retrieved 2026-06-14)*

The two standards differ in design philosophy. SPDX extends its scope of application through
profiles, while CycloneDX expresses it through component types and auxiliary objects. Both,
however, target the same problem in that they carry component identification, licensing, and
dependency relationships. Whichever you choose, conversion tools exist between the two formats,
so you can choose based on the format your trading partners require and the format your own tool
chain supports well. If license compliance is the focus, SPDX is the familiar starting point; if
vulnerability operations is the focus, CycloneDX is.

Next, we look at the [minimum elements](./1-minimum-elements/) that define what a format must
contain, and [identifiers and licenses](./2-identifiers/) for consistently pointing to
components.

## Sources

ISO/IEC (2021). *ISO/IEC 5962:2021 — SPDX Specification V2.2.1*. The Linux Foundation (2024).
*SPDX 3.0 Release*. <https://www.linuxfoundation.org/press/spdx-3-revolutionizes-software-management-in-systems-with-enhanced-functionality-and-streamlined-use-cases>.
Ecma International. *ECMA-424 — CycloneDX Bill of Materials Specification*.
<https://ecma-international.org/publications-and-standards/standards/ecma-424/>. CycloneDX (2025).
*CycloneDX v1.7 Released*. <https://cyclonedx.org/news/cyclonedx-v1.7-released/>. (All retrieved: 2026-06-14)
