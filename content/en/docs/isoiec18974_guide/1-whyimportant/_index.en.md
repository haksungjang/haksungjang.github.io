---
title: "1. Why Does Open Source Security Matter?"
linkTitle: "1. Why Does Open Source Security Matter?"
weight: 10
type: docs
description: >
---

This chapter introduces the concepts of open source software and security assurance, and explains the background, purpose, importance, and certification benefits of the ISO/IEC 18974 standard.

## 1.1 The Concepts of Open Source Software and Security Assurance

Open source software (OSS, Open Source Software) refers to software whose source code is published, allowing anyone to freely use, modify, and distribute it. This offers the advantages of transparency, collaboration, and innovation, but it also carries security risks.

**Characteristics of Open Source Software**

- Published source code
- Free use, modification, and distribution
- Community-based development
- Cost efficiency

**Table 1.1: Advantages and Disadvantages of Open Source Software**

| Advantages | Disadvantages |
| --- | --- |
| Fast innovation and development speed | Risk of exposure to security vulnerabilities |
| High quality and stability | Unclear support and accountability |
| Flexibility and customization potential | Complexity of license compliance |
| Easier code review and improvement due to broad developer participation | Possible dependency on a specific project |

Open source has become an essential element in modern software development. Many companies use open source components rather than developing everything in-house, reducing development time and cost. However, this has [introduced](https://www.pwc.de/en/digitale-transformation/open-source-software-management-and-compliance/understanding-the-open-source-security-iso-18974.html) new risks into the software supply chain.

The main security risks arising from the use of open source are as follows.

1. **Known vulnerabilities (CVE, Common Vulnerabilities and Exposures)**: Systems can be exposed to attacks that exploit publicly disclosed vulnerabilities registered in databases such as CVE.
    - **Example**: The Log4Shell vulnerability ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)), which occurred in 2021, was found in Apache Log4j, a widely used open source logging library, and had a serious impact on countless systems worldwide. This vulnerability allowed attackers to execute remote code.
2. **Insertion of malicious code**: If malicious code is inserted into an open source repository, systems that download and use it can become infected.
3. **Legal problems from license violations**: Failing to comply with open source license terms can lead to legal disputes such as copyright infringement.
4. **Use of unsupported components**: Open source components that are no longer maintained make it difficult to respond to new vulnerabilities, increasing security risk.

'Security assurance' is needed to manage these risks. Security assurance is the process of confirming that software operates safely as intended and is free of known vulnerabilities or malicious code. This is [essential](https://openchainproject.org/featured/2023/03/16/introducing-dis-18974) for risk mitigation, building trust, and regulatory compliance.

## 1.2 Background and Objectives of the ISO/IEC 18974 Standard

ISO/IEC 18974 is the international standard for open source security assurance. This standard originated in the Linux Foundation's OpenChain project and defines the core requirements for managing the security of open source software.

The background to the development of the ISO/IEC 18974 standard is as follows.

- **Growing use of open source and the resulting security risk**: As the use of open source increases, attempts to exploit security vulnerabilities are also increasing.
- **Rise in software supply chain attacks**: Cases such as SolarWinds and Log4Shell, which caused large-scale damage by attacking the software supply chain, are increasing.
- **Recognition among companies of the need for systematic open source security management**: Companies are recognizing the security risks that come with using open source and feel the need to build a systematic management system.

The main objectives of the ISO/IEC 18974 standard are as follows.

1. **Providing a standardized framework for open source security management**: Supports organizations in building consistent processes and procedures for open source security management.
2. **Improving an organization's open source security processes**: Provides criteria by which an organization can assess and improve its own level of open source security management.
3. **Strengthening the overall security of the software supply chain**: Encourages all participants in the supply chain to comply with open source security requirements, raising the overall level of security.

## 1.3 The Purpose and Importance of ISO/IEC 18974

The main purpose of ISO/IEC 18974 is to enable organizations to build a system for effectively managing known security vulnerabilities in open source software. This standard identifies the following core areas.

1. The key points at which security processes are needed
2. How roles and responsibilities are assigned
3. How the sustainability of the process is ensured

In the global software industry, ISO/IEC 18974 serves as a benchmark for open source security management. It provides companies with a tool to objectively assess and improve their open source management capabilities.

Compliance with the standard has a positive effect on an organization's sustainability.

- **Cost savings from fewer security incidents**: Managing vulnerabilities proactively reduces the likelihood of security incidents and lowers recovery costs when incidents do occur.
- **Improved customer trust**: Demonstrating the ability to develop and deliver safe software builds customer trust.
- **Easier regulatory compliance**: Helps organizations comply with privacy regulations such as GDPR and CCPA.
- **Competitive advantage**: Meets the requirements of security-conscious customers, providing an edge over competitors.

## 1.4 Benefits of ISO/IEC 18974 Certification

Through ISO/IEC 18974 certification, companies can obtain the following benefits.

1. **Building a systematic open source management system**
    - Establishing consistent security policies and processes
    - Systematic identification, tracking, and control of open source components
    - Building a process for generating and managing an SBOM (Software Bill of Materials)
2. **Improved supply chain trust**
    - Strengthened trust relationships with partners and customers
    - Business stability secured through reduced security risk
    - Objective criteria for evaluating suppliers
3. **Recognition of open source management capability**
    - Demonstrating open source management capability at a global level
    - Enhanced corporate image and brand value
    - Creation of new business opportunities
4. **Reduced legal liability**
    - Compliance with license obligations and prevention of infringement
    - Reduced litigation risk
    - Easier regulatory compliance (e.g., DORA, EU Cyber Resilience Act)

## Summary

ISO/IEC 18974 underscores the importance of open source security management and provides companies with a framework for carrying it out systematically. By complying with this standard, companies can make full use of the benefits of open source while effectively managing the associated risks.
