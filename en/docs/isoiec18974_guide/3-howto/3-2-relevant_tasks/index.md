# 3.2 Relevant Tasks Defined and Supported

LLMS index: [llms.txt](/llms.txt)

---

For an open source security assurance program to operate effectively, all relevant tasks must be clearly defined and the necessary resources must be properly allocated. This is essential for securing the personnel, budget, and technical expertise needed to operate the program, and for supporting its continual improvement.

## 3.2.1 Access

Providing third parties with access to make enquiries about known vulnerabilities affecting an organization's software is critical to increasing transparency, strengthening collaboration with the community, and quickly resolving potential security issues.

### 3.2.1.1 Publicly Visible Method for Vulnerability Enquiries

> **ISO/IEC 18974**  
> - 4.2.1.1: Publicly visible method to allow third parties to make known vulnerability or newly discovered vulnerability enquires (e.g., via an email address or web portal that is monitored by program participants);
> - 4.2.1.1 Publicly visible method to allow third parties to make known vulnerability or newly discovered vulnerability enquires (e.g., via an email address or web portal that is monitored by program participants)
>   
> **Self-Certification Checklist**  
> - [ ] We have a method to allow third parties to make Known Vulnerability or Newly Discovered Vulnerability enquires (e.g., via an email address or web portal that is monitored by Program Participants);
> - [ ] We have a method to allow third parties to make known vulnerability or newly discovered vulnerability enquires (e.g., via an email address or web portal).

The organization shall make it possible to provide information about software vulnerabilities through a method that anyone can easily access. This can be implemented through the organization's website, a dedicated security page, or a separate bug bounty platform. What matters is that the method for providing information is clear, easy to find, and continuously monitored.

#### Implementation Methods and Considerations

- **Dedicated Email Address**:
    - Create a dedicated email address for vulnerability reports, such as `security@example.com`, and publish it on the website.
    - The email address shall be continuously monitored by the security team or the relevant person in charge.
- **Web-Based Reporting Form**:
    - Provide a web-based reporting form where the information needed for a vulnerability report (e.g., software name, version, vulnerability description, reproduction steps) can be entered.
    - The reporting form shall be easy to use and include clear instructions.
- **Security Page**:
    - Publish a security page on the website that includes the organization's security policy, vulnerability reporting procedure, and related contact information.
    - Provide a link on the website's main page so the security page can be easily found.
- **Bug Bounty Program**:
    - Run a bug bounty program that encourages external security experts to test the organization's systems and discover vulnerabilities.
    - A bug bounty program provides rewards for vulnerability reports and encourages researchers to participate.

#### Examples

- Post a statement on the website such as: "If you discover a security vulnerability in our company's products, please contact us at `security@example.com`. For details, see the [security page](https://example.com/security)."
- The vulnerability reporting web form includes the following fields:
    - Reporter information (name, email address)
    - Affected product and version
    - Vulnerability description
    - Reproduction steps
    - Supporting evidence (screenshots, log files, etc.)


#### Documentation Approach

Include content on security vulnerabilities when responding to external enquiries, as shown below, within the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 9.1 Responsibility for Responding to External Enquiries

1. Designation of Responsible Party:
    - The **Open Source Program Manager (OSPM)** is responsible for responding to external open source-related enquiries and requests.
    - Where necessary, the OSPM cooperates with the legal team (for license compliance matters) or the security team (for security vulnerability matters) to resolve issues.
2. Enquiry Routing Procedure:
    - Any program participant who receives an open source-related enquiry from outside the organization shall immediately forward it to the **Open Source Program Manager**.
    - The enquiry is promptly routed to the department responsible for license compliance or security vulnerabilities, depending on its nature.

### 9.2 Publication of Contact Information

1. Public Contact Information:
    - The official contact information of the *Open Source Program Manager* is made publicly available.
    - The contact information is registered in the following channels:
        - Open source notices
        - Company website
        - The Linux Foundation's Open Compliance Directory
2. Guidance on How to Make Enquiries:
    - Clearly explain how external parties can make open source-related enquiries.
    - Operate a system to receive enquiries through channels such as an email address or a website enquiry form.

### 9.3 Procedure for Responding to External Enquiries

