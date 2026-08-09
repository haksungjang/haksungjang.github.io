# 1. Open Source Policy (Sample)

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-primary" role="alert"><div class="h4 alert-heading" role="heading">Note:</div>


This sample open source policy was written with reference to the following two materials.

1. [OpenChain Open Source Policy Template](https://github.com/OpenChain-Project/Reference-Material/blob/master/Open-Source-Policy/Official/2.1/en/Open-Source-Policy-Template-en-OpenChain2.1-ISO5230.xlsx)
2. [Linux Foundation Generic FOSS Policy](https://github.com/todogroup/policies/blob/master/linuxfoundation/lf_compliance_generic_policy.pdf)
</div>



## 1. Purpose

### (1) Purpose of the Policy<sub>(3.1.3.1)</sub>

This policy provides the following principles for the correct use of open source software (hereinafter "Open Source") by every organization at [Company Name], Inc. (hereinafter "the Company") that is involved in software development, service delivery, and distribution.

1. Principles for carrying out compliance with open source licenses
2. Principles for contributing to external open source projects
3. Principles for releasing internal projects as open source

These principles give every member of the Company a way to understand the value of open source, use open source correctly, and contribute to open source communities.

All members of the Company can find the open source policy at the following link on the internal wiki: [internal_link]<sub>(3.1.1.1)</sub>

### (2) Impact of Non-Compliance
Failure to comply with this policy can result in the following situations.

- The Company receives demands from outside parties to comply with open source licenses.
- The Company is forced to release source code it did not intend to release.
- The Company faces legal action from open source copyright holders.
- The Company is fined for copyright infringement or breach of contract, or is ordered to stop selling a product.
- The Company's reputation suffers.
- The Company breaches a contract with a supplier and faces a claim for damages.

For these reasons, the Company treats violations of this open source policy as serious, and members or organizations that violate it may be subject to disciplinary action.

### (3) How Members Can Contribute

All members of the Company can contribute to the effectiveness of this policy and to raising the Company's compliance level by understanding the rationale and content of this policy and faithfully carrying out the required activities.

## 2. Scope<sub>(3.1.4.1)</sub>
This policy applies to the following three areas.

1. It applies to [all products the Company provides or distributes externally]. However, using open source solely for internal purposes is not within the scope of this policy.
2. It applies when a member contributes to an external open source project.
3. It applies when releasing internal code as open source.

The scope can be changed to fit the Company's business environment, and the procedure for doing so is as follows.

1. If the open source program manager determines that a change in the policy's scope is needed due to changes in the Company's business environment, such as new business or organizational restructuring, they submit a proposal for this to the OSRB.
2. The OSRB approves an appropriate level of change to the scope.
3. The OSRB revises the open source policy to change the policy's scope.


## 3. Terminology
* BOM (Bill of Materials)
* Software distribution participant: refers to any employee involved in the Company's development, distribution, or contribution of software, including software developers, release engineers, and quality engineers.
* ...

## 4. Roles, Responsibilities, and Competencies<sub>(3.1.2.1)</sub>
  To ensure the effectiveness of this policy, the following roles, responsibilities, and the competencies required of each role's assignee are defined.

 The organization/person responsible for each role and the required competency level are defined in [Appendix 1. Roster of Responsible Parties].<sub>(3.1.2.2)</sub>

* The open source program manager periodically updates the roster to fit the Company's business situation.<sub>(3.2.2.1)</sub>
* The head of the organization responsible for each role designates a person in charge within the organization and allocates appropriate time and budget so that person can carry out the role faithfully.<sub>(3.2.2.2)</sub>
  * If a person responsible for a role feels they are not receiving adequate support in carrying it out, they must raise the issue with the open source program manager.
  * The open source program manager discusses resolving the issue with the relevant head of organization. If it is not resolved appropriately, the open source program manager can ask the OSRB to help resolve the issue.
  * The OSRB shares the issue with the head of the higher-level organization and requests a resolution.

### (1) OSRB
The OSRB (Open Source Review Board) is a body composed of the open source program manager and the heads of relevant organizations, including Legal, Patents, Development, and Infrastructure, formed for the Company's open source compliance.

* It creates the policies and processes for open source compliance and defines the roles and responsibilities within the Company for carrying them out.
* When an open source compliance issue arises within the Company, it discusses solutions and prepares a response.
* When necessary, it reports issues to executive leadership and obtains feedback on risk mitigation measures.

### (2) Open Source Program Manager
The open source program manager is overall responsible for the Company's open source program. To ensure open source compliance for products and services that use open source, they are responsible for the following.<sub>(3.2.2.4)</sub>

- Define the roles needed for open source compliance and designate the responsible organization and person for each role. Consult with the OSRB as needed.
- Organize and evaluate open source compliance training.
- Chair the OSRB and direct its activities.
- Respond to inquiries and requests from outside parties about open source use and compliance.
- Review and approve requests to use open source.
- Maintain records of the open source BOM.
- Provide members with a way to obtain open source-related legal counsel.<sub>(3.2.2.3)</sub>
- Maintain a repository for open source notices and source code releases.

### (3) OSPO
The OSPO (Open Source Program Office) supports and fosters the growth of open source activity both inside and outside the Company.

- Establishes, improves, and disseminates the open source policy.
- Provides guidance for contributing code to external open source projects.
- Provides guidance for releasing internal projects as open source.
- Develops and operates the open source portal.
- Develops and selects open source tooling.
- Sponsors open source project events.
- Manages relationships with open source communities.

### (4) Legal
Legal provides counsel on the legal risks that can arise in the course of using open source, and on mitigation measures, including interpreting open source licenses and obligations.

- Provides counsel on license and intellectual property issues, including conflicts arising from incompatible open source licenses.
- Reviews the legal matters required for contributing to external open source projects, including the open source license and the CLA (Contributor License Agreement).

### (5) IT Infrastructure
IT Infrastructure operates and automates open source analysis tooling, and builds the systems needed to ensure license analysis is carried out smoothly for all distributed software.

- Operates open source license analysis tooling.
- Integrates with the DevOps environment to automate license analysis.
- Builds the systems and processes needed to ensure license analysis is performed on all distributed software.
- Obtains and maintains the open source BOM for all distributed software.

### (6) Security
Security operates open source security vulnerability analysis tooling and builds the systems needed to ensure security vulnerability analysis is carried out smoothly for all distributed software.

- Operates open source security vulnerability analysis tooling.
- Integrates with the DevSecOps environment to automate open source security vulnerability analysis.
- Builds the systems and processes needed to ensure open source security vulnerability analysis is performed on all distributed software.

### (7) Developer Relations
Developer Relations supports in-house developers so they can actively use open source, participate in internal and external communities, and adopt leading development practices.

- Encourages participation in open source communities.
- Fosters a culture that recognizes active external open source project activity as an internal accomplishment.
- Builds a development culture that makes the Company attractive to open source developers.

### (8) Quality
The organization responsible for quality, such as QA, confirms that open source license obligations were properly carried out when software is distributed.

- Confirms that open source compliance activities were carried out at each stage of the development process.
- Confirms that the artifacts required by the open source licenses were produced.
- Confirms that the open source notice and any source code to be released are provided together with the distributed software.
- Notifies the software development/distribution organization of any issues found so they can be corrected immediately.


## 5. Training and Assessment
Every software distribution participant must complete the mandatory open source training provided on the [Learning Portal] each year. This ensures they are familiar with the open source policy, the related training policy, and how to look it up. Training records are retained on the [Learning Portal].<sub>(3.1.1.2)</sub>

Every member responsible for a role defined in Section 4 must complete the advanced open source training course provided on the [Learning Portal]. Training records and assessment results are retained on the [Learning Portal] for at least three years.<sub>(3.1.2.3)</sub>

## 6. Open Source Use

To develop and distribute products and services using open source, the obligations required by each open source license must be complied with. This activity is called open source compliance.

To carry out open source compliance correctly, the software development/distribution organization must comply with the following.<sub>(3.3.1.1)</sub>

* Every step of the open source compliance process is recorded and retained in the Jira Tracker.

### (1) Identifying Open Source and Reviewing License Obligations

When introducing open source into product/service development, first identify what open source license applies, and review and confirm the obligations the license requires.

The Company's [Open Source License Guide] includes a list of major open source licenses, and for each license, it separately explains the obligations required for each of the following distribution forms.<sub>(3.3.2.1)</sub>

- Binary form
- Source form
- Strong/weak copyleft
- SaaS-based delivery
- Whether modified
- Inclusion of open source requiring attribution, and so on.

The software development/distribution organization can refer to this guide when reviewing open source license obligations. If a review is needed for an open source license not covered in this guide, contact the open source program manager.

### (2) Designing with Open Source Licenses in Mind

Identify the combination relationships of open source components and design the software architecture so that the Company's own code is not affected by open source license terms.

The Company's [Open Source License Guide] explains, for each open source license, the scope of source code disclosure it requires and design methods for preventing disclosure of the Company's own code.

### (3) Producing Open Source Compliance Artifacts
The most basic part of open source compliance activity is understanding the open source contained in distributed software. This is precisely so that the open source license requirements at the core of open source compliance can be correctly satisfied. In other words, a set of compliance artifacts must be produced for the open source contained in distributed software.<sub>(3.4.1.1)</sub>

Open source compliance artifacts fall into two broad categories.

1. Open source notice: a document providing the full text of each open source license and copyright information
2. Source code package to be released: a package assembling the source code to be released to fulfill the obligations of open source licenses that require source code disclosure, such as GPL and LGPL

To assemble, distribute, and store these compliance artifacts, the following must be complied with.<sub>(3.4.1.2)</sub>

- Assemble the open source notice and the source code package to be released according to the conditions each license requires. For example, if a license requires that the full text of the license be included, providing only a link is not sufficient.
- Store the assembled artifacts in a separate repository.
- When providing source code to be released through a Written Offer, publish a download link so that external parties can access the repository of assembled artifacts.

The Company's open source compliance process can be used to issue the open source notice and assemble the source code package to be released.

### (4) Producing the Open Source BOM (Bill of Materials)
The open source contained in distributed software (BOM: Bill of Materials) must be produced and maintained.<sub>(3.3.1.2)</sub>

The Company's open source compliance process can be used to produce and retain the open source BOM using open source tooling.

### (5) Compliance Issue Remediation Procedure

When a compliance issue is raised, the open source program manager performs the following procedure to respond promptly.<sub>(3.2.2.5)</sub>

1. Acknowledge receipt of the inquiry and specify an appropriate resolution time.
2. Confirm whether the issue content points to an actual problem. (If not, inform the person who raised the issue that it is not a problem.)
3. If it is an actual problem, determine priority and decide on an appropriate response.
4. Carry out the response, and if necessary, appropriately update the open source compliance process.
5. Retain the above content using the Jira Tracker.

## 7. Open Source Contribution
The Company encourages participation in and contribution to external open source projects to create business value from open source. However, approaching this without sufficient understanding of and strategy for the open source project ecosystem and how communities operate can lead to unintended exposure of the Company's intellectual property or infringement of third-party rights. For this reason, when a member of the Company contributes to an external open source project, the following must be complied with.<sub>(3.5.1.1)</sub>

### (1) Requesting Review and Approval

From a copyright standpoint, an open source contribution grants the open source project the right to modify, use, and distribute the contributed work. In some cases, it may even require assigning your copyright to the open source project. However, the copyright to a work created during a period of employment generally belongs to the employer. In other words, a work created by a Company member belongs to the Company. If a member contributes a work to open source on their own judgment, it can create unnecessary copyright infringement issues.

Therefore, if there is an open source project you wish to contribute to, follow the review request and approval procedure defined by the open source contribution process before making your first contribution.

However, for the following kinds of simple content, the copyright infringement risk is low, so members may contribute based on their own judgment without going through the review procedure.

- Small code snippets of 10 lines or fewer
- Questions and answers on Stack Overflow
- Administrative activity on GitHub, such as creating issues or reviewing/approving pull requests

### (2) Contribute Only Code You Have the Right to Contribute
Contribute only code you have the right to contribute. That is, contribute code you wrote yourself. Do not contribute third-party code on your own judgment.

### (3) Beware of Intellectual Property Exposure
Do not contribute code or documents that raise concerns about exposing the Company's intellectual property, such as sensitive information or patents.

* If the code you wish to contribute includes a Company patent, you must confirm whether it is acceptable to contribute that patent to the project under an open source license. If anything is unclear, contact the OSPO.

### (4) Caution with CLA Signatures
Some open source projects require every contributor to sign a CLA (Contributor License Agreement). This is an agreement used to obtain contributors' consent in order to reduce copyright disputes that can arise as a project manages the works of many contributors. Projects led by large corporations commonly require a CLA signature.

CLAs vary by project, but they generally include agreement to the following.

- I (or my employer) have the right to contribute the contribution I intend to contribute to the project. (That is, I am the author of this contribution.)
- I (or my employer) grant the project the right to modify, distribute, and manage my contribution.
- I (or my employer) will not revoke the granted rights.
- I (or my employer) grant the project the right to change its license in the future as needed.

In addition, though rare, some CLAs also require agreement to the following condition.

- I (or my employer), upon contributing my contribution, simultaneously assign my copyright in it to the project or the organization managing the project.

To protect its own intellectual property, the Company does not permit contributions to open source projects that require copyright assignment. To make this determination, a Company member must request a review from the OSPO before signing, if the open source project they wish to contribute to requires a CLA signature.

### (5) Copyright Notice

The intellectual property of a work created by a member during their employment generally belongs to the Company. Accordingly, when a member contributes code to an external open source project, they must indicate the Company's copyright.

When contributing one or more files, indicate the copyright and license at the top of the file as follows.

~~~
Copyright (c) {$year} {$Company}
SPDX-License-Identifier: {$SPDX_license_name}
~~~
Here, $SPDX_license_name is written according to the license policy of the relevant open source project.

However, if you are only modifying existing code, such as for a bug fix, there is no need to add a copyright notice for that code change.

### (6) Use of Company Email
Do not use a personal email address when contributing to open source projects; use your Company email address. This (1) gives members a sense of responsibility as they communicate with the community on the Company's behalf, and (2) helps improve the Company's recognition as one that actively contributes to open source communities.

## 8. Open Source Release

The Company respects the value of collaboration with open source communities and encourages releasing internal software as open source projects. However, there are some rules that must be followed to protect the Company's intellectual property and prevent unintended copyright infringement.

### (1) Approval
From a copyright standpoint, an open source release grants anyone the right to modify, use, and distribute the work through an open source license. The copyright to a work created during a period of employment generally belongs to the employer. In other words, a work created by a Company member belongs to the Company. If a member releases a work as open source on their own judgment, it can create unnecessary copyright infringement issues.

Therefore, if you wish to release software as open source, follow the review request and approval procedure under the Company's open source release policy.

If anything about the release process seems questionable, do not hesitate to contact the OSPO.

### (2) Release Only Code You Have the Right to Release

One of the worst situations that can arise in an open source project is the inclusion of legally problematic code in the project. Code the Company does not have the right to distribute, or code that infringes another company's IP such as a patent, can create legal problems. Therefore, when preparing code for release, verify the origin of all code and remove any code that raises concerns.

### (3) Beware of Intellectual Property Exposure
Do not release code or documents that raise concerns about exposing the company's intellectual property, such as sensitive information or patents.

If the code you wish to release includes a Company patent, confirm whether it is acceptable to release that patent under an open source license. If anything is unclear, contact the OSPO.

### (4) Release Useful Code
For a project to succeed, it must also be useful to others. If a similar project already exists, participate in the existing project rather than creating a new one.

The open source you plan to release should be expected to (1) provide differentiated value to the open source community, (2) solve a problem the community has not yet solved, and (3) draw positive attention by showcasing our technical capability.
* Do not release code as open source if it has not been used in an actual product or service.
* Do not release code that addresses a problem the open source community has already solved. In such cases, contribute to the existing open source project instead.

### (5) Securing Resources
Secure the resources, including developers, that need to be committed to the project.

* Initially, a level of developer effort similar to a typical internal project is needed.
* Developers are needed who can quickly review external contributions.
* Roles from Legal and Marketing are also needed.
* Secure budget for the infrastructure required to maintain and manage the project. This includes tools for project hosting, such as GitHub.

If an environment with sufficient resource support cannot be created, do not release the software as open source.

### (6) Use of Company Email
Do not use a personal email address for open source release activity; use your Company email address. This (1) gives members a sense of responsibility as they communicate with the community on the Company's behalf, and (2) helps improve the Company's recognition as a company that actively releases open source.

## 9. Responding to External Inquiries

### (1) Responsibility for Responding to External Inquiries
The open source program manager is responsible for responding to inquiries and requests about open source compliance from outside the Company.<sub>(3.2.1.2)</sub>

* The open source program manager can assign all or part of the handling of an inquiry to an appropriate person within the Company. If necessary, the legal team is consulted for handling.
* Anyone who receives an external inquiry about open source compliance should notify the open source program manager so that a prompt response can be made.

### (2) Publishing Contact Information
The open source program manager publicly provides the contact information of the responsible person so that external parties can make open source-related inquiries and requests.<sub>(3.2.1.1)</sub>

* Provide contact email address information in the open source notice.
* Register contact information in the Linux Foundation's Open Compliance Directory.

### (3) Procedure for Responding to External Inquiries
Responding quickly and accurately to external open source compliance inquiries can greatly reduce the risk of escalation to litigation. To this end, the Company complies with the external inquiry response procedure defined in the Company's open source compliance process to respond to external open source compliance inquiries.<sub>(3.2.1.2)</sub>

## 10. OpenChain
The Company supports the spirit of the Linux Foundation's OpenChain project and actively participates in it to raise the level of open source compliance across the software supply chain.

- By applying this open source policy, the Company ensures compliance with ISO/IEC 5230:2020 as of October 1, 2021.<sub>(3.6.1.1)</sub>
- The Company ensures that, for at least 18 months after obtaining conformance certification, it satisfies all requirements of OpenChain Specification version 2.1 and ISO/IEC 5230:2020.<sub>(3.6.2.1)</sub>
- The Company reviews conformance at intervals of at least 18 months and revises and updates the policy as needed.


## Appendix 1. Roster of Responsible Parties

| No | Role | Responsibility | Required Competency | Responsible Organization | Assignee |
|---|:---|:---|:---|:---|:---|
| 1 | Open Source Program Manager | Overall responsible for the Company's open source program. | 1. Understanding of the software development process<br>2. Understanding of intellectual property related to open source licenses, such as copyright and patents<br>3. Expert knowledge of open source compliance<br>4. Open source development experience<br>5. Communication skills | CTO | [Name] |
| 2 | Legal | Interprets open source licenses and obligations. Provides counsel to mitigate the legal risks that can arise in the course of using open source, including actually fulfilling those obligations. | 1. Basic knowledge of the open source ecosystem<br>2. Expert knowledge of software copyright<br>3. Expert knowledge of open source licenses | Legal | [Name] |
| 3 | Infrastructure | Operates and automates open source analysis tooling, and builds the systems needed to ensure license analysis is carried out smoothly for all distributed software. | 1. Basic knowledge of the open source compliance process<br>2. Understanding of open source license analysis tooling<br>3. Expert knowledge of IT infrastructure | IT Infrastructure Team | [Name] |
| 4 | Security | Operates open source security vulnerability analysis tooling and builds the systems needed to ensure security vulnerability analysis is carried out smoothly for all distributed software. | 1. Basic knowledge of the open source compliance process<br>2. Understanding of open source license analysis tooling<br>3. Expert knowledge of security | Security Team | [Name] |
| 5 | Development culture | Supports in-house developers so they can actively use open source, participate in internal and external communities, and adopt leading development practices. | 1. Understanding of the software development process<br>2. Basic knowledge of open source compliance<br>3. Understanding of the open source policy | DR | [Name] |
| 6 | Development team | The software development/distribution organization complies with the open source policy and process for correct use of open source. | 1. Understanding of the software development process<br>2. Basic knowledge of open source compliance<br>3. Understanding of the open source policy<br>4. Basic knowledge of open source licenses | Development Team | All |
