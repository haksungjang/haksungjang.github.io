# 6. ISO/IEC 18974 Self-Certification Process

LLMS index: [llms.txt](/llms.txt)

---

The ISO/IEC 18974 self-certification process is how an organization confirms for itself that it is effectively implementing a security assurance program for open source software. This process consists of the following stages: preparation and gap analysis, implementation and process improvement, self-assessment and certification declaration, and maintenance and renewal.

## 6.1 Preparation and Gap Analysis

The preparation and gap analysis stage is the process of understanding the requirements of the ISO/IEC 18974 standard and assessing the organization's current level of open source security management to identify areas that need improvement. This stage consists of the following detailed tasks.

### 6.1.1 Detailed Review of the ISO/IEC 18974 Standard Document

1. **Compile a list of core requirements**
    - Thoroughly review the ISO/IEC 18974 standard document.
    - Extract and list the core requirements for each section.
    - Prioritize the requirements.
2. **Understand terminology and concepts**
    - Organize the technical terms and concepts used in the standard.
    - If necessary, prepare a glossary and share it within the organization.
3. **Obtain the self-certification checklist**
    - Download the latest version of the self-certification checklist from the OpenChain Project website.
    - Familiarize yourself with the structure and content of the checklist.

**Table 6.1: Example ISO/IEC 18974 Core Requirements**

| Area | Requirement | Priority |
| --- | --- | --- |
| Policy | Establish an open source security policy | High |
| SBOM | Build an SBOM generation and management process | High |
| Vulnerability management | Establish vulnerability scanning and response procedures | Medium |
| Training | Conduct open source security training for staff | Medium |

This table shows the key requirements of ISO/IEC 18974 and their priority. Organizations can use this as a basis for developing an implementation plan.

### 6.1.2 Analysis of the Current Open Source Security Management Process

1. **List existing policies, procedures, and tools**
    - Identify the open-source-related policies, procedures, and tools currently in use.
    - Clarify the purpose, scope, and owner of each item.
2. **Identify strengths and weaknesses**
    - Analyze the effective parts of the current process and the parts that need improvement.
    - Conduct a SWOT analysis to identify internal strengths and weaknesses, and external opportunities and threats.
3. **Create process flow diagrams**
    - Create flow diagrams for key open source management processes (for example, open source use approval, vulnerability response).
    - Specify the owner and required time for each step.

**Table 6.2: Example SWOT Analysis of the Current Open Source Security Management Process**

| Category | Details |
| --- | --- |
| Strengths (S) | - High open source utilization by the development team
- Expertise of the existing security team |
| Weaknesses (W) | - Lack of systematic SBOM management
- Insufficient open source security training program |
| Opportunities (O) | - Potential for collaboration with the open source community
- Advancement of cloud-based security tools |
| Threats (T) | - Increasing open source vulnerabilities
- Increasingly complex license requirements |

This SWOT analysis table comprehensively shows the organization's current open source security management status. It helps identify the areas that need improvement.

### 6.1.3 Performing the Gap Analysis

1. **Identify the gap between the current state and the requirements**
    - Compare the ISO/IEC 18974 requirements against the current process item by item.
    - Evaluate compliance with each requirement as "fully compliant," "partially compliant," or "non-compliant."
2. **Prioritize areas requiring improvement**
    - Based on the identified gaps, determine the priority of the areas that need improvement.
    - Set priorities by considering business impact, implementation difficulty, resource requirements, and other factors.
3. **Set specific improvement targets**
    - Set specific, measurable targets for each area of improvement.
    - Create a timeline for achieving the targets.

**Table 6.3: Example Gap Analysis and Improvement Plan**

| Requirement | Current State | Gap | Improvement Target | Priority | Target Completion |
| --- | --- | --- | --- | --- | --- |
| SBOM management | Partially compliant | No automated SBOM generation | Adopt an automated SBOM generation tool | High | In 3 months |
| Vulnerability management | Non-compliant | No systematic vulnerability scanning | Establish a weekly vulnerability scan process | High | In 2 months |
| Security training | Partially compliant | No regular training program | Conduct quarterly open source security training | Medium | In 6 months |

This table shows the gap analysis results and the corresponding improvement plan. Organizations can use this as a basis for developing a concrete action plan.

### 6.1.4 Using the OpenChain Project Checklist

The self-certification checklist provided by the OpenChain Project is a very useful tool for assessing compliance with ISO/IEC 18974. The checklist can be used as follows:

