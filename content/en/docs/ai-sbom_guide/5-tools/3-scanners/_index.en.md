---
title: "Model and Container Scanners (Lab700x, Trivy, Syft)"
linkTitle: "Model and Container Scanners"
weight: 30
type: docs
categories: ["guide"]
tags: ["AI SBOM", "Security", "Tools"]
description: >
  Introduces the key features and usage of security scanners that analyze AI model binaries,
  inference servers, and AI packages.
---

This page introduces analysis and identification tools that complement AI SBOM generation. Where
the generation tools (OWASP AIBOM Generator, cdxgen) record "what is in it," these tools look at
"whether it is safe" and "what version it is." The commands and features below are organized based
on each tool's official documentation (the tools actually run in this guide are
[OWASP AIBOM Generator](../1-aibom-generator/) and [cdxgen](../2-cdxgen/)).

## Lab700x AI SBOM Scanner — Static Analysis of Model Binaries

A tool that statically analyzes AI model files themselves to extract information. It performs deep
introspection on model binaries such as `.safetensors`, `.pt` (PyTorch), and `.pkl` (Pickle) without
executing them.

- **Key features**: Because it examines internal structure without executing the model, it can
  detect malicious code hidden in a model file (such as Pickle injection), vulnerabilities, or
  license violations before deployment.
- **Role in AI SBOM**: Used to inspect externally sourced models at the intake gate. Combined with
  the inbound metadata enforcement of
  [3.5 License Obligations](../../2-ai-extension/1-license-obligations/), it lets metadata
  verification and binary safety checking be performed together.

Pickle-format models carry a significant supply-chain risk because arbitrary code can execute during
deserialization. Inspecting the model without executing it is the core of this tool.

## Trivy — Scanning LLM Inference Server Containers

An open source scanner from Aqua Security that checks vulnerabilities in container images and
filesystems. It recently added awareness of AI model infrastructure.

- **Key features**: Scans LLM inference server containers such as Ollama and LocalAI to collect the
  open source libraries they contain and their container vulnerabilities.
- **Usage**:

```bash
# Scan a container image (vulnerabilities)
trivy image ollama/ollama:latest

# Generate an SBOM (CycloneDX)
trivy image --format cyclonedx --output sbom.json ollama/ollama:latest
```

Used in environments that deploy AI models as containers, to leave a record of the inference
server's vulnerabilities and components as an SBOM.

## Syft — Identifying AI Packages and Virtual Environments

An SBOM generator from Anchore that scans containers, filesystems, and virtual environments.

- **Key features**: Analyzes Python virtual environments to collect the exact versions of packages
  used to run AI, such as PyTorch and Transformers. Outputs in SPDX and CycloneDX format.
- **Usage**:

```bash
# Scan a directory and output CycloneDX
syft scan dir:. -o cyclonedx-json=sbom.json

# Scan a container image
syft scan registry:python:3.11-slim -o spdx-json
```

Its role overlaps with cdxgen's, so an organization already using the Anchore toolset (Syft, Grype)
would naturally generate the dependency SBOM of an AI application with Syft and check vulnerabilities
with Grype.

## Recommended Tool Combination

No single tool solves everything. In practice, combine tools by dividing up their roles.

| Purpose | Tool |
|------|------|
| Model metadata AIBOM generation | OWASP AIBOM Generator |
| Dependency SBOM generation | cdxgen, Syft |
| Model binary safety inspection | Lab700x AI SBOM Scanner |
| Inference server / container vulnerabilities | Trivy |
| SBOM storage and vulnerability monitoring | [Dependency-Track](https://openchain-project.github.io/OpenChain-KWG/guide/tools/7-dependency-track/) |

## See Also

- AI SBOM generation and management procedure: [3.9 AI SBOM](../../2-ai-extension/3-ai-sbom/)
- Execution results of generation tools: [OWASP AIBOM Generator](../1-aibom-generator/), [cdxgen](../2-cdxgen/)
