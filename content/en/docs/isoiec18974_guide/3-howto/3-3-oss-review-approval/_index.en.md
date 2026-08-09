---
title: "3.3 Open Source Software Content Review and Approval"
linkTitle: "3.3 OSS review & approval"
weight: 30
type: docs
description: >
---

Open source software has become an essential element in modern software development, but it also carries security and legal risks. Therefore, an organization must build a process to systematically review and approve the open source components included in the supplied software, in order to effectively manage these risks.

## 3.3.1 Software Bill of Materials

An SBOM (Software Bill of Materials) is a list of all the components, libraries, and dependencies that make up a piece of software. It is akin to a software "parts list," and it plays a crucial role in ensuring transparency in the software supply chain and identifying potential security vulnerabilities and license-related issues.

### 3.3.1.1 SBOM Generation and Maintenance Procedure

> **ISO/IEC 18974**  
> - 4.3.1.1: A documented procedure ensuring all open source software used in the supplied software is continuously recorded across the lifecycle of the supplied software. This includes an archive of all open source software used in the supplied software;
> - 4.3.1.1: A documented procedure ensuring all open source software used in the supplied software is continuously recorded across the lifecycle of the supplied software. This includes an archive of all open source software used in the supplied software.
>   
> **Self-Certification Checklist**  
> - [ ] We have a documented procedure ensuring all Open Source Software used in the Supplied Software is continuously recorded across the lifecycle of the Supplied Software. This includes an archive of all Open Source Software used in the Supplied Software.
> - [ ] We have a documented procedure ensuring all Open Source Software used in the Supplied Software is continuously recorded throughout the lifecycle of the Supplied Software. This procedure includes an archive of all Open Source Software used in the Supplied Software.

An SBOM is not something generated just once; it must be continuously updated and maintained throughout the software lifecycle. This is because, as the software changes, new components may be added or existing components may be updated. Therefore, an organization must clearly define the procedure for generating and maintaining an SBOM and document it.

#### Implementation Approach and Considerations

1. **Select an SBOM generation tool**:
    - Select a tool that can automatically generate and manage an SBOM.
    - It is advisable to choose a tool that supports standardized SBOM formats such as SPDX, CycloneDX, and SWID Tag. See the "Comparison of Major SBOM Generation Tools" table below.
    - Integrate the tool into the CI/CD pipeline and configure it to automatically generate an SBOM during the build process.
2. **Define the SBOM generation and update cycle**:
    - Define the cycle for when to generate and update the SBOM.
    - Generally, an SBOM is generated and updated whenever a new version of the software is released.
    - The SBOM must also be updated whenever there is a change to an open source component.
3. **Establish an SBOM verification process**:
    - Establish a process for verifying the accuracy and completeness of the generated SBOM.
    - The verification process includes confirming that all components included in the SBOM are accurately identified and checking that no components are missing.
    - An automated tool can also be used to verify the SBOM.
4. **Store and version-control the SBOM**:
    - Securely store the generated SBOM and perform version control.
    - The SBOM can be stored in the organization's internal repository or a cloud-based repository.
    - Version control makes it possible to accurately identify the components that made up the software at a specific point in time.
5. **Establish an SBOM access and sharing policy**:
    - Establish a policy on who can access the SBOM and how the SBOM will be shared.
    - The SBOM must be shared with relevant departments within the organization (for example, the development team, security team, and legal team).
    - The SBOM may also need to be provided upon request from a customer or a regulatory body.

#### Specific Examples

- Integrate OWASP Dependency-Track into the CI/CD pipeline to automatically generate the SBOM and analyze vulnerabilities during the build process.
- Generate an SBOM whenever a new version of the software is released, and store it in the organization's internal repository.
- Share the SBOM with the security team, development team, and legal team, and provide it to customers as needed.

#### Considerations for Implementation

- The SBOM generation and maintenance procedure should be tailored by considering the organization's size, software development process, and regulatory requirements.
- The SBOM generation process should be automated as much as possible to increase efficiency.
- Efforts should be made to ensure the accuracy and completeness of the information included in the SBOM.



#### Using Automation Tools

