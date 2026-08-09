# Enterprise AI BOM Field Requirements Matrix — Required and Optional Fields Defined by Standards and Regulatory Grounds

> Weighs the 50 elements of the G7 "SBOM for AI — Minimum Elements" against authoritative standards — SPDX 3.0.1, CycloneDX 1.6, NTIA 2021, OpenChain AI V1 — and regulatory grounds including the CRA, the AI Act, and FDA guidance, to determine which AI BOM fields are required and which are optional. Part of a five-part series that also applies the same matrix to production, ingestion, and supplier contexts and covers toolset strategy.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert">


This article was written with Claude Code, and the key facts cited here were cross-checked against primary sources.
</div>


## 1. Purpose and Context of Use

Enterprise open source governance programs have already reached the stage of mandating that suppliers submit a Software Bill of Materials (SBOM) and of operating concrete submission requirements. AI systems need the same transparency requirement extended to models and datasets, but existing SBOM requirements cover only software components and cannot capture AI-specific information. This report defines, using international standards and regulatory grounds, which fields a bill of materials for AI (hereafter AI BOM) should require and which it should treat as optional.

A note on why AI BOM is used as the umbrella term here. Three of the sources compared below call the same thing by different names. The G7 Cybersecurity Working Group, whose element list this report draws on, calls it SBOM for AI; the OpenChain project calls it AI SBOM; CycloneDX calls it a Machine Learning Bill of Materials (ML-BOM). Of the remaining two, SPDX expresses it as an AI profile rather than a separate abbreviation, and the NTIA minimum elements predate AI and cover the general SBOM. Elevating any one of these to represent the rest would misname the others, so what follows uses AI BOM for the general concept and reproduces each standard's own term only when referring to that standard specifically.

The fields assessed here are the 50 elements of "SBOM for AI — Minimum Elements," published by the G7 Cybersecurity Working Group. Using these 50 as rows, this report compares the requirement strength of five authoritative standards to sort each element into required or optional.

The same matrix is applied differently across three enterprise usage contexts.

- Production: the fields an in-house AI model development team must fill in when authoring an AI BOM directly.
- Ingestion: the fields that must be checked to assess transparency and risk when bringing in and using an external model or dataset.
- Supplier requirements: the fields to require submission of from suppliers that provide AI models to the organization.

![How each of the three roles redraws the boundary of required starting from the consensus determination. Production keeps the 20 consensus-required elements as is; ingestion lowers document metadata but raises a set of risk-judgment fields to reach 15 required; supplier requirements raises two more to reach 20 required](./role-scope.png)

**Figure 1.** How the boundary of required shifts by role for the same matrix *(compiled from research)*

## 2. Methodology

### 2.1 Sources Used for Consensus Tallying

Whether each field is required is determined by summing the requirement strength of the following five sources.

- G7 "SBOM for AI — Minimum Elements" (G7, jointly led by the BSI and the ACN, 2026): recommends all 50 elements as "minimum elements." Because it does not distinguish required from optional at the element level, this matrix credits G7 with one vote of "designated as a minimum element" for every element.
- SPDX 3.0.1: the specification directly defines the cardinality (whether required) of each property in the AI Profile's `AIPackage`, the Dataset Profile's `DatasetPackage`, and the common classes in Core.
- CycloneDX 1.6: required fields are defined by the `required` array in the JSON schema.
- NTIA "The Minimum Elements For a Software Bill of Materials (SBOM)" (2021): defines the seven baseline data fields for a general software SBOM.
- OpenChain AI Compliance Management Guide (Version 1, 2025): a process standard that does not define data fields, but whose license obligation procedures mandate identifying and documenting model and dataset licenses.

### 2.2 Determination Rule

A field is determined required if two or more sources require the field's existence itself, and optional otherwise. Since G7 gives one vote to every element, the determination in practice comes down to whether at least one other source requires the field's existence.

