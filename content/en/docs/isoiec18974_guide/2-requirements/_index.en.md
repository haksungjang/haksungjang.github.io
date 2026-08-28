---
title: "2. Key Requirements of ISO/IEC 18974"
linkTitle: "2. Key Requirements"
weight: 20
type: docs
description: >
---

ISO/IEC 18974 defines the key requirements for open source software security assurance. This standard provides the guidance organizations need to build a framework for effectively managing known security vulnerabilities in open source software. For details on each requirement, refer to the appendix.

## 2.1 Program Foundation

This section defines the fundamental requirements for policy, competence, awareness, resources, and measurement for an open source security assurance program. The program foundation provides the basis for an organization to effectively implement and continually maintain ISO/IEC 18974.

### 2.1.1 Policy

The organization shall establish a documented policy that governs open source software security assurance of supplied software. This policy shall be shared with all relevant parties within the organization, and the policy and its method of communication shall undergo a review process to ensure they remain current and relevant.

**Table 2.1: Policy Requirement and Verification Materials**

| Requirement       | Original Text                                                                                                                                  | English Translation                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **2.1.1 Policy**      | A written policy shall be created that governs open source software security assurance of supplied software. The policy shall be internally communicated. The policy and its method of communication shall have a review process to ensure they are current and relevant. | A written policy shall be created that governs open source software security assurance of supplied software. The policy shall be internally communicated. The policy and its method of communication shall have a review process to ensure they are current and relevant. |
| **Verification Materials** | 4.1.1.1: A documented open source software security assurance policy<br>4.1.1.2: A documented procedure to make program participants aware of the security assurance policy | 4.1.1.1: A documented open source software security assurance policy<br>4.1.1.2: A documented procedure to make program participants aware of the security assurance policy |



**Considerations for Establishing the Policy**

- **Scope**: Clearly define the scope of open source software to which the policy applies (e.g., all internally developed projects, external supply chains, etc.).
- **Roles and Responsibilities**: Clearly define the responsibilities of all roles involved in open source security management (e.g., developers, security team, legal team, management).
- **Process**: Provide guidance on key processes such as open source use approval, SBOM (Software Bill of Materials) management, vulnerability management, and license compliance.
- **Compliance**: Specify the monitoring and audit procedures for policy compliance.
- **Exceptions**: Define the procedure for handling exceptions to the policy.

### 2.1.2 Competence

The organization shall identify the roles and responsibilities that affect the performance and effectiveness of the program, and determine the competence required of program participants who fulfill each role. It shall also ensure that program participants have appropriate education, training, and/or experience.

**Table 2.2: Competence Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.1.2 Competence | The organization shall: Identify the roles and responsibilities that impact the performance and effectiveness of the program; Determine the necessary competence of program participants fulfilling each role; Ensure that program participants have appropriate education, training, and/or experience; Where applicable, ensure program participants take actions to acquire the necessary competence; Retain appropriate documented information as evidence of competence as well as who is currently a participant in the program. | The organization shall: Identify the roles and responsibilities that impact the performance and effectiveness of the program. Determine the necessary competence of program participants fulfilling each role. Ensure that program participants have appropriate education, training, and/or experience. Where applicable, ensure program participants take actions to acquire the necessary competence. Retain appropriate documented information as evidence of competence, along with who is currently a participant in the program. |
| Verification Materials | 4.1.2.1: A documented list of roles with corresponding responsibilities for the different program participants <br>4.1.2.2: A document that identifies the competencies for each role <br>4.1.2.3: List of participants and their roles <br>4.1.2.4: Documented evidence of assessed competence for each program participant <br>4.1.2.5: Documented evidence of periodic reviews and changes made to the process <br>4.1.2.6: Documented verification that these processes are current with company internal best practices and who is assigned to accomplish them | 4.1.2.1: A documented list of roles with corresponding responsibilities for the different program participants <br>4.1.2.2: A document that identifies the competencies for each role <br>4.1.2.3: List of participants and their roles <br>4.1.2.4: Documented evidence of assessed competence for each program participant <br>4.1.2.5: Documented evidence of periodic reviews and changes made to the process <br>4.1.2.6: Documented verification that these processes are current with company internal best practices and who is assigned to accomplish them |

