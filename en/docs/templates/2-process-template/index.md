# Open Source Process

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-primary" role="alert"><div class="h4 alert-heading" role="heading">Note:</div>


This sample open source process was written with reference to the following two materials.

1. [OpenChain Open Source Policy Template](https://github.com/OpenChain-Project/Reference-Material/tree/master/Policy-Templates/Official/2.1/en)
2. [Open Source Compliance In The Enterprise](https://www.linuxfoundation.org/compliance-and-security/2018/12/open-source-compliance-in-the-enterprise/)

**Author : OpenChain Korea Work Group Authors / [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**

</div>


[Company Name] (hereinafter referred to as "the Company") actively utilizes open source software in developing products and services that include software. To minimize open source risk, the Company must carry out (1) activities to comply with the obligations imposed by open source licenses and (2) appropriate activities to detect open source security vulnerabilities and take follow-up action, while distributing software. The Company follows the open source process to ensure these activities.

## 1. Open Source Process

[Company Name] (hereinafter referred to as "the Company") actively utilizes open source software in developing products and services that include software. To minimize open source risk, the Company must carry out (1) activities to comply with the obligations imposed by open source licenses and (2) appropriate activities to detect open source security vulnerabilities and take follow-up action, while distributing supplied software. The Company follows the open source process to ensure these activities.

The open source process defines the procedures that must be carried out to comply with open source license obligations and to ensure open source security assurance, at each development stage of developing and distributing the Company's supplied software. Program participants comply with the following 11 stages of the open source process.


![process](process.png)


Through the open source process, the Company strives to minimize open source risk and provide customers with safe and reliable supplied software.

The Open Source Program Manager periodically reviews the process at least once a year to disseminate internal best practices and improve any deficiencies.

### (1) Open Source Identification

The business unit complies with the following during the software design stage:

- While designing software, identify the anticipated open source usage and confirm the identified licenses.
- Confirm the obligations for each open source license. The obligations for each license can be found in the Company's Open Source License Guide: https://sktelecom.github.io/guide/use/obligation/
- Design the software considering the source code disclosure scope of each open source license.

The Open Source Program Manager writes and publishes a guide on the obligations, restrictions, and rights of major open source licenses so that business units across the Company can refer to it. This guide must include the following use cases so that common open source license use cases can be managed:

- Distributed in binary form
- Distributed in source form
- Integrated with other open source that triggers additional license obligations
- Includes modified open source
- Includes open source or other software under a license that is incompatible with other components within the supplied software
- Includes open source with attribution requirements

The business unit marks the copyright and license in the source code according to Company rules. The Company's rules for marking copyright and license in source code can be found on the following page. (insert_link)

When considering the introduction of new open source, the business unit first identifies the license. It confirms the license obligations, restrictions, and rights according to the Company's Open Source License Guide. If the license is not described in the Company's Open Source License Guide, it inquires with the Open Source Program Manager about whether it can be introduced and any precautions. A Jira Ticket is created for the inquiry.

The Open Source Program Manager analyzes open source license obligations and provides guidance to the software development organization.

- If there is a question, requests advice from Legal to provide clear guidance.
- Reflects newly analyzed license information in the company-wide license guide.

Security provides a guide for the Company's security assurance.

### (2) Source Code Inspection

The business unit requests an open source inspection according to IT's guidance and provides the source code.

IT performs an open source inspection using an open source analysis tool, and creates the SBOM (Software Bill of Materials).

The Open Source Program Manager reviews whether open source license obligations can be complied with and whether there are open source license conflicts, and requests the business unit to resolve any issues found. Issues are created as Jira Tickets and assigned to the business unit.

Security reviews the known vulnerabilities detected and provides response guidance to the business unit according to predefined Risk classification criteria. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and for Critical Risk, guidance is provided to establish an action plan that can be completed within 1 week.

### (3) Issue Resolution

The business unit resolves all issues found during the source code inspection stage.

It removes the open source in question, or replaces it with open source under a different license. For known vulnerability or newly discovered vulnerability issues, it takes measures such as replacing the component with a version in which the vulnerability has been fixed.

Once the business unit has resolved all issues found, it resolves the Jira Ticket issue and requests a re-review.

### (4) Review

The Open Source Program Manager reviews whether all issues have been adequately addressed. If necessary, it re-performs the source code inspection using an open source analysis tool.

Security reviews whether all serious vulnerabilities have been resolved. If a vulnerability that is difficult to resolve remains, it reviews whether approval is possible considering the business type and service exposure status.

### (5) Approval

The Open Source Program Manager gives final approval or rejection as to whether the open source license compliance procedure has been properly carried out. In case of rejection, it explains the reason to the business unit and proposes a method for correction.

### (6) Registration

The Open Source Program Manager finalizes the SBOM to track the list of open source used in each version of the supplied software.

IT registers the finalized SBOM in the system. The SBOM includes the list of open source contained in the supplied software and the following information:

- The product (or service) name and version of the supplied software
- List of open source
    - Component name, version, license, source (URL)
    - Purpose and manner of use
    - Whether modified and details of modifications
    - Version history and key changes for each version

The registered information is periodically reviewed and updated.

### (7) Notice

The Open Source Program Manager creates an open source notice to comply with the notice obligation. The open source notice includes the following content:

- Open source contact information for open source-related inquiries
- Notice content for each piece of open source
    - Copyright
    - Open source license name
    - Copy of the open source license
    - (if applicable) a Written Offer to obtain a copy of the source code

The Open Source Program Manager creates the open source notice and delivers it to the business unit. If source code disclosure is required, it guides the business unit on how to compile the source code to be disclosed.

The business unit includes the open source notice when distributing the product. For products with a screen, it takes measures so that users can view it through a menu. (e.g., App > Menu > Settings > Copyright Information > Open Source Licenses)

If the business unit has used open source under a license that requires source code disclosure, such as GPL or LGPL, it confirms the scope of source code disclosure required and compiles the source code to be disclosed.

- The source code compiled to comply with license obligations such as GPL and LGPL must match the source code that makes up the binary included in the product. In other words, building the compiled source code must produce a result identical to the binary included in the product.

### (8) Pre-Distribution Confirmation

The business unit submits the following compliance artifacts demonstrating that open source license compliance activities have been properly carried out:

1. The final open source notice included in the product
2. Material confirming that the open source notice is included in the product (e.g., a screenshot showing the open source notice)
3. (if applicable) the source code to be disclosed (submitted compressed into a single file)

The Open Source Program Manager reviews the material submitted by the business unit to check for any issues.

### (9) Distribution

The Open Source Program Manager submits the compliance artifacts submitted by the business unit to IT.

IT registers the compliance artifacts on the Company's open source distribution site.

### (10) Final Confirmation

The Open Source Program Manager conducts a comprehensive check to confirm that the compliance artifacts have been registered on the Company's open source portal without issue, and that they can be downloaded externally without issue.

### (11) Monitoring

The Open Source Program Manager periodically checks whether there is any supplied software for which the creation of open source license compliance artifacts is inadequate. It also operates a process to respond quickly to external inquiries. The detailed procedure for the external inquiry response process follows [2. External Inquiry Response Process].

Security operates a process to monitor and respond to known vulnerabilities or newly discovered vulnerabilities. This process must include the following:

1. A method for continuously monitoring known vulnerabilities or newly discovered vulnerabilities in the open source software components used in supplied software
2. A risk/impact assessment procedure for discovered vulnerabilities
3. A method for contacting customers and taking appropriate action, such as upgrading software components, as necessary
4. A method for maintaining continuous monitoring and response capability even after the supplied software has been released to market

The detailed procedure for this security vulnerability response process follows [2. Security Vulnerability Management Process].

## 2. Security Vulnerability Management Process

After supplied software has been released to market, if a known vulnerability or newly discovered vulnerability is reported, the following process is followed to take appropriate action according to the level of risk.

### (1) Continuous Security Testing Before Release

IT builds and operates a system that applies continuous, repeated security testing to all supplied software before release:

1. Automated security testing:
    - Integrate automated security testing tools into the CI/CD pipeline.
    - Automatically run security tests whenever code changes.
2. Vulnerability scanning:
    - Use an SCA tool to scan for known vulnerabilities in open source components.
    - Automatically update the vulnerability database and perform scans daily.
3. Security test result review:
    - Security reviews the security test results and takes necessary action.
    - If a serious vulnerability is found, immediately notifies the development team and establishes a resolution plan.

### (2) Monitoring Known Vulnerabilities and Newly Discovered Vulnerabilities

IT builds and operates a system to monitor known vulnerabilities and newly discovered vulnerabilities. To identify structural/technical threats, this system performs the following functions:

1. Automated vulnerability monitoring:
    - Analyzes newly published vulnerabilities daily and automatically identifies affected versions of supplied software.
    - Periodically collects publicly available security vulnerability information.
2. SBOM-based analysis:
    - Uses an SCA tool to perform SBOM-based analysis.
    - Integrates the SCA tool into the CI/CD pipeline to perform automated analysis.
3. Notification and record-keeping:
    - When a vulnerability is discovered, automatically sends a notification to the development lead and security lead for the affected supplied software.
    - Uses an issue tracking system so that everything from notification to review, action, and resolution is documented and recorded.

### (3) Vulnerability Assessment and Response

Security assesses each vulnerability according to predefined risk/impact assessment criteria and provides response guidance to the business unit. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and the action deadline is set according to severity.

| Risk | CVSS 3.0 | Recommended Action Schedule |
| --- | --- | --- |
| Low | 0.0 - 3.9 | 0.0 - 3.9 |
| Medium | 4.0 - 6.9 | 4.0 - 6.9 |
| Hgh | 7.0 - 10.0 | 7.0 - 8.9 |
| Critical | - | 9.0 - 10.0 |

If a known vulnerability or newly discovered vulnerability is confirmed in previously released supplied software, the business unit establishes an action plan according to the response guidance provided by Security.

If necessary, the business unit notifies customers of the confirmed vulnerability according to the risk/impact score.

### (4) Vulnerability Resolution and Verification

- The business unit resolves the vulnerability issue according to the established action plan.
- It resolves the vulnerability by removing the problematic open source software component or replacing it with a patched version, among other methods.
- IT uses an open source analysis tool to confirm that the issue has been properly resolved.
- Security performs additional security testing on the resolved vulnerability to verify that it has been completely resolved.
- The verification results are documented and recorded.
- Reviews whether all serious vulnerabilities have been resolved.
- If a vulnerability that is difficult to resolve remains, reviews whether approval is possible considering the business type and service exposure status.

### (5) Post-Release Vulnerability Analysis and Response

IT operates an automated system to analyze vulnerabilities in released supplied software daily, even after release, for all supplied software.

- When affected supplied software is identified, it immediately sends a notification to the development lead and security lead.
- The notified person assesses the severity of the vulnerability and establishes a response plan.
- Carries out patch development, mitigation measures, and other actions according to the response plan.
- Performs verification after the action is completed and documents the results.

### (6) Vulnerability Record Management

For each open source component, a vulnerability record is maintained that includes the following information:

- Vulnerability ID (e.g., CVE number)
- Vulnerability description
- Affected versions
- Severity (CVSS score)
- Date discovered
- Resolution status
- Resolution method applied
- Verification results

Vulnerability records are stored in a central database and backed up periodically.

IT registers the SBOM (Software Bill of Materials) with the vulnerability resolved in the system.

### (7) Reporting and Communication

- A monthly vulnerability management report is prepared and provided to management and relevant stakeholders.
- The report includes the number of newly discovered vulnerabilities, the number of resolved vulnerabilities, the status of and action plan for unresolved vulnerabilities, and key risk factors and response strategies.
- If a serious vulnerability is discovered, it is immediately reported to the relevant department and management.

### (8) Customer and Third-Party Notification

The Open Source Program Manager creates an updated open source notice based on the SBOM with the vulnerability resolved, and delivers it to the business unit.

1. Customer notification:
    
    The business unit notifies customers of the vulnerability resolution in the following ways:
    
    - Replaces the open source notice included with the product distribution.
    - Notifies customers directly by email or other means as necessary.
    - Redistributes the version of the supplied software with the vulnerability resolved.
2. Third-party disclosure:
    
    IT discloses risk information to third parties in the following ways:
    
    - Registers the revised open source notice and vulnerability-related information on the Company's open source website.
    - Submits vulnerability information to a public vulnerability database (e.g., NVD).
    - Notifies the maintainer of the open source project of the discovered vulnerability and its resolution.
3. Notification content:
    
    The information provided to customers and third parties includes the following:
    
    - Vulnerability overview and identifier (e.g., CVE number)
    - Affected products and versions
    - Potential impact of the vulnerability and CVSS score
    - Temporary response measures
    - Patch or update availability and how to apply it
    - Contact information for obtaining further information


## 3. External Inquiry Response Process

Responding quickly and accurately to external inquiries related to open source license compliance and security assurance can greatly reduce the risk of escalation to litigation. To this end, the organization complies with the following process:


![general-inquiry-process](general-inquiry-process.png)

### (1) Acknowledgment of Receipt

The Open Source Program Manager notifies the requester immediately upon receiving an inquiry that it has been received. At this time, it specifies an appropriate response time. If the inquiry is unclear, it requests additional explanation to accurately understand the requester's intent.

Main types of inquiries and requests:

- Whether specific supplied software uses open source
- A request to provide source code under a GPL or LGPL license mentioned in a Written Offer
- A request for an explanation and source code disclosure for open source missing from the open source notice
- A request to provide missing files or build instructions for disclosed source code
- A request for copyright notation
- Inquiries related to known vulnerabilities or newly discovered vulnerabilities

The Open Source Program Manager creates an issue for the received request and records the response status in detail.

### (2) Notification of Investigation

The Open Source Program Manager notifies the requester that the Company is faithfully carrying out open source license compliance and security assurance, and that the inquiry is under investigation. It provides periodic updates on the progress of the internal investigation.

### (3) Internal Investigation

The Open Source Program Manager conducts an internal investigation of the request. It confirms whether the license compliance and security assurance process was properly carried out for the supplied software in question, using the SBOM and the documented review history. It requests advice from Legal and Security as needed.

If confirmation is needed from a specific business unit, the Open Source Program Manager requests the investigation from that unit. The business unit that receives the investigation request immediately checks whether there is a problem with the compliance artifacts and security-related matters, and reports the results.

### (4) Report to the Requester

The Open Source Program Manager completes the internal investigation within the specified response time and notifies the requester of the results.

- If the requester's inquiry was a false claim caused by a misunderstanding, it explains this and closes the matter without further action.
- If a problem is confirmed, it notifies the requester of the accurate method and timing for fulfilling the open source license obligation or resolving the security vulnerability.

### (5) Issue Remediation / Notification

If an actual license compliance or security problem is found during the internal investigation, the relevant business unit carries out all procedures necessary to resolve it.

### (6) Notification of Issue Resolution

Once the problem has been resolved, the requester is notified immediately, and provided with the best way to confirm that the problem has been resolved.

### (7) Process Improvement

If there was a license compliance or security problem, the case is reviewed at an OSRB meeting to understand how the problem occurred, and process improvement measures are established to prevent recurrence.


## 4. Open Source Contribution Process

If the organization allows contributions to external open source projects, the following process must be carried out.

### (1) Establishing and Disseminating a Contribution Policy

- A documented policy governing contributions to open source projects must be established.
- This policy must be disseminated within the organization.
- There must be a process for enforcing the policy.

The Open Source Program Manager must do the following:
- Write a documented open source contribution policy.
- Establish a documented procedure to ensure that all program participants are aware of the open source contribution policy (e.g., education, an internal wiki, or other effective means of communication).

### (2) Contribution Review and Approval Procedure

A documented procedure for managing open source contributions must be established. This procedure must include the following:

- Confirm the origin and license of the code to be contributed.
- Review whether the contributor has the right to contribute the code.
- Review the license and contribution policy of the project being contributed to.
- Obtain review by the Legal team as necessary.
- Define the approval procedure for the contribution.
- Specify the submission method for approved contributions.

The Open Source Program Manager must maintain records demonstrating that this procedure has been carried out correctly.

Through this process, the organization can effectively manage contributions to external open source projects and minimize potential legal risk.