1. Enquiry Receipt and Confirmation:
    - When an external enquiry is received, the **Open Source Program Manager** immediately confirms it and specifies an appropriate resolution time.
    - The nature of the enquiry is reviewed and classified as either license compliance or a security vulnerability.
        - License compliance: Reviewed and addressed in cooperation with the legal team.
        - Security vulnerability: Severity is assessed and action is taken in cooperation with the security team.
2. Response Execution:
    - Appropriate response measures are carried out based on the content of the enquiry, with the help of external experts where necessary.
    - The entire response process is recorded through an internal system (e.g., a Jira tracker).
3. Providing Feedback and Improvement:
    - After the response, feedback is provided to the external party, and improvement measures are proposed where necessary.
    - Response records are analyzed and the process is improved to prevent recurring issues.


</div>


### 3.2.1.2 Internal Procedure for Responding to Vulnerability Enquiries

> **ISO/IEC 18974**  
> - 4.2.1.2: An internal documented procedure for responding to third party known vulnerability or newly discovered vulnerability inquiries.
> - 4.2.1.2 An internal documented procedure for responding to third party known vulnerability or newly discovered vulnerability inquiries exists.
>   
> **Self-Certification Checklist**  
> - [ ] We have an internal documented procedure for responding to third party Known Vulnerability or Newly Discovered Vulnerability inquiries.
> - [ ] We have documented the internal procedure for responding to external inquiries.

When a vulnerability enquiry is received from outside the organization, it is critical to have a procedure in place for responding to it in a systematic and efficient manner internally. This procedure covers the entire process of enquiry receipt, analysis, resolution, and reporting, and must clearly define the person responsible and the deadline for each stage. It must also account for information security and legal liability, so that sensitive information can be handled and shared securely.

#### Implementation Methods and Considerations

- **Forming a Response Team**:
    - Designate a responsible team or person in charge to receive and handle vulnerability enquiries.
    - The response team may include security experts, developers, and legal personnel.
- **Defining the Process**:
    - Document the entire process, including the stages of receiving, classifying, analyzing, resolving, and reporting vulnerability enquiries.
    - Clearly define the person responsible and the deadline for each stage.
- **Severity Assessment Criteria**:
    - Establish criteria for assessing the severity of a vulnerability.
    - The Common Vulnerability Scoring System (CVSS) score can be used to objectively assess the severity of a vulnerability.
- **Response Procedure**:
    - Establish different response procedures depending on the severity of the vulnerability.
    - Respond immediately to high-risk vulnerabilities, and consider monitoring or a long-term resolution plan for low-risk vulnerabilities.
- **Communication Guidelines**:
    - Establish guidelines on how to inform the person who reported the vulnerability of progress and how to request additional information.
    - Communication with the reporter shall be transparent and prompt.

#### Example of a Specific Procedure

1. **Receipt**: The security team confirms vulnerability enquiries received at `security@example.com` and assigns a case number.
2. **Classification**: The security team analyzes the type of vulnerability and the affected systems, and assesses its severity.
3. **Analysis**: The development team analyzes the cause of the vulnerability and explores resolution options.
4. **Resolution**: The development team modifies the code to resolve the vulnerability and performs testing.
5. **Verification**: The QA team confirms that the modified code contains no new vulnerabilities and verifies that the existing vulnerability has been resolved.
6. **Reporting**: The security team reports the vulnerability resolution results and updates the related documentation.
7. **Notification**: The security team notifies the person who reported the vulnerability of the resolution results.


#### Documentation Approach

Add a section on responding to security vulnerabilities to the external enquiry response procedure within the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (1) Receipt Notification

As soon as the Open Source Program Manager receives an enquiry, they notify the requester that it has been received, specifying an appropriate response time. If the enquiry is unclear, the Open Source Program Manager requests additional explanation to accurately understand the requester's intent.

Common types of enquiries and requests:

- Whether a specific supplied software uses open source
- Requests for source code under the GPL or LGPL licenses mentioned in a written offer
- Requests for explanation and source code disclosure for open source omitted from the open source notice
- Requests to provide missing files and build instructions for disclosed source code
- Copyright notice requests
- Enquiries related to known vulnerabilities or newly discovered vulnerabilities

The Open Source Program Manager creates an issue for the received request and records the response status in detail.