Requiring existence here means class-level required cardinality (the required properties of SPDX's `AIPackage`/`DatasetPackage`), document-root requirements (CycloneDX's `bomFormat`/`specVersion`), the seven NTIA baseline fields, and OpenChain's shall-level process. Conditional requirements enforced only when an object is created — for example, the algorithm and value inside a hash object, or the name inside a component object — are not requirements to include the object itself, so they were not counted as existence requirements. However, these conditional requirements and items of high integrity or security value were left optional while being marked recommended in the role-based application.

![Of the five sources, G7 always gives one vote to every element, so the determination in practice comes down to whether any one of the remaining four — SPDX, CycloneDX, NTIA, or OpenChain — requires it](./consensus-rule.png)

**Figure 2.** The consensus determination rule and G7's role in it *(compiled from research)*

Applying this rule yields 20 required and 30 optional elements out of the 50.

### 2.3 Marking Regulatory Basis

Whether a binding regulation applies to a given field is marked on a separate axis, not folded into the consensus tally, because no regulation mandates an AI BOM under that name. The Cyber Resilience Act (CRA) requires a general software SBOM; the AI Act, U.S. Food and Drug Administration (FDA) guidance, and domestic regimes require documentation obligations. `Direct` marks a case where the regulation explicitly requires that item; `Indirect` marks a case where the item is not itself an SBOM requirement but a documentation or vulnerability-handling obligation effectively requires the same information.

## 3. Overview of the Consensus Results

The distribution of required and optional elements by cluster is as follows.

| Cluster | Elements | Required | Optional |
|---|---|---|---|
| Metadata | 10 | 5 | 5 |
| System-Level Attributes | 9 | 4 | 5 |
| Model | 13 | 6 | 7 |
| Dataset Attributes | 10 | 5 | 5 |
| Infrastructure | 2 | 0 | 2 |
| Security Attributes | 4 | 0 | 4 |
| Key Performance Indicators | 2 | 0 | 2 |
| Total | 50 | 20 | 30 |

![Horizontal bars showing the distribution of required and optional elements by cluster. Metadata, System, Model, and Dataset each contain required elements, but Infrastructure, Security Attributes, and Key Performance Indicators have none](./cluster-distribution.png)

**Figure 3.** Required/optional distribution by cluster *(compiled from research)*

The 20 elements determined required are all foundational to identification and traceability: who made it (author, producer), what it is (name, identifier, version), when it was made (timestamp), what it is composed of (components, dependency relationships, dataset content), and what license applies (model and dataset licenses). Two or more standards consistently require the existence of this information.

By contrast, detailed model attributes (architecture, training technique, input/output characteristics), dataset statistics and sensitivity, security controls, and key performance indicators fall to optional because only G7 lists them as minimum elements and no other standard mandates their existence. These items are optional by consensus, but because they are used directly for transparency and risk assessment in the ingestion and supplier-requirement contexts, they are raised again in the role-based application.

One structural point is worth noting. The required determination in the AI-specific clusters (Model, Dataset) is effectively driven by G7 and SPDX 3.0. NTIA, being a general software SBOM standard, contributes only to metadata and the identification lineage; OpenChain defines no fields beyond licensing; and CycloneDX makes everything but its two root fields conditionally required. SPDX 3.0's AI and Dataset profiles are, in effect, still the only field-level standard for AI BOM with any real density.

## 4. Field Matrix

The notation conventions are as follows. The source columns use `Required` (existence required), `Conditional` (enforced only when the object is created), `Approximate` (no dedicated field; handled through a relationship or a general property instead), `Optional`, and `–` (no equivalent). OpenChain's `Required (P)` denotes process enforcement rather than a data field. The role columns use `Required`, `Recommended`, `Optional`, and `–`; given table width, the Production, Ingestion, and Supplier role columns are broken out into the §4.6 role-based application summary table.

### 4.1 Metadata Cluster

