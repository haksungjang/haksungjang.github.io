# 3.8 Effectively Resourced

> Explains how to assign responsibility, staffing, funding, and legal expertise to an AI SBOM compliance program, and how to remediate non-conformances.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert"><div class="h4 alert-heading" role="heading">Implementation Phase</div>


This clause is built during **Phase 3 — Operational Structure**.
[View the full implementation roadmap](../../#phased-implementation-roadmap)
</div>


## 1. Clause Overview

If competence (3.2) defines who should be able to do what, effective resourcing is what actually
attaches people, time, and budget to those roles so the program runs. When policy and procedures
exist only on paper and no resources back them, compliance is a name only.

3.8 requires assigning accountability for program tasks and allocating adequate resources. There
are five verification materials, covering the naming of role holders, the provision of staffing
and funding, access to legal expertise, an internal responsibility-assignment procedure, and a
non-conformance remediation procedure. The specification references the resource-related sections
of ISO/IEC 42001 Annex B (B.4.2, B.4.6) and the human oversight determination section (B.9.3).

## 2. Activities to Perform

- Assign accountability for the successful execution of program tasks.
- Allocate sufficient time and funding to the tasks.
- Make legal expertise on AI SBOM compliance accessible to those who need it.
- Have a procedure for reviewing and updating the policy and its supporting tasks.
- Have a procedure for reviewing and remediating non-conformances.

## 3. Requirement and Verification Material

| Clause | Requirement | Verification Material |
|-----------|--------------|---------|
| 3.8 | The organization shall assign accountability for program tasks, allocate sufficient time and funding, and have access to legal expertise and a non-conformance remediation procedure. | **3.8.1** A document identifying the persons, groups, or functions holding program roles<br>**3.8.2** Evidence that identified roles have been staffed and adequately funded<br>**3.8.3** Identification of expertise (internal or external) available to handle AI SBOM compliance matters<br>**3.8.4** A documented procedure for assigning internal responsibility for AI SBOM compliance<br>**3.8.5** A documented procedure for handling the review and remediation of non-conformances |

<details><summary>View original English text</summary>

> **3.8 Effectively resourced**
> Identify and Resource Program Task(s): assign accountability to ensure the successful execution of
> program tasks; program tasks are sufficiently resourced (time and adequate funding allocated); a
> process exists for reviewing and updating the policy and supporting tasks; legal expertise
> pertaining to AI SBOM Compliance is accessible to those who may need such guidance; and a process
> exists for the resolution of AI SBOM Compliance issues.
>
> **Verification material(s):**
> - Document with name of persons, group or function in program role(s) identified.
> - The identified program roles have been properly staffed and adequate funding provided.
> - Identification of expertise available to address AI SBOM Compliance matters which could be
>   internal or external.
> - A documented procedure that assigns internal responsibilities for AI SBOM Compliance.
> - A documented procedure for handling the review and remediation of non-compliant cases.
>
> See, e.g., Sections B.4.2 and B.4.6 of Annex B of ISO/IEC 42001. Section B.9.3 also provides
> guidance to determine if human resources for human oversight should be incorporated.

</details>

## 4. How to Comply with Each Verification Material, with Samples

### 3.8.1 Document Identifying Role Holders

**How to Comply**

Document, by name, the people, groups, or functions holding program roles. Including the job
title alongside the name is more stable against personnel changes. The AI SBOM program needs, in
addition to the usual open source roles, an AI governance lead, an AI SBOM verification owner,
and a model/dataset license review owner.

**Sample**

```
| Role | Holder (Job Title) | Contact |
|------|-------------|--------|
| AI Governance Lead | Kim, OO (AI Ethics & Governance Lead) | ai-gov@company.com |
| AI SBOM Verification Owner | Lee, OO (Platform Engineer) | sbom@company.com |
| License Review Owner | Park, OO (Open Source Legal) | oss-legal@company.com |
| Security Owner | Choi, OO (Product Security) | psirt@company.com |
```

---

### 3.8.2 Staffing and Funding

**How to Comply**

Show that identified roles are actually staffed and that budget has been allocated. Record the
time allocation (e.g., 30%) and the basis for the annual budget. AI SBOM compliance takes time for
model/dataset review and tool operation, so estimate the per-role time allocation realistically.

**Considerations**

- **State the time allocation**: For a shared role, record the percentage of time allocated to AI
  SBOM work.
- **Tool budget**: Include the cost of AI SBOM generation/management tools and legal counsel in
  the budget.

**Sample**

```
| Role | Holder | Time Allocation | Annual Budget Basis | Approver / Approval Date |
|------|--------|----------|---------------|--------------|
| AI Governance Lead | Kim, OO | 30% | Personnel cost + regulatory counsel | CTO / 2026-01-15 |
| AI SBOM Verification Owner | Lee, OO | 50% | Personnel cost + tool operation | CTO / 2026-01-15 |
```

---

### 3.8.3 Access to Legal Expertise

**How to Comply**

Make legal expertise on AI SBOM compliance accessible to those who need it. Because interpreting
non-standard licenses and determining regulatory obligations is legal's job, specify the access
path — internal legal counsel or an outside firm. Also define escalation criteria (which matters
get escalated to legal).

**Sample**

```
- Internal: Open Source Legal Owner (Park, OO) — first-pass license review
- External: XX Law Firm, AI/IP team — non-standard license disputes, regulatory interpretation
- Escalation criteria: a license not on the policy's prohibited/conditional lists, determining
  downstream disclosure obligations, matters where new regulation newly applies
```

---

### 3.8.4 Internal Responsibility Assignment Procedure

**How to Comply**

Document the procedure for assigning internal responsibility for AI SBOM compliance. Vague
responsibility leads to gaps, so a RACI matrix distinguishing Responsible (R), Accountable (A),
Consulted (C), and Informed (I) per task is effective.

**Sample (RACI Matrix)**

| Task | AI Governance Lead | AI SBOM Verification Owner | License Review Owner | Security Owner |
|------|:---:|:---:|:---:|:---:|
| AI SBOM generation | I | R | C | I |
| License obligation review | A | C | R | I |
| Transparency obligation review | A | C | R | I |
| Vulnerability monitoring | I | C | I | R |
| Periodic framework review | R/A | C | C | C |

*R Responsible, A Accountable, C Consulted, I Informed*

---

### 3.8.5 Non-Conformance Review and Remediation Procedure

**How to Comply**

Have a procedure for reviewing and remediating non-conformances (e.g., a prohibited-license model
brought in, a missing AI SBOM, a failure to meet transparency obligations). Vary the handling
deadline by severity. In AI, a licensing problem sometimes surfaces after a model has already been
deployed, so prepare a remediation path that includes recall or replacement.

**Sample (Remediation Procedure and Severity Criteria)**

```
Remediation procedure: identify/report → assess severity → root-cause analysis → corrective
action → recurrence prevention → record

| Severity | Example | Handling Deadline |
|--------|------|----------|
| High | A prohibited-license model is included in a product shipped externally | Immediate response (contain/replace review within 48 hours) |
| Medium | An inbound model is missing from the AI SBOM | Backfill within 7 days |
| Low | Some model card metadata is missing | Handle at the next periodic review |
```

## 5. References

- Competence definitions per role: [3.2 Competence](../../1-program-foundation/2-competence/)
- Governance review linked to non-conformance remediation: [3.10 Governance](../../4-governance/1-governance/)
- ISO/IEC 5230 resourcing model: [ISO/IEC 5230 Compliance Guide — 3.2.2 Effectively Resourced](https://openchain-project.github.io/OpenChain-KWG/guide/iso5230_guide/2-relevant-tasks/2-resourced/)