**Considerations for Building Competence**

- **Role Definition**: Define all roles related to open source security management (e.g., open source lead, developers, security engineers), and clarify the technical and legal knowledge required for each role.
- **Education and Training**: Provide education and training programs to build the competence required for each role. For example, secure coding training for developers, open source license training for the legal team, and the like.
- **Experience**: Support the accumulation of open source security management experience through participation in actual projects. Encourage the sharing of experience through mentoring programs, code reviews, and similar activities.
- **Assessment**: Conduct regular competence assessments to gauge the level of program participants and address any gaps.

### 2.1.3 Awareness

The organization shall ensure that program participants are aware of the open source software security assurance policy, relevant program objectives, their contribution to the effectiveness of the program, and the implications of not following the program's requirements.

**Table 2.3: Awareness Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.1.3 Awareness | The organization shall ensure that the program participants are aware of: The open source software security assurance policy; Relevant program objectives; Their contribution to the effectiveness of the program; The implications of not following the program's requirements. | The organization shall ensure that the program participants are aware of: The open source software security assurance policy; Relevant program objectives; Their contribution to the effectiveness of the program; The implications of not following the program's requirements. |
| Verification Materials | 4.1.3.1: Documented evidence of assessed awareness for the program participants - which should include the program's objectives, one's contribution within the program, and implications of program non-conformance. | 4.1.3.1: Documented evidence of assessed awareness for the program participants - which should include the program's objectives, one's contribution within the program, and implications of program non-conformance. |

**Activities to Raise Awareness**

- **Regular Training**: Conduct regular training on open source security policy and related processes.
- **Communication**: Share open source security information and announce the latest threats and vulnerabilities through internal bulletin boards, newsletters, email, and similar channels.
- **Encouraging Participation**: Encourage participation in open source security workshops, conferences, and study groups.
- **Recognition**: Establish a recognition program for employees who contribute to open source security.

### 2.1.4 Resources

The organization shall provide the resources needed for the establishment, implementation, maintenance, and improvement of the open source security assurance program. These resources include human resources, technical resources, and financial resources.

**Table 2.4: Resources Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.1.4 Resources | The organization shall determine and provide the resources needed for the establishment, implementation, maintenance and continual improvement of the program. | The organization shall determine and provide the resources needed for the establishment, implementation, maintenance and continual improvement of the program. |
| Verification Materials | 4.1.4.1: A documented procedure for determining and providing resources for the program. <br>4.1.4.2: A documented list of resources needed for the program. <br>4.1.4.3: Evidence that the documented resources have been provided. | 4.1.4.1: A documented procedure for determining and providing resources for the program. <br>4.1.4.2: A documented list of resources needed for the program. <br>4.1.4.3: Evidence that the documented resources have been provided. |

**Considerations for Providing Resources**

- **Human Resources**: Secure the necessary personnel, such as open source security experts, developers, and legal experts, and provide appropriate education and training suited to each role.
- **Technical Resources**: Introduce and maintain the necessary technical tools, such as SBOM generation tools, vulnerability scanners, and license checking tools.
- **Financial Resources**: Secure the budget needed to operate the program and allocate it appropriately.

### 2.1.5 Measurement

The organization shall establish metrics for measuring the effectiveness of the open source security assurance program, and measure and analyze them regularly. The measurement results shall be used to improve the program.

**Table 2.5: Measurement Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.1.5 Measurement | The organization shall determine metrics to measure program effectiveness and communicate the results. | The organization shall determine metrics to measure program effectiveness and communicate the results. |
| Verification Materials | 4.1.5.1: A documented procedure for determining, monitoring, and reviewing metrics to ensure the program is effective. | 4.1.5.1: A documented procedure for determining, monitoring, and reviewing metrics to ensure the program is effective. |

**Considerations for Measurement**