| Element | SPDX 3.0 | CycloneDX | NTIA | OpenChain | Consensus | Regulatory Basis |
|---|---|---|---|---|---|---|
| SBOM Author | Required | Approximate | Required | – | Required | FDA direct |
| SBOM Version | – | Optional | – | – | Optional | – |
| Data Format Name | Implicit | Required | Required | – | Required | CRA/FDA indirect |
| Data Format Version | Required | Required | Optional | – | Required | – |
| Author Signature | – | Optional | – | – | Optional | domestic indirect |
| Tool Name | Optional | Conditional | – | – | Optional | – |
| Tool Version | – | Optional | – | – | Optional | – |
| Generation Context | Optional | Optional | – | – | Optional | – |
| SBOM Timestamp | Required | Optional | Required | – | Required | FDA direct |
| Dependency Relationships | Conditional | Conditional | Required | – | Required | CRA/FDA direct |

### 4.2 System-Level Attributes Cluster

| Element | SPDX 3.0 | CycloneDX | NTIA | OpenChain | Consensus | Regulatory Basis |
|---|---|---|---|---|---|---|
| System Name | Required | Conditional | Required | Implied | Required | AI Act/FDA indirect |
| System Components | Approximate | Conditional | Required | Implied | Required | FDA direct, CRA indirect |
| System Producer | Optional | Conditional | Required | – | Required | FDA direct, AI Act indirect |
| System Version | Optional | Conditional | Required | – | Required | FDA direct, AI Act indirect |
| System Timestamp | Optional | Optional | – | – | Optional | – |
| System Data Flow | – | Optional | – | – | Optional | AI Act indirect |
| System Data Usage | Approximate | Approximate | – | Implied | Optional | AI Act/domestic indirect |
| Input/Output Properties | – | Approximate | – | – | Optional | AI Act indirect |
| Intended Application Domain | Optional | Approximate | – | Implied | Optional | AI Act/domestic indirect |

### 4.3 Model Cluster

| Element | SPDX 3.0 | CycloneDX | NTIA | OpenChain | Consensus | Regulatory Basis |
|---|---|---|---|---|---|---|
| Model Name | Required | Conditional | – | Implied | Required | AI Act indirect |
| Model Identifier | Required | Optional | – | Implied | Required | – |
| Model Version | Required | Optional | – | – | Required | AI Act indirect |
| Model Timestamp | Required | Optional | – | – | Required | AI Act indirect |
| Model Producer | Required | Optional | – | – | Required | AI Act indirect |
| Model Description | Optional | Optional | – | – | Optional | AI Act/domestic indirect |
| Model Hash Value | Conditional | Conditional | – | – | Optional | – |
| Model Hash Algorithm | Conditional | Conditional | – | – | Optional | – |
| Model Properties | Optional | Optional | – | – | Optional | AI Act indirect |
| Input/Output Properties | Approximate | Optional | – | – | Optional | AI Act indirect |
| Training Properties | Optional | Optional | – | Implied | Optional | AI Act/domestic indirect |
| Model License | Approximate | Optional | – | Required (P) | Required | AI Act indirect |
| External References | Optional | Conditional | – | Implied | Optional | – |

### 4.4 Dataset Attributes Cluster

| Element | SPDX 3.0 | CycloneDX | NTIA | OpenChain | Consensus | Regulatory Basis |
|---|---|---|---|---|---|---|
| Dataset Name | Required | Optional | – | Implied | Required | AI Act indirect |
| Dataset Description | Optional | Optional | – | – | Optional | AI Act/domestic indirect |
| Dataset Content | Required | Optional | – | – | Required | AI Act indirect |
| Dataset Identifier | Required | Optional | – | – | Required | – |
| Dataset Hash | Conditional | Conditional | – | – | Optional | – |
| Dataset Provenance | Required | Approximate | – | Implied | Required | AI Act/domestic indirect |
| Statistical Properties | Optional | Optional | – | – | Optional | AI Act indirect |
| Dataset Sensitivity | Optional | Optional | – | Implied | Optional | AI Act/domestic indirect |
| Dependency Relationships | Conditional | Conditional | – | Implied | Optional | – |
| Dataset License | Approximate | Optional | – | Required (P) | Required | – |

