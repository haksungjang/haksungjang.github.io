# 3. Process

LLMS index: [llms.txt](/llms.txt)

---

The open source process is an actionable procedure that enables an enterprise to comply with its open source policy throughout software development and distribution.

From the standpoint of open source license compliance, the enterprise carries out activities to comply with the conditions required by each license governing the open source used while developing and distributing the supplied software, producing compliance artifacts such as the open source notice and the source code to be disclosed.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 702px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/3-process/input_hu_eee543c7c23d09c5.png" width="692" height="176">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>Simplified view of the compliance end-to-end process : https://www.linuxfoundation.org/wp-content/uploads/OpenSourceComplianceHandbook_2018_2ndEdition_DigitalEdition.pdf</i></center>

</p>
</figcaption>
</figure>


For open source security assurance, the enterprise must detect the presence of Known Vulnerabilities or Newly Discovered Vulnerabilities in the supplied software, identify structural and technical threats, and carry out activities to resolve issues before release.

To achieve effective open source license compliance and security assurance, an enterprise must establish the following processes:

* Open source process
* Open source security vulnerability response process
* External inquiry response process
* Open source contribution process

Let's look at how each process should be structured, one by one.

## 1. Open Source Process

An enterprise must establish an open source process for license compliance and security assurance that aligns with its software development process.

The image below is a sample open source process that an enterprise can commonly adopt and use.

![](./process.png) 

The procedures to be taken at each stage, in line with the open source process above, are as follows.

### (1) Open Source Identification and Inspection

In the open source identification and inspection stage, the enterprise must identify the license of the open source it intends to use, determine what obligations the license requires, and check whether Known Vulnerabilities exist.

It reviews and records which open source it intends to use, what the license is, what obligations each license imposes, and what Known Vulnerabilities exist.

The ISO/IEC 5230 standard requires a documented procedure that can address common open source license use cases for license compliance, and that reviews and records the obligations, restrictions, and rights granted by each identified license.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.3.2.1 - A documented procedure for handling the common open source license use cases for the open source components of the supplied software.<br>`A documented procedure for handling the common open source license use cases for the open source components of the supplied software`
  
* 3.1.5.1 - A documented procedure to review and document the obligations, restrictions and rights granted by each identified license.<br>`A documented procedure to review and document the obligations, restrictions and rights granted by each identified license`

</div>


An example procedure for this is as follows:

1. The Open Source Program Manager creates and provides a guide on the obligations, restrictions, and rights of major open source licenses. To manage common open source license use cases, this guide must cover the following use cases:

   - Distribution in binary form
   - Distribution in source form
   - Integration with other open source that triggers additional license obligations
   - Inclusion of modified open source
   - Inclusion of open source or other software under a license incompatible with other components in the supplied software
   - Inclusion of open source with attribution requirements

2. The business unit checks the license and Known Vulnerabilities according to the criteria defined in the open source policy.
3. The business unit consults the Open Source Program Manager and the security officer with any questions. If necessary, it requests advice from external experts.
4. All decisions and their rationale are documented and retained.

To this end, an enterprise must establish a documented procedure, as in the example below, to review and record the obligations and restrictions imposed by each identified license and any Known Vulnerabilities, through the open source identification and inspection stage before releasing the supplied software.