- **Metric Selection**: Select appropriate metrics related to the program's objectives (e.g., vulnerability resolution time, SBOM accuracy, policy compliance rate).
- **Data Collection**: Regularly collect data for the selected metrics.
- **Result Analysis**: Analyze the collected data to evaluate the effectiveness of the program and identify areas that need improvement.

## 2.2 Relevant Tasks Defined and Supported

This section covers the requirements for defining and supporting the relevant tasks needed to effectively operate the open source security assurance program. The organization shall clearly define and support the relevant tasks so that the program's purpose is achieved and participants can access the information and tools they need.

### 2.2.1 Access

The organization shall identify internal and external issues that are relevant to the purpose of the program and that affect its ability to achieve that purpose. It shall also ensure that program participants can access the information and tools needed to meet the program requirements.

**Table 2.6: Access Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.2.1 Access | The organization shall determine the internal and external issues that are relevant to the purpose of the program and that affect its ability to achieve the intended results of the program. The organization shall ensure that the program participants have access to the information and tools required to meet the program requirements. | The organization shall determine the internal and external issues that are relevant to the purpose of the program and that affect its ability to achieve the intended results of the program. The organization shall ensure that the program participants have access to the information and tools required to meet the program requirements. |
| Verification Materials | 4.2.1.1: A documented procedure to identify and manage internal and external issues that may affect the program. <br>4.2.1.2: A documented procedure to ensure program participants have access to the information and tools required to meet program requirements. | 4.2.1.1: A documented procedure to identify and manage internal and external issues that may affect the program. <br>4.2.1.2: A documented procedure to ensure program participants have access to the information and tools required to meet program requirements. |

**Considerations for Ensuring Access**

- **Identifying Internal Issues**: Identify factors within the organization, such as policies, processes, technology, and personnel, that may affect the program.
    - Examples: "Absence of a clear policy on open source use," "Shortage of security team staff," "Inadequate SBOM generation tools," and the like.
- **Identifying External Issues**: Analyze how changes in the external environment, such as laws, regulations, industry trends, and the competitive landscape, may affect the program.
    - Examples: "Emergence of new open source licenses," "Increase in software supply chain attacks," "Strengthening of privacy regulations," and the like.
- **Information Sharing**: Build an information-sharing system so that program participants can easily access the information they need (e.g., open source security policy, SBOM (Software Bill of Materials), vulnerability information).
    - Examples: Use internal wikis, collaboration tools, and knowledge management systems to improve access to information.
- **Providing Tools**: Provide the tools program participants need to perform their work effectively (e.g., SBOM generation tools, vulnerability scanners, license checking tools).
    - Examples: Provide the development team with open source analysis tools integrated into the IDE (Integrated Development Environment), and provide the security team with specialized vulnerability scanning tools.

### 2.2.2 Effectively Resourced

The organization shall determine and provide the resources needed for the establishment, implementation, maintenance, and continual improvement of the program. These resources include human resources, technical resources, and financial resources.

**Table 2.7: Effectively Resourced Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.2.2 Effectively Resourced | The organization shall determine and provide the resources needed for the establishment, implementation, maintenance and continual improvement of the program. | The organization shall determine and provide the resources needed for the establishment, implementation, maintenance and continual improvement of the program. |
| Verification Materials | 4.2.2.1: A documented procedure for determining and providing resources for the program. <br>4.2.2.2: A documented list of resources needed for the program. <br>4.2.2.3: Evidence that the competence has been determined. <br>4.2.2.4: Evidence that resources are being provided to maintain and improve the program. | 4.2.2.1: A documented procedure for determining and providing resources for the program. <br>4.2.2.2: A documented list of resources needed for the program. <br>4.2.2.3: Evidence that the competence has been determined. <br>4.2.2.4: Evidence that resources are being provided to maintain and improve the program. |

**Considerations for Resource Allocation**

- **Human Resources**: Secure the personnel needed to operate the program and provide appropriate education and training suited to each role.
    - Examples: Hiring open source security experts, running security training programs for developers.
- **Technical Resources**: Introduce and maintain the necessary technical tools, such as SBOM generation tools, vulnerability scanners, and license checking tools.
    - Examples: Introducing a cloud-based SBOM management system, building automated vulnerability scanning tools.