### 4.5 Infrastructure, Security, and Key Performance Indicator Cluster

| Element | SPDX 3.0 | CycloneDX | NTIA | OpenChain | Consensus | Regulatory Basis |
|---|---|---|---|---|---|---|
| Infrastructure Software | Approximate | Optional | – | – | Optional | – |
| Infrastructure Hardware | – | Optional | – | – | Optional | AI Act indirect |
| Security Controls | – | Approximate | – | – | Optional | CRA/AI Act/FDA indirect |
| Security Compliance | Optional | Optional | – | – | Optional | conformity assessment indirect |
| Cybersecurity Policy Information | – | Approximate | – | – | Optional | CRA direct |
| Vulnerability References | Approximate | Optional | – | – | Optional | CRA/FDA direct |
| Security Metrics | Optional | Optional | – | – | Optional | AI Act indirect |
| Operational Performance Metrics | Optional | Optional | – | – | Optional | AI Act indirect |

The Security cluster is entirely optional by consensus, but Vulnerability References and Cybersecurity Policy Information are items the CRA and FDA require directly. The consensus tally looks only at how standards define data fields, while regulation mandates the same information. For that reason, these two items are raised to required or recommended in the ingestion and supplier contexts. This is the representative case where the regulatory-basis marking adjusts the role-based application.

### 4.6 Role-Based Application Summary

This table gathers, for all 50 elements, the result of applying the §4.1–4.5 consensus determinations to the three contexts of production, ingestion, and supplier requirements. The role columns use `Required`, `Recommended`, `Optional`, and `–`.

| Element | Consensus | Production | Ingestion | Supplier |
|---|---|---|---|---|
| **Metadata** | | | | |
| SBOM Author | Required | Required | Recommended | Required |
| SBOM Version | Optional | Recommended | Optional | Recommended |
| Data Format Name | Required | Required | Recommended | Required |
| Data Format Version | Required | Required | Recommended | Required |
| Author Signature | Optional | Recommended | Recommended | Recommended |
| Tool Name | Optional | Recommended | Optional | Recommended |
| Tool Version | Optional | Recommended | Optional | Optional |
| Generation Context | Optional | Recommended | Optional | Recommended |
| SBOM Timestamp | Required | Required | Recommended | Required |
| Dependency Relationships | Required | Required | Required | Required |
| **System-Level Attributes** | | | | |
| System Name | Required | Required | Required | Required |
| System Components | Required | Required | Required | Required |
| System Producer | Required | Required | Recommended | Required |
| System Version | Required | Required | Required | Required |
| System Timestamp | Optional | Recommended | Optional | Recommended |
| System Data Flow | Optional | Recommended | Recommended | Recommended |
| System Data Usage | Optional | Recommended | Recommended | Recommended |
| Input/Output Properties | Optional | Recommended | Recommended | Recommended |
| Intended Application Domain | Optional | Recommended | Recommended | Recommended |
| **Model** | | | | |
| Model Name | Required | Required | Required | Required |
| Model Identifier | Required | Required | Required | Required |
| Model Version | Required | Required | Required | Required |
| Model Timestamp | Required | Required | Recommended | Recommended |
| Model Producer | Required | Required | Recommended | Required |
| Model Description | Optional | Recommended | Required | Recommended |
| Model Hash Value | Optional | Recommended | Recommended | Recommended |
| Model Hash Algorithm | Optional | Recommended | Recommended | Recommended |
| Model Properties | Optional | Recommended | Recommended | Recommended |
| Input/Output Properties | Optional | Recommended | Recommended | Recommended |
| Training Properties | Optional | Recommended | Recommended | Recommended |
| Model License | Required | Required | Required | Required |
| External References | Optional | Recommended | Recommended | Recommended |
| **Dataset Attributes** | | | | |
| Dataset Name | Required | Required | Required | Required |
| Dataset Description | Optional | Recommended | Recommended | Recommended |
| Dataset Content | Required | Required | Recommended | Recommended |
| Dataset Identifier | Required | Required | Required | Required |
| Dataset Hash | Optional | Recommended | Recommended | Recommended |
| Dataset Provenance | Required | Required | Required | Required |
| Statistical Properties | Optional | Recommended | Optional | Optional |
| Dataset Sensitivity | Optional | Recommended | Required | Required |
| Dependency Relationships | Optional | Recommended | Optional | Optional |
| Dataset License | Required | Required | Required | Required |
| **Infrastructure, Security, and KPIs** | | | | |
| Infrastructure Software | Optional | Recommended | Optional | Recommended |
| Infrastructure Hardware | Optional | Optional | Optional | Optional |
| Security Controls | Optional | Recommended | Recommended | Recommended |
| Security Compliance | Optional | Recommended | Recommended | Recommended |
| Cybersecurity Policy Information | Optional | Recommended | Optional | Recommended |
| Vulnerability References | Optional | Recommended | Required | Required |
| Security Metrics | Optional | Recommended | Recommended | Optional |
| Operational Performance Metrics | Optional | Recommended | Optional | Optional |

