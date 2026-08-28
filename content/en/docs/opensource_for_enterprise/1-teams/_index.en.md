---
title: "1. Organization"
linkTitle: "1. Organization"
weight: 10
type: docs
categories: ["guide"]
tags: ["Organization"]
description: >
---

First, an enterprise must establish an organization responsible for open source management.

The following should be considered when forming the organization:

- Roles and responsibilities of the organization
- Competencies required for each role
- The organization/person responsible for each role

## 1. Defining the Roles and Responsibilities of the Organization

The ISO standards commonly require a document that describes the roles and responsibilities of the various participants in the program, as follows.

{{% alert title="ISO/IEC 5230 - License Compliance" color="success" %}}
* 3.1.2.1 - A documented list of roles with corresponding responsibilities for the different participants in the program.<br>`A document listing the roles of the various participants in the program and the responsibilities of each role`

{{% /alert %}}


{{% alert title="ISO/IEC 18974 - Security Assurance" color="warning" %}}

* 3.1.2.1: A documented list of roles with corresponding responsibilities for the different Program Participants<br>`A document listing the responsibilities of each of the various program participants`

{{% /alert %}}

### Open Source Program Manager

To build an open source management system, an enterprise first needs someone responsible for leading and carrying it out. This person is called by titles such as `Open Source Program Manager` or `Open Source Compliance Officer`; this guide uses the term `Open Source Program Manager`.

The Open Source Program Manager is in charge of the enterprise's Open Source Program Office (OSPO). `Open Source Program Office` refers to the organization responsible for an enterprise's open source management, and is also referred to by the term `Open Source Secretariat`.

A person with the following competencies can be considered well-suited for the role of Open Source Program Manager.

- Understanding of the open source ecosystem and development experience
- Broad understanding of the enterprise's business
- Passion and communication skills to spread effective open source use among employees

It is best for the Open Source Program Manager to be guaranteed the ability to perform the role full-time whenever possible.

