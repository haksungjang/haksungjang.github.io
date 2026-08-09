---
title: "Sharing and Governance"
linkTitle: "7. Sharing and Governance"
weight: 70
type: docs
categories: ["guide"]
tags: ["Access Control", "Sharing", "Governance"]
description: >
  Summarizes SBOM access control and disclosure scope, secure sharing channels, and
  roles-and-responsibilities governance.
---

An SBOM creates value only when it is delivered along the supply chain, but it is also sensitive
material that contains trade secrets and attack surface. Without governance that determines who
shares what, and how, excessive disclosure heightens risk, and excessive restriction forfeits value.

## Access Control and Disclosure Scope

Access to SBOM data is managed through Role-Based Access Control (RBAC). Because access needs
differ by stakeholder, general users are granted read-only access, administrators are granted edit
and update access, and sensitive information is granted restricted access.

For disclosure scope, maintaining two versions is common practice.

- **Public SBOM**: Contains non-sensitive information that can be shared with all stakeholders.
- Private SBOM: Contains sensitive information, such as vulnerabilities, and only approved parties can access it.

Regulation reflects this distinction as well. The EU Cyber Resilience Act does not require an SBOM
to be disclosed to the general public, but requires it to be retained in case market surveillance
authorities request it. Amid the tension between consumers wanting a more complete SBOM and
producers wanting to reduce disclosure, the public/private split is a practical device that
reconciles the two.

## Secure Sharing Channels

When delivering an SBOM, both integrity and confidentiality need to be preserved.

- Use a secure protocol such as HTTPS for transmission, and ensure integrity and confidentiality through digital signatures or encryption.
- Use a sharing platform equipped with access control and audit capabilities.
- Use API integration for automated exchange between systems, and dedicated repositories for industry- or community-level sharing.

Attach a digital signature to the document so recipients can verify its authenticity and check for
tampering, and clearly mark which information is public and which is private.

## Roles and Responsibilities

An SBOM program works only when multiple departments share responsibility for it. It should
include an executive sponsor, project leads, systems and design engineers, procurement
specialists, and operations personnel, adding IT, cybersecurity, and maintenance staff as security
needs require. When roles are scattered, responsibility scatters with them, so establishing clear
ownership is the starting point.

The key activities in building governance are as follows.

- Identify key stakeholders: Include representatives from development, IT operations, security,
  procurement, legal, and business leadership, and be sure to include a cybersecurity expert.
- Define responsibilities and assign ownership: Decide who will handle SBOM generation and
  consumption, vulnerability monitoring, supplier engagement, and security data management, and
  designate a cybersecurity expert as the program owner or co-owner.
- Establish a governance structure: A governance body with participation from stakeholders across
  the organization develops policies, standards, and processes, and implements data protection
  controls.
- Train and monitor: Train personnel on SBOM security requirements and secure data handling, and
  continuously assess the program's security posture through regular audits, adjusting it to
  evolving threats and compliance requirements.

## Sources

CISA (2024). *Framing Software Component Transparency*, Third Edition. CERT-In. *Technical Guidelines
on Software Bill of Materials (SBOM)*. Regulation (EU) 2024/2847 — Cyber Resilience Act, Annex I
Part II. (all accessed: June 14, 2026)