- **Financial Resources**: Secure the budget needed to operate the program and allocate it appropriately.
    - Examples: Securing a budget for purchasing open source security tools, securing a budget for running training programs.
- **Process**: Document the resource allocation process and review it regularly to improve efficiency.
    - Examples: When establishing the annual budget plan, allocate a separate budget for open source security and manage the execution details.


## 2.3 Open Source Software Content Review and Approval

This section covers the requirements for the review and approval process an organization needs to safely use open source software. An effective review and approval process allows an organization to identify and manage security vulnerabilities, license violations, and other risks in advance.

### 2.3.1 SBOM (Software Bill of Materials)

The organization shall establish a process for creating and managing a Software Bill of Materials (SBOM) that includes each open source component (and its identified licenses) comprising the supplied software. The SBOM ensures transparency of software components and facilitates vulnerability management and license compliance.

**Table 2.8: SBOM (Software Bill of Materials) Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.3.1 SBOM (Software Bill of Materials) | A process shall exist for creating and managing a bill of materials that includes each open source component (and its identified licenses) from which the supplied software is comprised. | A process shall exist for creating and managing a bill of materials that includes each open source component (and its identified licenses) from which the supplied software is comprised. |
| Verification Materials | 4.3.1.1: A documented procedure for identifying, tracking, reviewing, approving, and archiving information about the collection of open source components from which the supplied software is comprised. <br>4.3.1.2: Open source component records for the supplied software that demonstrate the documented procedure was properly followed. | 4.3.1.1: A documented procedure for identifying, tracking, reviewing, approving, and archiving information about the collection of open source components from which the supplied software is comprised. <br>4.3.1.2: Open source component records for the supplied software that demonstrate the documented procedure was properly followed. |

**Considerations for SBOM Management**

- **SBOM Generation Tools**: Select and introduce appropriate tools to automate SBOM generation (e.g., SPDX Tools, CycloneDX, Syft).
- **SBOM Format**: Use a standardized SBOM format (e.g., SPDX, CycloneDX) to ensure interoperability.
- **SBOM Content**: Define the essential information that must be included in the SBOM (e.g., component name, version, license, origin).
- **SBOM Updates**: Build a process to update the SBOM whenever software components change.
- **SBOM Storage and Sharing**: Define how the SBOM is securely stored and shared with the necessary stakeholders.

### 2.3.2 Security Assurance

The organization shall establish a process for identifying and managing known vulnerabilities in the open source components included in the supplied software. This allows the organization to quickly identify and respond to vulnerabilities, minimizing security risk.

**Table 2.9: Security Assurance Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.3.2 Security Assurance | A process shall exist for identifying and managing known vulnerabilities in the open source components of the supplied software. | A process shall exist for identifying and managing known vulnerabilities in the open source components of the supplied software. |
| Verification Materials | 4.3.2.1: A documented procedure for identifying and managing known vulnerabilities in the open source components of the supplied software. <br>4.3.2.2: Records identifying and managing known vulnerabilities in the open source components of the supplied software that demonstrate the documented procedure was properly followed. | 4.3.2.1: A documented procedure for identifying and managing known vulnerabilities in the open source components of the supplied software. <br>4.3.2.2: Records identifying and managing known vulnerabilities in the open source components of the supplied software that demonstrate the documented procedure was properly followed. |

**Considerations for Security Assurance**

- **Vulnerability Scanning**: Use automated vulnerability scanning tools to periodically check open source components for vulnerabilities (e.g., OWASP Dependency-Check, Snyk, Black Duck).
- **Vulnerability Databases**: Use up-to-date vulnerability databases (e.g., the National Vulnerability Database (NVD), Common Vulnerabilities and Exposures (CVE)) to obtain information on known vulnerabilities.
- **Vulnerability Assessment**: Evaluate the severity, impact, and exploitability of discovered vulnerabilities to determine response priority.
- **Patch Management**: Apply patches for vulnerabilities promptly and verify the results of the patch application.
- **Exception Handling**: When applying a patch is difficult, take appropriate mitigation measures (e.g., changing Web Application Firewall (WAF) settings, modifying code).

