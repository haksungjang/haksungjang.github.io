# Supplier AI BOM Submission Requirements

> Requirements for the AI BOM that a supplier providing AI models or systems to your organization must submit. Defines the standard data format, the information that must be included, identifier rules, and the requirements for licensing, provenance, and sensitivity.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert">


This article was written with Claude Code, and the key facts cited here were cross-checked against primary sources.
</div>


This document defines the requirements for the AI Bill of Materials (AI BOM) that a supplier providing AI models or AI systems to your organization must submit. It extends the existing Software Bill of Materials (SBOM) submission requirements to models and datasets, and the required items were derived from the supplier column of the [AI BOM Field Requirements Matrix](/en/research/2026-ai-bom-requirements/).

## 1. Standard Data Format

The AI BOM must be submitted in a machine-readable standard format. The following two formats are accepted.

| Format | Version | AI representation | Notes |
|---|---|---|---|
| SPDX | 3.0 or later | `AIPackage` in the AI Profile, `DatasetPackage` in the Dataset Profile | Specifies model and dataset fields most tightly |
| CycloneDX | 1.6 or later | `machine-learning-model` and `data` component types, `modelCard` | Strong on vulnerability (VEX) linkage |

Both formats are accepted on equal terms, but SPDX 3.0, which enforces the required properties of models and datasets at the format level, is recommended. CycloneDX below 1.6 and SPDX 2.x have no AI-specific profile and are not accepted as submission formats.

## 2. Information That Must Be Included

The following items must be included in every submitted AI BOM. Items whose values cannot be confirmed must not be left blank; they must be marked explicitly as "unknown."

### 2.1 Document Metadata

| Item | Description |
|---|---|
| Author | The entity that generated the AI BOM. The formal name of the operating entity, not the tool |
| Data format name | SPDX or CycloneDX |
| Data format version | e.g., SPDX 3.0.1, CycloneDX 1.6 |
| Timestamp | Date and time of the last update (ISO 8601 or RFC 9557) |
| Dependency relationships | Containment and derivation relationships among components |

### 2.2 System-Level Information

| Item | Description |
|---|---|
| System name | An identifiable name for the supplied AI system |
| System components | The AI models, databases, and software included in the system |
| System producer | The entity that created the system |
| System version | The version of the supplied system |

### 2.3 Model Information

| Item | Description |
|---|---|
| Model name | The name assigned by the model producer |
| Model identifier | A machine-readable identifier such as a PURL or CPE |
| Model version | The version of the model |
| Model producer | The entity involved in pretraining, post-training, or fine-tuning |
| Model license | The license type, including whether it is open weight, and a link to the license document |

### 2.4 Dataset Information

| Item | Description |
|---|---|
| Dataset name | The name of the dataset used for training or evaluation |
| Dataset identifier | The dataset URL or URI |
| Dataset provenance | Source, collection method, preprocessing and labeling steps, and whether synthetic data was used |
| Dataset sensitivity | Whether personally identifiable information, copyrighted data, or other sensitive data is included |
| Dataset license | The dataset license type and a link to the document |

### 2.5 Security Information

| Item | Description |
|---|---|
| Vulnerability referencing | A link to the database or repository providing known vulnerability information for the model and system |

Vulnerability referencing is optional under the consensus criteria, but it is treated as required for supplier submissions because the Cyber Resilience Act and U.S. Food and Drug Administration (FDA) guidance require it directly.

## 3. Identifier Rules

Models and datasets must be identified with machine-readable standard identifiers.

- Model identifiers use a Package URL (PURL) or Common Platform Enumeration (CPE). Native identifiers such as a model repository path or commit hash may be provided alongside these.
- Dataset identifiers use an accessible URL or URI.
- If multiple identifiers exist, all of them must be included.

## 4. Strengthened Requirements for Licensing, Provenance, and Sensitivity

Unlike existing software SBOM requirements, the AI BOM enforces the following three items with particular strictness.

Licensing must be stated separately for the model weights and the dataset. The submission must distinguish whether the model is open weight, open architecture, or open data, and must provide a link to the license document. Dataset provenance must go beyond a simple source statement to include the collection method (web crawling versus a commercial agreement), preprocessing and labeling steps, and whether synthetic data was used. Dataset sensitivity must indicate whether personally identifiable information, copyrighted data, or sensitive data such as financial or medical data is included.

## 5. Sample Document

The following is a minimal AI BOM skeleton in CycloneDX 1.6 format. An actual submission must fill in all the required items from Section 2 above.

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "metadata": {
    "timestamp": "2026-06-29T09:00:00Z",
    "authors": [{ "name": "Supplier legal name" }],
    "component": { "type": "application", "name": "Supplied AI system", "version": "1.0.0" }
  },
  "components": [
    {
      "type": "machine-learning-model",
      "name": "Supplied model name",
      "version": "1.0",
      "bom-ref": "pkg:huggingface/org/model@1.0",
      "supplier": { "name": "Model producer" },
      "licenses": [{ "license": { "id": "Apache-2.0" } }],
      "modelCard": {
        "modelParameters": {
          "datasets": [
            { "type": "dataset", "name": "Training dataset name", "classification": "public",
              "governance": { "owners": [{ "organization": { "name": "Data source" } }] } }
          ]
        }
      }
    }
  ],
  "vulnerabilities": []
}
```

## 6. Pre-Submission Verification Checklist

Suppliers must confirm the following before submission.

- Is the format SPDX 3.0 or later, or CycloneDX 1.6 or later?
- Are all required items from Section 2 filled in, or explicitly marked "unknown"?
- Are the model and dataset identified with standard identifiers?
- Is a license stated for both the model weights and the dataset?
- Are dataset provenance and sensitivity indicated?
- Is a vulnerability reference link provided?
- Was it generated at a point in time after the build or model release was complete?

For detailed inspection criteria, see the [Ingestion Vetting Checklist](/en/research/2026-ai-bom-requirements/ingestion-checklist/).