```
(1) Open Source Identification

The business unit complies with the following during the software design stage:

- While designing the software, it identifies the open source expected to be used and confirms the identified licenses.
- It checks the obligations for each open source license. License-specific obligations can be found in the company's open source license guide: https://sktelecom.github.io/guide/use/obligation/
- It designs the software taking into account the source code disclosure scope required by each open source license.

The Open Source Program Manager creates and publishes a guide on the obligations, restrictions, and rights of major open source licenses so that business units across the company can refer to it. To manage common open source license use cases, this guide must cover the following use cases:

- Distribution in binary form
- Distribution in source form
- Integration with other open source that triggers additional license obligations
- Inclusion of modified open source
- Inclusion of open source or other software under a license incompatible with other components in the supplied software
- Inclusion of open source with attribution requirements

The business unit marks copyright and license notices in the source code according to company rules. The company's rules for copyright and license notices in source code can be found on the following page. (insert_link)

When reviewing the adoption of new open source, the business unit first identifies the license. It checks the license obligations, restrictions, and rights according to the company's open source license guide. If the license is not covered by the company's open source license guide, it consults the Open Source Program Manager on whether adoption is possible and what precautions apply. It creates a Jira Ticket for the inquiry. 

The Open Source Program Manager analyzes the open source license obligations and provides guidance to the software development organization.

- If there are questions, it requests advice from the legal department to provide clear guidance.
- Newly analyzed license information is reflected in the company-wide license guide.

The security officer provides a guide for the company's security assurance.

(2) Source Code Inspection

The business unit requests an open source inspection according to the guidance of the IT staff and provides the source code.

The IT staff performs the open source inspection using an open source analysis tool and generates an SBOM (Software Bill of Materials).

The Open Source Program Manager reviews whether the open source license obligations can be complied with and whether there are open source license conflicts, and requests the business unit to resolve any issues found. Issues are created as Jira Tickets and assigned to the business unit.

The security officer reviews the detected Known Vulnerabilities and provides response guidance to the business unit according to predefined risk classification criteria. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and for Critical Risk, the business unit is guided to establish a remediation plan within one week.
```

In the open source identification and inspection stage, a source code scan tool can be used. This is described in detail in "[1. Source Code Scan Tools](../4-tool/#1-source-code-scanning-tools)".

### (2) Issue Resolution

After identifying open source and confirming license and security vulnerability risks through open source identification and inspection, a procedure to resolve issues is needed. All detected issues must be resolved using the following methods:

- Remove the open source causing the issue.
- Replace it with open source under a different license to resolve the license issue. 
- Replace it with a version of the open source in which the Known Vulnerability or Newly Discovered Vulnerability has been resolved. 

An example of a documented process for this is as follows:

```
(3) Issue Resolution

The business unit resolves all issues found during the source code inspection stage. 

It removes the open source causing the issue or replaces it with open source under a different license. For issues involving a Known Vulnerability or a Newly Discovered Vulnerability, it takes measures such as replacing the component with a version in which the vulnerability has been fixed.

Once the business unit resolves all issues found, it resolves the Jira Ticket issue and requests a re-review.
```

### (3) SBOM Identification, Review, and Retention

The most fundamental part of open source license compliance activities is understanding the open source contained in the supplied software. An enterprise must establish a process to identify the open source and its licenses contained in the supplied software, and to create and manage an SBOM (Software Bill of Materials) that holds this information. This is because knowing which open source is included in each version of the supplied software is necessary to comply with the obligations required by each open source license when distributing the software. This is also an essential process for discovering and responding to open source security vulnerabilities.

All open source must be reviewed and approved before being integrated into the supplied software. In addition to the functionality and quality of the open source, it must be reviewed beforehand for its origin, whether it can meet license requirements, and whether Known Vulnerabilities or Newly Discovered Vulnerabilities have been resolved. This requires a review request → review → approval process.

The ISO standards commonly require a documented procedure ensuring that all open source software used in the supplied software is continuously recorded throughout the software life cycle, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.3.1.1 - A documented procedure for identifying, tracking, reviewing, approving, and archiving information about the collection of open source components from which the supplied software is comprised. <br>`A documented procedure for identifying, tracking, reviewing, approving, and archiving information about the open source components that make up the supplied software`

</div>



<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



* 3.3.1.1: A documented procedure ensuring all Open Source Software used in the Supplied Software is continuously recorded across the lifecycle of the Supplied Software. This includes an archive of all Open Source Software used in the Supplied Software;<br>`A documented procedure ensuring that all open source software used in the supplied software is continuously recorded throughout the lifecycle of the supplied software. This includes an archive of all open source software used in the supplied software.`

</div>


To this end, an enterprise can reflect SBOM-related content in its open source process, as in the example below:

```
(4) Review

The Open Source Program Manager reviews whether all issues have been properly remediated. If necessary, it re-runs the source code inspection using an open source analysis tool.

The security officer reviews whether all serious vulnerabilities have been resolved. If vulnerabilities that are difficult to resolve remain, it reviews whether approval is possible, taking into account the type of business and the extent of service exposure.

(5) Approval

The Open Source Program Manager gives final approval or rejection of whether the open source license compliance procedure was performed properly. In the case of rejection, it explains the reason to the business unit and proposes a way to remediate it.

(6) Registration

The Open Source Program Manager finalizes the SBOM to track the list of open source used, by version, in the supplied software.

The IT staff registers the finalized SBOM in the system. The SBOM includes the list of open source contained in the supplied software along with the following information:

- The product (or service) name and version of the supplied software
- List of open source
  - Open source name / version
  - Open source license

The Open Source Program Manager finalizes the SBOM to track the list of open source used, by version, in the supplied software.
```

Tools for SBOM management are described in detail in "[SBOM Management Tools](../4-tool/#3-open-source-governance--sbom-management-tools)".

In addition, every process and result of this open source process must be documented. Rather than using email, using an issue tracking system such as [Jira](https://www.atlassian.com/software/jira) or [Bugzilla](https://www.bugzilla.org/) can document this process more efficiently.


### (4) Creating License Compliance Artifacts

The most fundamental part of open source license compliance activities is understanding the open source contained in the supplied software. This is to correctly meet open source license requirements, which are at the core of open source license compliance. In other words, a process must be established to produce a set of compliance artifacts for the open source contained in the supplied software.

The ISO/IEC 5230 standard requires a documented procedure describing the process for preparing compliance artifacts and providing them together with the supplied software, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.4.1.1 - A documented procedure that describes the process under which the compliance artifacts are prepared and distributed with the supplied software as required by the identified licenses.<br>`A documented procedure that describes the process under which the compliance artifacts required by the identified licenses are prepared and distributed with the supplied software`

</div>


Compliance artifacts are broadly divided into two types:

1. Open source notice: a document providing the full text of open source licenses and copyright information

    ![](ossnotice.png)


* How to generate an open source notice corresponding to an SBOM compiled using a tool is further explained in "[Open Source Compliance Artifact Generation Tools](../4-tool/#5-open-source-compliance-artifact-generation-tools)".  

2. Source code package to be disclosed: a package compiling the source code to be disclosed in order to fulfill the obligations of open source licenses such as GPL and LGPL that require source code disclosure

Compliance artifacts must be provided together when distributing the supplied software.

To this end, an enterprise can reflect the creation of compliance artifacts, from the notice stage through the distribution stage, in its open source process, as in the example below:

```
(7) Notice

The Open Source Program Manager creates an open source notice to comply with the notice obligation. The open source notice includes the following content:

- An open source contact for open source-related inquiries
- Notice content for each open source
  - Copyright 
  - Open source license name
  - Copy of the open source license
  - (if applicable) a Written Offer to obtain a copy of the source code

The Open Source Program Manager creates the open source notice and delivers it to the business unit. If source code disclosure is required, it also guides the business unit on how to compile the source code to be disclosed.

The business unit includes the open source notice when distributing the product. For a product with a screen, it takes measures so that users can view it through a menu. (e.g., App > Menu > Settings > Copyright Information > Open Source Licenses)

If the business unit has used open source under a license requiring source code disclosure, such as GPL or LGPL, it checks the required scope of disclosure and compiles the source code to be disclosed.

- The source code compiled to comply with obligations under licenses such as GPL and LGPL must match the source code that makes up the binary shipped in the product. In other words, building the compiled source code must produce the same result as the binary shipped in the product.

(8) Pre-Distribution Check

The business unit submits the following compliance artifacts demonstrating that open source license compliance activities were properly performed:

1. The final open source notice included in the product
2. Materials confirming that the open source notice is included in the product (e.g., a screenshot showing the open source notice)
3. (if applicable) the source code to be disclosed (submitted compressed into a single file)

The Open Source Program Manager reviews the materials submitted by the business unit to confirm there are no issues.

(9) Distribution

The Open Source Program Manager submits the compliance artifacts submitted by the business unit to the IT staff.

The IT staff registers the compliance artifacts on the company's open source distribution site.
```

When distributing the supplied software, it may be difficult to enclose the source code package to be disclosed. In this case, this can be replaced by providing a Written Offer to supply the source code for at least three years. A Written Offer is generally provided through the product's user manual, and an example is as follows:

```
The software included in this product contains copyrighted software 
that is licensed under the GPL. A copy of that license is included 
in this document on page X. You may obtain the complete Corresponding 
Source code from us for a period of three years after our last shipment 
of this product, which will be no earlier than 2011-08- 01, by sending 
a money order or check for $5 to:

GPL Compliance Division
Our Company
Any Town, US 99999

Please write"source for product Y" in the memo line of your payment.
You may also find a copy of the source at http://www.example.com/sources/Y/.
This offer is valid to anyone in receipt of this information.

<Source: SFLC Guide to GPL Compliance>
```

Therefore, compliance artifacts must be retained for at least three years, and a process must be established for this. 

To this end, an enterprise can consider building an open source website. Details can be found in "[Open Source Compliance Artifact Retention](../4-tool/#6-archiving-open-source-compliance-artifacts)".

### (5) Security Vulnerability Inspection and Assessment

The security officer must establish a process to inspect and assess Known Vulnerabilities or Newly Discovered Vulnerabilities in the open source software components of the supplied software. This process must include the following stages:

1. Vulnerability database search: Use a public vulnerability database such as the [National Vulnerability Database (NVD)](https://nvd.nist.gov/) to search for Known Vulnerabilities in the open source components in use.

2. Use of automated vulnerability scanning tools: Use a tool such as [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) to scan the dependencies of the supplied software and identify Known Vulnerabilities.

3. Vulnerability severity assessment: Use [CVSS (Common Vulnerability Scoring System)](https://www.first.org/cvss/) to assess the severity of discovered vulnerabilities.

4. Risk analysis: Analyze the potential impact of the identified vulnerabilities on the supplied software.

5. Response plan development: Establish a response plan for each vulnerability based on its severity and risk analysis results.

```
(2) Source Code Inspection

The security officer reviews the detected Known Vulnerabilities and provides response guidance to the business unit according to predefined risk classification criteria. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and for Critical Risk, the business unit is guided to establish a remediation plan within one week.

| Risk | CVSS 2.0 | CVSS 3.0 | Recommended Remediation Timeline |
|---|:---:|:---:|:---:|
| Low | 0.0 - 3.9 | 0.0 - 3.9 | - |
| Medium | 4.0 - 6.9 | 4.0 - 6.9 | - |
| High | 7.0 - 10.0 | 7.0 - 8.9 | Within 4 weeks | 
| Critical | - | 9.0 - 10.0 | Within 1 week |
```

6. Reporting and documentation: Document the inspection results, assessment content, and response plan, and report them to relevant stakeholders.

7. Continuous monitoring: Establish a continuous monitoring system, since new vulnerabilities may be discovered or the severity of existing vulnerabilities may change.

Through this process, an enterprise can effectively manage security vulnerabilities in the supplied software and meet the requirements of ISO/IEC 18974.

## 2. Open Source Security Vulnerability Response Process

While developing the supplied software, an enterprise must carry out activities for security assurance, such as detecting and resolving open source security vulnerabilities.

The ISO/IEC 18974 standard requires a documented procedure for the security assurance method and a record of the actions taken, as follows.

<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



3.1.5 - Standard Practice Implementation  `3.1.5 - Standard Practice Implementation`

The Program demonstrates a sound and robust handling procedures of Known Vulnerabilities and Secure Software Development by defining and implementing following procedures:<br>`The Program defines and implements the following procedures to demonstrate sound and robust handling of Known Vulnerabilities and Secure Software Development.`

* Method to identify structural and technical threats to the Supplied Software is defined;<br>`A method to identify structural and technical threats to the Supplied Software`
* Method for detecting existence of Known Vulnerabilities in Supplied Software;<br>`A method for detecting the existence of Known Vulnerabilities in the Supplied Software`
* Method for following up on identified Known Vulnerabilities;<br>`A method for following up on identified Known Vulnerabilities`
* Method to communicate identified Known Vulnerabilities to customer base when warranted;<br>`A method to communicate identified Known Vulnerabilities to the customer base under warranty when warranted`
* Method for analyzing Supplied Software for newly published Known Vulnerabilities post release of the Supplied Software;<br>`A method for checking whether newly published Known Vulnerabilities exist in already-released Supplied Software after a new Known Vulnerability is published following the release of the Supplied Software`
* Method for continuous and repeated Security Testing is applied for all Supplied Software before release;<br>`A method for applying continuous and repeated Security Testing to all Supplied Software before release`
* Method to verify that identified risks will have been addressed before release of Supplied Software;<br>`A method to verify that identified risks are addressed before release of the Supplied Software`
* Method to export information about identified risks to third parties as appropriate.<br>`A method to appropriately export information about identified risks to third parties`

* 3.1.5.1: A documented procedure exists for each of the methods identified above.<br>`A documented procedure exists for each of the methods identified above`


3.3.2 - Security Assurance `3.3.2 - Security Assurance`

* 3.3.2.1: A documented procedure for handling detection and resolution of Known Vulnerabilities for the Open Source Software components of the Supplied Software;<br>`A documented procedure for detecting and resolving Known Vulnerabilities in the open source software components of the Supplied Software`
* 3.3.2.2: For each Open Source Software component a record is maintained of the identified Known Vulnerabilities and action(s) taken (including even if no action was required).<br>`For each open source software component, a record is maintained of the identified Known Vulnerabilities and the action(s) taken (including cases where no action was required).`

</div>


To this end, an enterprise must have methods and procedures to detect the presence of Known Vulnerabilities or Newly Discovered Vulnerabilities in the supplied software, resolve identified risks before release, and also respond to vulnerabilities newly published after release.


First, an enterprise must detect whether Known Vulnerabilities exist in the software to be distributed and resolve identified risks before release. This procedure for detecting and resolving Known Vulnerabilities can be carried out through the open source identification, source code inspection, and issue resolution stages of the [Open Source Process](#1-open-source-process).

In addition, to check whether a newly published Known Vulnerability exists in software that has already been distributed after the release of the distributed software, and to resolve it, an enterprise must establish a new security vulnerability response process.

Below is a sample process for responding when a new security vulnerability is discovered.

![](./securityprocess.png)
<center><i>New Security Vulnerability Response Process (Sample)</i></center><br>

### (1) Monitoring Known Vulnerabilities and Newly Discovered Vulnerabilities

```
(1) Monitoring

The IT staff builds and operates a system to monitor new security vulnerabilities. This system performs the following functions.

- It periodically collects newly published security vulnerabilities.
- If open source with a newly discovered Known Vulnerability is used in an already-released product/service, it sends a notification to the business unit responsible for that product/service. From notification through review, action, and resolution, everything is documented and recorded using the Jira Issue Tracker.
```

The IT staff builds and operates a system that monitors Known Vulnerabilities and Newly Discovered Vulnerabilities. This system performs the following functions:

- It periodically collects new security vulnerability information from a public vulnerability database such as the [National Vulnerability Database (NVD)](https://nvd.nist.gov/).
- If an open source software component with a Known Vulnerability or a Newly Discovered Vulnerability is used in already-released supplied software, it sends a notification to the business unit responsible for that supplied software. 
- It uses an issue tracking system such as [Jira](https://www.atlassian.com/software/jira) so that everything from notification through review, action, and resolution is documented and recorded.

### (2) Vulnerability Assessment and Response

```
(2) Initial Response

The security officer provides response guidance to the business unit according to predefined risk classification criteria. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and for Critical Risk, the business unit is guided to establish a remediation plan within one week.

If a new security vulnerability is discovered in a previously released product/service, the business unit establishes a remediation plan according to the response guidance provided by the security officer.

If there are customers under warranty, the business unit notifies them of the identified Known Vulnerability by email or other means, as necessary, according to the risk level.
```

The security officer assesses each vulnerability according to predefined risk/impact assessment criteria and provides response guidance to the business unit. Risk is classified by [CVSS (Common Vulnerability Scoring System)](https://www.first.org/cvss/) score, and remediation deadlines are set according to severity.

If a Known Vulnerability or a Newly Discovered Vulnerability is identified in previously released supplied software, the business unit establishes a remediation plan according to the response guidance provided by the security officer.

If necessary, the business unit notifies customers of identified vulnerabilities according to the risk/impact score.

### (3) Applying Security Testing

The IT staff builds and operates a system that applies continuous, repeated security testing to all supplied software before release. This system performs the following functions:

- It identifies structural and technical threats to the supplied software.
- It detects the presence of Known Vulnerabilities or Newly Discovered Vulnerabilities.
- It verifies that identified risks are resolved before the supplied software is released.

### (4) Vulnerability Resolution and Patch Management

```
(3) Issue Resolution

The business unit resolves the security vulnerability issue according to the established remediation plan, by methods such as removing the problematic open source or replacing it with a patched version. Once all identified issues are resolved, it requests a re-review.

(4) Review

The IT staff uses an open source analysis tool to confirm that the issue has been properly resolved.

(5) Approval

The security officer reviews whether all serious vulnerabilities have been resolved. If vulnerabilities that are difficult to resolve remain, it reviews whether approval is possible, taking into account the type of business and the extent of service exposure.

(6) Registration

The IT staff registers the SBOM, with the open source security vulnerability resolved, in the system.
```

The business unit resolves the vulnerability issue according to the established remediation plan, by methods such as removing the problematic open source software component or replacing it with a patched version.

The IT staff uses an open source analysis tool to confirm that the issue has been properly resolved.

The security officer reviews whether all serious vulnerabilities have been resolved. If vulnerabilities that are difficult to resolve remain, it reviews whether approval is possible, taking into account the type of business and the extent of service exposure.

The IT staff registers the SBOM (Software Bill of Materials), with the vulnerability resolved, in the system.

### (5) Customer Notification

```
(7) Notice

The Open Source Program Manager creates an open source notice based on the SBOM in which the open source security vulnerability has been resolved, and delivers it to the business unit.

The business unit replaces the open source notice included with the product distribution.

The IT staff registers the revised open source notice on the company's open source distribution site.

(8) Distribution

The business unit redistributes the version of the software in which the open source security vulnerability has been resolved.

The security officer identifies whether there is risk information that needs to be disclosed to third parties, and if so, delivers it to the IT staff.

The IT staff registers the identified risk information on the open source website so that third parties can review it.
```

The Open Source Program Manager creates an updated open source notice based on the SBOM in which the vulnerability has been resolved, and delivers it to the business unit.

The business unit notifies customers of the vulnerability resolution using the following methods:

- It replaces the open source notice included with the product distribution.
- If necessary, it notifies customers directly by email or other means.
- It redistributes the version of the supplied software in which the vulnerability has been resolved.

The IT staff registers the revised open source notice and vulnerability-related information on the company's open source distribution site so that third parties can review them.

Through this process, continuous monitoring and response capability is maintained even after the supplied software has been released to the market.

Through this systematic approach, an organization can gain the following benefits:

1. Rapid response capability for new vulnerabilities
2. Improved transparency and trust with customers
3. Minimization and management of security risk
4. Assurance of compliance with regulatory requirements
5. Continuous improvement of product quality and security

This process also satisfies the requirements of ISO/IEC 18974 and can continuously improve the effectiveness of the organization's open source security assurance program.


## 3. External Inquiry Response Process

To prevent external claims from escalating into legal action, it is important for an enterprise to respond to external inquiries and requests as quickly and accurately as possible. To this end, an enterprise must establish a process for responding quickly and effectively to external open source inquiries.

The ISO standards commonly require an internal documented procedure for responding to third-party inquiries, as follows. 

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.2.1.2 - An internal documented procedure for responding to third party open source license compliance inquiries.<br>`An internal documented procedure for responding to third-party open source license compliance inquiries`

</div>



<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



* 3.2.1.2: An internal documented procedure exists for responding to third party Known Vulnerability or Newly Discovered Vulnerability inquiries.<br>`An internal documented procedure for responding to third-party inquiries about a Known Vulnerability or a Newly Discovered Vulnerability`

</div>


The figure below is a sample process an enterprise should have in place to respond to external inquiries.  

![](general-inquiry-process.png)

<center><i>External Inquiry Response Process (Sample)</i></center><br>

The following is the external inquiry response process presented in the open source process template:

```
Responding quickly and accurately to external inquiries related to open source license compliance and security assurance can greatly reduce the risk of escalation to legal action. To this end, the organization follows the process below:
```

### (1) Receipt Notification

As soon as an inquiry is received, the Open Source Program Manager notifies the requester that the inquiry has been received. At this time, it specifies an appropriate response time. If the inquiry is unclear, it requests additional explanation to accurately understand the requester's intent.

Major inquiries and requests include:
- Whether specific open source is used in a particular supplied software
- A request for the source code under a GPL or LGPL license mentioned in a Written Offer
- A request for clarification and source code disclosure regarding open source missing from the open source notice
- A request for missing files in the disclosed source code and instructions on how to build it
- A request for copyright notice
- An inquiry related to a Known Vulnerability or a Newly Discovered Vulnerability

The Open Source Program Manager creates an issue for the received request and records the response status in detail.

### (2) Investigation Notification

The Open Source Program Manager notifies the requester that open source license compliance and security assurance are being faithfully carried out and that the inquiry is under investigation. It periodically updates and notifies the requester of the progress of the internal investigation.

### (3) Internal Investigation

The Open Source Program Manager conducts an internal investigation into the request. It checks, through the SBOM and documented review history, whether the license compliance and security assurance processes were properly carried out for the relevant supplied software. If necessary, it requests advice from the legal department and the security officer.

If confirmation from a specific business unit is needed, the Open Source Program Manager requests that unit to investigate. The business unit that receives the request immediately checks whether there is a problem with the compliance artifacts and security-related matters, and reports the results.

### (4) Reporting to the Requester

The Open Source Program Manager completes the internal investigation within the specified response time and notifies the requester of the results.

- If the requester's inquiry was a mistaken claim due to a misunderstanding, it explains this without further action and closes the matter.
- If a problem is confirmed, it informs the requester of the exact method and timing for fulfilling the obligations of the relevant open source license or resolving the security vulnerability.

### (5) Remediation / Notification

If an actual license compliance or security problem is found during the internal investigation, the relevant business unit carries out all procedures necessary to resolve it.

### (6) Resolution Notification

After resolving the problem, it immediately notifies the requester and provides the best available means to confirm that the problem has been resolved.

### (7) Process Improvement

If there was a license compliance or security problem, the case is reviewed through an [OSRB (Open Source Review Board)](https://www.linuxfoundation.org/tools/open-source-glossary/#osrb) meeting to understand how the problem occurred, and process improvement measures are established to prevent recurrence.

Through this systematic external inquiry response process, an enterprise can respond quickly and effectively to open source-related issues and minimize potential legal risk.

## 4. Open Source Contribution Process

If an enterprise has a policy that permits contributions to external open source projects, there must be a documented procedure governing how program participants can contribute to external projects.

The ISO/IEC 5230 standard requires a documented procedure governing open source contributions, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



3.5.1.2 - A documented procedure that governs open source contributions; <br>`A documented procedure that governs open source contributions`

</div>


### (1) Establishing and Communicating the Contribution Policy

The open source process template describes the establishment and communication of the contribution policy as follows:

```
(1) Establishing and Communicating the Contribution Policy
- A documented policy governing contributions to open source projects must be established.
- This policy must be communicated within the organization.
- There must be a process for enforcing the policy.

The Open Source Program Manager must do the following:
- Draft a documented open source contribution policy.
- Establish a documented procedure to ensure that all program participants are aware of the open source contribution policy (e.g., through training, an internal wiki, or other effective means of communication).
```

### (2) Contribution Review and Approval Procedure

The open source process template describes the contribution review and approval procedure as follows:

```
(2) Contribution Review and Approval Procedure

A documented procedure governing open source contributions must be established. This procedure must include the following:
- Confirm the origin and license of the code to be contributed.
- Review whether there is a right to contribute the code.
- Review the license and contribution policy of the project to which the contribution is directed.
- If necessary, obtain a legal team review.
- Define an approval procedure for the contribution.
- Specify how an approved contribution is to be submitted.

The Open Source Program Manager must maintain records demonstrating that this procedure has been properly carried out.
```

Through this process, an organization can effectively manage contributions to external open source projects and minimize potential legal risk.

The [open source contribution procedure](https://sktelecom.github.io/guide/contribute/process/) published by [SK telecom](https://www.sktelecom.com/) is a good example:


![](contribution.png)

[https://sktelecom.github.io/guide/contribute/process/](https://sktelecom.github.io/guide/contribute/process/)

This procedure clearly shows the process from the contribution review request through approval to submission of the contribution, making it easy for program participants to understand and follow.


## 5. Keeping the Process Current

A process is not effective if it exists only on paper without being actually operated, or if it no longer fits the work situation or organizational structure. An enterprise must ensure that its processes are always kept up to date to match its internal organization and circumstances.

The ISO/IEC 18974 standard requires that the process be periodically reviewed and improved, as follows:

<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



* 3.1.2.5: Documented Evidence of periodic reviews and changes made to the process;<br>`Documented evidence that the process has been periodically reviewed and improved`
* 3.1.2.6: Documented verification that these processes are current with company internal best practices and who is assigned to accomplish them.<br>`Documented evidence that these processes are kept current with the company's internal best practices, specifying who is responsible for carrying them out`

</div>


### (1) Periodic Process Review

The open source process template describes periodic process review as follows:

```
The OSRB (Open Source Review Board) is a body composed of the Open Source Program Manager and the heads of related organizations, such as the legal team, patent team, development team, and infrastructure team, for the company's open source management.

The OSRB reviews the policy and process annually on a regular basis and improves them. All improvement processes are documented and recorded.
```

### (2) Identifying and Implementing Improvements

The following activities are carried out to improve the process:

- The OSRB analyzes the company's process performance, shortcomings, and best practices.
- It improves the process to reflect changes in the business environment.
- The Open Source Program Manager is responsible for managing the policy and process for open source license compliance.
- The security officer is responsible for managing the policy and process for open source security assurance.

### (3) Documenting Process Updates

The process improvement and update process is documented and recorded. This must include:

- Review date and participants
- Identified improvements
- Implemented changes
- Reason for the change
- Approver of the change

These documented records can be managed using tools such as [Jira](https://www.atlassian.com/software/jira) or [Confluence](https://www.atlassian.com/software/confluence).

By keeping its processes current, an enterprise can continuously improve the effectiveness of its open source license compliance and security assurance programs and meet the requirements of ISO/IEC 5230 and ISO/IEC 18974.

## 6. Summary

By establishing the processes described so far, an enterprise can meet the key requirements of the ISO/IEC 5230 and ISO/IEC 18974 standards.

![](./processno.png)

 Through establishing these processes, an enterprise can gain the following benefits:

1. Establishing an open source license compliance framework
   - Accurately understanding the open source usage status of the supplied software
   - Minimizing legal risk by complying with license obligations
   - Systematic creation and management of compliance artifacts

2. Strengthening open source security assurance
   - Continuous monitoring of Known Vulnerabilities and Newly Discovered Vulnerabilities
   - Establishing a vulnerability assessment and response framework
   - Preventing risk in advance through security testing

3. Effective response to external inquiries
   - Establishing a systematic external inquiry handling process
   - Reducing legal risk through fast and accurate response

4. Systematizing open source contribution activities
   - Ensuring consistent contribution activity through an established contribution policy
   - Protecting intellectual property through a contribution review and approval procedure

5. Continuous process improvement
   - Improving efficiency through periodic process review and improvement
   - Strengthening responsiveness to the latest open source trends and technological changes

By establishing these processes, an enterprise can systematically manage open source license compliance and security assurance, and build a foundation for continuous improvement. In addition, by having processes that align with international standard initiatives such as the [OpenChain Project](https://www.openchainproject.org/), it can enhance its credibility within the global software supply chain.