Global ICT enterprises are making efforts to hire capable Open Source Program Managers of this kind. Various job postings can be found at the following site: [https://github.com/todogroup/job-descriptions](https://github.com/todogroup/job-descriptions)


### Documenting Roles and Responsibilities

An enterprise must define each role needed for the OSPO and determine what responsibilities to assign to it.

In a small enterprise, it is possible for the Open Source Program Manager alone to perform all the roles. Depending on the size of the enterprise, an IT staff member to operate open source tools may also be needed, and a legal role may be required to provide specialized legal counsel.

In general, the following roles are needed to build an enterprise's open source management system.

- Legal
- IT
- Security
- Developer Relations

{{< imgproc complianceofficer Fit "900x600" >}}
<center><i>Individuals and teams involved in ensuring open source compliance : https://www.linuxfoundation.org/wp-content/uploads/OpenSourceComplianceHandbook_2018_2ndEdition_DigitalEdition.pdf</i></center>
{{< /imgproc >}}


To this end, the roles and responsibilities that make up the OSPO must be documented as follows.

| No | Role | Responsibility |
|---|:---|:---|
| 1 | Open Source Program Manager | Holds overall responsibility for the company's open source program. |
| 2 | Legal | Interprets open source licenses and obligations. Provides advice to mitigate legal risks that may arise from open source use, including fulfilling these obligations in practice. | 
| 3 | IT | Operates and automates open source scanning tools, building a system so that open source analysis is performed smoothly for all software to be distributed. |
| 4 | Security | Operates open source vulnerability scanning tools, builds a system so that vulnerability analysis is performed for all software to be distributed, and takes action to ensure that identified vulnerabilities are remediated according to defined criteria. |
| 5 | Developer Relations | Supports in-house developers in actively using open source and participating in internal and external communities to adopt advanced development practices.  | 
| 6 | Business Unit | Software development/distribution organizations comply with open source policy and process to ensure proper open source use.  |


## 2. Defining Required Competencies

Once each role and its responsibilities have been defined, the essential competencies that the person performing that role must have need to be identified.

The ISO standards commonly require a document that describes the competencies needed for each role, as follows.

{{% alert title="ISO/IEC 5230 - License Compliance" color="success" %}}

* 3.1.2.2 - A document that identifies the competencies for each role.<br>`A document that describes the competencies needed for each role`

{{% /alert %}}


{{% alert title="ISO/IEC 18974 - Security Assurance" color="warning" %}}

* 3.1.2.2: A document that identifies the competencies for each role.<br>`A document that describes the competencies needed for each role`

{{% /alert %}}

This is because it is necessary to assess whether the person assigned to each role has the competencies to perform it, and to provide training if needed.

To this end, an enterprise must document the competencies needed for each role, as follows.


| No | Role | Required Competencies |
|---|:---|:---|
| 1 | Open Source Program Manager  | 1. Understanding of the software development process<br>2. Understanding of intellectual property related to open source licenses, including copyright and patents<br>3. Expert knowledge of open source compliance<br>4. Open source development experience<br>5. Communication skills<br>6. Basic knowledge of open source security assurance  |
| 2 | Legal | 1. Basic knowledge of the open source ecosystem<br>2. Expert knowledge of software copyright<br>3. Expert knowledge of open source licenses<br>4. Ability to assess open-source-related legal risk |
| 3 | IT | 1. Basic knowledge of the open source compliance process<br>2. Understanding of open source scanning tools<br>3. Expert knowledge of IT infrastructure<br>4. Understanding of automation and CI/CD pipelines |
| 4 | Security | 1. Broad understanding of [DevSecOps](https://www.redhat.com/ko/topics/devops/what-is-devsecops)<br>2. Understanding of open source vulnerability scanning tools<br>3. Expert knowledge of open source vulnerabilities<br>4. Communication skills<br>5. Risk assessment and management ability |
| 5 | Developer Relations | 1. Understanding of the software development process<br>2. Basic knowledge of open source compliance<br>3. Understanding of open source policy<br>4. Ability to design education and training<br>5. Experience participating in open source communities |
| 6 | Business Unit | 1. Understanding of the software development process<br>2. Basic knowledge of open source compliance<br>3. Understanding of open source policy<br>4. Basic knowledge of open source licenses<br>5. Understanding of the business impact of open source use |



## 3. Assigning Owners

The Open Source Program Manager consults with the relevant departments to assign an owner for each role and document this. To do so, the goals and direction for building the open source compliance system must be reported to the top decision-maker, such as the CEO, in order to obtain the necessary support.

The organization and owners related to open source do not necessarily need to work on open source full-time. It is also possible to form a virtual organization in the form of an OSRB (Open Source Review Board) to carry out the necessary roles.

The ISO standards commonly require a document naming the persons, groups, or functions responsible for each role in the program, as follows.

{{% alert title="ISO/IEC 5230 - License Compliance" color="success" %}}

* 3.2.2.1 - Document with name of persons, group or function in program role(s) identified.<br>`A document naming the persons, group, or function responsible for each role in the program`

{{% /alert %}}


{{% alert title="ISO/IEC 18974 - Security Assurance" color="warning" %}}

* 3.1.2.3: List of participants and their roles<br>`A list of participants and their roles`
* 3.2.2.1: Document with name of persons, group or function in Program role(s) identified<br>`A document naming the persons, group, or function responsible for each role in the program`

{{% /alert %}}

To this end, an enterprise must document the names of the persons, groups, or functions responsible for each role in the program, as follows.

| No | Role | Responsible Organization | Owner | 
|---|:---|:---|:---|
| 1 | Open Source Program Manager | CTO | OOO |
| 2 | Legal |  Legal Team | OOO | 
| 3 | IT |  IT Infrastructure Team | OOO | 
| 4 | Security | Security Team | OOO | 
| 5 | Developer Relations | DR | OOO | 
| 6 | Business Unit | Development Team | All members | 

A documented sample of roles, responsibilities, required competencies, and owner assignments can be found on the next page. [[Appendix 1] Open Source Policy (Sample) - Appendix 1. Assigned Owners](../../templates/1-policy/)

[SK telecom](https://www.sktelecom.com/) has formed an [OSRB](https://sktelecom.github.io/about/osrb/) to create open source policies and processes within the company, and collaborates to prepare response plans when issues arise.

{{< imgproc sktosrb Fit "600x300" >}}
<center><i>https://sktelecom.github.io/about/osrb/</i></center>
{{< /imgproc >}}

## 4. Summary

A documented sample of roles, responsibilities, required competencies, and owner assignments can be found in the open source policy template document: [Appendix 1. Assigned Owners](../../templates/1-policy/)

An enterprise can refer to this to organize its open source management structure to fit its own situation.

By designating and documenting the OSPO organization in this way, an enterprise satisfies the requirements marked in red below among the ISO standard specifications.



In fact, more important than the documentation itself is appointing an owner who will faithfully carry out the actual work, and supporting that owner in acquiring the necessary competencies.

Taking part in systematic training, such as the [Open Source License Professional Training](https://www.olis.or.kr/consulting/openswStudy.do) offered by the Korea Copyright Commission or the [NIPA Open Software Management Academy](https://www.oss.kr/oss_data/show/448d2e96-6819-45f4-b114-73cd41b3e9d3), is also very helpful.

The roles of the Open Source Program Manager and the Security role are becoming increasingly important. The Open Source Program Manager must also have a basic understanding of open source security assurance, and the Security role needs an understanding of new security requirements such as [SBOM](https://www.cisa.gov/sbom) (Software Bill of Materials) management.

In addition, continuous learning and staying current with the latest trends are becoming important across every role. The open source ecosystem and related technologies and regulations are changing rapidly, so each owner must continuously update their knowledge in their own field. Participating in international communities such as [OpenChain](https://www.openchainproject.org/) or the [TODO Group](https://todogroup.org/), or attending [domestic open source conferences](https://www.oss.kr/), is also a good approach.