Among the automation tools for SBOM generation and management, open source tools include FOSSLight, SW360, and OSV-SCALIBR. See the guides below for how to install and use these tools.
- [FOSSLight](../../../tools/3-fosslight/)
- [SW360](../../../tools/2-sw360/)
- [OSV-SCALIBR](../../../tools/4-osvscalibr/)

**Table: Comparison of Major SBOM Generation Tools**

| Tool Name | Supported Languages/Packages | CI/CD Integration | Output Format | Open Source | Notes |
| --- | --- | --- | --- | --- | --- |
| SPDX Tools | Various | Yes | SPDX | Yes | Specialized in the SPDX format |
| FOSSLight | Various | Yes | SPDX, CycloneDX, Excel, Text | Yes | Integrates with various scanners, provides integrated management through FOSSLight Hub |
| SW360 | Various | Limited | SPDX | Yes | Open source compliance management features, suited to large organizations |
| OSV-SCALIBR | Various | Limited | JSON | Yes | Provided as a library, requires direct integration |
| Tern (container-specific) | Container images | Yes | SPDX, CycloneDX | Yes | Analyzes container image layers |
| Syft (container-specific) | Container images, file systems, various artifacts | Easy | SPDX, CycloneDX, Text, Table | Yes | Supports various artifact types, provides an easy-to-use CLI |

#### Documentation Approach

Include the SBOM generation procedure in the open source process as shown below. (Reference: [Open Source Process Template](../../../templates/2-process-template/))

{{% pageinfo %}}

### (2) Source Code Inspection

The business unit requests an open source review and provides the source code according to the IT staff's guidance.

IT staff perform the open source review using an open source analysis tool and generate an SBOM (Software Bill of Materials).

{{% /pageinfo %}}


### 3.3.1.2 Evidence of SBOM Management Procedure Compliance

> **ISO/IEC 18974**  
> - 4.3.1.2: open source software component records for the supplied software that demonstrates the documented procedure was properly followed.
> - 4.3.1.2: open source software component records for the supplied software that demonstrate the documented procedure was properly followed.
>   
> **Self-Certification Checklist**  
> - [ ] We have open source component records for the Supplied Software which demonstrate the documented procedure was properly followed.
> - [ ] Our open source component records for the Supplied Software demonstrate that the documented procedure was properly followed.

Effective SBOM management means more than simply generating an SBOM; it means having a system in place to continuously manage it, keep it up to date, and use it when needed. Evidence of compliance with the SBOM management procedure is used to demonstrate that the organization is properly operating such a system.

#### Implementation Approach and Considerations

1. **Automated SBOM generation process**:
    - Integrate an SBOM generation tool into the CI/CD pipeline so that an SBOM is automatically generated during the software build.
    - An automated process increases the consistency and efficiency of SBOM generation and helps reduce human error.
    - The automation tool must record SBOM generation logs and store the resulting files in a designated location.
2. **SBOM verification process**:
    - Confirm the accuracy and completeness of the SBOM through an automated or manual verification process.
    - The verification process includes comparing the list of components in the SBOM with the list of components actually used in the software and checking for missing or incorrect information.
    - Document the verification results and take corrective action if necessary.
3. **SBOM storage and access management**:
    - Securely store the SBOM and appropriately manage access permissions.
    - The SBOM can be stored in an internal repository, a version control system, or an SBOM management platform.
    - Manage access permissions on a role basis, and grant access only to those who need it.
4. **SBOM update and version control**:
    - Update the SBOM and perform version control whenever the software changes.
    - Maintain an SBOM for each version so that the components that made up the software at a specific point in time can be accurately identified.
5. **Regular audit and review**:
    - Regularly audit and review the effectiveness of the SBOM management process.
    - Use the audit results to improve the process, and update policies and procedures as needed.

#### Examples of Supporting Evidence

- **SBOM generation logs**:
    - Record the execution log of the SBOM generation tool, the date and time of generation, and the generation results.
- **SBOM files**:
    - Securely retain the generated SBOM files and perform version control.
- **SBOM verification reports**:
    - Record the verification method, verification results, and any issues found along with their resolutions.
- **SBOM change history**:
    - Record the reason for the change, the details of the change, and the date and time of the change.

#### Considerations for Implementation

- The SBOM management procedure should be tailored by considering the organization's size, software development process, and regulatory requirements.
- Tools and systems for SBOM management should be used effectively.
- The SBOM management process should be continuously improved to reflect the latest technology and threat trends.


