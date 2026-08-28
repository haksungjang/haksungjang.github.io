---
title: "AI SBOM Compliance Guide"
linkTitle: "AI SBOM Compliance Guide"
weight: 45
type: docs
categories: ["guide"]
tags: ["AI SBOM", "OpenChain", "ISO/IEC 5230", "ISO/IEC 42001", "Compliance"]
description: >
  An enterprise practice guide that explains the requirements of the OpenChain AI SBOM
  Compliance Guide (Version 1.0) clause by clause.
---

This guide explains, one by one, each requirement of *AI System Bill of Materials — Compliance
Management Guide for the Supply Chain* (Version 1.0), published by the OpenChain AI Work Group.
It walks through what verification material each clause requires, how to comply with it, and
what samples and tools are ready to use.

This specification carries the same structure as ISO/IEC 5230, the open source license
compliance standard — requirements, verification material, and rationale — over into the AI
supply chain. It brings into scope not only code but also the licensing and transparency
obligations of model weights, training datasets, and the Model Tree.

**Author : OpenChain Korea Work Group / [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**

{{% alert title="Note" color="info" %}}
All 10 requirements (3.1–3.10) per the specification body have been written. The compare page
that positions the standards relative to each other is still being expanded.
{{% /alert %}}

## Intended Audience

- Compliance staff at organizations that develop AI systems or exchange them through the supply chain
- Practitioners who have an open source compliance (ISO/IEC 5230) program in place and want to extend it into AI
- Legal, security, and development staff who need to check the licensing and transparency obligations of AI models and datasets

## How to Use This Guide

{{% alert title="Division of Roles Between the OpenChain Specification and the KWG Practice Guide" color="success" %}}
The OpenChain specification defines "what must be demonstrated." This guide fills in "how to
achieve it." Each clause page does more than restate the specification's requirements — it walks
through the actual procedures, samples, tools, and how to handle the parts that tools alone
cannot fill.
{{% /alert %}}

{{% alert title="Notation — [Specification Requirement] vs [Guide Recommendation]" color="info" %}}
The content of each clause page falls into two categories.

- **[Specification Requirement]** — Items the AI SBOM Compliance Guide body specifies with
  `shall` or as verification material.
- **[Guide Recommendation]** — Items not found in the specification body but recommended by the
  OpenChain Korea Work Group based on practical experience, best practices, and other standards
  (ISO/IEC 5230, 42001, etc.). Adoption is at the organization's discretion.

Activities presented alongside a verification material number (e.g., `3.1.1`) are
**[Specification Requirement]**. Enhancements this guide adds, such as automation, tool use, and
intake gates, are **[Guide Recommendation]**.
{{% /alert %}}

{{% alert title="Note on Clause Numbering" color="info" %}}
The original specification's table of contents and body section numbers are out of sync (the
"3.9 AI content review and approval" section listed in the table of contents does not appear in
the body, shifting all subsequent numbers down by one). This discrepancy has been reported to
the OpenChain AI Work Group. This guide follows the **body's section numbers (3.1–3.10)**.
{{% /alert %}}

## Phased Implementation Roadmap

The 10 requirements are divided into four phases by implementation priority. Phase 1 establishes
the program's foundation, Phase 2 builds AI-specific compliance processes, Phase 3 puts
operational structures in place, and Phase 4 establishes governance.

---

### Phase 1 — Program Foundation

**Goal**: Define the program's scope, establish policy, and secure competence and awareness.

| Done | Verification Material | Description | Detailed Guide |
|:----:|---------|------|------------|
| ☐ | **3.4.1** | Program scope statement | [3.4 →](./1-program-foundation/4-scope/) |
| ☐ | **3.1.1** | Documented AI SBOM policy | [3.1 →](./1-program-foundation/1-policy/) |
| ☐ | **3.1.2** | Policy awareness procedure | [3.1 →](./1-program-foundation/1-policy/) |
| ☐ | **3.2.1~3.2.3** | Role list, competence definitions, competence assessment evidence | [3.2 →](./1-program-foundation/2-competence/) |
| ☐ | **3.3.1** | Evidence of participant awareness assessment | [3.3 →](./1-program-foundation/3-awareness/) |

---

### Phase 2 — AI Extension Processes

**Goal**: Build AI-specific licensing, transparency, and SBOM processes that cover not just code
but also models, weights, and datasets. This is the area where the AI SBOM Guide expands most on
ISO/IEC 5230.

| Done | Verification Material | Description | Detailed Guide |
|:----:|---------|------|------------|
| ☐ | **3.5.1** | License obligation review and documentation procedure | [3.5 →](./2-ai-extension/1-license-obligations/) |
| ☐ | **3.6.1** | Transparency obligation review procedure | [3.6 →](./2-ai-extension/2-transparency-obligations/) |
| ☐ | **3.9.1** | AI SBOM identification, tracking, review, approval, and archiving procedure | [3.9 →](./2-ai-extension/3-ai-sbom/) |
| ☐ | **3.9.2** | Records demonstrating procedure compliance | [3.9 →](./2-ai-extension/3-ai-sbom/) |

---

### Phase 3 — Operational Structure

**Goal**: Create a channel for responding to external compliance inquiries, and assign
accountability and resources to the program.