## 5. Role-Based Application in Detail

### 5.1 Production Perspective

When an in-house development team builds the model, information access is at its best, so the requirement level is set highest here. The 20 consensus-required elements remain required as is. In addition, items that are optional by consensus — detailed model and dataset attributes, hashes, training information — are set to recommended at production time, because if the producer does not record this information, no one downstream, whether an adopter or the rest of the supply chain, can ever recover it.

### 5.2 Ingestion Perspective

When bringing in an external model or dataset, fields that are used directly for transparency and risk assessment take priority. In addition to identification information (name, identifier, version, producer), Model Description, model and dataset licenses, Dataset Provenance, Dataset Sensitivity, and Vulnerability References are treated as required. Licenses are the basis for judging compliance risk; provenance and sensitivity for judging data legality and privacy risk; vulnerability references for judging security risk. These are optional by consensus but are core to ingestion review, so they are raised to required.

### 5.3 Supplier Requirement Perspective

The scope required from suppliers takes the 20 consensus-required elements as the baseline, considering what is realistically enforceable through contract. Model and dataset licenses, Dataset Provenance and Sensitivity, and Vulnerability References are added as required on top of that. This extends to models and data the same structure that existing software SBOM supplier requirements already enforce for identification, dependencies, and format compliance.

## 6. Limitations and Items Requiring Verification

The consensus determinations in this matrix rest on the cardinality defined in the standard specifications and on minimum-element provisions, with the regulatory-basis marking as a separate axis. The following items had limited access to primary sources and require separate verification.

The primary NTIA minimum elements specification (ntia.gov) blocks automated retrieval, so the seven baseline fields were reconfirmed against a public mirror. The primary text of the CRA Annex I, the AI Act annexes, and the FDA guidance (EUR-Lex, fda.gov) also had rendering and access-blocking issues and were cross-checked using mirrors and search aggregation. The training-data obligations in Korea's Basic Act on AI could not be matched against the primary text down to the article and paragraph level, so they are marked "indirect (article unspecified)." These items will be reconfirmed against primary sources at a follow-up verification stage.

The field cardinality of SPDX 3.0 and CycloneDX 1.6 was confirmed directly from the specification's class definitions and the original JSON schema, so confidence in these is high.

## References

The main primary sources are as follows.

**A1.** G7 Cybersecurity Working Group (2026). *Software Bill of Materials for AI — Minimum Elements*. Jointly led by the BSI and the ACN, and jointly published with the other G7 cybersecurity agencies and the European Commission. — *Used for: the 50-element row structure.*

