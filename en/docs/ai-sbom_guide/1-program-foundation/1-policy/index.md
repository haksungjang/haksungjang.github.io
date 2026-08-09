# 3.1 Policy

> Explains how to establish and communicate a written policy that governs AI SBOM compliance.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert"><div class="h4 alert-heading" role="heading">Implementation Phase</div>


This clause is built during **Phase 1 — Program Foundation**.
[View the full implementation roadmap](../../#phased-implementation-roadmap)
</div>


## 1. Clause Overview

Without an AI SBOM policy, an organization ends up deploying AI systems while developers remain
unaware of the licensing obligations attached to models and datasets. In AI, what needs to be
tracked goes beyond code. Model weights, training datasets, and the model tree derived from other
models each carry their own license, and non-standard licenses that restrict the purpose of use —
such as the Llama Community License or the RAIL family — are common. Missing these obligations
leads to copyright disputes, violations of usage restrictions, and terminated business contracts.

To prevent this risk, 3.1 requires establishing a documented policy that governs AI SBOM
compliance and communicating it so that program participants are aware of its existence. This
policy must reflect business strategy, the legal requirements of relevant jurisdictions, and the
level of risk appropriate to the use case. All subsequent clauses (competence, license
obligations, AI SBOM, governance, and so on) operate on top of this policy.

## 2. Activities to Perform

- Draft and formalize a policy document that governs AI SBOM compliance.
- Define the scope of application in the policy (AI systems deployed externally, external
  models/datasets brought in, internal models released publicly, etc.).
- Reflect business strategy, the legal requirements of relevant jurisdictions, and the risk level
  for each use case in the policy.
- Include in the policy a list of licenses allowed or prohibited for models and datasets.
  *([Guide Recommendation] Because compliance with non-standard licenses is hard to track
  automatically after the fact, decide it through policy at intake time.)*
- Establish and document a procedure for communicating the policy to program participants
  (development, legal, security, data staff, etc.).
- Retain records that prove the policy was communicated (training completion, notice history, etc.).
- Include in the policy a procedure for periodically reviewing it and re-communicating it when it
  changes.

## 3. Requirement and Verification Material

| Clause | Requirement | Verification Material |
|-----------|--------------|---------|
| 3.1 | A written policy shall exist that governs AI SBOM compliance, and it shall be communicated internally. The policy shall reflect business strategy, the legal requirements of relevant jurisdictions, and the level of risk appropriate to the use case. | **3.1.1** A documented policy meeting the above requirement<br>**3.1.2** A documented procedure that makes program participants aware of the existence of the policy (e.g., training, an internal wiki, or another practical communication method) |

<details><summary>View original English text</summary>

> **3.1 Policy**
> A written policy shall exist that governs AI System Bill of Materials (AI SBOM) compliance.
> The policy shall be internally communicated, and informed by business strategy, legal
> requirements in the relevant jurisdictions, and the level of risk appropriate for the use case.
>
> **Verification material(s):**
> - A documented policy meeting the above requirements
> - A documented procedure that makes program participants aware of the existence of the policy
>   (e.g. via training, internal wiki or other practical communication method)

</details>

## 4. How to Comply with Each Verification Material, with Samples

### 3.1.1 Documented AI SBOM Policy

**How to Comply**

The AI SBOM policy is a formal document that captures the principles and procedures by which the
organization manages the licensing and transparency obligations of its AI systems. The policy
should include its purpose, scope, roles and responsibilities, principles for reviewing model and
dataset licenses, AI SBOM management, how transparency obligations are addressed, and the review
cycle. Because this document itself is verification material 3.1.1, manage it as a formal
document with recorded version and approval history.

For an organization that already has an ISO/IEC 5230 open source policy, it is more efficient to
add an AI-related section to the existing policy than to create a separate new one. Add that
models and datasets fall within the scope of license review, how non-standard licenses are
handled, and what format is used to manage the AI SBOM.

A policy is not a document to be written once and left alone. Because the AI regulatory landscape
changes quickly, conduct a periodic review at least once a year and record the change history.

**Considerations**

- **State the AI-specific scope explicitly**: Clearly state in the policy that license review
  covers not only code but also model weights, training/testing/validation datasets, and the
  derivation relationships in the model tree.
- **Allowed/prohibited license lists**: Divide model and dataset licenses into allowed and
  prohibited lists, based on whether commercial use is permitted and whether there are behavioral
  use restrictions, and set this in the policy in advance. *([Guide Recommendation])*
- **Approval procedure**: Have the legal team or the AI governance lead give final approval, and
  record the approval date and approver.
- **Version control**: Maintain the document version and change history so that previous versions
  can be compared during an audit.
- **Periodic review**: Review at least once a year, and record the review completion date and
  reviewer.

**Sample**

Below is a sample of the scope of application and the allowed/prohibited license lists for an AI
SBOM policy. This text becomes a core component of verification material 3.1.1. Check the actual
terms of each license against its original text, then classify it to fit the organization's use
case.

```
## 1. Purpose and Scope

This policy defines the compliance principles and procedures for the company to
develop and deploy AI systems safely and responsibly. It is designed to satisfy
the requirements of ISO/IEC 5230 (open source license compliance) and the
OpenChain AI SBOM Compliance Guide.

Scope:
- All AI systems, models, and services distributed externally.
- Pre-trained models and datasets brought in from outside.
- Activities that release internal models to the outside.

## 2. Model/Dataset License Classification

Licenses for models and datasets being brought in are reviewed against the
classification below. A license not in this classification goes through review
by the AI governance lead before being brought in.

- Allowed (commercial use permitted, no behavioral restrictions): Apache-2.0, MIT, BSD, CC-BY-4.0, etc.
- Conditionally allowed (use after review): licenses with restrictions on purpose or
  scale of use, such as the Llama Community License, the Gemma Terms of Use,
  and the OpenRAIL family
- Prohibited (non-commercial only, etc.): using a CC-BY-NC dataset in a commercial product, etc.
```

---

### 3.1.2 Policy Awareness Procedure

**How to Comply**

Writing the policy document alone is not enough. A communication procedure must be established
and documented so that program participants actually become aware the policy exists. This
communication procedure document itself is verification material 3.1.2. Because AI systems
involve not just developers but also data staff, legal, and security, design the channel so the
policy reaches all of them.

Include AI SBOM policy guidance in onboarding for new hires, and use internal wiki postings and
email notices for existing employees. To prove that the policy was communicated, retain evidence
such as notice history and training completion records for at least three years.

**Considerations**

- **Use multiple channels**: Use two or more channels, such as an internal wiki, email notices,
  and onboarding training.
- **Include AI-related roles**: Include dataset owners and model operators as recipients as well.
- **When the policy changes**: Have a separate procedure to notify participants of changes
  immediately.
- **Retain evidence**: Keep notice history and training completion certificates for at least
  three years.

**Sample**

Below is a sample policy communication notice email. Retaining the send history serves as
evidence for verification material 3.1.2.

```
Subject: [AI Compliance] AI SBOM Policy Notice and Acknowledgment Request

To: Employees involved in AI system development, operations, and data
From: AI Compliance Officer

Hello,

Our AI SBOM compliance policy has been established (or revised).
All employees involved in using, bringing in, or deploying AI models and
datasets are asked to review and familiarize themselves with the policy
document below.

- Policy document: [internal portal link]
- Key contents: model/dataset license classification, license obligation
             review procedure, AI SBOM management, transparency obligation response
- Policy version: v1.0 (effective date: YYYY-MM-DD)

Contact: AI Compliance Officer (ai-compliance@company.com)
```

## 5. References

- License obligation review procedure: [3.5 License Obligations](../../2-ai-extension/1-license-obligations/)
- Basic structure of an open source policy: [ISO/IEC 5230 Compliance Guide — 3.1.1 Policy](https://openchain-project.github.io/OpenChain-KWG/guide/iso5230_guide/1-program-foundation/1-policy/)
- AI license management strategy: [Enterprise Open Source Management Guide — AI Compliance](https://openchain-project.github.io/OpenChain-KWG/guide/opensource_for_enterprise/7-ai-compliance/)
