# AI BOM Toolset Design Strategy

> Surveys seven tool categories through their official repositories and documentation to lay out what to reuse, extend, or build new; the build order; the policy schema for codifying the matrix; and the Dependency-Track integration architecture.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert">


This article was written with Claude Code, and the key facts cited here were cross-checked against primary sources.
</div>


Based on a survey of seven tool categories through their official repositories and documentation, this document lays out what to reuse from existing tools, what to extend or build new, in what order to build it, and what policy schema should define the matrix. The acquisition strategy was not fixed in advance but determined from the survey results, and the premise is that the organization already operates an existing SBOM platform (Dependency-Track).

## 1. Three Core Judgments

The standard path for generation, verification, storage, and model scanning already works with open source software. The `aibom` command in cdxgen actually produces CycloneDX 1.6 AI BOMs, sbomqs and OPA check field conformance, Dependency-Track ingests the software layer, and ModelScan and sigstore model-signing reinforce model integrity. There is no need to build everything from scratch in-house.

Standardizing the format on CycloneDX 1.6 is the more realistic choice. The SPDX 3.0 AI Profile has richer expressive power, but no mature tool actually generates it, and Dependency-Track cannot ingest SPDX. SPDX 3.0 is kept as a standard to track, while CycloneDX is set as the primary operational format.

Where new construction is unavoidable is narrow and clear: the policy layer that checks AI-specific fields, an inventory that treats models and datasets as first-class objects, and the determination of license usage restrictions. Everything else is covered by reuse or extension.

## 2. Reuse Determinations by Area