### (2) Investigation Notification

The Open Source Program Manager notifies the requester that the organization is faithfully carrying out open source license compliance and security assurance, and that the matter is under investigation. Updates on the internal investigation's progress are provided periodically.

### (3) Internal Investigation

The Open Source Program Manager conducts an internal investigation of the request. Using the SBOM and documented review history, the manager confirms whether the license compliance and security assurance processes were properly carried out for the supplied software. Where necessary, the manager consults the legal and security personnel.

If confirmation from a specific business unit is required, the Open Source Program Manager requests that unit to investigate. The business unit that receives the request immediately checks the compliance deliverables and security-related matters for any issues and reports the results.

### (4) Reporting to the Requester

The Open Source Program Manager completes the internal investigation within the specified response time and notifies the requester of the results.

- If the requester's enquiry was a misunderstanding, the manager explains this and closes the matter without further action.
- If an issue is confirmed, the manager informs the requester of the exact method and timing for fulfilling the relevant open source license obligation or resolving the security vulnerability.

### (5) Issue Remediation / Notification

If the internal investigation finds an actual license compliance or security issue, the relevant business unit carries out all the procedures necessary to resolve it.

### (6) Resolution Notification

After the issue is resolved, the requester is notified immediately and provided with the best available means of confirming that the issue has been resolved.

### (7) Process Improvement

If there was a license compliance or security issue, the case is reviewed in an OSRB meeting to understand how the issue occurred, and process improvements are established to prevent recurrence.


</div>



## 3.2.2 Effectively Resourced

To successfully operate an open source security assurance program, simply establishing policies and procedures is not enough. For these policies and procedures to be truly effective, the personnel, budget, and technical expertise needed for the program must be properly secured and allocated. This is critical for ensuring the program's sustainability and enabling it to respond effectively to a changing threat landscape.

### 3.2.2.1 Program Role Identification Document

> **ISO/IEC 18974**  
> - 4.2.2.1: Document with name of persons, group or function in program role(s) identified;
> - 4.2.2.1 Document with name of persons, group or function in program role(s) identified.
>   
> **Self-Certification Checklist**  
> - [ ] We have documented the people, group or functions related to the Program.
> - [ ] We have documented the people, group or functions related to the program.

The program role identification document is a cornerstone for the successful operation of an open source security assurance program. This document helps all stakeholders participating in the program clearly understand their respective roles and responsibilities, and enables efficient collaboration and communication. It also clarifies accountability, preventing confusion and the avoidance of responsibility that can otherwise occur during program operation.

#### Implementation Methods and Considerations

1. **Comprehensive Role Definition**:
    - Identify all roles needed to operate the program, and clearly define the objectives, responsibilities, and authority of each role.
    - Consider various roles, such as program manager, security expert, legal personnel, developer, and operations personnel.
2. **Responsibility Assignment**:
    - Designate a person in charge or team suited to each role, and clearly assign responsibility and authority.
    - The person in charge shall have the expertise and experience required for that role.
3. **Using a RACI Matrix (Optional)**:
    - A RACI (Responsible, Accountable, Consulted, Informed) matrix can be used to define the responsibilities of each role more clearly.
    - A RACI matrix clearly shows who is responsible, who is accountable, who is consulted, and who is informed for each task.
4. **Documentation**:
    - Document the role definitions, responsibility assignments, and the RACI matrix (optional) so that program participants can easily access them.
    - The document can be posted on the organization's internal wiki, a shared document repository, or other collaboration tools.
5. **Regular Review and Update**:
    - The program's role definitions may change with the organization's structure, operating methods, and technical environment.
    - Therefore, the role definition document shall be regularly reviewed and updated to keep it current.

#### Example

| Role | Responsibility | Description |
| --- | --- | --- |
| Open Source Program Manager (OSPM) | Overall program management | - Establish and manage open source policy<br>- Review and approve open source use requests<br>- Manage security vulnerabilities and license violations |
| Security Expert | Security vulnerability analysis and response | - Scan open source components for vulnerabilities<br>- Assess vulnerability severity and develop response plans<br>- Respond to security incidents |
| Legal Personnel | License compliance and legal risk management | - Review and analyze open source licenses<br>- Assess and manage legal risk<br>- Support dispute resolution |
| Development Team | Secure code development and open source use | - Comply with open source policy and guidelines<br>- Fix security vulnerabilities and apply patches<br>- Request review when using new open source components |

