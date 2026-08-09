# 3.2 Competence

> Explains how to define the roles and responsibilities of an AI SBOM compliance program and identify and assess the competence required for each role.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert"><div class="h4 alert-heading" role="heading">Implementation Phase</div>


This clause is built during **Phase 1 — Program Foundation**.
[View the full implementation roadmap](../../#phased-implementation-roadmap)
</div>


## 1. Clause Overview

If policy (3.1) defines what must be done, competence ensures there are people who can do it. AI
SBOM compliance demands broader knowledge than open source compliance, which dealt only with code
licensing. It requires judgment on the licensing of model weights and datasets, interpreting
model cards, emerging AI regulation, and the usage restrictions of non-standard licenses.

3.2 requires identifying the roles and responsibilities that affect the program's performance,
determining the competence each role needs, and ensuring participants have it. The specification
specifies competence in governance, security, safety, privacy, development, and supplier
management functions where relevant to the use case.

## 2. Activities to Perform

- Identify and document the roles that affect the program's performance and their responsibilities.
- Define the competence required for each role (governance, security, safety, privacy,
  development, supplier management).
- Add AI-specific competence (model/dataset licensing, model card interpretation, AI regulation)
  to the role-level competence definitions.
- Ensure participants are competent on the basis of education, training, and experience.
- Retain competence assessment evidence, and periodically check that the list stays up to date.

## 3. Requirement and Verification Material

| Clause | Requirement | Verification Material |
|-----------|--------------|---------|
| 3.2 | The organization shall identify the roles and responsibilities that affect the program's execution and effectiveness, determine the competence required for each role, and ensure participants have it. Where relevant to the use case, competence shall be secured in the governance, security, safety, privacy, development, and supplier management functions. | **3.2.1** A documented list of roles with the responsibilities of each participant<br>**3.2.2** A document identifying the competence for each role<br>**3.2.3** Documented evidence of assessed competence for each participant (including periodic checks to keep the list up to date) |

<details><summary>View original English text</summary>

> **3.2 Competence**
> The organisation shall identify the roles and the corresponding responsibilities of those roles
> that affect the performance and effectiveness of the program; determine the necessary competence
> of program participants fulfilling each role (Governance, Security, Safety, Privacy, Development,
> Supplier management if relevant to the use case); ensure that program participants are competent on
> the basis of appropriate education, training, and/or experience; and retain appropriate documented
> information as evidence of competence.
>
> **Verification material(s):**
> - A documented list of roles with corresponding responsibilities for the different participants in
>   the program.
> - A document that identifies the competencies for each role.
> - Documented evidence of assessed competence for each program participant, with periodic checks to
>   keep the list up-to-date.

</details>

## 4. How to Comply with Each Verification Material, with Samples

### 3.2.1 List of Roles and Responsibilities

**How to Comply**

Document the roles involved in the program and the responsibilities of each. In addition to the
usual open source roles, an AI SBOM program includes an AI governance role and roles that review
models and datasets. Writing responsibilities out specifically makes the later work of defining
competence (3.2.2) and assigning accountability (3.8.4) clearer.

**Sample**

```
| Role | Responsibility |
|------|------|
| AI Governance Lead | Approves the framework, determines regulatory obligations, chairs periodic reviews |
| AI SBOM Verification Owner | Generates, reviews, and approves the AI SBOM; reflects inbound materials |
| License Review Owner | Determines licensing obligations for models, datasets, and the model tree |
| Data Owner | Manages the provenance and licensing of training/validation datasets |
```

---

### 3.2.2 Competence Required per Role

**How to Comply**

Define the competence each role must have. Of the six functions the specification lists
(governance, security, safety, privacy, development, supplier management), select the ones that
apply to the role and use case, and add AI-specific competence. For example, the license review
owner needs the competence to interpret the usage restrictions of non-standard licenses (Llama
Community, OpenRAIL).

**Sample**

```
| Role | Required Competence |
|------|----------|
| AI Governance Lead | Governance, understanding of AI regulation (EU AI Act, Korea's AI Basic Act), risk management |
| AI SBOM Verification Owner | Development, SPDX/CycloneDX formats, model card interpretation, generation tool operation |
| License Review Owner | Supplier management, interpreting open source and non-standard licenses, model tree tracing |
| Data Owner | Privacy, dataset licensing, provenance management |
```

---

### 3.2.3 Competence Assessment Evidence

**How to Comply**

Assess whether each participant actually has the competence their role requires, and retain the
evidence. Training completion, qualifications, and hands-on experience serve as the basis. Since
AI regulation and licensing change quickly, periodically check the list to keep it current.

**Considerations**

- **Diversify the basis for assessment**: Use not only training completion but also practical
  work products (e.g., license review records) as competence evidence.
- **Periodic checks**: Re-review competence requirements when new regulation takes effect or new
  license types emerge.
- **Fill gaps**: When an assessment reveals a competence gap, close it with training or outside
  expertise ([3.8 Effectively Resourced](../../3-relevant-tasks/2-resourced/)).

**Sample (Competence Assessment Log)**

```
| Participant (Role) | Role | Assessment Item | Basis | Result | Assessment Date |
|-------------|------|----------|----------|------|--------|
| Lee, OO | AI SBOM Verification Owner | Writing CycloneDX ML-BOM | Internal training + work products | Met | 2026-03-10 |
| Park, OO | License Review Owner | Interpreting non-standard licenses | 5 years of OSS legal experience | Met | 2026-03-10 |
```

## 5. References

- Procedure for attaching resources to roles: [3.8 Effectively Resourced](../../3-relevant-tasks/2-resourced/)
- Securing participant awareness: [3.3 Awareness](../3-awareness/)
- ISO/IEC 5230 competence model: [ISO/IEC 5230 Compliance Guide — 3.1.2 Competence](https://openchain-project.github.io/OpenChain-KWG/guide/iso5230_guide/1-program-foundation/2-competence/)
