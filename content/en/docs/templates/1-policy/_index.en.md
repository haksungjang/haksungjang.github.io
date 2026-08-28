---
title: "Open Source Policy"
weight: 10
type: docs
categories: ["guide"]
tags: ["Policy"]
---

{{< alert title="Note:" >}}
This sample open source policy was written with reference to the following two materials.

1. [OpenChain Open Source Policy Template](https://github.com/OpenChain-Project/Reference-Material/tree/master/Policy-Templates/Official/2.1/en)
2. [Linux Foundation Generic FOSS Policy](https://github.com/todogroup/policies/blob/master/linuxfoundation/lf_compliance_generic_policy.pdf)

**Author : OpenChain Korea Work Group Authors / [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**

{{< /alert >}}

## 1. Purpose and Scope

### 1.1 Purpose

This policy provides principles and procedures for the Company to safely and effectively utilize open source software. The main objectives of the policy are as follows:

1. **Open Source License Compliance**:
    - Comply with the license obligations of open source components included in supplied software, and satisfy relevant legal requirements.
2. **Open Source Security Assurance**:
    - Identify security vulnerabilities in open source components included in supplied software, and minimize security risk through appropriate response measures.
3. **Contribution to External Open Source Projects**:
    - Promote collaboration with the open source community by contributing to external open source projects, and protect the Company's intellectual property.
4. **Open Sourcing of Internal Projects**:
    - Release internal projects as open source to enhance collaboration with the open source community and promote the Company's technical capabilities.

These principles are designed to satisfy the requirements of ISO/IEC 5230 (open source license compliance) and ISO/IEC 18974 (open source security assurance).

### 1.2 Impact of Non-Compliance

If the Company fails to comply with this policy, it may face the following risks:

- **Legal Risk**: The Company may receive external demands for open source license compliance, and may face litigation or fines.
- **Reputational Damage**: The Company's reputation may be damaged due to source code disclosure obligations or security incidents.
- **Business Loss**: Relationships with customers or suppliers may deteriorate due to contract violations.
- **Security Incidents**: Serious security incidents may occur due to known vulnerabilities or newly discovered vulnerabilities.

### 1.3 How Program Participants Can Contribute

All program participants of the Company must understand and comply with this policy. Participants can contribute in the following ways:

- Perform the responsibilities and obligations defined in the policy according to their role.
- Complete education related to open source licenses and security, and apply it in practice.
- Report immediately if they discover an issue that impedes compliance with the policy.

### 1.4 Scope

This policy applies to all software projects that the Company develops, distributes, or uses. The main scope of application is as follows:

- All supplied software provided or distributed externally.
- Activities contributing to external open source projects.
- Activities releasing internal projects as open source.

However, open source used only for internal purposes may be subject to a separate review procedure to determine whether the policy applies.

The scope of the policy is reviewed and updated periodically according to changes in the Company's business environment.

## 2. Definitions

This section defines the key terms used in the policy. These definitions are necessary to help clearly understand and apply the policy.

### 2.1 Key Terms

1. **Open Source Software**:
    - Software that satisfies the Open Source Definition defined by the Open Source Initiative or the Free Software Definition defined by the Free Software Foundation. This is software with a license that allows users to freely use, modify, and distribute the software.
2. **SBOM (Software Bill of Materials)**:
    - A list of all components, libraries, and dependencies that make up a piece of software. This is like a software "bill of materials," and is used to ensure transparency in the software supply chain and to identify potential security vulnerabilities and license-related issues.
3. **Known Vulnerability**:
    - A previously discovered, publicly available security vulnerability. This can be found in databases such as NVD and CVE.
4. **Newly Discovered Vulnerability**:
    - A new security vulnerability that had not previously been discovered. This may be discovered while software is in use, or reported by external researchers.
5. **Security Assurance**:
    - Confidence that a system satisfies the requirements for security best practices and is resilient against known vulnerabilities.
6. **Verification Material**:
    - Material demonstrating that a given requirement of a specification has been satisfied. This may be provided in various forms such as documents, records, and test results.
7. **Supplied Software**:
    - All software that an organization provides or distributes to a third party.
8. **Program**:
    - The set of policies, processes, and personnel that make up an organization's open source license compliance and security assurance activities.
9. **Program Participant**:
    - Any member of the organization or contractor responsible for defining, contributing to, or preparing supplied software. This includes software developers, release engineers, quality engineers, product marketing, and product managers.
10. **Compliance Artifact**:
    - Represents the output of an open source license compliance program, and is the collection of deliverables that must be provided along with supplied software. This includes attribution notices, source code, copies of licenses, copyright notices, notices of modification, and Written Offers.
11. **Identified License**:
    - The set of open source licenses identified by an appropriate method for identifying the open source components included in supplied software.

## 3. Roles and Responsibilities

This section defines the key roles and responsibilities related to open source software management. Each role is essential to ensuring the organization's open source license compliance and security assurance.

### 3.1 Role Descriptions

1. **Open Source Program Manager (OSPM)**
    - **Responsibility**: Overall responsibility for the Company's open source program.
    - **Key Duties**:
        - Manage open source license compliance and security assurance activities.
        - Create and maintain the SBOM.
        - Respond to external inquiries related to open source.
        - Manage internal best practices.
    - **Required Competencies**: Understanding of software development processes, expertise in open source licenses, communication skills.
2. **Legal**
    - **Responsibility**: Assess legal risk related to open source licenses and provide advice.
    - **Key Duties**:
        - Interpret and review open source license obligations.
        - Review license compatibility and provide advice on intellectual property protection.
    - **Required Competencies**: Expertise in software copyright, expertise in open source licenses, ability to assess legal risk.
3. **IT**
    - **Responsibility**: Operate and automate open source analysis tools.
    - **Key Duties**:
        - Operate open source analysis tools and integrate them into the DevOps environment.
        - Create and maintain the SBOM.
    - **Required Competencies**: Expertise in IT infrastructure, understanding of open source analysis tools, understanding of CI/CD pipelines.
4. **Security**
    - **Responsibility**: Operate open source security vulnerability analysis tools.
    - **Key Duties**:
        - Respond to known vulnerabilities and newly discovered vulnerabilities.
        - Integrate into the DevSecOps environment and perform security measures.
    - **Required Competencies**: Understanding of DevSecOps, understanding of security vulnerability analysis tools, ability to assess and manage risk.
5. **Developer Culture**
    - **Responsibility**: Support in-house developers in actively utilizing open source.
    - **Key Duties**:
        - Encourage participation in the open source community and improve developer culture.
        - Support external contribution activities.
    - **Required Competencies**: Understanding of software development processes, ability to design education, experience with community engagement.
6. **Quality**
    - **Responsibility**: Verify open source license obligations when distributing supplied software.
    - **Key Duties**:
        - Verify the creation of compliance artifacts.
        - Review compliance with license obligations before distribution.
    - **Required Competencies**: Understanding of software development processes, basic knowledge of compliance.
7. **OSRB (Open Source Review Board)**
    - **Responsibility**: Establish and improve policies and processes for open source management.
    - **Key Duties**:
        - Periodically review and improve the policy.
        - Discuss key issues and develop resolutions.
    - **Required Competencies**: Expertise in policy development, experience operating a governance body.
8. **OSPO (Open Source Program Office)**
    - **Responsibility**: Support contributions to external open source projects and the release of internal projects.
    - **Key Duties**:
        - Provide guidance for external contributions.
        - Manage the release procedure for internal projects.
    - **Required Competencies**: Experience with community engagement, project management skills.

### 3.2 Staffing and Funding

1. Appropriate staffing:
    - Assign appropriate personnel with the necessary competencies and expertise for each role.
    - The head of each department must designate a suitable person to perform the role.
2. Sufficient funding:
    - The Company provides sufficient budget and resources necessary to perform each role.
    - Budget items include education, tool licensing fees, and external consulting costs.
3. Periodic review:
    - The OSRB reviews the staffing and funding status of each role at least once a year, and recommends adjustments as needed.
    - The review results are documented and reported to the OSPO (Open Source Program Office).
4. Issue resolution procedure:
    - If a department's person in charge lacks the necessary support (personnel or funding), they must immediately report this to the OSPM.
    - The OSPM works with the relevant departments to resolve the issue, and requests the OSRB to resolve the issue if necessary.

### 3.3 Internal Responsibility Assignment Procedure

1. Responsibility assignment procedure:
    
    a. The OSPM convenes an annual responsibility assignment meeting.
    
    b. Consults with each department head (Legal, IT, Security, Development, Quality, etc.) to select a person responsible for each activity.
    
    c. Submits the list of selected persons responsible to the OSRB (Open Source Review Board) for final approval.
    
2. Balance of responsibility and authority:
    - Each person responsible is granted appropriate authority necessary to perform the relevant duties.
    - They have the authority to request the resources (e.g., budget, personnel) necessary to fulfill their responsibilities.
3. Periodic review and updates:
    - The OSRB reviews the status of responsibility assignments at least once a year and makes adjustments as needed.
    - Responsibility assignments are updated immediately whenever there is a major change, such as an organizational restructuring or personnel change.
4. Documentation:
    - The results of responsibility assignment are recorded as an official document and registered in the Company's document management system.
    - The document specifies each activity, the person responsible, their role, and the required competencies.
5. Education and awareness:
    - Provide necessary education to newly assigned persons responsible.
    - Share the results of responsibility assignment with the entire organization to raise awareness.

### 3.4 Current Assignees

The organization and person responsible for each role can be found in [Appendix A: Current Assignees]. The list is updated as needed.

## 4. Open Source License Compliance

This section describes the procedures for complying with the license obligations of open source components included in supplied software. Through this, the Company can ensure open source license compliance and minimize legal risk.

### 4.1 Open Source Identification and License Obligation Review

1. **Open Source Identification**:
    - Identify all open source components used when developing supplied software.
    - Use SCA (Software Composition Analysis) tools to automatically detect and record open source components.
2. **License Obligation Review**:
    - Review the licenses of identified open source components and confirm the obligations required by each license.
    - Refer to the Company's [Open Source License Guide] to understand licenses, and work with the Legal team to resolve compatibility issues.

### 4.2 Design Considering Open Source Licenses

1. **Software Architecture Design**:
    - Design the software architecture to minimize the impact of open source licenses.
    - Identify the coupling relationship between open source components and the Company's own code to comply with license obligations.
2. **License Compatibility Review**:
    - Review whether the licenses of multiple open source components are compatible with each other.
    - If incompatible licenses are used, propose alternative components or take appropriate action.

### 4.3 Creating and Managing Compliance Artifacts

1. **Creating Open Source Notices**:
    - Prepare a notice containing the copyright information and licenses of the open source components included in supplied software.
    - The notice is prepared according to the conditions required by each license, and is included in the distribution package.
2. **Creating Source Code Packages for Disclosure**:
    - Create the source code packages necessary to comply with licenses that require source code disclosure, such as GPL and LGPL.
    - Source code packages are securely stored in a separate repository and provided upon external request.
3. **Distribution and Storage of Compliance Artifacts**:
    - All compliance artifacts are distributed together with supplied software and systematically managed in an internal repository.
    - Operate a system that can provide artifacts upon external request.

### 4.4 Creating and Managing the SBOM

1. **Creating the SBOM**:
    - Create the SBOM (Software Bill of Materials) for all open source components that make up supplied software.
    - The SBOM includes the name, version, license information, and download location of each component.
2. **Maintaining and Updating the SBOM**:
    - The SBOM is updated with each software release and kept up to date.
    - The SBOM is securely managed in an internal repository and prepared to be provided upon external request.
3. **Managing Open Source Component Records**:
    - Maintain detailed records for each open source component. These records include the following information:
        
        a. Component identification information (name, version, source)
        
        b. License information and obligations
        
        c. Purpose and manner of use
        
        d. Whether modified and details of modifications
        
        e. Vulnerability analysis results and response measures
        
    - These records are periodically reviewed and updated, and managed according to documented procedures.
4. **Record Verification Procedure**:
    - Verify the accuracy and completeness of open source component records quarterly.
    - Verification results are documented and stored, and improvement measures are taken as needed.

### 4.5 Compliance Issue Response Procedure

1. **Issue Identification and Response**:
    - When a compliance issue occurs, the OSPM immediately identifies the issue and develops a response plan.
    - Works with the Legal team to assess the severity of the issue and determine the necessary action.
2. **Maintaining Response Records**:
    - All response processes are recorded and preserved through Jira or another issue tracking system.
    - Response records are periodically reviewed and used as reference material in the event of a similar problem in the future.

## 5. Open Source Security Assurance

This section describes the procedures for ensuring the security of open source components included in supplied software. Through this, the Company can effectively manage known vulnerabilities and newly discovered vulnerabilities, and raise the security level of its software.

### 5.1 Known Vulnerability Detection and Response Procedure

1. **Vulnerability Detection**:
    - Use SCA (Software Composition Analysis) tools to detect known vulnerabilities in each open source component included in the SBOM.
    - Regularly update vulnerability databases such as the NVD (National Vulnerability Database) and CVE (Common Vulnerabilities and Exposures) to check the latest information.
2. **Vulnerability Severity Assessment**:
    - Assess the severity of a vulnerability using its CVSS (Common Vulnerability Scoring System) score.
    - Determine response priority considering the exploitability of the vulnerability, its scope of impact, and its potential impact on the system.
3. **Response Measures**:
    - Immediately apply a patch or take mitigation measures for high-risk vulnerabilities.
    - If customers may be affected, notify customers and present a resolution plan.
4. **Maintaining Response Records**:
    - All vulnerabilities and response measures are recorded in a database, and reports are generated periodically.
    - Response records are used as reference material in the event of a similar problem in the future.

### 5.2 Newly Discovered Vulnerability Response Procedure

1. **Detecting Newly Discovered Vulnerabilities**:
    - Identify and assess new security vulnerabilities that had not previously been discovered.
    - Newly discovered vulnerabilities may be reported by external researchers or through internal testing.
2. **Severity Assessment and Response**:
    - Assess the severity of a newly discovered vulnerability using its CVSS score.
    - Determine response priority based on the assessment results and take necessary action.
    - If customers may be affected, notify customers and present a resolution plan.
3. **Maintaining Response Records**:
    - Newly discovered vulnerabilities and response measures are recorded in a database, and reports are generated periodically.

### 5.3 Continuous Monitoring and Response

1. **Vulnerability Monitoring**:
    - Continuously monitor software even after release to identify known vulnerabilities or newly discovered vulnerabilities.
    - Use automated tools to detect anomalies based on the latest data.
2. **Response Preparation**:
    - Security experts prepare the response, and receive assistance from external experts as needed.
    - The response plan is periodically reviewed and updated.
3. **Reporting and Improvement**:
    - All monitoring and response activities are reported periodically and shared with program participants.
    - Improve processes based on monitoring results to continuously enhance the security level.

### 5.4 Alignment with Internal Best Practices

1. **Investigating Internal Best Practices**:
    - Investigate security-related activities and processes that are successfully operated by other teams or departments within the Company.
    - Example: the information security team's vulnerability management process, the development team's secure coding guidelines, etc.
2. **Comparing and Analyzing Processes**:
    - Compare and analyze how the investigated best practices operate relative to the open source security assurance program.
    - Identify differences, weaknesses, and opportunities for improvement.
3. **Integrating and Improving Processes**:
    - Adjust or integrate the open source security assurance program to align with the Company's internal best practices.
    - Example: applying the company-wide vulnerability management system to open source vulnerability management as well.
4. **Assigning and Managing Responsibility**:
    - The OSPM is responsible for compliance with internal best practices, and periodically reviews the operating approach and proposes improvements.

## 6. Education and Awareness

This section describes the education and awareness activities necessary to ensure the competency and awareness of program participants. Through this, participants can fully understand the open source policy, the goals of the related program, and their own roles and responsibilities, and raise their awareness of open source license compliance and security assurance.

### 6.1 Open Source Education

1. **Education Objectives**:
    - Help program participants use open source correctly, and understand and apply license compliance and security assurance procedures in practice.
    - Key education content:
        - The purpose and principles of the open source policy.
        - License obligations and compliance procedures.
        - How to create and use the SBOM.
        - Procedures for managing known vulnerabilities and newly discovered vulnerabilities.
2. **Education Methods**:
    - Completed through online courses provided on the [Learning Portal].
    - Additional education is provided in workshop or seminar format as needed.
    - Case-based learning is used to strengthen the ability to solve real-world problems.

### 6.2 Competency Assessment

1. **Assessment Criteria**:
    - Assess the competencies required for each role.
    - Assessment items:
        - Understanding of the open source policy.
        - Ability to perform compliance procedures.
        - Ability to manage security vulnerabilities.
2. **Assessment Methods**:
    - Measure participants' competency through periodic tests and practical evaluations.
    - Assessment results are reflected in individual performance records, and additional education is provided as needed.

### 6.3 Awareness-Raising Activities

1. **Periodic Newsletters and Workshops**:
    - Share the latest open source trends and policy changes through a periodic newsletter.
    - Raise program participants' understanding and promote collaboration through workshops and seminars.
2. **Use of Communication Channels**:
    - Share open source-related information through internal communication channels (e.g., email, internal portal).
    - Encourage collaboration and information exchange among program participants.

### 6.4 Record Retention

1. **Education and Assessment Records**:
    - All education completion records and assessment results are retained for at least 3 years.
    - This allows the Company to demonstrate that program participants have a sufficient understanding of the policy and processes.
2. **Periodic Review and Updates**:
    - The OSPM reviews the education content and assessment methods at least once a year and updates them as needed to reflect the latest open source trends and the organization's requirements.

### 6.5 Identifying and Utilizing Expertise

1. **Identifying Required Areas of Expertise**:
    - Periodically identify the technical and legal areas of expertise necessary to operate the program.
    - Example: web security, cryptography, network security, systems administration, open source license interpretation, etc.
2. **Preparing and Updating a List of Internal Experts**:
    - Prepare a list of personnel with expertise in the relevant field within the Company, and update it periodically.
    - Record each expert's career history, certifications, and contact information.
3. **Establishing a Plan to Secure External Resources**:
    - Establish a plan to utilize external experts or consulting firms for problems that are difficult to resolve internally.
    - Secure reliable external resources and clearly define contract terms.
4. **Establishing a Procedure for Accessing Expertise**:
    - Establish a procedure so that program participants can easily access the expertise they need.
    - Example: how to consult an internal expert, how to utilize an external consulting firm, etc.

## 7. Contribution to External Open Source Projects

This section describes the procedures and principles that the Company's program participants must follow when contributing to external open source projects. Through this, the Company can actively participate in external open source projects while preventing intellectual property and copyright issues.

### 7.1 Contribution Procedure

1. **Review Request and Approval**:
    - To contribute to an external open source project, a program participant must obtain review and approval from the OSPO (Open Source Program Office).
    - The OSPO confirms that the code to be contributed does not infringe on the Company's intellectual property, and requests review by the Legal team as needed.
2. **Contribute Only Code You Have the Right to Contribute**:
    - Program participants may only contribute code they have written themselves or code owned by the Company.
    - Third-party code must not be contributed without authorization.
3. **Caution Regarding Exposure of Intellectual Property**:
    - Take care not to include sensitive information, patents, or other Company intellectual property.
    - If the code to be contributed includes a Company patent, it must be reviewed by the OSPO and the Legal team.

### 7.2 Caution Regarding CLA Signing

1. **CLA Review**:
    - Some open source projects require contributors to sign a CLA (Contributor License Agreement).
    - Before signing a CLA, request a review from the OSPO to ensure protection of the Company's intellectual property.
2. **Prohibition on Copyright Assignment**:
    - To protect its own intellectual property, the Company does not permit contributions to open source projects whose CLA terms require copyright assignment.

### 7.3 Copyright Notice

1. **Copyright Notation**:
    - When a program participant contributes code to an external open source project, the Company's copyright must be clearly stated.
    - State the copyright and license at the top of the file as follows:
        
        `textCopyright (c) [Year] [Company Name]
        SPDX-License-Identifier: [SPDX_license_name]`
        
2. **Use of Company Email**:
    - When contributing to an open source project, use the Company email rather than a personal email.
    - This instills a sense of responsibility for communicating with the community on behalf of the Company.

### 7.4 Maintaining Contribution Records

1. **Managing Contribution History**:
    - Manage the entire history of contributions to external open source projects, and report it to the OSPO.
    - Contribution history is retained in an internal system (e.g., the Learning Portal) for at least 3 years.
2. **Assessing Contribution Activities**:
    - Contribution activities to external open source projects are reflected in program participants' performance evaluations.
    - The OSPO periodically assesses the effectiveness of contribution activities and proposes improvement measures as needed.

## 8. Releasing Internal Projects as Open Source

This section describes the procedures and principles for releasing internal projects as open source. Through this, the Company can promote collaboration with the open source community, protect its intellectual property, and minimize legal risk.

### 8.1 Approval Procedure

1. **Review and Approval**:
    - To release an internal project as open source, review and approval must be obtained from the OSPO (Open Source Program Office).
    - The OSPO confirms that the code to be released does not infringe on the Company's intellectual property, and requests review by the Legal team as needed.
2. **Intellectual Property Protection**:
    - Take care not to include sensitive information, patents, or other Company intellectual property.
    - For code that includes a patent, work with the Legal team to confirm whether it can be released.
3. **Copyright Notice**:
    - State the Company's copyright in the code being released.
    - Example: "Copyright (c) [Year] [Company Name]"

### 8.2 Release Preparation

1. **Code Preparation**:
    - Organize and document the code to be released so it can be used externally.
    - Verify the origin of the code, and delete or modify any code that poses a potential problem.
2. **Choosing an Open Source License**:
    - Select an appropriate open source license under which to release the code.
    - When choosing a license, consider protection of the Company's intellectual property and the needs of the community.
3. **Securing Resources**:
    - Secure the infrastructure and budget necessary to maintain and manage the project.
    - Use a project hosting platform such as GitHub to maintain transparency.

### 8.3 Post-Release Management

1. **Community Management**:
    - Collect community feedback on the released project and respond appropriately.
    - The OSPO manages the relationship with the community and actively accepts external contributions.
2. **Ongoing Maintenance**:
    - The released project is continuously maintained, with bug fixes and feature improvements.
    - Quality is ensured through code review, and the project collaborates with external contributors.
3. **Use of Company Email**:
    - Use the Company email rather than a personal email during open source activities, to maintain the Company's representation.

### 8.4 Record Retention

1. **Retaining Release Records**:
    - All records related to a released project are retained for at least 3 years.
    - Records include the approval procedure, code versions, and community feedback.
2. **Periodic Review and Updates**:
    - Released projects are periodically reviewed and updated as needed.
    - Continuously improved to reflect the latest open source trends and organizational requirements.

## 9. Responding to External Inquiries

This section describes the procedure by which the Company responds quickly and effectively when there is an external open source-related inquiry or request, particularly one related to open source license compliance and open source security vulnerabilities. Through this, the Company can appropriately respond to external demands, minimize legal risk, and promote collaboration with the open source community.

### 9.1 Responsibility for Responding to External Inquiries

1. **Designating the Person Responsible**:
    - Responding to external open source-related inquiries and requests is handled by the **OSPM**.
    - As needed, works with the Legal team (for license compliance matters) or the Security team (for security vulnerability matters) to resolve the issue.
2. **Inquiry Escalation Procedure**:
    - Any program participant who receives an external open source-related inquiry must immediately forward it to the **OSPM**.
    - Depending on the nature of the inquiry, it is promptly assigned to the department responsible for license compliance or security vulnerabilities.

### 9.2 Publishing Contact Information

1. **Public Contact Information**:
    - The official contact information for the *OSPM* is made publicly available.
    - The contact information is registered on the following channels:
        - The open source notice
        - The Company website
        - The Linux Foundation's Open Compliance Directory
2. **Guidance on How to Make Inquiries**:
    - Clearly explain how external parties can make open source-related inquiries.
    - Operate a system that can accept inquiries by email address, website inquiry form, and other means.

### 9.3 External Inquiry Response Procedure

1. **Receiving and Confirming the Inquiry**:
    - When an external inquiry is received, the **OSPM** immediately confirms it and specifies an appropriate resolution time.
    - Reviews the nature of the inquiry and classifies it as a license compliance or security vulnerability matter.
        - License compliance: reviewed and addressed in cooperation with the Legal team.
        - Security vulnerability: assessed for severity and addressed in cooperation with the Security team.
2. **Carrying Out the Response**:
    - Take appropriate response measures according to the content of the inquiry, and receive assistance from external experts as needed.
    - All response processes are recorded through an internal system (e.g., Jira Tracker).
3. **Providing Feedback and Improving**:
    - After responding, provide feedback to the external inquirer, and propose improvement measures as needed.
    - Analyze response records and improve processes to prevent recurring problems.

## 10. Measuring and Improving Program Effectiveness

This section describes the procedure for measuring and continuously improving the effectiveness of the open source program. Through this, the Company can evaluate and improve the performance of its open source license compliance and security assurance program.

### 10.1 Defining Performance Indicators

1. **List of Performance Indicators**:
    - Number of supplied software analyzed.
    - Number of known vulnerabilities and newly discovered vulnerabilities resolved.
    - Number of compliance artifacts created and distributed.
    - Response time for external inquiries.
    - Education completion rate of program participants.
    - Number of external open source contributions and released projects.
2. **Setting Indicator Targets**:
    - Set target values for each indicator so that the program's performance can be evaluated.
    - Target values are set in line with the organization's business goals and the program's objectives.

### 10.2 Periodic Program Assessment

1. **Assessment Cycle**:
    - Conduct a program assessment at least once a year.
    - Conduct additional assessments as needed when there is a change in the business environment or a major issue occurs.
2. **Assessment Procedure**:
    - Document the assessment results and report them to the OSRB (Open Source Review Board).
    - Collect and reflect feedback from program participants during the assessment process.
    - Assessment results are recorded and preserved through an internal system (e.g., Jira Issue Tracker).
3. **Periodic Policy Review and Renewal**:
    - The policy is periodically reviewed and, if necessary, renewed to reflect the latest open source trends and the organization's requirements.
    - This continuously improves the effectiveness of the program.

### 10.3 Continuous Improvement Plan

1. **Identifying Areas for Improvement**:
    - Identify areas that need improvement based on assessment results, and set priorities.
    - Areas needing improvement may include process efficiency, education content, response time, and more.
2. **Setting Improvement Targets**:
    - Set specific improvement targets and schedules.
    - The progress of improvement activities is monitored and documented.
3. **Reflecting Improvement Results**:
    - Reflect improvement results in the next assessment cycle to continuously enhance the program's effectiveness.
    - Improvement results are shared with program participants to encourage continued commitment to improvement.

### 10.4 Integrating and Improving Internal Best Practices

1. **Planning Integration Activities**:
    - Identify the gaps between internal best practices and the open source security assurance program, and establish an integration plan based on this.
    - Example: integrating vulnerability management systems, standardizing code review procedures.
2. **Periodic Review and Updates**:
    - Review the alignment between internal best practices and the open source program at least once a year, and reflect improvements as needed.
    - The review results are reported to the OSRB (Open Source Review Board).

### 10.5 Assessing Personnel and Resources

1. Assessment cycle:
    - The Company assesses the staffing and funding status for each role at least once a year.
    - Assessment results are reported to the OSRB, and improvements are implemented as needed.
2. Assessment items:
    - Whether appropriate personnel have been assigned for each role.
    - Whether sufficient budget has been provided to perform each role.
    - Cases of problems caused by insufficient support, and their resolutions.
3. Establishing an improvement plan:
    - Establish a specific plan to supplement insufficient personnel or resources based on the assessment results.
    - The improvement plan is implemented upon approval by the OSRB.

## 11. ISO Standard Compliance Declaration and Maintenance

This section describes the procedure by which the Company complies with and maintains the requirements of ISO/IEC 5230 (open source license compliance) and ISO/IEC 18974 (open source security assurance). Through this, the Company can ensure the continuous improvement of its open source program and compliance with the standards.

### 11.1 ISO Standard Compliance Declaration

1. **Compliance Declaration**:
    - Through this policy, the Company declares that it satisfies all the requirements of ISO/IEC 5230 (open source license compliance) and ISO/IEC 18974 (open source security assurance).
    - The date of declaration and validity period (18 months) are clearly stated.
    - The compliance declaration may be made through Self Certification under the Linux Foundation's OpenChain project.
2. **Documenting Evidence**:
    - The OSPM documents and maintains evidence of satisfaction for each requirement.
    - Evidence documents include policy documents, process descriptions, education records, compliance artifacts, and security vulnerability management records.
    - All evidence documents are stored in a central repository and retained for at least 3 years.
    - This document must be prepared within 18 months after undergoing conformance verification, and is renewed at least once a year.
3. **Periodic Review and Renewal**:
    - The OSRB reviews whether the requirements are satisfied at least once a year, and improves the policy and processes as needed.
    - The review results and improvements are documented and stored.
4. **Preparing for External Verification**:
    - Prepare to provide evidence documents to external auditors or certification bodies upon request.

### 11.2 Maintaining Compliance Status

1. **Periodic Review**:
    - The OSRB conducts an internal review of all the requirements of ISO/IEC 5230 and ISO/IEC 18974 at least once a year.
    - The review results are documented and stored, and an improvement plan is established for any items not satisfied.
2. **Periodic Internal Audit**:
    - Internal audits assess whether program participants are performing their roles, whether compliance artifacts are adequate, and the effectiveness of security assurance activities.
    - Based on the audit results, areas for improvement are identified and necessary action is taken.
3. **Providing Education and Training**:
    - Provide periodic education and training to continuously improve the competency and awareness of program participants.
    - Education content reflects the latest open source trends and the organization's requirements, and emphasizes compliance with ISO standards.
4. **Preparing to Respond to External Inquiries**:
    - Maintain a system that can respond quickly and effectively to external inquiries related to ISO standard compliance.
    - Inquiry response is handled by the OSPM, who works with the Legal team as needed.
5. **Periodic Policy Renewal**:
    - The policy is reviewed at least once a year, and renewed to reflect the latest open source trends and the organization's requirements.
    - The renewed policy is shared with all program participants.