#### Implementation Considerations

- The document shall be written concisely and clearly, so that all program participants can easily understand it.
- The document's access permissions shall be properly managed to protect confidential information.
- The document shall be regularly reviewed and updated to keep it current.

#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 3.1 Role Descriptions

1. Open Source Program Manager (OSPM)
    - **Responsibility**: Overall responsibility for the company's open source program.
    - **Key Tasks**:
        - Manage open source license compliance and security assurance activities.
        - Create and maintain the SBOM.
        - Respond to external open source-related enquiries.
        - Manage internal best practices.
    - **Required Competence**: Understanding of software development processes, expertise in open source licensing, communication skills.
2. Legal Personnel
    - **Responsibility**: Assess legal risk related to open source licenses and provide advice.
    - **Key Tasks**:
        - Interpret and review open source license obligations.
        - Review license compatibility and provide advice on protecting intellectual property.
    - **Required Competence**: Expertise in software copyright, expertise in open source licensing, ability to assess legal risk.
3. IT Personnel
    - **Responsibility**: Operate and automate open source analysis tools.
    - **Key Tasks**:
        - Operate open source analysis tools and integrate them into the DevOps environment.
        - Create and maintain the SBOM.
    - **Required Competence**: Expertise in IT infrastructure, understanding of open source analysis tools, understanding of CI/CD pipelines.
4. Security Personnel
    - **Responsibility**: Operate open source security vulnerability analysis tools.
    - **Key Tasks**:
        - Respond to known vulnerabilities and newly discovered vulnerabilities.
        - Integrate with the DevSecOps environment and carry out security measures.
    - **Required Competence**: Understanding of DevSecOps, understanding of security vulnerability analysis tools, ability to assess and manage risk.
5. Development Culture Lead
    - **Responsibility**: Support internal developers in actively using open source.
    - **Key Tasks**:
        - Encourage participation in open source communities and improve development culture.
        - Support external contribution activities.
    - **Required Competence**: Understanding of software development processes, ability to design training, experience with community participation.
6. Quality Personnel
    - **Responsibility**: Confirm open source license obligations when distributing supplied software.
    - **Key Tasks**:
        - Confirm that compliance deliverables have been generated.
        - Review compliance with license obligations prior to distribution.
    - **Required Competence**: Understanding of software development processes, basic knowledge of compliance.
7. OSRB (Open Source Review Board)
    - **Responsibility**: Establish and improve policies and processes for open source management.
    - **Key Tasks**:
        - Regularly review and improve policy.
        - Discuss key issues and develop resolutions.
    - **Required Competence**: Expertise in policy development, experience operating a governing body.
8. OSPO (Open Source Program Office)
    - **Responsibility**: Support contributions to external open source projects and the release of internal projects.
    - **Key Tasks**:
        - Provide guidance for external contributions.
        - Manage the release process for internal projects.
    - **Required Competence**: Experience with community participation, project management ability.


</div>


### 3.2.2.2 Proper Staffing and Funding of Program Roles

> **ISO/IEC 18974**  
> - 4.2.2.2: The identified program roles have been properly staffed and adequate funding provided;
> - 4.2.2.2 The identified program roles have been properly staffed and adequate funding provided.
>   
> **Self-Certification Checklist**  
> - [ ] We have ensured the identified Program roles have been properly staffed and adequate funding has been provided.
> - [ ] We have ensured the identified program roles have been properly staffed and adequate funding has been provided.

No matter how well the program roles are defined, the program cannot operate properly if there is insufficient personnel to fill those roles or if the necessary funding is not properly provided. Therefore, the organization shall properly staff each role and provide sufficient funding for program operations. This is an essential condition for the successful operation of the program.

#### Implementation Methods and Considerations

1. **Developing a Staffing Plan**:
    - Accurately estimate the number of personnel needed for each role.
    - When estimating staffing needs, consider the scope of responsibility, workload, and required skill level for the role.
    - Forecast personnel needs from a long-term perspective, and develop a plan for hiring or reassigning internal personnel.
