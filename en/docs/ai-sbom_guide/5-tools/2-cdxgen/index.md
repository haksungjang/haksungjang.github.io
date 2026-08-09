# cdxgen

> Explains how to use the AI BOM mode of OWASP cdxgen, which generates a CycloneDX SBOM from projects and models, together with actual execution output.

---

LLMS index: [llms.txt](/llms.txt)

---

## Overview

cdxgen is the official SBOM generator of the OWASP CycloneDX project. It supports more than 20
languages and package managers, and the latest version offers a dedicated AI BOM mode. It
automatically identifies the dependencies of AI applications (PyTorch, Transformers, and so on) and
integrates well with CI/CD pipelines.

From an AI SBOM standpoint, cdxgen's strength is speed and automation. Its weakness is that it does
not fill in license information in a default run. This trait shows up in the execution result below.
Where OWASP AIBOM Generator centers on model card metadata, cdxgen centers on code and dependencies.
Using both together covers both models and dependencies.

## Key Features

- Identifies dependencies from source code and container images to generate a CycloneDX SBOM.
- Includes AI/ML metadata (formulation) with AI BOM mode (`-t ai`).
- Takes Hugging Face model URLs, Modelfiles, and GGUF artifacts directly as input.
- Automatically submits SBOMs to a Dependency-Track server for continuous management.

## Installation

```bash
# One-off run (requires Node.js)
npx @cyclonedx/cdxgen@latest --version

# Global install
npm install -g @cyclonedx/cdxgen
```

## Usage — Generating an AI BOM

Run in AI BOM mode from the AI project directory.

```bash
# Generate an AI BOM
cdxgen -t ai -o aibom.json .

# Generate including AI/ML metadata (formulation)
cdxgen -t ai --include-formulation -o aibom.json .
```

Below is the actual result of running cdxgen against a summarization app (`transformers`, `torch`
dependencies) that loads a pretrained model (`facebook/bart-large-cnn`). It automatically identifies
5 dependencies and produces a CycloneDX 1.7 BOM.

```text
$ cdxgen -t python --include-formulation -o aibom.json .
CycloneDX Generator 12.5.1 (Node.js)

Generated components — 5 entries (CycloneDX 1.7):
  transformers     4.44.2    pkg:pypi/transformers@4.44.2      license: empty
  torch            2.4.0     pkg:pypi/torch@2.4.0             license: empty
  numpy            1.26.4    pkg:pypi/numpy@1.26.4            license: empty
  tokenizers       0.19.1    pkg:pypi/tokenizers@0.19.1       license: empty
  huggingface-hub  0.24.6    pkg:pypi/huggingface-hub@0.24.6   license: empty
```

**Figure 1.** cdxgen execution output *(cdxgen 12.5.1, run 2026-06-13)*

One of the generated components looks like this. The identification evidence is filled in, but the
`licenses` field is empty.

```json
{
  "name": "transformers",
  "version": "4.44.2",
  "purl": "pkg:pypi/transformers@4.44.2",
  "type": "library",
  "evidence": {
    "identity": [
      { "field": "purl", "confidence": 0.5,
        "methods": [{ "technique": "manifest-analysis", "value": "requirements.txt" }] }
    ]
  }
}
```

## What the Execution Result Shows

<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">cdxgen identifies quickly, but a human must fill in the license</div>


cdxgen quickly identified 5 dependencies from `requirements.txt`, but the `licenses` field of each
component is empty. Also, the pretrained model `facebook/bart-large-cnn` that the app loads was not
captured in the BOM by code scanning alone. It must be collected separately as inbound material and
added. A realistic combination is to build the dependency skeleton quickly with cdxgen, have a human
verify and fill in the licenses, and generate the model separately with OWASP AIBOM Generator before
merging.
</div>


## See Also

- AI SBOM generation and management procedure: [3.9 AI SBOM](../../2-ai-extension/3-ai-sbom/)
- Generator centered on model metadata: [OWASP AIBOM Generator](../1-aibom-generator/)
- SBOM management: [Dependency-Track](https://openchain-project.github.io/OpenChain-KWG/guide/tools/7-dependency-track/), [cdxgen + Dependency-Track integration](https://openchain-project.github.io/OpenChain-KWG/guide/tools/8-cdxgen-dt/)
- Official: [cdxgen AI-BOM documentation](https://github.com/cdxgen/cdxgen/blob/master/docs/AI_BOM.md)
