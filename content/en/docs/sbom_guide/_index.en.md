---
title: "A Practical Guide to SBOM (Software Bill of Materials)"
linkTitle: "SBOM Practical Guide"
weight: 40
type: docs
categories: ["guide"]
tags: ["SBOM", "Supply Chain Security", "SPDX", "CycloneDX", "VEX", "CRA"]
description: >
  A guide covering the Software Bill of Materials (SBOM), from its concepts and standard formats
  to regulatory trends, adoption roadmap, tools, vulnerability management, and governance,
  organized from the perspective of practitioners in Korea.
---

A Software Bill of Materials (SBOM) is a formal record of what components make up a piece of
software and how those components connect within the supply chain. A US executive order compares
it to the ingredient list on food packaging. Just as an ingredient list is the starting point for
responding to allergies, an SBOM is the data layer on which vulnerability response, license
management, and asset management all rest. An SBOM is not a security tool in itself, but without
one, an organization cannot immediately answer the question, "Where in our product is this library
used?"

This guide covers that data layer from beginning to end. Drawing on primary sources, it explains
why SBOM has moved to the forefront of regulation and procurement, what standards and identifiers
underpin it, in what order organizations adopt it and with what tools they automate it, how they
manage vulnerabilities and licenses, and how they share it securely across the supply chain.

## Intended Audience

- Security, development, procurement, and legal staff at organizations that develop or procure
  software
- Practitioners who must respond to the EU Cyber Resilience Act (CRA) or US federal procurement
  requirements
- Teams seeking to establish supply chain transparency and open source license compliance systems

## Guide Structure

The guide is divided into eight sections. The earlier sections cover concepts, standards, and
regulation, while the later sections cover the practicalities of adoption and operation. You can
read only the sections you need.

| Section | Content | Link |
|---|---|---|
| 1. Overview | SBOM definition, supply chain threats and benefits, levels and classification | [View](./1-overview/) |
| 2. Standards and Formats | SPDX, CycloneDX, minimum elements, identifiers and licenses | [View](./2-standards/) |
| 3. Regulatory Trends | United States, EU CRA, India, and Korea | [View](./3-regulation/) |
| 4. Adoption Roadmap | Step-by-step activities from building the foundation to operational maturity | [View](./4-adoption/) |
| 5. Tools and Automation | Generation, management, and scanning tools, and automation maturity | [View](./5-tools/) |
| 6. Vulnerability Management | SBOM-based tracking, VEX, CSAF, the Log4j case | [View](./6-vulnerability/) |
| 7. Sharing and Governance | Access control, disclosure scope, sharing channels, roles and responsibilities | [View](./7-governance/) |
| 8. Recommendations and Checklist | Key recommendations and an adoption checklist | [View](./8-checklist/) |

## Quick Starting Points

If you already understand SBOM and are looking for where to start, see
[4. Adoption Roadmap](./4-adoption/) and [8. Recommendations and Checklist](./8-checklist/) first.
If you are deciding which format and tools to use, [2. Standards and Formats](./2-standards/) and
[5. Tools and Automation](./5-tools/) are good starting points. If your goal is regulatory
compliance, check the jurisdiction-specific obligations in [3. Regulatory Trends](./3-regulation/).

## Sources and Editorial Basis

This guide is not a translation of any single document; it is a reconstruction that synthesizes
current primary sources. It draws on the National Telecommunications and Information
Administration (NTIA)'s 2021 minimum elements and its update by the Cybersecurity and
Infrastructure Security Agency (CISA) — the 2024 *Framing Software Component Transparency*, Third
Edition, and the 2025 draft revision of the minimum elements — as well as the SPDX and CycloneDX
standard specifications, the EU Cyber Resilience Act (Regulation (EU) 2024/2847), and the supply
chain security guidelines of India's CERT-In and Korea. The first edition began as a translation of
CERT-In's SBOM technical guidelines; the current edition updates that framework with the sources
above and broadens it to a general practitioner's perspective.

Every factual claim is cited to a primary source, and the materials cited were accessed on
June 14, 2026.

**Author : [Haksung Jang](https://haksungjang.github.io/)**