2. **Developing a Budget Plan**:
    - Identify all cost items needed to operate the program (personnel costs, training costs, tool purchase costs, consulting costs, etc.) and estimate the budget for each item.
    - The budget shall be estimated on a well-founded basis so that it can realistically be executed.
    - Develop a plan for securing the budget and obtain management approval.
3. **Securing and Allocating Resources**:
    - Secure the necessary personnel through hiring or the reassignment of internal personnel.
    - Appropriately allocate the secured budget across each item.
    - When allocating resources, consider the program's priorities and objectives.
4. **Regular Review and Adjustment**:
    - Regularly review the adequacy of the staffing and budget plan, and adjust it as needed.
    - Update the plan considering program operation status, budget execution status, and changes in the external environment.

#### Example

- **Personnel**:
    - Hire two open source security experts for the security team to handle vulnerability analysis and response for open source components.
    - Designate one open source license expert on the legal team to support legal review when using open source.
- **Budget**:
    - Allocate an annual budget of KRW 50 million for purchasing open source security tools (SCA, SAST, etc.).
    - Allocate an annual budget of KRW 10 million for running the open source security training program.
    - Allocate an annual budget of KRW 20 million for external security consulting costs.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 3.2 Staffing and Funding

1. Proper Staffing:
    - Assign appropriate personnel with the required competence and expertise to each role.
    - The head of each department shall designate a suitable person in charge who can perform that role.
2. Sufficient Funding:
    - The company provides sufficient budget and resources needed to perform each role.
    - Budget items include training, tool usage fees, and external consulting costs.
3. Regular Review:
    - The OSRB reviews the staffing and funding status of each role at least once a year and recommends adjustments where necessary.
    - The review results are documented and reported to the OSPO (Open Source Program Office).
4. Issue Resolution Procedure:
    - If the person in charge of a department finds that the required support (personnel or funding) is insufficient, they shall immediately report this to the Open Source Program Manager.
    - The Open Source Program Manager cooperates with the relevant department to resolve the issue, and requests the OSRB to resolve it where necessary.

### 10.5 Personnel and Resource Assessment

1. Assessment Cycle:
    - The company assesses the staffing and funding status of each role at least once a year.
    - The assessment results are reported to the OSRB, and improvements are implemented where necessary.
2. Assessment Items:
    - Whether the personnel needed for each role have been properly staffed.
    - Whether the budget needed to perform each role has been sufficiently provided.
    - Cases of issues caused by insufficient support and their resolutions.
3. Developing an Improvement Plan:
    - Based on the assessment results, develop a specific plan to make up for any shortage of personnel or resources.
    - The improvement plan is executed upon approval by the OSRB.


</div>


### 3.2.2.3 Identifying Expertise to Resolve Known Vulnerabilities

> **ISO/IEC 18974**  
> - 4.2.2.3: Identification of expertise available to address identified known vulnerabilities;
> - 4.2.2.3 Identification of expertise available to address identified known vulnerabilities.
>   
> **Self-Certification Checklist**  
> - [ ] We have ensured expertise available is to address identified Known Vulnerabilities;
> - [ ] We have ensured expertise available is to address identified known vulnerabilities.

When a known vulnerability is discovered in an open source component, personnel with expertise in that vulnerability are needed to resolve it quickly and effectively. This expertise can be secured from internal personnel or obtained with the help of external experts. What matters is building a system that can secure and apply the necessary expertise in a timely manner.

#### Implementation Methods and Considerations

1. **Identifying the Required Areas of Expertise**:
    - Identify the technical areas of expertise needed to operate the program.
    - Examples: web security, cryptography, network security, systems administration, and open source licensing.
    - Clearly define the level of knowledge and experience required for each area of expertise.
2. **Compiling a List of Internal Experts**:
    - Compile a list of personnel within the organization who have knowledge and experience in the relevant areas of expertise.
    - Record each expert's area of expertise, career background, and contact information.
    - The expert list shall be kept up to date.
3. **Planning for External Resources**:
    - Develop a plan to use external experts or consulting firms in preparation for issues that are difficult to resolve internally.
    - Secure trustworthy external resources and clearly define the contract terms.
4. **Establishing an Access Procedure**:
    - Establish a procedure so that program participants can easily access the expertise they need.
    - Examples: how to consult an internal expert, how to use an external consulting firm.
    - Document the access procedure so that all program participants are familiar with it.