1. **Download and review the checklist**
    - Download the latest version of the checklist from the OpenChain Project website.
    - Review each item on the checklist and, if necessary, adjust the terminology to fit the organization's context.
2. **Perform the self-assessment**
    - Answer each item on the checklist with "yes," "no," or "not applicable."
    - Be sure to record the reason for any "no" or "not applicable" response.
3. **Collect supporting evidence**
    - For each "yes" response, collect evidence that supports it.
    - Evidence can take various forms, such as documents, screenshots, and logs.
4. **Develop an improvement plan**
    - Develop an improvement plan for items with a "no" response.
    - Assign an owner and a target completion date to each improvement plan.

**Table 6.4: Example OpenChain Project Checklist**

| Item | Question | Response | Evidence | Improvement Plan |
| --- | --- | --- | --- | --- |
| 1.1 | Is the open source policy documented? | Yes | policy_document.pdf | - |
| 1.2 | Are all software staff aware of the policy? | No | - | Conduct company-wide training (within 3 months) |
| 1.3 | Is there a process for generating and managing SBOMs? | Partial | SBOM_management_procedure.docx | Adopt an SBOM automation tool (within 6 months) |

This table shows some items from the OpenChain Project checklist and the corresponding self-assessment results. It allows organizations to understand their current compliance status and develop an improvement plan.

Through the preparation and gap analysis stage, an organization can lay the foundation for implementing ISO/IEC 18974. The information gathered and plans developed in this stage form the basis for the next stage, "Implementation and Process Improvement."

## 6.2 Implementation and Process Improvement

In this stage, based on the gap analysis results, an organization establishes or revises its open source security policy, improves related processes and procedures, and adopts and configures the necessary tools. The goal is to build an effective open source security management system that meets the ISO/IEC 18974 requirements.

### 6.2.1 Establishing or Revising the Open Source Security Policy

1. **Reflect the ISO/IEC 18974 requirements**:
    - Based on the gap analysis results, confirm that all ISO/IEC 18974 requirements are reflected in the policy.
    - In particular, core requirements such as Software Bill of Materials (SBOM) management, vulnerability management, and license compliance must all be included without exception.
2. **Develop detailed guidelines suited to the organization's characteristics**:
    - Refine the policy by considering the organization's size, industry, technology stack, and risk management policy.
    - For example, a financial company should specify additional security measures in the policy to comply with privacy protection and financial regulations.
3. **Obtain top management approval**:
    - Obtain approval from the CEO (Chief Executive Officer) or the CISO (Chief Information Security Officer) to secure the policy's enforceability.
    - Manage the approved policy as an official document and share it with all relevant parties in the organization.

**Table 6.5: Contents of the Open Source Security Policy**

| Area | Details | Example |
| --- | --- | --- |
| Scope | Target systems, projects, and components to which the policy applies | All internal development projects, external supply chain |
| Roles and responsibilities | Responsibilities for each role related to open source management | Developers: secure coding; security team: vulnerability scanning |
| SBOM management | SBOM generation, update, and storage procedures | Periodic SBOM generation and version control |
| Vulnerability management | Vulnerability scanning, assessment, and response procedures | CVSS score-based prioritization and patch application |
| License compliance | License review and notice-obligation compliance procedures | Mandatory license review before open source use |
| Exception handling | Procedures for handling policy exceptions | Exception approval procedure for emergencies |

### 6.2.2 Improving Processes and Procedures

1. **Build an SBOM generation and management process**:
    - SBOM generation: Build a process that automatically generates an SBOM during the software build.
    - SBOM storage and management: Securely store the generated SBOM and manage it in conjunction with a version control system.
    - SBOM distribution: Establish a system for rapidly distributing the SBOM when needed (for example, upon customer request or when a security incident occurs).
    - **Use tools**: Automate the process using SBOM generation tools such as SPDX Tools, FOSSLight, and SW360.
2. **Establish a vulnerability monitoring and response system**:
    - Vulnerability scanning: Build a process that periodically scans open source components for vulnerabilities.
        - **Use tools**: Use vulnerability scanning tools such as OWASP Dependency-Check, Snyk, and Black Duck.
        - **Scan interval**: Set the scan interval by considering the project's importance and rate of change.
    - Vulnerability assessment and prioritization: Assess the severity, impact, and exploitability of discovered vulnerabilities, and determine response priority.
    - Vulnerability response: Take appropriate response measures, such as patching, mitigation, or component replacement, based on the assessment results.
    - **Set response deadlines**: Set response deadlines according to vulnerability severity, and follow the exception handling procedure if a vulnerability is not resolved within the deadline.