### 2.3.3 Review and Approval

The organization shall establish a process for reviewing and approving the use of open source components. This allows the organization to assess security, license, and technical risk, and ensures that only safe and appropriate open source components are used.

**Table 2.10: Review and Approval Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.3.3 Review and Approval | A process shall exist for reviewing and approving the use of open source components. | A process shall exist for reviewing and approving the use of open source components. |
| Verification Materials | 4.3.3.1: A documented procedure for reviewing and approving the use of open source components. <br>4.3.3.2: Records of the review and approval of open source components that demonstrate the documented procedure was properly followed. | 4.3.3.1: A documented procedure for reviewing and approving the use of open source components. <br>4.3.3.2: Records of the review and approval of open source components that demonstrate the documented procedure was properly followed. |

**Considerations for the Review and Approval Process**

- **Review Criteria**: Define clear criteria for evaluating open source components, such as security, license, and technical fitness.
- **Review Body**: Conduct the review through an Open Source Review Board (OSRB) or a designated person in charge.
- **Approval Procedure**: Define the procedure for approving or rejecting the use of an open source component based on the review results.
- **Record Management**: Document the review and approval results and systematically manage the related information.

## 2.4 Conformance to Document Requirements

This section covers what an organization needs to build a process for continually conforming to and improving upon the requirements of the ISO/IEC 18974 standard. Conformance to the standard's requirements is essential for maintaining and continually improving the effectiveness of the open source security management system.

### 2.4.1 Program Conformance

The organization shall establish a process for verifying that its own open source security assurance program meets the requirements of the ISO/IEC 18974 document. This process may include regular internal audits, self-assessments, and, where necessary, external verification.

**Table 2.11: Program Conformance Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.4.1 Program Conformance | A process shall exist for determining the program's adherence to the requirements of this document. | A process shall exist for determining the program's adherence to the requirements of this document. |
| Verification Materials | 4.4.1.1: A documented procedure for determining program conformance to this document. | 4.4.1.1: A documented procedure for determining program conformance to this document. |

**Considerations for Verifying Program Conformance:**

- **Internal Audit**: Verify through regular internal audits that program operations conform to ISO/IEC 18974 requirements. The audit cycle can be adjusted based on the organization's size and complexity (e.g., quarterly, semi-annually, annually).
- **Self-Assessment**: Use self-assessment to identify the program's strengths and weaknesses and find opportunities for improvement. The self-certification checklist provided by the OpenChain Project can be used for self-assessment.
- **External Verification**: Where necessary, have the program's conformance verified by an external expert or certification body. This can increase the program's credibility and build trust with customers and partners.
- **Documentation**: Document all procedures and records used to determine program conformance. This ensures transparency during audits and reviews and supports continual improvement.

### 2.4.2 Continuous Improvement

The organization shall continually improve the open source security assurance program to ensure its suitability, adequacy, and effectiveness. Continuous improvement is essential for responding to the changing threat landscape and maximizing the program's effectiveness.

**Table 2.12: Continuous Improvement Requirement and Verification Materials**

| Requirement | Original Text | English Translation |
| --- | --- | --- |
| 2.4.2 Continuous Improvement | The organization shall continuously improve the suitability, adequacy, and effectiveness of the program. | The organization shall continuously improve the suitability, adequacy, and effectiveness of the program. |
| Verification Materials | 4.4.2.1: A documented procedure for reviewing and improving the program. | 4.4.2.1: A documented procedure for reviewing and improving the program. |

**Considerations for Continuous Improvement:**

- **Feedback Collection**: Collect feedback on program operations from various stakeholders (e.g., developers, security team, legal team, management).
- **Data Analysis**: Analyze the collected feedback and program operation data to identify areas that need improvement.
- **Improvement Plan Development**: Develop specific plans for the identified areas of improvement and define actionable steps.
- **Execution and Review**: Execute the improvement plan and measure the results to evaluate its effectiveness.
- **Process Integration**: Reflect effective improvements in the program's operating processes to ensure continuous improvement.
