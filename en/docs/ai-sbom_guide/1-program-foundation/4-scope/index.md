# 3.4 Program Scope

> Explains how to clearly declare the scope and limits to which the AI SBOM compliance program applies.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert"><div class="h4 alert-heading" role="heading">Implementation Stage</div>


This clause is established during **Phase 1 — Program Foundation**.
[View the full implementation roadmap](../../#phased-implementation-roadmap)
</div>


## 1. Clause Overview

Program scope determines how far compliance extends. If the scope is ambiguous, it becomes unclear
which AI systems need an SBOM and which models' licenses need review. Scope must be declared first
so that every subsequent clause knows what it applies to.

3.4 requires declaring the scope of application for each program. Scope can differ by organization.
Some organizations cover a single product line; others cover an entire department or the whole
organization. In AI, scope determination covers not only self-developed models but also externally
sourced models and datasets, and the external release of in-house models.

## 2. Required Activities

- Define what the program applies to (externally deployed AI systems, externally sourced models and
  datasets, external release of in-house models, and so on).
- Record what is excluded from application and the rationale for the exclusion.
- Keep the scope statement consistent with the scope of application in the policy document.
- Review and update the scope periodically as the business environment changes.

## 3. Requirements and Verification Material

| Clause | Requirement (EN) | Verification Material |
|-----------|--------------|---------|
| 3.4 | Different programs may be governed by different levels of scope. For example, a program could govern a single product line, an entire department, or an entire organisation. The scope designation needs to be declared for each program. | **3.4.1** A written statement that clearly defines the scope and limits of the program |

<details><summary>View original English text</summary>

> **3.4 Program scope**
> Different programs may be governed by different levels of scope. For example, a program could govern
> a single product line, an entire department, or an entire organisation. The scope designation needs
> to be declared for each program.
>
> **Verification material(s):**
> - A written statement that clearly defines the scope and limits of the program.

</details>

## 4. Compliance Methods and Samples by Verification Material

### 3.4.1 Program scope statement

**Compliance Method**

State the program's scope and limits in writing. Clearly note what is included, what is excluded,
and if excluded, on what grounds. An AI SBOM program becomes clearer when it declares what it
applies to by breaking it down into material types and activities. The table below is an example of
organizing scope.

**Table 1.** Example of an AI SBOM program scope declaration

| Category | Applies | Notes |
|---|---|---|
| AI systems, models, and services deployed externally | Yes | AI SBOM generation and license review obligations |
| Pretrained models sourced externally | Yes | Reflected in the AI SBOM as inbound material |
| Datasets sourced externally | Yes | License and provenance review |
| External release of in-house models | Yes | Review of public-release license and transparency obligations |
| Internal experimental models (not deployed externally) | Conditionally excluded | Applicability determined by separate review |

**Considerations**

- **Consistency with policy**: The scope statement should not conflict with the scope of
  application in [3.1 Policy](../1-policy/).
- **Grounds for exclusion**: Record the rationale for excluded items. Even an internal
  experimental model falls into scope once it moves to external deployment, so put a review
  procedure in place for that transition point. *([Recommendation of this guide])*
- **Periodic review**: Update the scope whenever a new product line or new AI service is
  introduced.

**Sample (Scope Statement)**

```
## AI SBOM Compliance Program Scope

### Applies To
This program applies to all AI systems, models, and services that the company deploys
externally, and to pretrained models and datasets sourced externally. It also covers
activities that release in-house models externally.

### Excluded
Models used solely for internal experimentation or research and not deployed externally
are excluded. However, if such a model transitions to external deployment, it is brought
into scope through the intake review procedure.

### Review Cycle
Scope is reviewed and updated at least once a year, or as the business environment
changes.
```

## 5. See Also

- Scope of application in the policy: [3.1 Policy](../1-policy/)
- AI SBOM for material within scope: [3.9 AI SBOM](../../2-ai-extension/3-ai-sbom/)
- ISO/IEC 5230 scope example: [ISO/IEC 5230 Compliance Guide — 3.1.4 Program Scope](https://openchain-project.github.io/OpenChain-KWG/guide/iso5230_guide/1-program-foundation/4-scope/)