3. **Build an incident reporting system**:
    - Reporting procedure: Clearly define the reporting procedure for when an open-source-related security incident occurs (for example, vulnerability exploitation or license violation).
    - Reporting recipients: Designate the parties who must be notified (for example, the security team, legal team, or management).
    - Reporting format: Prepare a reporting format that includes the information needed for a report (for example, when the incident occurred, the scope of impact, and the components involved).

**Table 6.6: Process and Procedure Improvements**

| Process | Improvement | Tool/Method |
| --- | --- | --- |
| SBOM generation | Automated SBOM generation | CI/CD integration with SPDX Tools, FOSSLight, SW360, etc. |
| Vulnerability scanning | Periodic scanning and assessment | OWASP Dependency-Check, Snyk, CVSS |
| Incident reporting | Clear reporting procedure and designated owner | Prepare reporting format, designate reporting recipients |

### 6.2.3 Adopting and Configuring the Necessary Tools

1. **Select open source discovery and vulnerability scanning tools**:
    - Select appropriate tools by considering the organization's development environment, technology stack, and budget.
    - Compare free open source tools with commercial tools, and select a tool with the necessary features.
    - **Free tools**: OWASP Dependency-Check, Bandit, Trivy, etc.
    - **Commercial tools**: Snyk, Black Duck, WhiteSource, etc.
2. **Integrate with the existing development environment**:
    - Integrate the selected tools with the existing development environment, such as the IDE (Integrated Development Environment) and the CI/CD (Continuous Integration/Continuous Delivery) pipeline.
    - The integration helps developers easily use the tools and automate security checks.
3. **Use automation features**:
    - Make full use of the tools' automation features to automate tasks such as SBOM generation, vulnerability scanning, and license checking.
    - Automation saves human resources and reduces the likelihood of human error.

**Table 6.7: Criteria for Selecting Open Source Security Tools**

| Criterion | Description | Considerations |
| --- | --- | --- |
| Functionality | Whether the necessary features are provided | SBOM generation, vulnerability scanning, license checking |
| Accuracy | Minimizing false positives and false negatives | Integration with an up-to-date vulnerability database |
| Ease of use | Easy installation and usage | User interface, documentation |
| Compatibility | Integration with the existing development environment | Integration with IDE and CI/CD tools |
| Cost | Reasonable price within budget | Comparing free open source tools and commercial tool pricing |

### 6.2.4 Documentation Work

1. **Prepare detailed documentation of policies, processes, and procedures**:
    - Prepare detailed documentation of the established or revised policy, the improved processes, and the related procedures.
    - Documents should be written in clear, easy-to-understand language and be readily accessible to everyone concerned within the organization.
2. **Clarify roles and responsibilities**:
    - Clearly define and document the owner and person in charge of each process step.
    - A RACI (Responsible, Accountable, Consulted, Informed) matrix can be used to clearly define roles and responsibilities.
3. **Manage document versions**:
    - Build a document version control system to manage the change history and maintain the latest version.
    - Version control tools such as Git and Subversion, or collaboration tools such as SharePoint and Confluence, can be used.

**Table 6.8: Documentation Work Items**

| Document | Content | Example |
| --- | --- | --- |
| Open source security policy | Rules, responsibilities, and constraints for open source use | - Open source use approval procedure <br>- License compliance guidelines |
| SBOM management procedure | How to generate, store, and distribute SBOMs | - How to use the SBOM generation tool  <br>- SBOM storage location and access permissions |
| Vulnerability management procedure | How to scan, assess, and respond to vulnerabilities | - Response deadlines by vulnerability severity  <br>- How to apply patches |
| Incident response plan | Response procedure for open-source-related security incidents | - Incident reporting format  <br>- Emergency contact list |

Through this stage, an organization can establish the systematic foundation needed to implement ISO/IEC 18974 and complete its preparations for continuous improvement. Next is the self-assessment and certification declaration stage.

## 6.3 Self-Assessment and Certification Declaration