#### Specific Examples

- **Vulnerability Analysis**:
    - If a SQL injection vulnerability is found in a specific open source component, a web security expert is asked to analyze it and identify the attack path and scope of impact.
- **Licensing**:
    - If interpretation of the obligations of a specific open source license is needed, an open source license expert is asked to conduct a legal review.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 6.5 Identifying and Utilizing Expertise

1. Identifying the Required Areas of Expertise:
    - Regularly identify the technical and legal areas of expertise needed to operate the program.
    - Examples: web security, cryptography, network security, systems administration, open source license interpretation, and the like.
2. Compiling and Updating the List of Internal Experts:
    - Compile a list of personnel within the company who have expertise in the relevant fields, and update it regularly.
    - Record each expert's career background, certifications, and contact information.
3. Developing a Plan for Securing External Resources:
    - Develop a plan to use external experts or consulting firms in preparation for issues that are difficult to resolve internally.
    - Secure trustworthy external resources and clearly define the contract terms.
4. Establishing an Expertise Access Procedure:
    - Establish a procedure so that program participants can easily access the expertise they need.
    - Examples: how to consult an internal expert, how to use an external consulting firm.


</div>


### 3.2.2.4 Procedure for Assigning Internal Responsibility for Security Assurance

> **ISO/IEC 18974**  
> - 4.2.2.4: A documented procedure that assigns internal responsibilities for security assurance.
> - 4.2.2.4 A documented procedure that assigns internal responsibilities for security assurance.
>   
> **Self-Certification Checklist**  
> - [ ] We have a documented procedure that assigns internal responsibilities for Security Assurance.
> - [ ] We have a documented procedure that assigns internal responsibilities for security assurance.

A procedure is established to clearly assign internal responsibility for the effective operation of the open source security assurance program. This procedure is as follows:

1. Party Responsible for Assignment:
    - The Open Source Program Manager (OSPM) leads the internal responsibility assignment procedure.
2. Assignment Procedure:
    - The OSPM convenes an annual responsibility assignment meeting.
    - The OSPM consults with each department head (legal, IT, security, development, quality, etc.) to select a person responsible for each security assurance activity.
    - The list of selected persons in charge is submitted to the OSRB (Open Source Review Board) for final approval.
3. Documentation:
    - The approved responsibility assignment results are drawn up as an official document.
    - The document specifies each security assurance activity, the person responsible, their role, and the required competence.
    - The completed document is registered in the company's document management system and version-controlled.
4. Assignment Criteria:
    - Define the skills and experience required for each role, and select suitable personnel accordingly.
    - Link responsibility performance to performance evaluations to provide motivation.
5. Regular Review and Renewal:
    - Review the status of responsibility assignments at least once a year and adjust as needed.
    - Update immediately whenever there is a major change, such as an organizational restructuring or personnel transfer.
6. Training and Awareness:
    - Provide the necessary training to newly assigned persons in charge.
    - Share the responsibility assignment results with the entire organization to raise awareness.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 3.3 Internal Responsibility Assignment Procedure

1. Assignment Procedure:
    - a. The Open Source Program Manager (OSPM) convenes an annual responsibility assignment meeting.
    - b. The OSPM consults with each department head (legal, IT, security, development, quality, etc.) to select a person responsible for each activity.
    - c. The list of selected persons in charge is submitted to the OSRB (Open Source Review Board) for final approval.
    
2. Balance of Responsibility and Authority:
    - Each person in charge is granted the appropriate authority needed to perform their duties.
    - They have the authority to request the resources (e.g., budget, personnel) needed to fulfill their responsibilities.
3. Regular Review and Update:
    - The OSRB reviews the status of responsibility assignments at least once a year and adjusts as needed.
    - Responsibility assignments are updated immediately whenever there is a major change, such as an organizational restructuring or personnel transfer.
4. Documentation:
    - The responsibility assignment results are drawn up as an official document and registered in the company's document management system.
    - The document specifies each activity, the person responsible, their role, and the required competence.
5. Training and Awareness:
    - Provide the necessary training to newly assigned persons in charge.
    - Share the responsibility assignment results with the entire organization to raise awareness.


</div>
