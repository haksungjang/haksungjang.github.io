---
title: "3.10 Governance"
weight: 10
type: docs
categories: ["guide"]
tags: ["AI SBOM", "Governance", "AI Regulation"]
description: >
  Explains how to establish a governance framework spanning the full AI system lifecycle and
  review it periodically to reflect emerging AI regulation.
---

{{% alert title="Implementation Phase" color="info" %}}
This clause is built during **Phase 4 — Governance**.
[View the full implementation roadmap](../../#phased-implementation-roadmap)
{{% /alert %}}

## 1. Clause Overview

Governance is the framework that ties all the preceding clauses together to ensure the AI
system's lifecycle is developed, deployed, and managed responsibly from end to end. Where policy
(3.1) sets the principles and license obligations (3.5) and the AI SBOM (3.9) build individual
processes, governance manages these so they keep operating consistently through regulatory change
and model replacement.

3.10 requires an AI governance framework, policies, and practices. The specification emphasizes
compliance with emerging AI laws such as the EU AI Act, the Hiroshima AI Process, and China's
Global AI Governance Initiative, and addresses ethical considerations, risk management, and
transparency together. The core is to review a framework, once built, periodically so it reflects
the latest regulation and model changes.

## 2. Activities to Perform

- Write a governance framework document that spans the full AI system lifecycle.
- Include emerging AI regulation tracking, risk management, transparency, and ethical
  considerations in the framework.
- Have a procedure for periodically reviewing and updating the framework.
- Monitor the risks that come with the ongoing use of AI systems and training data.
- Reflect events such as model tree changes, regulatory enforcement, and OSAID classification
  changes in governance. *([Guide Recommendation])*

## 3. Requirement and Verification Material

| Clause | Requirement | Verification Material |
|-----------|--------------|---------|
| 3.10 | The organization shall have an AI governance framework, policies, and practices that help ensure AI systems are developed, deployed, and managed responsibly. This shall emphasize compliance with emerging AI laws (the EU AI Act, the Hiroshima AI Process, China's initiative) and address ethical considerations, risk management, and transparency. | **3.10.1** A documented AI governance framework for the AI system lifecycle, including a procedure for periodically reviewing the framework |

<details><summary>View original English text</summary>

> **3.10 Governance**
> An organization shall have a governance framework for AI, policies, and practices to help ensure
> that AI systems are developed, deployed, and managed responsibly. Governance emphasizes compliance
> with emerging AI laws and regulations, such as the EU AI Act, Hiroshima AI process or Global AI
> Governance Initiative (China), and addresses ethical considerations, risk management, and
> transparency. For example, understand the risks associated with ongoing use of AI Systems and
> training data in the context of their intended Programs. This could include the ability to monitor
> the lifecycle of the AI system and perform ongoing analysis of its intended uses.
>
> **Verification material(s):**
> - A documented AI governance framework for the lifecycle of an AI system with a process to review
>   the framework periodically.

</details>

## 4. How to Comply with Each Verification Material, with Samples

### 3.10.1 AI Governance Framework and Periodic Review Procedure

**How to Comply**

The governance framework covers three things: tracking emerging regulation to derive obligations,
monitoring the AI system lifecycle, and a procedure for periodically reviewing the framework
itself. Because regulation changes quickly, the framework must be a living system built for
updates, not a fixed document.

The three axes the specification names differ in character. The EU AI Act imposes concrete,
article-level obligations; the Hiroshima AI Process runs voluntary transparency reporting; and
China's initiative is closer to a policy declaration. Governance distinguishes these differences
and tracks each accordingly.

The table below lists the major regulations to track from an AI SBOM perspective. The full
regulatory matrix and its ISO/IEC 42001 context are covered in [ISO/IEC 42001 Guide —
Organizational Context and
Leadership](https://openchain-project.github.io/OpenChain-KWG/guide/iso42001_guide/1-context-leadership/).

**Table 1.** Major AI regulations intersecting with AI SBOM (as of 2026-06)

| Regulation/Initiative | Timing | Core AI SBOM-Relevant Obligation | Governance Reflection |
|---|---|---|---|
| EU AI Act Article 11 + Annex IV | 2027 (high-risk) | Technical documentation obligation | Produce the AI SBOM as a core element of the technical documentation |
| EU AI Act Article 53 (GPAI) | 2026-08 | Disclosure of a training data summary, respecting copyright opt-outs | Track dataset provenance and licensing |
| EU AI Act Article 50 | 2026-08 | Labeling of AI-generated content | Links to the transparency obligation (3.6) |
| Hiroshima AI Process | Launched 2025, Reporting 2.0 (2026-05) | Voluntary transparency reporting | Consider participating in the OECD reporting framework |
| China's Global AI Governance Initiative | Announced 2023 | Policy declaration (no concrete deliverable) | Monitor trends |
| Korea's AI Basic Act | Effective 2026-01 | High-impact AI impact assessment, labeling obligation, disclosure of training data provenance | AI SBOM and model card production |

Lifecycle monitoring means placing governance checkpoints along the flow from development to
retirement. The figure below shows lifecycle governance built around the AI SBOM.

![Governance cycle that runs from model intake through development, review, deployment, and
operational monitoring, looping back to development or review depending on the type of change](./governance-cycle.png)

**Figure 1.** Lifecycle governance built around the AI SBOM

**Considerations**

- **Assign regulatory-tracking responsibility**: Specify in governance who tracks emerging
  regulation and derives obligations from it. The EU AI Act's obligations expand in stages in
  August 2026 and 2027, so manage the timing.
- **Manage model tree changes**: When an imported model moves to a new version or a parent model
  is replaced, license obligations can change. Register the change as a governance review event.
  *([Guide Recommendation])*
- **Update OSAID classification**: The distinction between "open source AI" and "open weight"
  (OSAID 1.0) affects model licensing judgments. Include classification changes in the periodic
  review.
- **State the review cycle**: Review model and dataset changes quarterly, and regulation and the
  overall framework annually. Record the review completion date and reviewer.
- **Connect to other clauses**: Governance ties together the regulatory review under the
  transparency obligation (3.6) and the lifecycle management under the AI SBOM (3.9) from above.
  Connect them rather than building duplicate procedures.

**Sample (Governance Framework and Annual Review Plan)**

Below is a sample of the core part of a governance framework document and periodic review plan.
This document becomes verification material 3.10.1.

```
## AI Governance Framework

### 1. Scope and Purpose
Manages licensing, transparency, risk, and regulatory compliance across the full
lifecycle of an AI system — intake, development, deployment, operation, and
retirement.

### 2. Governance Structure
- AI Governance Lead: approves the framework, makes the final call on regulatory obligations
- Regulatory Tracking Owner: monitors emerging AI regulation, derives obligations
- AI SBOM Verification Owner: runs the generation, review, and approval procedure
- Legal: interprets non-standard licenses and regulation

### 3. Periodic Review Plan
| Frequency | Review Item | Owner | Deliverable |
|------|----------|------|--------|
| Quarterly | Model/dataset changes, model tree licensing | AI SBOM Verification Owner | Change review record |
| Semiannual | Non-standard license classification, OSAID updates | Legal | Updated classification |
| Annual | Regulatory enforcement schedule, overall framework, policy alignment | AI Governance Lead | Revised framework |

### 4. Change Management
When a model tree change, new regulation taking effect, or a license policy change
occurs, convene an ad hoc review rather than waiting for the periodic review. Record
the review outcome and action taken in the change history.
```

## 5. References

- Policy foundation: [3.1 Policy](../../1-program-foundation/1-policy/)
- Transparency obligations and regulatory review: [3.6 Transparency Obligations](../../2-ai-extension/2-transparency-obligations/)
- AI SBOM lifecycle management: [3.9 AI SBOM](../../2-ai-extension/3-ai-sbom/)
- Full regulatory matrix and ISO/IEC 42001 context: [ISO/IEC 42001 Guide — Organizational Context and Leadership](https://openchain-project.github.io/OpenChain-KWG/guide/iso42001_guide/1-context-leadership/)