In this stage, based on the preparation and improvements made earlier, an organization assesses for itself whether it meets the ISO/IEC 18974 requirements and declares self-certification on the OpenChain Project website. The self-assessment must be conducted objectively and systematically, and the certification declaration must be approved by the organization's top executive.

### 6.3.1 Using the OpenChain Project Self-Certification Checklist

1. **Download the latest version of the checklist**:
    - Download the latest version of the checklist for ISO/IEC 18974 self-certification from the OpenChain Project website (https://www.openchainproject.org/security-assurance).
    - The checklist may be provided in spreadsheet (.xlsx) or document (.pdf) format.
2. **Understand and interpret the checklist items**:
    - Carefully read each item on the checklist and interpret it in light of the organization's context.
    - Checklist items generally reflect a specific requirement of the ISO/IEC 18974 standard and are used to assess how the organization meets that requirement.
3. **Prepare supporting evidence**:
    - For each checklist item, prepare evidence that demonstrates the organization meets the corresponding requirement.
    - Evidence can take various forms, such as policy documents, procedure manuals, audit reports, training materials, and system logs.

### 6.3.2 Performing a Systematic Self-Assessment

1. **Check compliance with each requirement**:
    - Review the prepared evidence and determine, for each item on the checklist, whether the organization complies with the corresponding requirement.
    - Answer each item with "yes," "no," or "not applicable."
2. **Maintain an objective perspective**:
    - Exclude subjective judgment from the self-assessment process and evaluate based on objective evidence.
    - Consider seeking help from an independent audit team or an external expert to increase the reliability of the assessment results.
3. **Record the assessment results**:
    - Record in detail the assessment result and the basis for each checklist item.
    - In particular, for items answered "no" or "not applicable," clearly record the reason and the improvement plan.

**Table 6.9: Example OpenChain Project Self-Certification Checklist**

| No. | Requirement | Compliance | Evidence | Description | Improvement Plan |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Is the open source policy documented? | Yes | `opensource_policy.pdf` | The organization's open source policy is documented and shared with relevant stakeholders. | - |
| 1.2 | Is an SBOM generation process in place? | Yes | `sbom_generation_procedure.pdf` | A process is in place to automatically generate an SBOM during the software build. | - |
| 1.3 | Is a vulnerability management process in operation? | No | - | Vulnerability scanning is currently performed manually, and no automated process is in place. | Adopt an automated vulnerability scanning tool (within 6 months) |

### 6.3.3 Identifying Unmet Items and Developing an Improvement Plan

1. **Analyze the root causes of gaps**:
    - Analyze the root cause of each item answered "no" or "not applicable" in the self-assessment.
    - When analyzing root causes, consider various factors such as technical issues, budget constraints, staffing shortages, and inadequate processes.
2. **Derive short-term and long-term improvement measures**:
    - Derive short-term and long-term improvement measures to address the identified causes.
    - Start short-term improvement measures with those that can be implemented relatively easily, and aim long-term improvement measures at strengthening the organization's overall capabilities.
3. **Designate a schedule and owner for each improvement**:
    - Clearly designate the implementation schedule and owner for each improvement measure.
    - The owner is responsible for tracking the progress of the improvement plan, securing the necessary resources, and completing the plan.

**Table 6.10: Example Improvement Plan for Unmet Items**

| Item | Reason for Non-Compliance | Improvement Measure | Owner | Target Completion |
| --- | --- | --- | --- | --- |
| 1.3 | No automated vulnerability scanning tool | Adopt an automated vulnerability scanning tool and integrate it into the CI/CD pipeline | Security team | June 30, 2025 |
| 2.1 | No open source security training program | Develop and implement an open source security training program for all staff | HR team | March 31, 2025 |

### 6.3.4 Declaring Certification on the OpenChain Project Website

1. **Access the self-certification page**:
    - Go to the ISO/IEC 18974 self-certification page on the OpenChain Project website (https://www.openchainproject.org/security-assurance).
2. **Enter the required information**:
    - Enter the organization's basic information, such as its name, address, and contact information.
    - Enter certification-related information, such as the self-assessment results and improvement plan.
    - Enter the certification owner's contact information, such as name, title, and contact details.
3. **Agree to and submit the declaration**:
    - Agree to the OpenChain Project's self-certification declaration.
    - Verify the entered information, obtain approval from the organization's top executive (for example, the CISO or head of legal), and submit it.
4. **Obtain the certification badge**:
    - Once the certification declaration is complete, obtain the ISO/IEC 18974 certification badge provided by the OpenChain Project.
    - The organization can use the certification badge on its website, marketing materials, and other channels to promote its open source security capabilities.

By completing this stage, an organization can formally declare its compliance with the ISO/IEC 18974 requirements and publicly announce that it has built its own open source security management system. Next is the certification maintenance and renewal stage.

## 6.4 Maintenance and Renewal

ISO/IEC 18974 self-certification is not a one-time event but an ongoing process. Through this stage, an organization can maintain its certification, continuously improve its open source security management system, and effectively respond to the changing threat landscape.

### 6.4.1 Conducting Regular Internal Audits

1. **Develop an audit plan**:
    - Develop a plan to conduct internal audits annually or semiannually.
    - Clearly define the audit scope, audit cycle, the departments and systems subject to audit, and the audit owner.
2. **Conduct the audit**:
    - Conduct the audit using various methods, such as checklists, interviews, document review, and system log analysis.
    - During the audit, assess compliance with the ISO/IEC 18974 requirements, the effectiveness of policies and procedures, and opportunities for improvement.
3. **Report the audit results**:
    - Document the audit results and clearly present the issues found, improvements, and recommendations.
    - The audit report must be shared with relevant stakeholders (for example, the CISO, legal team, and development team).
4. **Track improvement activities**:
    - Develop and implement a corrective action plan based on the audit results.
    - Regularly track the progress of the corrective action plan and confirm its completion.

**Table 6.11: Example Internal Audit Checklist Items**

| Check Item | Description | Check Content |
| --- | --- | --- |
| Policy compliance | Confirm compliance with the open source security policy | Compliance rate, cases of policy violation |
| SBOM management | Check the SBOM generation, update, and management process | SBOM generation cycle, SBOM accuracy, SBOM management system |
| Vulnerability management | Check the vulnerability scanning, assessment, and response process | Scan cycle, patch application rate, number of unresolved vulnerabilities |
| License compliance | Confirm compliance with license review and notice obligations | Cases of license violation, license review process |

### 6.4.2 Tracking New Requirements and Updates

1. **Gather information**:
    - Collect the latest information related to ISO/IEC 18974 through the OpenChain Project website, newsletters, community forums, and other sources.
    - Participate in open-source-security-related conferences, seminars, and workshops to learn about the latest technology trends and best practices.
    - Monitor changes to security-related laws and regulations (for example, GDPR, CCPA, DORA, and the EU Cyber Resilience Act).
2. **Assess the impact**:
    - Assess the impact of new requirements or updates on the organization's open source security management system.
    - Confirm whether existing policies, procedures, and tools need to be changed.
3. **Reflect changes in the process**:
    - Reflect the necessary changes in policies and procedures based on the assessment results.
    - Train members of the organization on the changes and adopt new tools.

### 6.4.3 Formal Reassessment Every 18 Months (Recommended)

1. **Conduct a full reassessment**:
    - Reassess compliance with the ISO/IEC 18974 requirements using the latest checklist provided by the OpenChain Project.
    - Identify the areas that have improved since the previous assessment and the areas that need further improvement.
2. **Develop an improvement plan**:
    - Develop and implement an improvement plan based on the reassessment results.
    - This process is equivalent to repeating the gap analysis and implementation stages described earlier.
3. **Update documentation**:
    - Reflect the results of the reassessment and improvement activities to keep policies, procedures, and related documents up to date.

### 6.4.4 Continuous Improvement Activities

1. **Collect feedback**:
    - Collect feedback on the open source security management system from internal and external stakeholders.
    - Various methods can be used, such as surveys, interviews, and workshops.
2. **Analyze data**:
    - Along with the collected feedback, analyze various data, such as SBOM data, vulnerability analysis results, and audit results, to identify opportunities for improvement.
3. **Implement improvements**:
    - Develop and implement a specific action plan for each identified improvement opportunity.
    - Various activities can be carried out, such as adopting new technologies, improving processes, and developing training programs.
4. **Measure performance**:
    - Set KPIs (Key Performance Indicators) to measure the effectiveness of improvement activities, and measure them regularly.
    - Analyze the measurement results to evaluate the effectiveness of the improvement activities, and revise the plan if necessary.
5. **Share knowledge**:
    - Share success and failure cases from improvement activities within the organization to enhance learning.
    - Use internal wikis, blogs, newsletters, and other channels to share knowledge and encourage communication.