| Done | Verification Material | Description | Detailed Guide |
|:----:|---------|------|------------|
| ☐ | **3.7.1~3.7.2** | Public inquiry channel, internal response procedure | [3.7 →](./3-relevant-tasks/1-access/) |
| ☐ | **3.8.1~3.8.5** | Role assignment, resources, legal expertise, remediation procedure | [3.8 →](./3-relevant-tasks/2-resourced/) |

---

### Phase 4 — Governance

**Goal**: Put in place a governance framework spanning the full AI system lifecycle, and reflect
emerging AI regulation.

| Done | Verification Material | Description | Detailed Guide |
|:----:|---------|------|------------|
| ☐ | **3.10.1** | AI governance framework and periodic review procedure | [3.10 →](./4-governance/1-governance/) |

---

## Full Clause Checklist

The body of the AI SBOM Compliance Guide consists of **10 clauses and 19 verification material
items** in total (by this guide's verification material numbering).

| Clause | Title | Verification Material | Detail |
|------|------|:---:|------|
| 3.1 | Policy | 2 items | [Go to →](./1-program-foundation/1-policy/) |
| 3.2 | Competence | 3 items | [Go to →](./1-program-foundation/2-competence/) |
| 3.3 | Awareness | 1 item | [Go to →](./1-program-foundation/3-awareness/) |
| 3.4 | Program Scope | 1 item | [Go to →](./1-program-foundation/4-scope/) |
| 3.5 | License Obligations | 1 item | [Go to →](./2-ai-extension/1-license-obligations/) |
| 3.6 | Transparency Obligations | 1 item | [Go to →](./2-ai-extension/2-transparency-obligations/) |
| 3.7 | Access | 2 items | [Go to →](./3-relevant-tasks/1-access/) |
| 3.8 | Effectively Resourced | 5 items | [Go to →](./3-relevant-tasks/2-resourced/) |
| 3.9 | AI SBOM | 2 items | [Go to →](./2-ai-extension/3-ai-sbom/) |
| 3.10 | Governance | 1 item | [Go to →](./4-governance/1-governance/) |

**Total: 10 clauses / 19 verification material items**

## Automation Maturity Map

This is an honest breakdown of how far each AI SBOM compliance task is automated by tools today.
For "generation," usable open source tools already exist. Interpreting license obligations and
tracking compliance with non-standard licenses, on the other hand, remain the work of people and
policy. Each clause page follows this line to distinguish "what a tool handles" from "what a
person must fill in."

| Task | Automation Level | Representative Open Source Tool |
|------|------------|-------------------|
| Code/dependency SBOM generation | Mature | cdxgen, Syft |
| AI model/metadata BOM generation | Tools emerging | OWASP AIBOM Generator, cdxgen `aibom` mode |
| Static analysis of model binaries | Tools emerging | Lab700x AI SBOM Scanner |
| Identifying LLM inference servers and AI packages | Mature | Trivy, Syft |
| SBOM storage and vulnerability monitoring | Mature | Dependency-Track, SW360 |
| Interpreting license obligations, tracking non-standard compliance | Immature (people/policy) | Tool support still developing |

{{% alert title="Generation by Tool, Interpretation by People" color="info" %}}
Several tools already generate AI SBOMs automatically. But whether the license fields in a
generated BOM are accurate, whether the behavioral use restrictions of non-standard licenses
(the RAIL family, the Llama Community License) are respected, and whether obligations propagate
downstream without being dropped — a tool cannot automatically guarantee any of this. Policy and
human review fill this gap. See [3.5 License Obligations](./2-ai-extension/1-license-obligations/)
for details.
{{% /alert %}}

The installation and use of each tool is covered with execution screens and command output in
the [Tools](./5-tools/) section.

## Relationship to Other Standards

{{% alert title="Relationship to ISO/IEC 5230 and 42001" color="info" %}}
- **ISO/IEC 5230 (License Compliance)**: The AI SBOM Guide inherits the 5230 methodology
  directly. Organizations that already have a 5230 program in place can reuse program
  foundations such as policy, competence, and resources, and only need to add the AI extension
  areas. See the [ISO/IEC 5230 Compliance Guide](https://openchain-project.github.io/OpenChain-KWG/guide/iso5230_guide/).
- **ISO/IEC 42001 (AI Management System)**: The technical details of AI SBOM formats (SPDX 3.0 AI
  Profile, CycloneDX ML-BOM) and generation tools are covered in the
  [ISO/IEC 42001 Guide — AI SBOM](https://openchain-project.github.io/OpenChain-KWG/guide/iso42001_guide/4-operation/2-ai-sbom/).
  Building on that, this guide focuses on "how to operate the compliance program."
{{% /alert %}}

## Original Specification

{{% pageinfo %}}
- **Document**: Artificial Intelligence System Bill of Materials — Compliance Management Guide for
  the Supply Chain, Version 1.0
- **Published**: OpenChain Project AI Work Group, 2025-10-20
- **License**: Creative Commons Attribution 4.0 (CC-BY-4.0)
- **Authoritative copy**: Published as PDF and markdown in the OpenChain Reference-Material
  repository (`AI-SBOM-Compliance/en`)
- **Announcement**: [openchainproject.org](https://openchainproject.org/news/2025/10/20/welcoming-the-openchain-ai-system-bill-of-materials-compliance-guide)
{{% /pageinfo %}}
