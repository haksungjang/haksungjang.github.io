---
title: "Minimum Elements of an SBOM"
linkTitle: "Minimum Elements"
weight: 10
type: docs
categories: ["guide"]
tags: ["NTIA", "CISA", "Minimum Elements", "Data Fields"]
description: >
  Covers the data fields an SBOM must contain, from the NTIA 2021 minimum elements to the
  CISA 2025 revision draft.
---

Once a format is chosen, the next question is what that format must contain. The documents that
define this floor are the US Minimum Elements series. Though they are recommendations, they
function as the de facto standard for federal procurement, and SBOM requirements in the EU and
other jurisdictions largely reference this same framework.

## Lineage: From NTIA 2021 to CISA 2025

The National Telecommunications and Information Administration (NTIA) published *The Minimum
Elements For a Software Bill of Materials (SBOM)* in July 2021, under the delegation of
Executive Order 14028. The document organized the minimum elements into three categories: the
data fields to track per component, automation support requiring a machine-readable format, and
practices and processes covering generation frequency, depth, and the like.

Stewardship of the community's work then moved to the Cybersecurity and Infrastructure Security
Agency (CISA), and two lines of revision followed. One was the third edition (September 2024) of
*Framing Software Component Transparency*, a reference document that defines attributes, which
added License and Copyright Notice to the baseline attributes. The other was a revision of the
minimum elements document itself: CISA released *2025 Minimum Elements for a Software Bill of
Materials* as a public comment draft in August 2025, with the comment period closing on
October 3, 2025. As of June 2026, this revision remains in draft status, and the date of a final
version has not been confirmed.

## The Data Fields and Three Categories of NTIA 2021

The NTIA 2021 minimum elements set seven per-component data fields.

| Data field | Description |
|---|---|
| Supplier Name | The entity that supplied the component |
| Component Name | The name of the component or library |
| Version | The version identifier of the component |
| Other Unique Identifiers | Identifiers such as PURL, CPE |
| Dependency Relationship | The inclusion relationship with the parent component |
| Author of SBOM Data | The entity that generated this SBOM |
| Timestamp | The date and time of generation |

The three categories are as follows.

- **Data fields**: The seven items above — the basic information for tracking and identifying
  components.
- Automation support: Specified SPDX, CycloneDX, and SWID as standard formats for automated
  generation and machine readability.
- Practices and processes: Covers generation frequency, depth, handling of known unknowns,
  distribution and delivery, access control, and how errors are accommodated.

## What the CISA 2025 Draft Adds

The CISA 2025 minimum elements draft expanded the data fields to reflect the maturing state of
tooling. Four core elements were newly added.

| New field | Purpose |
|---|---|
| Component Hash | Ensures integrity and precise identification through a cryptographic hash |
| License | Primary data for tracking legal compliance |
| Tool Name | Records which tool generated it |
| Generation Context | Records at which stage of the lifecycle it was created |

Existing items were also revised. The roles of SBOM Author and Software Producer were
distinguished, "Other Unique Identifiers" was updated to "Software Identifiers," and the access
control element, previously separate, was folded into the distribution and delivery item. The
trajectory of License — entering as a baseline attribute in Framing 3rd edition and hardening
into a data field in the 2025 draft — shows that the SBOM is establishing itself as primary data
for open source license compliance, beyond a security inventory. Behind adding Tool Name,
Generation Context, and Hash together lies the concern that an SBOM produced by an untrustworthy
tool cannot itself be trusted. Tool integrity is covered in
[5. Tools and Automation](../../5-tools/).

## Practical Recommendations

The minimum elements are, as the name says, a floor. Organizations can, and should, add fields
suited to their own purposes. Carrying CVE references and patch status for vulnerability
identification, SPDX license identifiers and copyright notices for license management, and
release and End-of-Life dates for lifecycle management, together in one SBOM, lets a single SBOM
answer multiple operational questions. If you are introducing an SBOM for the first time,
starting with the NTIA seven fields as a base but including the four new fields from the CISA
2025 draft — especially hash and license — from the outset saves the effort of rebuilding it
later.

## Sources

NTIA (2021). *The Minimum Elements For a Software Bill of Materials (SBOM)*.
<https://www.ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf>. CISA (2024).
*Framing Software Component Transparency*, Third Edition.
<https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024>.
CISA (2025). *2025 Minimum Elements for a Software Bill of Materials (SBOM)* (public comment
draft). <https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom>.
(All retrieved: 2026-06-14)