**A2.** SPDX Project (2024). *System Package Data Exchange (SPDX) Specification, Version 3.0.1* — AI Profile, Dataset Profile, Core. <https://spdx.github.io/spdx-spec/v3.0.1/> — *Used for: model and dataset field cardinality.*

**A3.** OWASP / ECMA International (2024). *CycloneDX Bill of Materials Specification 1.6* (ECMA-424), JSON schema. <https://cyclonedx.org/docs/1.6/json/> — *Used for: determining required fields in the schema.*

**A4.** NTIA, U.S. Department of Commerce (2021). *The Minimum Elements For a Software Bill of Materials (SBOM)*. <https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom> — *Used for: general SBOM minimum elements.*

**A5.** OpenChain Project AI Work Group (2025). *Artificial Intelligence System Bill of Materials — Compliance Management Guide, Version 1*. — *Used for: license obligation process.*

**A6.** European Parliament and Council (2024). *Regulation (EU) 2024/2847 — Cyber Resilience Act*, Annex I. — *Used for: SBOM and vulnerability-handling regulatory basis.*

**A7.** European Parliament and Council (2024). *Regulation (EU) 2024/1689 — AI Act*, Article 53, Annex IV, XI, XII. — *Used for: documentation and transparency regulatory basis.*

**A8.** U.S. FDA (2023). *Cybersecurity in Medical Devices: Premarket Submissions*; FD&C Act §524B. — *Used for: medical device SBOM regulatory basis.*

**A9.** Ministry of Science and ICT, National Intelligence Service, and KISA (2026). *Software Supply Chain Security Enhancement Roadmap for an Era of Everyday AI*; *Basic Act on the Development of Artificial Intelligence and the Establishment of Trust, etc.* — *Used for: domestic regulatory basis.*

## 8. Structure of This Series

This article is the starting point of a five-part series. It carries the matrix above into operational documents for the three usage contexts, together with the toolset strategy that supports them.

- [Supplier AI BOM Submission Requirements](/en/research/2026-ai-bom-requirements/supplier-requirements/) — the fields to require from suppliers and the submission protocol
- [In-House Development Team AI BOM Authoring Guide](/en/research/2026-ai-bom-requirements/producer-guide/) — the required and recommended items an in-house production team must fill in
- [External Model and Dataset Ingestion Checklist](/en/research/2026-ai-bom-requirements/ingestion-checklist/) — risk review when bringing in external models and datasets
- [AI BOM Toolset Design Strategy](/en/research/2026-ai-bom-requirements/toolset-strategy/) — the strategy for codifying the matrix as policy and integrating it with existing tools

---

Section pages:

- [Supplier AI BOM Submission Requirements](/en/research/2026-ai-bom-requirements/supplier-requirements/): Requirements for the AI BOM that a supplier providing AI models or systems to your organization must submit. Defines the standard data format, the information that must be included, identifier rules, and the requirements for licensing, provenance, and sensitivity.
- [AI BOM Authoring Guidelines for In-House Development Teams](/en/research/2026-ai-bom-requirements/producer-guide/): Guidelines for the AI BOM that in-house development teams must produce when building an AI model or system. Drawing on the information accessibility available at the point of production, this sets out the required and recommended fields to fill and how to record integrity and provenance.
- [Ingestion Vetting Checklist for External Models and Datasets](/en/research/2026-ai-bom-requirements/ingestion-checklist/): A checklist for vetting transparency and risk, on the basis of the AI BOM, when bringing in and using an external AI model or dataset. Checks identification, licensing, data lawfulness, and security risk step by step.
- [AI BOM Toolset Design Strategy](/en/research/2026-ai-bom-requirements/toolset-strategy/): Surveys seven tool categories through their official repositories and documentation to lay out what to reuse, extend, or build new; the build order; the policy schema for codifying the matrix; and the Dependency-Track integration architecture.
