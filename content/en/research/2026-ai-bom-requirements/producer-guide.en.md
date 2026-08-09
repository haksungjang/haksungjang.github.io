---
title: "AI BOM Authoring Guidelines for In-House Development Teams"
linkTitle: "In-House Authoring Guide"
date: 2026-06-29
weight: 2
type: docs
description: >-
  Guidelines for the AI BOM that in-house development teams must produce when building an AI
  model or system. Drawing on the information accessibility available at the point of
  production, this sets out the required and recommended fields to fill and how to record
  integrity and provenance.
author: Haksung Jang
categories: ["research"]
tags: ["SBOM", "AI BOM", "SPDX", "CycloneDX", "Software Supply Chain Security", "Dependency-Track"]
ai_generated: true
---

{{% alert color="info" %}}
This article was written with Claude Code, and the key facts cited here were cross-checked against primary sources.
{{% /alert %}}

This document sets out the guidelines for the AI Bill of Materials (AI BOM) that in-house development teams must produce when building an AI model or AI system. Information accessibility is at its best at the point of production, so this document sets the required level at its highest. The required fields are drawn from the production column of the [AI BOM Field Requirements Matrix]({{< relref "_index.md" >}}).

Much of the information that the production team fails to record can never again be obtained by the adopting team or by parties further down the supply chain. For that reason, model and dataset details that the consensus baseline treats as optional are recommended for production-time authoring.

## 1. Authoring Principles

The AI BOM is generated after model training or system build completes. The lifecycle stage at the time of generation (pre-build, build, or post-build) is recorded in the metadata. Use SPDX 3.0 or later, or CycloneDX 1.6 or later, as the format, and where possible generate it automatically with a generation tool, then fill in the missing items by hand.

Fields whose value cannot be determined must be marked "unable to confirm" rather than left blank. Whenever a model or dataset is updated, the AI BOM version and timestamp are updated together.

## 2. Required Fields

The following must always be filled in. These are the items for which two or more standards in the matrix require presence.

| Cluster | Required fields |
|---|---|
| Metadata | Author, data format name, data format version, timestamp, dependency relationships |
| System level | System name, system components, system producer, system version |
| Model | Model name, model identifier, model version, model timestamp, model producer, model license |
| Dataset | Dataset name, dataset contents, dataset identifier, dataset provenance, dataset license |

## 3. Recommended Fields

The following are optional under the consensus baseline, but since they can only be recorded accurately at the point of production, authoring them is recommended. If model cards and data cards are maintained, their contents should in particular be linked to the AI BOM.

| Cluster | Recommended fields | Reason to author |
|---|---|---|
| Metadata | SBOM version, author signature, tool name and version, generation context | Securing integrity and traceability |
| System level | Data flow, data usage, input/output properties, intended application domain | Basis for downstream risk assessment |
| Model | Model description and lineage, model hash value and algorithm, model properties, input/output properties, training properties, external references | Reproducibility and integrity verification, linkage to model cards |
| Dataset | Dataset description, dataset hash, statistical properties, dataset sensitivity, dependency relationships | Basis for data lawfulness and risk assessment |
| Security and metrics | Security controls, security assertions, vulnerability references, security metrics, operational metrics | Linkage to cybersecurity risk management |

## 4. Model Hashes and Integrity

The model hash value and algorithm are optional under the consensus baseline, but the recommendation is strong. Recording the hash of the weight file or model artifact lets downstream parties verify model integrity. For the hash algorithm, use hash function names from the Internet Assigned Numbers Authority (IANA), and use algorithms approved by the National Institute of Standards and Technology (NIST).

## 5. Dataset Provenance and Sensitivity

The production team knows the provenance of the training dataset best. Record the source, the collection method, the preprocessing and labeling steps, and whether synthetic data was used, and indicate whether personally identifiable information, copyrighted data, or sensitive data is included. This information serves as the basis for meeting the training data documentation obligations of the AI Act and the training data overview requirements of Korea's Framework Act on Artificial Intelligence.

## 6. Post-Authoring Checklist

- Are all the required fields in Section 2 filled in?
- Among the recommended fields in Section 3, have those obtainable from model cards or data cards been linked?
- Are licenses stated separately for the model weights and for the dataset?
- Is the lifecycle stage at the time of generation recorded?
- When the model or dataset is updated, are the version and timestamp updated as well?