#### Documentation Approach

Include the SBOM generation and maintenance procedure in the open source process as shown below. (Reference: [Open Source Process Template](../../../templates/2-process-template/))

{{% pageinfo %}}

### (6) Registration

The open source program manager finalizes the SBOM for tracking the list of open source used, by version, in the supplied software.

IT staff register the finalized SBOM in the system. The SBOM includes the list of open source included in the supplied software and the following information:

- The name and version of the supplied software product (or service)
- The list of open source
    - Component name, version, license, and source (URL)
    - Purpose and manner of use
    - Whether the component was modified and the details of the modification
    - Version history and key changes for each version

The registered information is reviewed and updated regularly.

{{% /pageinfo %}}


Through this approach, an organization can effectively comply with the SBOM management procedure, ensure transparency in the software supply chain, and effectively respond to potential security threats and legal risks.


## 3.3.1 Security Assurance

As the use of open source software increases, security assurance has become a core part of the software development and management process. Security assurance refers to the process of identifying and managing vulnerabilities in open source components to strengthen the security of the overall system. It goes beyond simply finding vulnerabilities, aiming to ensure security throughout the entire software lifecycle through continuous monitoring, rapid response, and systematic management.

An effective security assurance program should include the following elements:

1. Vulnerability detection and resolution procedures
2. A continuous monitoring system
3. Security update and patch management
4. Security risk assessment and management
5. Security awareness raising and training

By managing these elements in an integrated manner, an organization can minimize the security risks arising from the use of open source and build a secure software development environment.

### 3.3.2.1 Vulnerability Detection and Resolution Procedure

> **ISO/IEC 18974**  
> - 4.3.2.1: A documented procedure for handling detection and resolution of known vulnerabilities for the open source software components of the supplied software;
> - 4.3.2.1: A documented procedure for handling the detection and resolution of known vulnerabilities in the open source software components of the supplied software.
>   
> **Self-Certification Checklist**  
> - [ ] We have a documented procedure for handling detection and resolution of Known Vulnerabilities for the Open Source Software components of the Supplied Software.
> - [ ] We have a documented procedure for handling the detection and resolution of Known Vulnerabilities in the Open Source Software components of the Supplied Software.

Effective security assurance requires a clear, documented procedure for systematically detecting and resolving vulnerabilities found in open source components. This procedure should include the stages of vulnerability detection, severity assessment, response planning, remediation, and result verification, and must clearly define the owner and deadline for each stage.

#### Implementation Approach and Considerations

1. **Documented procedure**:
    - Clearly document the vulnerability detection and resolution procedure.
    - The document should specify each stage of the procedure, the owner, the deadline, and the necessary tools and systems.
    - Publish the document on a shared document repository, wiki, or other collaboration tool so that program participants can easily access it.
2. **Vulnerability detection**:
    - Use an SCA (Software Composition Analysis) tool to detect known vulnerabilities in each open source component included in the SBOM.
      - Examples: OWASP Dependency-Check, Black Duck
    - Periodically update vulnerability databases (for example, NVD and CVE) and check for new vulnerability information.
      - **NVD (National Vulnerability Database)**: A vulnerability database maintained by NIST (National Institute of Standards and Technology) in the United States. It provides vulnerability information indexed by CVE (Common Vulnerabilities and Exposures) ID.
      - **CVE (Common Vulnerabilities and Exposures)**: A list of publicly known information security vulnerabilities maintained by the MITRE Corporation. Each vulnerability is assigned a unique ID (CVE ID).
    - Perform automated vulnerability scans regularly, and conduct manual review when necessary.
    - Recommended open source vulnerability scanning tools are as follows. Detailed guides on installing, configuring, and using these tools are provided in the appendix.
      - OWASP Dependency-Check: Checks open source dependencies for vulnerabilities
      - Trivy: A vulnerability scanner for container images and file systems
3. **Severity assessment**:
    - Assess the severity of each detected vulnerability.
    - The CVSS (Common Vulnerability Scoring System) score can be used to objectively assess the severity of a vulnerability.
    - Adjust the severity by considering the vulnerability's exploitability, scope of impact, and potential impact on the system.
