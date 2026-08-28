---
title: "Tools"
linkTitle: "Tools"
weight: 50
type: docs
categories: ["guide"]
tags: ["AI SBOM", "Tools"]
description: >
  Introduces the key features and usage of open source tools that generate and analyze AI SBOMs, with actual
  execution screens.
---

This section covers open source tools that automate AI SBOM compliance. It summarizes each tool's key
features, installation, and usage together with actual execution results. This elaborates, tool by tool, on
the categories seen in the automation maturity map in [3.9 AI SBOM](../2-ai-extension/3-ai-sbom/).

There is a boundary worth stating honestly. Tools generate a BOM automatically, but they cannot guarantee
that the license information in the generated BOM is accurate or that no components are missing. In the tool
comparison below, OWASP AIBOM Generator fills in license information from model cards, while cdxgen quickly
identifies dependencies but leaves the license field empty. Look at this difference when choosing a tool.

## Tools at a Glance

| Tool | Input | Output | Strengths | Covered In |
|---|---|---|---|---|
| OWASP AIBOM Generator | Hugging Face model ID | CycloneDX 1.6/1.7 | Model card and license metadata, completeness score | [Go to section](./1-aibom-generator/) |
| cdxgen | Project directory, model files | CycloneDX | Automatic dependency identification, CI/CD integration | [Go to section](./2-cdxgen/) |
| Lab700x, Trivy, Syft | Model binaries, containers, virtual environments | Reports, SBOM | Static model analysis, inference server and package identification | [Go to section](./3-scanners/) |

Each tool automates part of the generation, analysis, or management stage. No single tool solves everything,
so combine tools that generate AI SBOMs (OWASP AIBOM Generator, cdxgen) with tools that analyze security
(Lab700x, Trivy) and a tool that manages them
([Dependency-Track](https://openchain-project.github.io/OpenChain-KWG/guide/tools/7-dependency-track/)).