| Functional Area | Representative Tool | Determination | Basis |
|---|---|---|---|
| AI BOM generation (CycloneDX) | cdxgen `aibom` | Reuse | Automatic CycloneDX 1.6 AI BOM generation works (under active development as of this research) |
| AI BOM generation (SPDX 3.0) | spdx-tools | Not viable | 3.0 support is experimental write-only, with no AI Profile generation support |
| Deep-field auto-extraction | None | New | Cannot automatically fill in dataset statistics, bias, hashes, or license |
| Validation/conformance engine | sbomqs, sbom-utility | Reuse | Provides general-purpose field-presence checking and scoring |
| AI- and role-specific conformance rules | None | New | No off-the-shelf profile exists that checks the G7's 50 elements and role-specific required sets |
| Repository/inventory (SW layer) | Dependency-Track | Reuse | Software dependency inventory and impact analysis are mature |
| Repository/inventory (model/data layer) | Dependency-Track | Extension pending | Does not yet ingest the `machine-learning-model` and `data` classifiers or modelCard (issue #4361, open as of this research) |
| Vulnerability matching (SW dependencies) | Dependency-Track, OSV | Reuse | Already connected; ML libraries are matched as ordinary packages too |
| Risk feed (model-specific) | huntr, Insights | Extend | CVEs issued by huntr flow in via NVD; there is no direct connector |
| Model serialization scanning | ModelScan, Fickling | Reuse | Mature; can be inserted into CI via JSON reports and exit codes |
| Integrity/signing | sigstore model-signing | Reuse | Uses DSSE and in-toto, which map onto BOM integrity and provenance fields |
| Data poisoning detection | None (research stage) | Replaced with traceability | No production tool exists; provenance and integrity records substitute for a detection guarantee |
| License identification/declaration | ScanCode, ORT + SPDX/HF dictionaries | Reuse + extend | Reuse the engine; the AI license dictionary needs to be augmented |
| License usage-restriction determination | None | New | No standard exists for machine-readable, automated determination of RAIL-family conduct restrictions |
| Policy codification | OPA/Rego, sbomqs YAML | Reuse | Express the matrix by separating policy files per role |

In summary, of the thirteen areas, seven are reuse, three are extension, and three are new. The three new areas — AI- and role-specific conformance rules, the model/data inventory, and license usage-restriction determination — are where this project's unique value is concentrated.

## 3. Build Priority

### P0 — A Minimal Working Pipeline (Reuse-Focused)

The first step is to wire together off-the-shelf tools into an end-to-end pipeline. Generation produces CycloneDX 1.6 with cdxgen `aibom`, model files are scanned with ModelScan and signed with sigstore, and the results are uploaded to Dependency-Track to obtain software-layer vulnerabilities and impact analysis. Validation checks the presence of required fields with an sbomqs custom policy. Almost all of this stage is reuse, so it delivers value quickly.

### P1 — Extending the AI-Specific Layer

The next step adds new value. Codify the matrix into a policy schema to implement role-specific conformance checking (Section 4), and carry models and datasets through CycloneDX `properties` or external references to secure inventory traceability. Augment the license pipeline with an AI license dictionary (RAIL, OpenRAIL, Llama, Gemma, OpenMDW, CDLA), and receive model risk as huntr CVEs relayed through NVD.

### P2 — New and Research Areas

Last are the parts where standards and research still need to mature. Automatic extraction of deep fields such as dataset statistics or bias, automatic determination of license usage restrictions, and data poisoning are handled through provenance and integrity traceability instead of detection. Bring SPDX 3.0 generation on board once the tool ecosystem matures, but for now keep it only as a standard to track. When Dependency-Track's support for model/data classifiers (issue #4361) lands, promote P1's workaround to a first-class inventory.

## 4. Policy Schema Design

Defining the matrix's "element x required/optional x role" as a machine-readable policy is the core of this toolset. Since the survey found no tool that treats role-specific required sets as a first-class concept, this must be designed directly. It is split into two layers.

### 4.1 Field Registry

A table mapping each of the G7's 50 elements to a CycloneDX path (and, eventually, an SPDX path) is kept in one place. The [AI BOM Field Requirements Matrix](/en/research/2026-ai-bom-requirements/) already contains an element-by-element source mapping, so moving it into a machine-readable form looks like this.

```yaml
# field-registry.yaml — maps G7 elements to BOM paths
model_license:
  g7: Model license
  cyclonedx: "components[?type=='machine-learning-model'].licenses"
  spdx: "Relationship(hasDeclaredLicense) from AIPackage"
dataset_provenance:
  g7: Dataset provenance
  cyclonedx: "components[?type=='data'].data[].governance"
  spdx: "DatasetPackage.originatedBy / dataCollectionProcess"
vulnerability_referencing:
  g7: Vulnerability referencing
  cyclonedx: "vulnerabilities[] or externalReferences[?type=='vcs']"
  spdx: "VulnAssessmentRelationship"
```

### 4.2 Role-Specific Policy Files

The required set for each of production, ingestion, and supplier is kept as a separate policy file. This simply carries over the role column of the matrix.

```yaml
# policy/supplier.yaml — required elements for supplier submission (Section 4.6, 20 supplier-required elements)
required:
  - sbom_author
  - sbom_data_format_name
  - sbom_data_format_version
  - sbom_timestamp
  - sbom_dependency_relationship
  - system_name
  - system_components
  - system_producer
  - system_version
  - model_name
  - model_identifier
  - model_version
  - model_producer
  - model_license
  - dataset_name
  - dataset_identifier
  - dataset_provenance
  - dataset_sensitivity
  - dataset_license
  - vulnerability_referencing
recommended:
  - model_timestamp
  - dataset_content
  - model_hash_value
```

### 4.3 Determination Engine

Two engines are recommended together. For a quick start, an sbomqs custom policy (YAML) puts the role-specific files into operation today with no engine to learn, converting the fulfillment rate into a score. Where expressiveness is needed, OPA/Rego (conftest) branches on the input BOM's role value to determine the required set. Because Rego follows the field registry's paths to evaluate presence, it can express conditional requirements and cross-field consistency as well.

```rego
# policy/aibom.rego — skeleton for role-specific required-field checking
package aibom

deny[msg] {
    role := input.metadata.properties[_].value  # e.g. "supplier"
    req := data.policy[role].required[_]
    not field_present(req)
    msg := sprintf("Required element missing: %s (role: %s)", [req, role])
}
```

OSCAL is a tool built for expressing security controls, which makes it more than SBOM fields need, and it does not execute validation on its own, so it is not adopted. It is worth considering only if there arises a need to produce upper-level artifacts for regulatory or audit purposes (a requirements catalog, an assessment result report) in a federal-friendly format.

## 5. Reference Architecture and Dependency-Track Integration

The BOM for an AI system splits into a software dependency layer and a model/dataset layer. Dependency-Track handles the former layer right now, and does not yet accept the latter as a first-class citizen (issue #4361 is open as of this research and may change later). Integration is therefore split by layer.

![The common pipeline has three stages — generation, enrichment, and validation — after which it splits into two layers. The software layer is ingested by Dependency-Track as-is, but the model/dataset layer, lacking classifier support, is uploaded as a generic component and routed around via properties](/research/2026-ai-bom-requirements/toolchain-layers-en.png)

**Figure 4.** The common pipeline and the two layers it splits into after validation *(compiled from the survey)*

The software layer needs almost no extra work. cdxgen turns an ML project's PyPI or npm dependencies into CycloneDX, which is uploaded to Dependency-Track, correlating vulnerabilities against OSV and NVD and even providing impact analysis for "which projects use this component?" CVEs that huntr issued for ML libraries are also caught, passing through NVD.

The model/dataset layer is routed around until classifier support arrives. In the short term, models and datasets are uploaded as generic components, while core model card fields are carried through CycloneDX `properties` or external references to preserve them. Discoverability is limited, but traceability is preserved. Threats unique to model files (unsafe pickle, backdoored weights) don't fit the CVE matching model, so they are checked separately with ModelScan and the results are linked to policy or tickets.

## 6. Limitations and Items Requiring Verification

The tool facts in this strategy were confirmed against each project's official repository and documentation. The following require reconfirmation before adoption.

The licensing area carries the risk of a mismatch between what is declared and what is actually true. The so-called permissive-washing risk, in which the license declared on a platform diverges from the actual component license of the model or dataset, is well known, and it compounds an existing limitation: existing software license tools cannot parse model cards or dataset cards, or trace training data provenance. This toolset does not promise automatic detection for this and leaves verifying the match between declared license and actual output as a new-build target.

The timing of Dependency-Track's support for model/data classifiers (#4361) is an external schedule outside our control. Because P1's model/data inventory depends on this schedule, it should be designed with the workaround (preserving `properties`) as the default, promoting to first-class inventory once classifier support lands.

GUAC's AI-specific handling, OSV's model-specific record scheme, and any connector letting Dependency-Track directly consume huntr Insights and ModelScan results are all confirmed absent or unverifiable. No standard yet links model risk feeds and SBOM inventories, so this connection has to be filled with custom glue code.

There is no production tool for data poisoning detection. This toolset does not promise automatic poisoning detection and limits itself to traceability and preventive controls that record data provenance, hashes, and whether verification passed.

## 7. References

The tool determinations in this article were confirmed against each project's official repository and documentation as primary sources. All access dates are 2026-06.

**A1.** CycloneDX / cdxgen Project. *cdxgen — AI/ML BOM generation and the `aibom` CLI, `--spec-version`*. <https://github.com/CycloneDX/cdxgen> (accessed 2026-06). — *Used for: basis that cdxgen's `aibom` automatically generates CycloneDX 1.6 AI BOMs.*

**A2.** CycloneDX. *Machine Learning Bill of Materials (ML-BOM) Capability Overview*. <https://cyclonedx.org/capabilities/mlbom/> (accessed 2026-06). — *Used for: standard basis that CycloneDX 1.6 defines `machine-learning-model` and modelCard.*

**A3.** SPDX. *SPDX 3.0.1 — AI Profile Specification*. <https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/> (accessed 2026-06). — *Used for: basis that the SPDX 3.0 AI Profile exists at the specification level (expressiveness comparison).*

**A4.** SPDX. *tools-python (spdx-tools) — 3.0 experimental write-only, not recommended for production*. <https://github.com/spdx/tools-python> (accessed 2026-06). — *Used for: basis that no mature tool exists to generate the SPDX 3.0 AI Profile.*

**A5.** interlynk-io. *sbomqs — Policy Guide (custom policy, required type, feature scoring)*. <https://github.com/interlynk-io/sbomqs/blob/main/docs/guides/policy.md> (accessed 2026-06). — *Used for: basis that sbomqs enforces field presence via custom policy and converts it into a conformance score.*

**A6.** Open Policy Agent. *Conftest — OPA/Rego policy evaluation for configuration files*. <https://github.com/open-policy-agent/conftest> (accessed 2026-06). — *Used for: basis that CycloneDX/SPDX JSON can be evaluated with Rego to branch role-specific required sets.*

**A7.** OWASP Dependency-Track. *Policy Compliance Documentation (condition types, regex values)*. <https://docs.dependencytrack.org/usage/policy-compliance/> (accessed 2026-06). — *Used for: basis that the Dependency-Track policy engine centers on license, vulnerability, and component coordinates, with policies configurable per project/tag.*

**A8.** DependencyTrack. *Issue #4361 — Request to support CycloneDX 1.5/1.6 classifiers (`machine-learning-model`, `data`)*. <https://github.com/DependencyTrack/dependency-track/issues/4361> (accessed 2026-06). — *Used for: basis that Dependency-Track does not yet ingest the model/data classifiers or modelCard (open as of this research).*

**A9.** Protect AI. *ModelScan — Static Scanner for Model Serialization Attacks (JSON reports, exit codes)*. <https://github.com/protectai/modelscan> (accessed 2026-06). — *Used for: basis that model file serialization scanning is mature enough to insert into CI.*

**A10.** Sigstore / OpenSSF. *model-transparency (model-signing) — DSSE + in-toto Model Signing*. <https://github.com/sigstore/model-transparency> (accessed 2026-06). — *Used for: basis that model signing and provenance attestation map onto BOM integrity and provenance fields.*

**A11.** Z. Tian et al. (2025). *Data Poisoning in Deep Learning: A Survey*. <https://arxiv.org/html/2503.22759v1> (accessed 2026-06). — *Used for: basis that data poisoning detection remains at the research stage with no general-purpose production tool.*

**A12.** AboutCode. *ScanCode Toolkit — License and Copyright Text Matching Engine*. <https://github.com/aboutcode-org/scancode-toolkit/> (accessed 2026-06). — *Used for: basis for reusing the license identification engine while noting that AI license text needs to be added.*

**A13.** Responsible AI Licenses (RAIL). *FAQ / BigScience OpenRAIL-M — Use-Based Restrictions That Propagate to Derivatives*. <https://www.licenses.ai/faq-2> (accessed 2026-06). — *Used for: basis that no standard exists for machine-reading and automatically determining RAIL-family conduct restrictions.*

**A14.** LF AI & Data. *Simplifying AI Model Licensing with OpenMDW*. <https://lfaidata.foundation/blog/2025/07/22/simplifying-ai-model-licensing-with-openmdw/> (accessed 2026-06). — *Used for: basis that OpenMDW, a permissive license bundling models, data, and weights, is listed with SPDX (a candidate for the AI license dictionary).*

**A15.** Protect AI. *huntr — Bug Bounty and CNA for AI and ML*. <https://huntr.com/> (accessed 2026-06). — *Used for: basis that CVEs issued by huntr flow into Dependency-Track matching via NVD.*

**A16.** Google and OpenSSF. *OSV.dev — Open Source Vulnerability Database*. <https://osv.dev/> (accessed 2026-06). — *Used for: basis that OSV includes ML library vulnerabilities but does not record model-weight-specific risks themselves.*

**A17.** Trail of Bits. *Fickling — Static Analysis Tool for Pickle*. <https://github.com/trailofbits/fickling> (accessed 2026-06). — *Used for: basis for a high-risk pickle deep-inspection tool.*

**A18.** OSS Review Toolkit. *ORT — License Compliance Orchestration*. <https://github.com/oss-review-toolkit/ort> (accessed 2026-06). — *Used for: basis for reusing the policy rule engine and SBOM reporter.*

**A19.** OpenSSF. *GUAC — SBOM Graph and Impact Analysis*. <https://guac.sh/> (accessed 2026-06). — *Used for: basis that it is an option for reinforcing impact analysis, while AI-specific handling remains unverified.*