4. **Response planning**:
    - Develop an appropriate response plan according to the vulnerability's severity.
    - The response plan may include applying a patch, upgrading, mitigation measures, or replacing the component.
    - The response plan should be determined by considering not only technical aspects but also business impact, cost, and time constraints.
5. **Executing the remediation**:
    - Immediately carry out the necessary action according to the established response plan.
    - When applying a patch or upgrading a component, sufficient testing must be conducted to minimize the impact on the system.
    - When taking a mitigation measure, a long-term resolution must also be prepared.
6. **Result verification**:
    - After the remediation is complete, verify that the vulnerability has actually been resolved.
    - Rerun the vulnerability scanner to confirm that the vulnerability is no longer detected.
    - Perform a manual review to additionally check for vulnerabilities that the automated tool did not find.
7. **Documentation and reporting**:
    - Document the activities carried out at each stage, including vulnerability detection, severity assessment, response planning, remediation, and result verification.
    - The documentation should record the vulnerability information, the person responsible, the date and time of execution, and the results.
    - Regularly report the status of vulnerability management, and report to management when necessary.

#### Considerations for Implementation

- The vulnerability detection and resolution procedure should be tailored by considering the organization's size, software development process, and security policy.
- Automated tools should be actively used to increase efficiency.
- Close cooperation among security experts, developers, and operators is required.

#### Documentation Approach

Include the security vulnerability management process in the open source process as shown below. (Reference: [Open Source Process Template](../../../templates/2-process-template/))

{{% pageinfo %}}

## 2. Security Vulnerability Management Process

After the supplied software is released to market, when a known vulnerability or a newly discovered vulnerability is reported, the following process is followed to take appropriate action according to the risk level.

### (1) Continuous Security Testing Before Release

IT staff build and operate a system that applies continuous, repeated security testing to all supplied software before release:

1. Automated security testing:
    - Integrate automated security testing tools into the CI/CD pipeline.
    - Automatically run security tests whenever the code changes.
2. Vulnerability scanning:
    - Use an SCA tool to scan open source components for known vulnerabilities.
    - Automatically update the vulnerability database and perform a scan every day.
3. Reviewing security test results:
    - Security staff review the security test results and take the necessary action.
    - When a critical vulnerability is found, immediately notify the development team and develop a resolution plan.

### (2) Monitoring Known and Newly Discovered Vulnerabilities

IT staff build and operate a system that monitors known and newly discovered vulnerabilities. This system performs the following functions to identify structural and technical threats:

1. Automated vulnerability monitoring:
    - Analyze newly published vulnerabilities every day and automatically identify the affected versions of the supplied software.
    - Periodically collect publicly available security vulnerability information.
2. SBOM-based analysis:
    - Perform SBOM-based analysis using an SCA tool.
    - Integrate the SCA tool into the CI/CD pipeline to perform automated analysis.
3. Notification and recording:
    - When a vulnerability is found, automatically send a notification to the development staff and security staff responsible for the affected supplied software.
    - Use an issue tracking system so that everything from notification to review, action, and resolution is documented and recorded.

### (3) Vulnerability Assessment and Response

Security staff assess each vulnerability according to predefined risk/impact assessment criteria and provide response guidance to the business unit. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and a response deadline is set according to severity.

| Risk | CVSS 2.0 | CVSS 3.0 | Recommended Action Timeline |
|---|:---:|:---:|:---:|
| Low | 0.0 - 3.9 | 0.0 - 3.9 | - |
| Medium | 4.0 - 6.9 | 4.0 - 6.9 | - |
| High | 7.0 - 10.0 | 7.0 - 8.9 | Within 4 weeks | 
| Critical | - | 9.0 - 10.0 | Within 1 week |

When a known vulnerability or a newly discovered vulnerability is confirmed in previously released supplied software, the business unit develops an action plan according to the response guidance provided by security staff.

When necessary, the business unit notifies customers of the confirmed vulnerability according to the risk/impact score.


{{% /pageinfo %}}

### 3.3.2.2 Maintaining Vulnerability Records

> **ISO/IEC 18974**  
> - 4.3.2.2: For each open source software component a record is maintained of the identified known vulnerabilities and action(s) taken (including even if no action was required).
> - 4.3.2.2: For each open source software component, a record is maintained of the identified known vulnerabilities and the action(s) taken (including cases where no action was required).
>   
> **Self-Certification Checklist**  
> - [ ] We have open source component records for the Supplied Software which track identified Known Vulnerabilities and action(s) taken (including even if no action was required).
> - [ ] We have open source component records for the Supplied Software that track identified Known Vulnerabilities and the action(s) taken (including cases where no action was required).

Recording the known vulnerabilities identified for each open source component, along with the actions taken in response, is a core element of effective vulnerability management. These records help track the history of past vulnerabilities and enable a rapid response when similar issues arise. They can also be used for audit and reporting purposes.

#### Implementation Approach and Considerations

1. **Build a vulnerability database**:
    - Build a database that can systematically manage all identified vulnerabilities.
    - The database should include the following information:
        - Component name and version
        - Vulnerability ID (for example, CVE)
        - Vulnerability description
        - Severity (for example, CVSS score)
        - Date discovered
        - Response status (for example, resolved, pending, ignored)
        - Details of the response action
        - Person responsible
2. **Use automated tools**:
    - Integrate with an SCA (Software Composition Analysis) tool to automatically collect vulnerability information and store it in the database.
    - Periodically update the vulnerability database and reflect new vulnerability information.
3. **Manual review and update**:
    - Manually review vulnerabilities not detected by the automated tool and add them to the database.
    - When the response action for a vulnerability is complete, update the database and record the related information.
4. **Generate regular reports**:
    - Generate regular reports based on the vulnerability database.
    - Reports may include the following information:
        - The total number of vulnerabilities
        - The distribution of vulnerabilities by severity
        - The list of unresolved vulnerabilities
        - Trends in vulnerability resolution
5. **Data security and access control**:
    - Since the vulnerability database contains sensitive information, particular attention must be paid to data security.
    - Manage access permissions appropriately, and grant access only to those who need it.

#### Specific Examples

- **Vulnerability tracking system**: Manage vulnerability information using an issue tracking system such as Jira, Bugzilla, or YouTrack.
- **Spreadsheets**: For simple projects, vulnerability information can be managed using a spreadsheet such as Excel or Google Sheets.
- **Security dashboard**: Build a security dashboard linked to the vulnerability database to monitor the vulnerability status in real time.

#### Considerations for Implementation

- The vulnerability database must be kept up to date.
- The vulnerability database must be securely stored.
- The vulnerability database must have its access permissions appropriately managed.
- The vulnerability database must be backed up regularly.


#### Documentation Approach

Include the security vulnerability management process in the open source process as shown below. (Reference: [Open Source Process Template](../../../templates/2-process-template/))

{{% pageinfo %}}

### (4) Vulnerability Resolution and Verification

- The business unit resolves the vulnerability issue according to the established action plan.
- The vulnerability is resolved by removing the problematic open source software component or replacing it with a patched version, among other methods.
- IT staff use an open source analysis tool to confirm that the issue has been properly resolved.
- Security staff perform additional security testing on the resolved vulnerability to verify that it has been completely resolved.
- The verification result is documented and recorded.
- A review is conducted to confirm that all critical vulnerabilities have been resolved.
- If a vulnerability that is difficult to resolve remains, approval is reviewed by considering the business form and the service exposure status, among other factors.

### (5) Post-Release Vulnerability Analysis and Response

IT staff operate an automated system that analyzes vulnerabilities in released supplied software every day, even after release, for all supplied software.

- When affected supplied software is identified, a notification is immediately sent to the development staff and security staff.
- The staff who receive the notification assess the severity of the vulnerability and develop a response plan.
- Patch development, mitigation measures, and other actions are carried out according to the response plan.
- After the action is complete, verification is performed and the results are documented.

### (6) Vulnerability Record Management

A vulnerability record containing the following information is maintained for each open source component:

- Vulnerability ID (for example, CVE number)
- Vulnerability description
- Affected version
- Severity (CVSS score)
- Date discovered
- Resolution status
- Resolution method applied
- Verification result

Vulnerability records are stored in a central database and backed up regularly.

IT staff register in the system the SBOM (Software Bill of Materials) reflecting the resolved vulnerability.
{{% /pageinfo %}}


Through this approach, an organization can systematically manage vulnerabilities in open source components and improve the security level of its software.
