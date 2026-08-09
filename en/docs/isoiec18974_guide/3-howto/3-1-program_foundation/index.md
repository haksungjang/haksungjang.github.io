# 3.1 Program Foundation

LLMS index: [llms.txt](/llms.txt)

---

The core of the ISO/IEC 18974 standard is building a systematic foundation for an organization to safely manage open source software. This foundation encompasses not only technical aspects but also various factors such as organizational culture, policy, and workforce competence. The 3.1 Program Foundation chapter explains in detail the essential elements for building this foundation.

## 3.1.1 Policy

An open source software security assurance policy is a core document for an organization to use open source safely and effectively. This policy guides all members of the organization to take responsibility for open source use, understand the associated risks, and comply with the required procedures. Therefore, the policy should be written in clear, easy-to-understand language and managed so that all members of the organization can easily access it.

### 3.1.1.1 Documented Open Source Software Security Assurance Policy

> **ISO/IEC 18974**
> - 4.1.1.1: A documented open source software security assurance policy
>
> **Self-Certification Checklist**
> - [ ] We have a documented policy governing the open source security assurance of Supplied Software.

A documented open source software security assurance policy is the core document that provides an organization's formal guidance on open source use. This policy presents the standards for all members of the organization to safely use and manage open source, and helps minimize legal and security risks.


#### Example Policy Content

- Open source usage approval procedure: Clearly defines the review and approval procedure required before using open source.
- SBOM (Software Bill of Materials) management: Specifies how to generate and manage the list of open source components.
- Vulnerability management: Defines the procedure for detecting and responding to vulnerabilities in open source components.
- License compliance: Provides guidance for complying with open source license terms.
- Contribution policy: Presents guidelines on how the organization contributes to open source projects.
- Exception handling procedure: Defines the procedure for handling exceptional situations where complying with the policy is difficult.

The policy should be tailored to the size and characteristics of the organization. For example, a large organization may need a more detailed and complex policy, while a small organization may prefer a more concise and flexible policy.

In addition, the policy should be reviewed and updated regularly, and should reflect the latest laws and security threat trends.

This guide provides an open source policy template that satisfies all ISO/IEC 18974 requirements: [Open Source Policy Template](../../../templates/1-policy/)

### 3.1.1.2 Documented Procedure to Make Program Participants Aware of the Security Assurance Policy

> **ISO/IEC 18974**
> - 4.1.1.2: A documented procedure to make program participants aware of the security assurance policy.
>
> **Self-Certification Checklist**
> - [ ] We have a documented procedure to communicate the existence of the open source policy to all Software Staff.

No matter how well a policy is written, it cannot be effective if members of the organization are unaware of its existence or do not understand its content. Therefore, an organization must establish a documented procedure to effectively communicate the security assurance policy to all program participants.

#### Example Procedures

- New employee training: Mandatory open source policy training is provided to new employees.
- Regular training: Regular training on the open source policy (e.g., once a year) is conducted for existing employees.
- Policy publication: The policy document is posted on an internal wiki, portal, or other accessible location.
- FAQ: An FAQ document summarizing questions and answers about the policy is provided.
- Newsletter: The latest open source information and policy changes are shared through a newsletter.
- Awareness campaigns: Awareness campaigns emphasizing the importance of open source security are conducted regularly.

Training should not simply convey the policy content, but should be conducted in a way that encourages participants' engagement and improves their understanding through actual case studies, workshops, quizzes, and similar activities. In addition, training materials should use visual elements to improve readability and be provided in a way that suits various learning styles.

#### Example Improvement Plan

- Improve the training program: Update the training content to reflect the latest trends and real-world cases, and strengthen participatory learning elements.
- Strengthen communication channels: Use internal communication channels to continuously share policy-related information and provide answers to questions.
- Expand awareness campaigns: Expand awareness campaigns that emphasize the importance of open source security, and encourage participation through various events.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


## 6. Training and Awareness

This section describes the training and awareness activities required to ensure the competence and awareness of program participants. Through this, participants can fully understand the open source policy, related program objectives, and their own roles and responsibilities, and raise their awareness of open source license compliance and security assurance.

### 6.1 Open Source Training

1. Training objectives:
    - Helps program participants correctly utilize open source, understand license compliance and security assurance procedures, and apply them in practice.
    - Key training content:
        - The purpose and principles of the open source policy.
        - License obligations and compliance procedures.
        - How to generate and use an SBOM.
        - Procedures for managing Known Vulnerabilities and newly discovered vulnerabilities.
2. Training methods:
    - Completed through online courses provided on the [Learning Portal].
    - Additional training in the form of workshops or seminars is provided as needed.
    - Case-based learning is used to strengthen practical problem-solving skills.



</div>


## 3.1.2 Competence

The success of an open source software security assurance program depends heavily on the competence of the members participating in the program. Clearly defining the competencies required for each role and supporting members in acquiring those competencies is essential to raising an organization's level of open source security.

### 3.1.2.1 Documented List of Roles and Responsibilities

> **ISO/IEC 18974**
> - 4.1.2.1: A documented list of roles with corresponding responsibilities for the different program participants;
>
> **Self-Certification Checklist**
> - [ ] We have identified the roles and responsibilities that affect the performance and effectiveness of the Program.

Clearly defining and documenting the roles and responsibilities of all members participating in the open source security assurance program is the first step toward effective program operation. Only when each member clearly understands their own role and responsibilities can effective collaboration be achieved to reach the program's objectives.

#### Implementation Methods and Considerations

- **Comprehensive role definition**: Define all roles participating in the program, such as program manager, legal counsel, security expert, and developer.
- **Clear specification of responsibilities**: Specify concretely, for each role, the tasks to be performed, decision-making authority, information-sharing obligations, and so on.
- **Reflecting the organizational structure**: The definition of roles and responsibilities should reflect the organization's structure and culture.
- **Regular review**: Review and revise the definition of roles and responsibilities regularly in response to organizational changes, program updates, and the like.

#### Example (Based on Personnel Assignments) - Sample Roles and Responsibilities Document:

| Role | Key Responsibilities | Detailed Responsibilities |
| --- | --- | --- |
| Open Source Program Manager | Overall management of the open source program | - Policy establishment and management<br>- Budget management<br>- Performance measurement |
| Legal | Legal review and license management | - License compliance review<br>- Legal risk assessment<br>- Dispute resolution |
| IT | Operation of analysis tools and system setup | - Installation and maintenance of analysis tools<br>- Preparation of analysis result reports |
| Security | Vulnerability analysis and security hardening | - Vulnerability scanning and assessment<br>- Development of response plans<br>- Security training |
| Development team | Secure code development and policy compliance | - Policy compliance<br>- Code quality management<br>- Security vulnerability remediation |

See [Open Source Policy Template Appendix 1. Personnel Assignments](../../../templates/1-policy/Appendix/#appendix-1-personnel-assignments) for detailed examples.

### 3.1.2.2 Document Defining the Competencies Required for Each Role

> **ISO/IEC 18974**
> - 4.1.2.2: A document that identifies the competencies for each role;
>
> **Self-Certification Checklist**
> - [ ] We have identified and documented the competencies required for each role.

Defining the competencies required for each role is essential for placing the right people and developing the necessary education and training programs. Competency definitions should include not only technical knowledge but also non-technical competencies such as problem-solving ability, communication skills, and collaboration ability.

#### Implementation Methods and Considerations

- **Concrete competency definitions**: Specify concretely the knowledge, skills, experience, certifications, and the like required for each role.
- **Measurable criteria**: Present measurable criteria that can be used to assess the level of competence.
- **Regular assessment**: Regularly assess members' competence levels and provide necessary education and training opportunities.
- **Reflecting the latest information**: Continuously update competency requirements as new technologies or threats emerge.

#### Example (Based on Personnel Assignments) - Sample Required Competencies by Role

| Role | Required Competencies | Competency Assessment Method |
| --- | --- | --- |
| Open Source Program Manager | - Understanding of open source licenses<br>- Understanding of the software development process<br>- Risk management ability<br>- Communication skills | - Verify completion of related training<br>- Assess project participation experience<br>- Assess communication skills |
| Legal | - Legal knowledge such as copyright law and contract law<br>- Expert knowledge of open source licenses<br>- Legal risk assessment ability | - Verify attorney qualification<br>- Verify completion of related training<br>- Assess legal review reports |
| IT | - IT infrastructure operation experience<br>- Ability to use security tools<br>- Ability to write automation scripts | - Verify related certifications<br>- Assess system operation experience<br>- Assess script-writing ability |
| Security | - Security vulnerability analysis ability<br>- Incident response ability<br>- Experience using security tools | - Verify information security-related certifications<br>- Assess vulnerability analysis reports<br>- Assess incident response experience |
| Development team | - Open source use and contribution experience<br>- Secure coding skills<br>- Security vulnerability remediation ability | - Code review results<br>- Security test results<br>- Project participation history |

See [Open Source Policy Template Appendix 1. Personnel Assignments](../../../templates/1-policy/Appendix/#appendix-1-personnel-assignments) for detailed examples.

Through this approach, an organization can secure personnel suited to each role and strengthen members' competence through continuous education and training.

### 3.1.2.3 List of Participants and Their Roles

> **ISO/IEC 18974**
> - 4.1.2.3: List of participants and their roles;
>
> **Self-Certification Checklist**
> - [ ] We have identified and documented a list of Program Participants and how they fill their respective roles.

Maintaining a list that clearly records the names and roles of all members participating in the open source security assurance program is essential for clarifying accountability and building an efficient communication system. This list improves the transparency of program operations and supports a rapid response when an emergency occurs.

#### Implementation Methods and Considerations

- **Keeping information current**: If the list of participants changes due to organizational restructuring, personnel changes, or the like, it should be updated immediately.
- **Access permission management**: Manage access permissions to the participant list appropriately to maintain information security.
- **Accuracy of information**: Accurately record and manage participant names, roles, contact information, and the like.

#### Example (Based on Personnel Assignments) - Sample List of Participants and Roles

| Name | Role | Department | Contact |
| --- | --- | --- | --- |
| Cheolsu Kim | Open Source Program Manager | Information Security Team | [cheolsu.kim@example.com](mailto:cheolsu.kim@example.com) |
| Younghee Lee | Legal | Legal Team | [younghee.lee@example.com](mailto:younghee.lee@example.com) |
| Sunyoung Park | Security Engineer | Information Security Team | [sunyoung.park@example.com](mailto:sunyoung.park@example.com) |
| Minho Choi | Development Team Lead | Development Team 1 | [minho.choi@example.com](mailto:minho.choi@example.com) |

See [Open Source Policy Template Appendix 1. Personnel Assignments](../../../templates/1-policy/Appendix/#appendix-1-personnel-assignments) for detailed examples.

### 3.1.2.4 Documented Evidence of Assessed Competence for Each Participant

> **ISO/IEC 18974**
> - 4.1.2.4: Documented evidence of assessed competence for each program participant;
>
> **Self-Certification Checklist**
> - [ ] We have documented the assessed competence for each Program Participant.

Assessing whether the competencies required for each role are actually held is very important for ensuring the effectiveness of the program. Competency assessment should go beyond simply checking whether a certification is held, and should comprehensively assess actual job performance ability, problem-solving ability, and adaptability to change.

#### Implementation Methods and Considerations

- **Use a variety of assessment methods**: Assess competence using a variety of methods, such as written exams, practical assessments, interviews, and 360-degree evaluations.
- **Conduct regular assessments**: Assess competence regularly, at least once a year, and provide additional education or training opportunities as needed.
- **Utilize assessment results**: Reflect assessment results in individual competency development plans, compensation, promotion, and the like.

#### Example (Based on Personnel Assignments) - Sample Competence Assessment Results

| Name | Role | Assessment Item | Assessment Result | Improvement Plan |
| --- | --- | --- | --- | --- |
| Cheolsu Kim | Open Source Program Manager | Understanding of open source licenses | High | - |
|  |  | Risk management ability | Medium | Complete risk management training |
| Younghee Lee | Legal | Copyright law knowledge | High | - |
|  |  | Open source license analysis ability | Medium | Complete specialized open source license training |
| Sunyoung Park | Security Engineer | Vulnerability analysis ability | High | - |
|  |  | Incident response ability | Medium | Participate in incident response simulation |
| Minho Choi | Development Team Lead | Secure coding skills | Medium | Complete secure coding guideline training |
|  |  | Security vulnerability remediation ability | Medium | Participate in code review and security vulnerability remediation practice |

#### Example Improvement Plan

- **Develop competency-strengthening programs**: Develop and operate education, training, and mentoring programs to strengthen the competencies required for each role.
- **Support certification acquisition**: Encourage the acquisition of related certifications and provide necessary support, such as exam fee support and study materials.
- **Provide career development opportunities**: Support members in gaining practical experience by providing opportunities to participate in various projects.

#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 6.2 Competence Assessment

1. Assessment criteria:
    - Assess the competencies required for each role.
    - Assessment items:
        - Understanding of the open source policy.
        - Ability to carry out compliance procedures.
        - Ability to manage security vulnerabilities.
2. Assessment methods:
    - Measure participants' competence through regular tests and practical assessments.
    - Assessment results are reflected in individual performance records, and additional training is provided as needed.


### 6.4 Record Keeping

1. Training and assessment records:
    - All training completion records and assessment results are retained for at least three years.
    - This makes it possible to demonstrate that program participants sufficiently understand the policy and processes.
2. Regular review and update:
    - The Open Source Program Manager reviews the training content and assessment methods at least once a year and updates them as needed to reflect the latest open source trends and the organization's requirements.


</div>


### 3.1.2.5 Recording Process Reviews and Changes

> **ISO/IEC 18974**
> - 4.1.2.5: Documented evidence of periodic reviews and changes made to the process;
>
> **Self-Certification Checklist**
> - [ ] We have a way to document periodic reviews and changes made to our processes.

An open source security assurance program must be continuously improved to keep pace with an ever-changing threat landscape and technology trends. To this end, an organization must build a system for periodically reviewing roles and responsibilities, competency requirements, and the like, and applying changes as needed. These reviews and changes must be documented and managed, and it must be possible to verify the program's progress through change history tracking.

#### Implementation Methods and Considerations

- **Set a regular review cycle**: Conduct reviews at least once a year, or as needed from time to time. The review cycle is determined by considering the organization's characteristics, the scale of open source use, the frequency of security threats, and the like.
- **Define the review scope**: Clearly define the review scope, including role and responsibility definitions, competency requirements, training programs, and assessment methods.
- **Establish a review procedure**: Document a review procedure that includes the purpose of the review, participants, review method, and result reporting.
- **Manage changes**: Record changes made based on review results in detail, specifying the reason for the change, the content of the change, and the timing of application.
- **Manage history**: Systematically manage the change history so that past decisions and the current state can be compared and analyzed.

#### Sample Evidence

- Process review meeting minutes: Record in detail the meeting attendees, discussion content, and decisions made.
- Change report: Specify the reason for the change, the content of the change, and the roles and processes affected.
- Updated policy document: Kept up to date to reflect changes.
- Process improvement proposal: Record proposed content for program improvement and document the review results.
- Competency assessment result analysis report: Analyze competency assessment results and use them to improve training programs.

**Sample Table: Process Review and Change Record**

| Review Date | Review Item | Content Before Change | Content After Change | Reason for Change | Owner |
| --- | --- | --- | --- | --- | --- |
| 2025-01-15 | Role and responsibility definition | Security team: Vulnerability analysis and response | Security team: Vulnerability analysis, response, and prevention | Strengthen security incident prevention | Cheolsu Kim |
| 2025-01-15 | Competency requirements | Development team: Perform code review | Development team: Code review and completion of secure coding training | Strengthen secure code development competence | Minho Choi |
| 2025-07-20 | Training program | Open source license training (1 hour) | Open source license and security training (2 hours) | Raise awareness of license and security risks | Younghee Lee |

#### Example Improvement Plan

- **Build an automated change management system**: Introduce a system that automates change tracking, approval workflow management, and history management.
- **Conduct regular audits**: Conduct regular audits to assess process compliance and effectiveness.
- **Expand stakeholder participation**: Involve various stakeholders (developers, security experts, legal counsel, and the like) in the review process to gather diverse opinions.
- **Collect continuous feedback**: Collect feedback from program participants and reflect it in process improvement.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


## 10. Measuring and Improving Program Effectiveness

This section describes the procedures for measuring and continuously improving the effectiveness of the open source program. Through this, the company can assess and improve the performance of its open source license compliance and security assurance program.

### 10.1 Defining Performance Indicators

1. List of performance indicators:
    - Number of Supplied Software analyzed.
    - Number of Known Vulnerabilities and newly discovered vulnerabilities resolved.
    - Number of compliance deliverables created and distributed.
    - Response time to external inquiries.
    - Training completion rate of program participants.
    - Number of external open source contributions and public projects.
2. Setting indicator targets:
    - Set target values for each indicator so that the program's performance can be assessed.
    - Target values are set in line with the organization's business objectives and the program's purpose.

### 10.2 Regular Program Assessment

1. Assessment cycle:
    - Conduct a program assessment at least once a year.
    - Conduct additional assessments as needed in response to changes in the business environment or major issues.
2. Assessment procedure:
    - Document the assessment results and report them to the OSRB (Open Source Review Board).
    - Collect and reflect feedback from program participants during the assessment process.
    - Assessment results are recorded and retained through an internal system (e.g., the Jira Issue Tracker).
3. Regular policy review and renewal:
    - The policy is reviewed regularly and renewed as needed to reflect the latest open source trends and the organization's requirements.
    - This continuously improves the effectiveness of the program.

### 10.3 Continuous Improvement Plan

1. Identify areas for improvement:
    - Identify areas requiring improvement based on the assessment results and set priorities.
    - Areas requiring improvement may include process efficiency, training content, response time, and the like.
2. Set improvement targets:
    - Set specific improvement targets and schedules.
    - The progress of improvement activities is monitored and documented.
3. Reflect improvement results:
    - Reflect improvement results in the next assessment cycle to continuously enhance the program's effectiveness.
    - Improvement results are shared with program participants to encourage continued commitment to improvement.


</div>



### 3.1.2.6 Verifying Alignment with Company Internal Best Practices

> **ISO/IEC 18974**
> - 4.1.2.6: Documented verification that these processes are current with company internal best practices and who is assigned to accomplish them.
>
> **Self-Certification Checklist**
> - [ ] We have a way to verify that our processes align with current company best practices and staff assignments.

To maximize the effectiveness of the open source security assurance program, it is important that the way the program is operated remains consistent with other security-related activities and best practices within the company. This helps the program integrate with the organization's overall security strategy to create synergy and avoid unnecessary duplication.

#### Implementation Methods and Considerations

- **Survey internal best practices**:
    - Survey security-related activities or processes that other teams or departments in the organization are operating successfully.
    - Example: the information security team's security vulnerability management process, the development team's secure coding guidelines, and the like.
- **Compare and analyze processes**:
    - Compare and analyze the surveyed best practices against how the open source security assurance program is operated.
    - Identify strengths, weaknesses, and opportunities for improvement.
- **Integrate and improve processes**:
    - Adjust the open source security assurance program to align with the company's internal best practices.
    - Example: applying the company-wide vulnerability management system to open source vulnerability management as well, conducting open source code reviews in accordance with internal coding conventions, and the like.
- **Assign and manage an owner**:
    - Assign an owner responsible for compliance with internal best practices and clarify that role.
    - The owner regularly reviews how the program is operated and proposes improvements.

#### Sample Evidence

- Best practice survey report: Record in detail the survey targets, survey method, and analysis results.
- Process comparison and analysis report: Clearly present strengths, weaknesses, and opportunities for improvement.
- Process improvement plan: Specify concrete improvement targets, an implementation plan, and an assessment method.
- Owner assignment document: Clearly define the owner's name, role, and responsibilities.

**Sample Table: Verifying Alignment with Company Internal Best Practices**

| Check Item | Description | Compliant | Improvement Plan |
| --- | --- | --- | --- |
| Vulnerability management process | Consistency with the company-wide vulnerability management process | Yes | - |
| Code review procedure | Compliance with internal code review guidelines | Yes | - |
| Access control policy | Compliance with the internal access control policy | No | Strengthen access control for open source-related systems |
| Security training program | Participation in the company-wide security training program | No | Add open source-related training content |

#### Example Improvement Plan

- **Strengthen the security training program**: Include open source security content in the company-wide security training program and expand the training audience and hours.
- **Strengthen the access control policy**: Minimize access permissions to open source-related systems and conduct regular access permission reviews.
- **Integrate audit processes**: Integrate audits of open source-related activities into the company-wide audit process, conduct audits regularly, and derive improvements.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 3.1 Role Descriptions

1. Open Source Program Manager (OSPM)
    - **Responsibility**: Overall responsibility for the company's open source program.
    - **Key duties**:
        - Manage open source license compliance and security assurance activities.
        - Create and maintain the SBOM.
        - Respond to external open source-related inquiries.
        - Manage internal best practices.

### 5.4 Verifying Alignment with Internal Best Practices

1. Survey internal best practices:
    - Survey security-related activities and processes that other teams or departments in the company are operating successfully.
    - Example: the information security team's vulnerability management process, the development team's secure coding guidelines, and the like.
2. Compare and analyze processes:
    - Compare and analyze how the surveyed best practices and the open source security assurance program are operated.
    - Identify differences, weaknesses, and opportunities for improvement.
3. Integrate and improve processes:
    - Adjust or integrate the open source security assurance program to align with the company's internal best practices.
    - Example: applying the company-wide vulnerability management system to open source vulnerability management as well.
4. Assign and manage an owner:
    - The OSPM is responsible for compliance with internal best practices, regularly reviews the way the program is operated, and proposes improvements.

### 10.4 Integrating and Improving Internal Best Practices

1. Integration activity planning:
    - Identify gaps between internal best practices and the open source security assurance program, and develop an integration plan based on them.
    - Example: integrating vulnerability management systems, standardizing code review procedures.
2. Regular review and update:
    - Review alignment between internal best practices and the open source program at least once a year, and reflect improvements as needed.
    - The review results are reported to the OSRB (Open Source Review Board).


</div>


Through this approach, an organization can align its open source security assurance program with the company's internal best practices, thereby increasing the program's effectiveness and raising the organization's overall level of security.

## 3.1.3 Awareness

For an open source security assurance program to operate successfully, raising the awareness of program participants is essential. Program participants must clearly understand the organization's open source policy, the program's objectives, and their own roles and responsibilities. They must also be fully aware of the impact that can result from failing to comply with the program's requirements.

### 3.1.3.1 Documented Evidence of Assessed Awareness of Program Participants

> **ISO/IEC 18974**
> - 4.1.3.1: Documented evidence of assessed awareness for the program participants - which should include the program's objectives, one's contribution within the program, and implications of program non-conformance.
>
> **Self-Certification Checklist**
> - We have documented the awareness of our Program Participants on the following topics:
>   - [ ] The open source security assurance policy and where to find it;
>   - [ ] Relevant open source objectives;
>   - [ ] Contributions expected to ensure the effectiveness of the Program;
>   - [ ] The implications of failing to follow the Program requirements.

To confirm whether program participants are sufficiently aware of open source-related policies and procedures and the importance of security, an organization must conduct regular assessments and document the results. Such assessments can be used to measure the program's effectiveness and, if necessary, improve the training program.

#### Implementation Methods and Considerations

- **Use a variety of assessment methods**:
    - **Multiple-choice exams**: Assess knowledge related to the open source policy, licenses, and security.
    - **Case studies**: Present scenarios that could actually occur and have participants choose an appropriate response.
    - **Surveys**: Gather program participants' opinions on their level of awareness, satisfaction, and areas for improvement.
- **Structure of assessment content**:
    - **Policy understanding**: Assess understanding of the purpose, scope of application, and key content of the open source policy.
    - **License understanding**: Assess understanding of the major types of open source licenses and their obligations.
    - **Security vulnerability response procedure**: Assess understanding of the reporting and handling procedure when a vulnerability is found.
    - **Contribution method**: Assess understanding of the procedures and guidelines for contributing to open source projects.
- **Analysis of assessment results**:
    - Analyze the assessment results to identify the strengths and weaknesses of program participants.
    - Provide additional education or training for areas of weakness.
- **Use of assessment results**:
    - Improve the training program: Supplement the training content and improve the training method based on the assessment results.
    - Improve processes: Improve the open source management process based on the assessment results.

#### Sample Evidence

- Training program materials: Specify the training content, audience, and schedule.
- Assessment methods: Include exam papers, questionnaires, case study materials, and the like.
- Assessment result report: Include assessment scores, analysis content, and an improvement plan.
- List of training attendees: Record the names and signatures of the people who participated in the training.

#### Example (Based on Personnel Assignments)

| Assessment Item | Description | Assessment Method | Assessment Timing | Owner |
| --- | --- | --- | --- | --- |
| Understanding of the open source policy | Purpose, scope of application, key content of the policy | Multiple-choice exam, essay questions | At onboarding, once a year | OSPO, Legal Team |
| Understanding of open source licenses | Major license types and obligations | Case analysis, role-play | At onboarding, once a year | Legal Team |
| Security vulnerability response procedure | Reporting and handling procedure when a vulnerability is found | Simulation, workshop | Once a year | Security Team |
| Contribution method | Procedures and guidelines for contributing to open source projects | Project participation report | At the time of project participation | Development Team |

#### Example Improvement Plan

- **Diversify training content**: Develop training content in a variety of formats, such as videos, infographics, and games, to increase participation.
- **Provide customized training**: Provide customized training focused on the knowledge and skills required for each role.
- **Build a feedback system**: Collect feedback on the training program and reflect it in improvements.
- **Introduce a reward system**: Provide rewards to people who contribute to open source security to motivate them.


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 1.1 Purpose

This policy provides the principles and procedures for the company to use open source software safely and effectively. The main purposes of the policy are as follows:

1. Open source license compliance:
    - Comply with the license obligations of the open source components included in Supplied Software and meet related legal requirements.
2. Open source security assurance:
    - Identify security vulnerabilities in the open source components included in Supplied Software and minimize security risk through appropriate response measures.
3. Contribution to external open source projects:
    - Promote collaboration with the open source community by contributing to external open source projects, and protect the company's intellectual property.
4. Open-sourcing internal projects:
    - Promote collaboration with the open source community by releasing internal projects as open source, and promote the company's technical capabilities.

These principles are designed to satisfy the requirements of ISO/IEC 5230 (open source license compliance) and ISO/IEC 18974 (open source security assurance).

### 1.2 Impact of Non-Compliance

If this policy is not complied with, the company may face the following risks:

- Legal risk: The company may receive external demands for open source license compliance, with the risk of litigation or fines.
- Reputational damage: The company's reputation may be damaged due to source code disclosure obligations or security incidents.
- Business loss: Relationships with customers or suppliers may deteriorate due to breach of contract.
- Security incidents: Serious security incidents may occur due to Known Vulnerabilities or newly discovered vulnerabilities.

### 1.3 How Program Participants Can Contribute

All program participants at the company must understand and comply with this policy. Participants can contribute in the following ways:

- Carry out the responsibilities and obligations defined in the policy according to their role.
- Complete open source license and security-related training and apply it in practice.
- Immediately report any problem discovered that impedes policy compliance.


</div>


Through this approach, an organization can raise the awareness level of program participants and contribute to spreading an open source security culture.

## 3.1.4 Program Scope

Clearly defining the scope of the open source security assurance program is very important for efficiently allocating the organization's resources and effectively achieving the program's objectives. The scope of the program should be carefully determined by considering the organization's size, business characteristics, and the scale of open source use.

### 3.1.4.1 Written Statement Clearly Defining the Scope and Limits of the Program

> **ISO/IEC 18974**
> - 4.1.4.1: A written statement that clearly defines the scope and limits of the program;
>
> **Self-Certification Checklist**
> - [ ] We have a written statement clearly defining the scope and limits of the Program.

A written statement that clearly defines the scope and limits of the program contributes to preventing confusion and clarifying accountability by clearly distinguishing what the program applies to and what it does not. This statement must remain consistent with the program's objectives and be written so that all members of the organization can easily understand it.

#### Implementation Methods and Considerations

- **Comprehensive definition**: Clearly list all the targets to which the program applies (e.g., all software projects, specific teams, specific product lines, specific technology stacks).
- **Clear exceptions**: Specifically state the exceptions to which the program does not apply. Example: open source used only for internal testing, personal projects, and the like.
- **Possibility of scope adjustment**: State that the scope of the program can be adjusted according to changes in the organization's circumstances, and briefly describe the scope adjustment procedure.

#### Example (Considering Organization Size and Business Characteristics)

- **Large organization**:
    - Scope of application: "Applies to open source components included in all software projects developed, deployed, or used by all business units of the company."
    - Exception: "However, open source used only for research and development purposes may be excluded from the scope of this program. In this case, prior approval from the OSPO is required."
- **Small organization**:
    - Scope of application: "Applies to open source components included in the company's flagship products."
    - Exception: "Open source used in internal management systems is excluded from the scope of this program."

#### Sample Table: Program Scope Definition

| Category | Content |
| --- | --- |
| In scope | 1. All software the company distributes externally<br>2. All services provided in the form of cloud services<br>3. All software development kits (SDKs) provided to customers |
| Out of scope | 1. Open source used only in internal development and test environments<br>2. Open source used for personal purposes |
| Related departments | Development team, QA team, Security team, Legal team, OSPO |


#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 1.4 Scope of Application

This policy applies to all software projects the company develops, deploys, or uses. The main scope of application is as follows:

- All Supplied Software provided or distributed externally.
- Activities contributing to external open source projects.
- Activities that release internal projects as open source.

However, whether the policy applies to open source used only for internal purposes may be determined through a separate review procedure.

The scope of application of the policy is reviewed and renewed regularly in response to changes in the company's business environment.


</div>



### 3.1.4.2 Set of Metrics to Achieve for Program Improvement

> **ISO/IEC 18974**
> - 4.1.4.2: A set of metrics the program shall achieve to improve;
>
> **Self-Certification Checklist**
> - [ ] We have a set of metrics to measure Program performance.

To continuously measure and improve the effectiveness of the open source security assurance program, it is essential to set specific, measurable metrics. These metrics are used to assess whether the program's objectives are being achieved, identify areas for improvement, and track progress.

#### Implementation Methods and Considerations

- **SMART metrics**: Metrics should be Specific, Measurable, Achievable, Relevant, and Time-bound.
- **Linking to key objectives**: Metrics should be directly linked to the program's key objectives (e.g., risk reduction, cost savings, efficiency improvement).
- **Data collection and analysis**: A system for collecting and analyzing the data needed to measure the metrics must be built.
- **Regular review**: The appropriateness of the metrics should be reviewed regularly and adjusted as needed.

#### Example Metrics

| Metric | Description | Measurement Method | Target Value |
| --- | --- | --- | --- |
| Open source usage approval turnaround time | Average time from an open source component usage request to approval | Analysis of request management system data | Within 5 days |
| Vulnerability resolution time | Average time from vulnerability discovery to completion of a patch or mitigation | Analysis of vulnerability management system data | Critical: within 24 hours, High: within 7 days |
| License compliance rate | Percentage of all open source components used without license violations | Regular internal audit | 99% or higher |
| Security training completion rate | Percentage of program participants who have completed security training | Analysis of training system data | 90% or higher |
| SBOM generation rate | Percentage of all software projects for which an SBOM has been generated | Analysis of project management system data | 100% |

#### Data Collection Methods

- **Use automated tools**: Automatically collect data using SBOM generation tools, vulnerability scanners, license inspection tools, and the like.
- **Regular audits**: Verify data accuracy through manual audits and collect information that automated tools fail to capture.
- **Surveys**: Gather program participants' opinions and collect subjective data.

#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 10.1 Defining Performance Indicators

1. List of performance indicators:
    - Number of Supplied Software analyzed.
    - Number of Known Vulnerabilities and newly discovered vulnerabilities resolved.
    - Number of compliance deliverables created and distributed.
    - Response time to external inquiries.
    - Training completion rate of program participants.
    - Number of external open source contributions and public projects.
2. Setting indicator targets:
    - Set target values for each indicator so that the program's performance can be assessed.
    - Target values are set in line with the organization's business objectives and the program's purpose.

### 10.2 Regular Program Assessment

1. Assessment cycle:
    - Conduct a program assessment at least once a year.
    - Conduct additional assessments as needed in response to changes in the business environment or major issues.
2. Assessment procedure:
    - Document the assessment results and report them to the OSRB (Open Source Review Board).
    - Collect and reflect feedback from program participants during the assessment process.
    - Assessment results are recorded and retained through an internal system (e.g., the Jira Issue Tracker).
3. Regular policy review and renewal:
    - The policy is reviewed regularly and renewed as needed to reflect the latest open source trends and the organization's requirements.
    - This continuously improves the effectiveness of the program.

### 10.3 Continuous Improvement Plan

1. Identify areas for improvement:
    - Identify areas requiring improvement based on the assessment results and set priorities.
    - Areas requiring improvement may include process efficiency, training content, response time, and the like.
2. Set improvement targets:
    - Set specific improvement targets and schedules.
    - The progress of improvement activities is monitored and documented.
3. Reflect improvement results:
    - Reflect improvement results in the next assessment cycle to continuously enhance the program's effectiveness.
    - Improvement results are shared with program participants to encourage continued commitment to improvement.


</div>



### 3.1.4.3 Documented Evidence from Reviews, Updates, or Audits to Demonstrate Continuous Improvement

> **ISO/IEC 18974**
> - 4.1.4.3: Documented evidence from each review, update, or audit to demonstrate continuous improvement.
>
> **Self-Certification Checklist**
> - [ ] We have Documented Evidence from each review, update, or audit to demonstrate continuous improvement.

An open source security assurance program is not built and maintained as a one-time effort; its effectiveness must be maintained and strengthened through continuous review and improvement. The program's scope, policy, and procedures must be continuously reviewed and updated to keep pace with the changing threat landscape, new technology trends, and changes in the organization's business requirements. These review, update, and audit activities must be documented and managed, and serve as important evidence demonstrating the program's continuous improvement.

#### Implementation Methods and Considerations

- **Regular review meetings**: Hold regular review meetings attended by program management, security experts, legal counsel, and other relevant stakeholders. The meetings discuss the program's effectiveness, problems, and improvements, and decide on necessary actions.
- **Conduct internal audits**: Conduct regular internal audits to assess the program's operational status, policy compliance, and level of risk management. Audits may be conducted by an independent audit team or external experts.
- **Collect and analyze feedback**: Collect and analyze feedback from program participants, development teams, and users, and use it to improve the program. Gather diverse opinions using surveys, interviews, suggestion systems, and the like.
- **Change management process**: When changing the program's scope, policy, or procedures, clearly record the reason for the change, the content of the change, and the affected parties, and notify relevant stakeholders of the changes.
- **Documentation and history management**: Document and manage all review, update, and audit activities so that the change history can be tracked.

#### Sample Evidence

- Review meeting minutes: Record in detail the meeting attendees, discussion content, decisions, and execution plan.
- Internal audit report: Include the audit scope, audit method, audit results, and improvement recommendations.
- Feedback analysis report: Analyze the collected feedback content and derive key improvements.
- Change management record: Specify the reason for the change, the content of the change, and the timing of application.
- Updated policy document: Kept up to date to reflect changes.

#### Sample Table: Continuous Improvement Activity Record

| Date | Activity Type | Description | Owner | Result | Related Document |
| --- | --- | --- | --- | --- | --- |
| 2025-03-15 | Review meeting | Discussion of program operation status and improvement plans | OSPO, Security Team, Legal Team | Reviewed automation of the SBOM generation process | Meeting minutes 20250315 |
| 2025-06-30 | Internal audit | Audit of license compliance and vulnerability management status | Audit Team | Identified missing license notices in some projects | Audit report 20250630 |
| 2025-09-01 | Feedback analysis | Received an SBOM generation automation requirement from the development team | OSPO | Established a plan for the SBOM generation automation project | Feedback analysis report 20250901 |
| 2025-12-31 | Process update | Automated the SBOM generation process | Development Team, OSPO | Reduced SBOM generation time by 50% | SBOM generation process v2.0 |

#### Example Improvement Plan

- **Introduce automation tools**: Introduce tools that automate repetitive tasks such as SBOM generation, vulnerability scanning, and license inspection, thereby improving efficiency.
- **Strengthen the training program**: Operate a regular training program to strengthen the competencies of program participants, and share the latest information and technology trends.
- **Use threat intelligence**: Collect and analyze the latest security threat information and reflect it in the program.
- **Use external experts**: Seek advice from external experts as needed and obtain professional technical support.
- **Community participation**: Actively participate in the open source community to identify the latest information and technology trends, and collaborate with other organizations for the program.

#### Documentation Approach

Include the following content in the open source policy. (Reference: [Open Source Policy Template](../../../templates/1-policy/))


<div class="pageinfo pageinfo-primary">


### 10.2 Regular Program Assessment

1. Assessment cycle:
    - Conduct a program assessment at least once a year.
    - Conduct additional assessments as needed in response to changes in the business environment or major issues.
2. Assessment procedure:
    - Document the assessment results and report them to the OSRB (Open Source Review Board).
    - Collect and reflect feedback from program participants during the assessment process.
    - Assessment results are recorded and retained through an internal system (e.g., the Jira Issue Tracker).
3. Regular policy review and renewal:
    - The policy is reviewed regularly and renewed as needed to reflect the latest open source trends and the organization's requirements.
    - This continuously improves the effectiveness of the program.

### 10.3 Continuous Improvement Plan

1. Identify areas for improvement:
    - Identify areas requiring improvement based on the assessment results and set priorities.
    - Areas requiring improvement may include process efficiency, training content, response time, and the like.
2. Set improvement targets:
    - Set specific improvement targets and schedules.
    - The progress of improvement activities is monitored and documented.
3. Reflect improvement results:
    - Reflect improvement results in the next assessment cycle to continuously enhance the program's effectiveness.
    - Improvement results are shared with program participants to encourage continued commitment to improvement.


</div>


## 3.1.5 Standard Practice Implementation

To build a secure open source software supply chain, an organization must manage the risks it has identified on its own and implement standardized procedures that strengthen security throughout the software development process. These procedures must focus not only on systematically responding to Known Vulnerabilities, but also on preventing security threats that may arise in the future.

### 3.1.5.1 Method to Identify Structural and Technical Threats to Supplied Software

> **ISO/IEC 18974**
> - Method to identify structural and technical threats to the supplied software;
>
> **Self-Certification Checklist**
> - [ ] We have a method to identify structural and technical threats to the Supplied Software;

Identifying structural and technical threats to Supplied Software is an essential process for discovering and resolving potential security issues at an early stage of development. This process must consider various factors, such as design flaws in the software architecture, inappropriate technology stack choices, and unsafe coding practices. From an open source software security assurance standpoint, particular focus should be placed on identifying security vulnerabilities that can arise from the use of open source components.

#### Implementation Methods and Considerations

1. **Use SCA (Software Composition Analysis) tools**:
    - **SBOM-based analysis**: Use an SCA tool to generate a list (SBOM) of all open source components used in the software and identify each component's Known Vulnerabilities.
    - **Integration with vulnerability databases**: Integrate the SCA tool with vulnerability databases such as the NVD (National Vulnerability Database) and CVE (Common Vulnerabilities and Exposures) to make use of the latest vulnerability information.
    - **Automated analysis**: Integrate the SCA tool into the CI/CD pipeline to automatically perform analysis when code changes and detect new vulnerabilities.
2. **Architecture risk analysis**:
    - **Inter-component dependency analysis**: Analyze the software architecture to understand the dependency relationships between components and identify potential security risks.
    - **Data flow analysis**: Analyze how data moves and is processed within the system to assess the possibility of data leakage or tampering.
    - **Authentication and authorization review**: Identify security vulnerabilities in authentication and authorization mechanisms and apply appropriate security measures.

#### Example

- Identify a Known Vulnerability (e.g., CVE-2017-5638) in the Apache Struts 2 framework and assess the vulnerability's impact on the organization's system.
- In a microservices architecture, review the authentication and authorization mechanism used for inter-service communication, and apply security measures to prevent unauthorized access between services.
- Verify whether the version of an open source component in use is the latest, and identify components that are no longer maintained.

#### Implementation Considerations

- **Keeping information current**: Vulnerability databases must be continuously updated.
- **Automation**: Automate the threat identification process as much as possible to improve efficiency.
- **Use of experts**: Obtain the help of security experts as needed to assess and respond to threats.

#### Automation Tool Options

Among the automation tools available as open source for SBOM generation/management and vulnerability identification are FOSSLight, SW360, and OSV-SCALIBR. See the guides below for how to install and use these tools.
- [FOSSLight](../../../tools/3-fosslight/)
- [SW360](../../../tools/2-sw360/)
- [OSV-SCALIBR](../../../tools/4-osvscalibr/)

#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (2) Monitoring Known Vulnerabilities and Newly Discovered Vulnerabilities

IT builds and operates a system for monitoring Known Vulnerabilities and newly discovered vulnerabilities. This system performs the following functions for identifying structural / technical threats:

1. Automated vulnerability monitoring:
    - Analyzes newly published vulnerabilities every day and automatically identifies affected Supplied Software versions.
    - Periodically collects publicly available security vulnerability information.
2. SBOM-based analysis:
    - Performs SBOM-based analysis using an SCA tool.
    - Integrates the SCA tool into the CI/CD pipeline to perform automated analysis.
3. Notification and recording:
    - When a vulnerability is discovered, automatically sends a notification to the development owner and security owner of the affected Supplied Software.
    - Uses an issue tracking system so that everything from notification through review, action, and resolution is documented and recorded.


</div>


Through this approach, an organization can effectively identify structural and technical threats to Supplied Software and minimize the security risk arising from open source use.

### 3.1.5.2 Method to Detect Known Vulnerabilities in Supplied Software

> **ISO/IEC 18974**
> - Method for detecting existence of known vulnerabilities in supplied software;
>
> **Self-Certification Checklist**
> - [ ] We have a method for detecting existence of Known Vulnerabilities in Supplied Software;

Detecting Known Vulnerabilities in the open source components included in Supplied Software is very important for protecting the organization's systems from potential attacks. This process includes using a vulnerability database to check the Known Vulnerability information for each component included in the SBOM, assessing the severity of the vulnerabilities, and taking appropriate response measures. Effective vulnerability detection methods are as follows.

#### Implementation Methods and Considerations

- **Automated vulnerability scanning**:
    - Integrate an SCA tool into the CI/CD pipeline to automatically perform a vulnerability scan whenever code changes.
    - Share the scan results with the development team, security team, and legal team, and take immediate response action as needed.
- **Integration with vulnerability databases**:
    - Integrate the SCA tool with the NVD (National Vulnerability Database), CVE (Common Vulnerabilities and Exposures), and other trusted vulnerability databases.
    - Vulnerability databases must be continuously updated with the latest information.
- **Severity-based classification**:
    - Use the CVSS (Common Vulnerability Scoring System) score to automatically classify the severity of vulnerabilities.
    - Determine the vulnerability response priority based on severity and take the necessary action.
- **Manual verification**:
    - For high-risk vulnerabilities detected by automated tools, a security expert performs manual verification.
    - Manual verification helps reduce false positives and identify vulnerabilities that automated tools fail to detect.

#### Example

- Use an SCA tool to detect a vulnerability in the Apache Struts 2 framework and check the CVSS score to assess its severity.
- For high-risk vulnerabilities, a security expert directly reviews the code and analyzes the likelihood of exploitation.
- When a vulnerability is found, the development team immediately applies a patch or takes mitigation measures.

#### Implementation Considerations

- **Accuracy**: Tools must be selected and configured to reduce false positives and accurately detect actual security threats.
- **Automation**: Configure the process to be integrated into the development process and run automatically.
- **Keeping information current**: Vulnerability databases must be continuously updated with the latest information.

#### Automation Tool Options

Among the tools available as open source that provide automated vulnerability scanning functionality integrated with vulnerability databases are FOSSLight, SW360, and OSV-SCALIBR. See the guides below for how to install and use these tools.
- [FOSSLight](../../../tools/3-fosslight/)
- [SW360](../../../tools/2-sw360/)
- [OSV-SCALIBR](../../../tools/4-osvscalibr/)

#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (2) Monitoring Known Vulnerabilities and Newly Discovered Vulnerabilities

IT builds and operates a system for monitoring Known Vulnerabilities and newly discovered vulnerabilities. This system performs the following functions for identifying structural / technical threats:

1. Automated vulnerability monitoring:
    - Analyzes newly published vulnerabilities every day and automatically identifies affected Supplied Software versions.
    - Periodically collects publicly available security vulnerability information.
2. SBOM-based analysis:
    - Performs SBOM-based analysis using an SCA tool.
    - Integrates the SCA tool into the CI/CD pipeline to perform automated analysis.
3. Notification and recording:
    - When a vulnerability is discovered, automatically sends a notification to the development owner and security owner of the affected Supplied Software.
    - Uses an issue tracking system so that everything from notification through review, action, and resolution is documented and recorded.


</div>


Through this approach, an organization can effectively detect Known Vulnerabilities in the open source components included in Supplied Software and protect its systems from potential attacks.

### 3.1.5.3 Method to Follow Up on Identified Known Vulnerabilities

> **ISO/IEC 18974**
> - Method for following up on identified known vulnerabilities;
>
> **Self-Certification Checklist**
> - [ ] We have a method for following up on identified Known Vulnerabilities;

Once a vulnerability is found in an open source component, the organization's systems and data must be protected through prompt and systematic follow-up action. This involves more than simply applying a patch; it includes a series of steps such as assessing the severity of the vulnerability, determining the response priority, selecting an appropriate resolution, and verifying the result. Effective follow-up methods are as follows.

#### Implementation Methods and Considerations

1. **Establish vulnerability severity assessment criteria**:
    - Use the CVSS (Common Vulnerability Scoring System) score to assess the severity of a vulnerability.
    - Classify severity into High, Medium, Low, and the like, and set a response deadline for each severity level.
    - Example:
        - CVSS 7.0 or higher: High (respond within 24 hours)
        - CVSS 4.0 to 6.9: Medium (respond within 7 days)
        - CVSS 0.1 to 3.9: Low (respond within 30 days)
2. **Define a vulnerability response process**:
    - Define a clear response process that includes reporting, assessment, resolution, and verification stages when a vulnerability is found.
    - Assign an owner for each stage and clearly specify responsibility and authority.
    - Document the process and share it with all relevant members.
3. **Establish a method for setting vulnerability resolution priority**:
    - Determine the resolution priority by considering the vulnerability's severity, scope of impact, and likelihood of exploitation.
    - Resolve vulnerabilities that affect systems of high business importance first.
    - Respond immediately to vulnerabilities for which publicly known exploit code exists.
4. **Vulnerability resolution methods**:
    - **Apply a patch**: If possible, upgrade to the latest version of the open source component that resolves the vulnerability.
    - **Mitigation measures**: If a patch cannot be applied immediately, reduce risk through temporary mitigation measures. (e.g., changing WAF settings, restricting access)
    - **Component replacement**: If the vulnerability is severe and applying a patch is difficult, consider replacing the component with a different one.

#### Example

- For a high-risk vulnerability (CVE-2017-5638) in the Apache Struts 2 framework discovered through an SCA tool, the security team immediately assesses the severity, and the development team upgrades to the latest version within 24 hours.
- If the upgrade is not possible, the WAF (Web Application Firewall) settings are changed to block attacks that exploit the vulnerability.
- All discovered vulnerabilities are registered and managed in an issue tracking system (e.g., Jira), and the resolution process is tracked.

#### Implementation Considerations

- **Automation**: Automate the process from vulnerability detection through resolution as much as possible to improve efficiency.
- **Collaboration**: Respond promptly through close collaboration between the development team, security team, and operations team.
- **Continuous monitoring**: Continue monitoring after a vulnerability is resolved to prevent recurrence.


#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (3) Vulnerability Assessment and Response

Security assesses each vulnerability according to predefined risk/impact assessment criteria and provides response guidance to the business unit. Risk is classified by CVSS (Common Vulnerability Scoring System) score, and a remediation deadline is set based on severity.

| Risk | CVSS 2.0 | CVSS 3.0 | Recommended Remediation Timeline |
|---|:---:|:---:|:---:|
| Low | 0.0 - 3.9 | 0.0 - 3.9 | - |
| Medium | 4.0 - 6.9 | 4.0 - 6.9 | - |
| High | 7.0 - 10.0 | 7.0 - 8.9 | Within 4 weeks |
| Critical | - | 9.0 - 10.0 | Within 1 week |

When a Known Vulnerability or newly discovered vulnerability is identified in previously released Supplied Software, the business unit establishes a remediation plan in accordance with the response guidance provided by the security owner.

If necessary, the business unit notifies customers of the identified vulnerability based on the risk/impact score.

### (4) Vulnerability Resolution and Verification

- The business unit resolves the vulnerability in accordance with the established remediation plan.
- The vulnerability is resolved by removing the problematic open source software component or replacing it with a patched version, among other methods.
- IT uses an open source analysis tool to verify that the issue has been properly resolved.
- Security performs additional security testing on the resolved vulnerability to verify that it has been completely resolved.
- The verification result is documented and recorded.
- A review is conducted to confirm that all severe vulnerabilities have been resolved.
- If a vulnerability that is difficult to resolve remains, whether to approve it is reviewed by considering the business form and the extent of service exposure, among other factors.


</div>


Through this approach, an organization can systematically follow up on identified Known Vulnerabilities and keep its systems secure.

### 3.1.5.4 Method to Communicate Identified Known Vulnerabilities to Customers

> **ISO/IEC 18974**
> - Method to communicate identified known vulnerabilities to customer base when warranted;
>
> **Self-Certification Checklist**
> - [ ] We have a method to communicate identified Known Vulnerabilities to customer base when warranted;

To minimize the impact on customers of Known Vulnerabilities identified in open source components, transparent and prompt communication is essential. An organization must build a system for communicating vulnerability information, scope of impact, and response measures to customers clearly and in a timely manner. This helps maintain customer trust, protect the brand image, and reduce legal liability.

#### Implementation Methods and Considerations

1. **Establish a customer communication process**:
    - Clearly define the procedure for communicating information to customers when a vulnerability occurs.
    - The procedure should include criteria for deciding on disclosure, the method of communication, and owner assignment.
2. **Define vulnerability disclosure criteria**:
    - Clearly define the criteria for what level of severity a vulnerability must have to be disclosed to customers.
    - The decision on whether to disclose is generally based on the CVSS (Common Vulnerability Scoring System) score.
3. **Maintain a customer contact database**:
    - Maintain up-to-date customer contact information so that vulnerability information can be communicated promptly.
    - Use customer segmentation so that information can be communicated only to affected customers.

**Communication methods**:

- **Email**: The most common method, allowing information to be communicated promptly.
- **Customer portal**: Allows customers to directly check vulnerability information and download response measures.
- **Website notice**: Discloses general vulnerability information and directs customers to the customer portal for details.

**Content of the communication**:

- Vulnerability summary: Explains the vulnerability in easy-to-understand terms.
- Impact: Clearly explains the potential impact of the vulnerability on customer systems.
- Resolution: Provides a patch, mitigation measure, or other resolution, if available.
- Contact: Specifies the owner or department the customer can contact for additional questions or support.

#### Implementation Considerations

- **Timeliness**: Communicate information to customers as quickly as possible.
- **Accuracy**: Provide accurate and reliable information.
- **Transparency**: Honestly disclose the severity and impact of the vulnerability.
- **Consistency**: Provide consistent information to all customers.

#### Example

- When a remote code execution vulnerability is discovered in the Apache Struts 2 framework, send an email to affected customers and guide them to apply the patch for the vulnerability.
- Post detailed information about the vulnerability on the customer portal and provide answers to frequently asked questions.
- If necessary, call the customer directly to explain the situation and support the patch application.

#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (8) Customer and Third-Party Notification

The Open Source Program Manager generates an updated open source notice based on the SBOM in which the vulnerability has been resolved, and delivers it to the business unit.

1. Customer notification:

    The business unit notifies customers of the vulnerability resolution in the following ways:

    - Replaces the open source notice included with the product distribution.
    - Notifies customers directly by email or other means, as needed.
    - Redistributes a version of the Supplied Software in which the vulnerability has been resolved.
2. Third-party information disclosure:

    IT discloses risk information to third parties in the following ways:

    - Registers the revised open source notice and vulnerability-related information on the company's open source website.
    - Submits vulnerability information to a public vulnerability database (e.g., the NVD).
    - Notifies the open source project maintainer of the discovered vulnerability and the resolution method.
3. Notification content:

    The information provided to customers and third parties includes the following:

    - Vulnerability overview and identifier (e.g., CVE number)
    - Affected products and versions
    - The vulnerability's potential impact and CVSS score
    - Temporary response measures
    - Availability of a patch or update and how to apply it
    - Contact information for obtaining additional information


</div>



Through this approach, an organization can effectively communicate information about identified Known Vulnerabilities to customers, maintain customer trust, and protect its brand image.

### 3.1.5.5 Method to Analyze Supplied Software for Newly Published Known Vulnerabilities After Release

> **ISO/IEC 18974**
> - Method for analyzing supplied software for newly published known vulnerabilities post release of the supplied software;
>
> **Self-Certification Checklist**
> - [ ] We have a method for analyzing Supplied Software for newly published Known Vulnerabilities post release of the Supplied Software;

New vulnerabilities can be discovered even after Supplied Software has been released. Such vulnerabilities can penetrate a system through unexpected attack paths or bypass existing security measures. Therefore, an organization must have a system in place to continuously monitor and analyze new vulnerabilities even after Supplied Software has been released. This is essential for minimizing potential damage through a prompt response and maintaining customer trust.

#### Implementation Methods and Considerations

1. **Build a vulnerability monitoring system**:
    - Continuously monitor the NVD (National Vulnerability Database), CVE (Common Vulnerabilities and Exposures), and other trusted vulnerability information sources.
    - Use automated tools to collect new vulnerability information and identify vulnerabilities that could affect the organization's systems.
2. **Initial classification and impact analysis**:
    - After identifying new vulnerability information, check whether the vulnerability exists in an open source component used in the organization's systems.
    - Assess the vulnerability's severity, likelihood of exploitation, and potential impact on the system.
3. **Detailed analysis and reproduction**:
    - For vulnerabilities that are likely to have an impact, perform a detailed analysis and attempt to reproduce the vulnerability based on a real-world attack scenario.
    - Use the reproduction result to understand the vulnerability's actual level of risk and develop an appropriate response.
4. **Develop a response plan**:
    - Based on the vulnerability analysis results, decide on a patch application, mitigation measure, or other response.
    - The response plan should consider not only technical aspects but also business impact, legal requirements, and customer communication strategy.
5. **Execute and verify the response**:
    - Immediately execute the necessary action according to the established response plan.
    - After applying a patch or taking mitigation measures, always re-verify the vulnerability to confirm that the issue has been resolved.
6. **Customer notification (as needed)**:
    - If the vulnerability has a significant impact on customers, notify them of the fact and guide them on the necessary action.
    - Communication with customers should be transparent and prompt.

#### Implementation Considerations

- **Automation**: Automate the vulnerability monitoring, initial classification, and impact analysis processes as much as possible to improve efficiency.
- **Use of experts**: Detailed analysis, reproduction, and development of a response plan require the specialized knowledge and experience of security experts.
- **Collaboration**: Enable a prompt and effective response through close collaboration between the development team, security team, operations team, and legal team.
- **Documentation**: Record the vulnerability analysis results, response plan, and execution results in detail so that they can be referenced when a similar issue occurs in the future.

#### Example

- Confirm information that a new vulnerability (e.g., CVE-2025-XXXX) has been discovered in the Apache Struts 2 framework via the NVD.
- Use an SCA tool to check whether the vulnerability exists in the version of Struts 2 used in the organization's systems.
- Check the vulnerability's CVSS score and assess its severity.
- A security expert reproduces the vulnerability and analyzes the actual likelihood of attack.
- Coordinate with the development team to determine the timing of patch application, and apply the patch to the system together with the operations team.
- Rerun the vulnerability scanner to confirm that the vulnerability has been resolved.
- If the vulnerability is likely to have a significant impact on customers, send them an email and guide them on the necessary action.

#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (5) Post-Release Vulnerability Analysis and Response

IT operates an automated system to analyze vulnerabilities in released Supplied Software every day, even after release, for all Supplied Software.

- When affected Supplied Software is identified, a notification is immediately sent to the development owner and security owner.
- The owner who receives the notification assesses the severity of the vulnerability and develops a response plan.
- Patch development, mitigation measures, and the like are executed according to the response plan.
- Verification is performed after the action is completed, and the result is documented.


</div>



Through this approach, an organization can respond promptly to newly discovered vulnerabilities after the release of Supplied Software and keep its systems secure.

### 3.1.5.6 Method for Continuous and Repeated Security Testing Before Release

> **ISO/IEC 18974**
> - Method for continuous and repeated security testing to be applied for all supplied software before release;
>
> **Self-Certification Checklist**
> - [ ] We have a method for continuous and repeated Security Testing is applied for all Supplied Software before release;

To provide secure software, it is not enough to perform security testing just once before release. Continuous and repeated security testing is essential for strengthening security throughout the software development lifecycle (SDLC) and for identifying and resolving potential vulnerabilities before release. In particular, when open source components are used, such testing plays an important role in confirming open source license compliance and identifying potential security vulnerabilities.

#### Implementation Methods and Considerations

1. **Integrate into the CI/CD pipeline**:
    - Integrate security testing into the CI/CD pipeline so that tests run automatically whenever code changes.
    - This allows security issues to be discovered and resolved from the early stages of development.
2. **Use SCA tools**:
    - Use an SCA (Software Composition Analysis) tool to scan open source components for vulnerabilities and confirm license compliance.
    - Integrate the SCA tool into the CI/CD pipeline so that it runs automatically during the build process.
3. **Regular manual review**:
    - Since automated tools alone may not discover all security issues, conduct regular manual security reviews.
    - Manual review may include code review, architecture review, penetration testing, and the like.
4. **Analyze and improve test results**:
    - Analyze the security test results and develop a plan to resolve discovered vulnerabilities.
    - Share the test results with the development team, security team, and operations team, and resolve issues collaboratively.
    - Continuously improve the testing process to enable more effective testing.

#### Specific Examples

- **Automate vulnerability scanning**: Integrate a vulnerability scanning tool such as OWASP Dependency-Check into the CI/CD pipeline to automatically scan open source components for vulnerabilities during the build process.
- **Automate license inspection**: Integrate a license inspection tool such as FOSSology into the CI/CD pipeline to automatically inspect open source components for license compliance during the build process.
- **Mandate code review**: Mandate code review for all code changes and make an effort to find security vulnerabilities.
- **Perform penetration testing**: Commission external security experts to perform penetration testing on the system before release, and identify potential security vulnerabilities.

#### Implementation Considerations

- **Test scope**: Security testing must be performed on all open source components and custom code.
- **Test cycle**: Security testing must be performed whenever code changes and before release.
- **Test environment**: Build a test environment similar to the actual production environment to increase the reliability of the test results.

#### Automation Tool Options

Among the tools available as open source that enable continuous and repeated security testing before release are FOSSLight, SW360, and OSV-SCALIBR. See the guides below for how to install and use these tools.

- [FOSSLight](../../../tools/3-fosslight/)
- [SW360](../../../tools/2-sw360/)
- [OSV-SCALIBR](../../../tools/4-osvscalibr/)

#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (1) Continuous Security Testing Before Release

IT builds and operates a system that applies continuous and repeated security testing to all Supplied Software before release:

1. Automated security testing:
    - Integrates automated security testing tools into the CI/CD pipeline.
    - Automatically runs security testing whenever code changes.
2. Vulnerability scanning:
    - Uses an SCA tool to scan open source components for Known Vulnerabilities.
    - Automatically updates the vulnerability database and performs a scan every day.
3. Review of security test results:
    - The security owner reviews the security test results and takes the necessary action.
    - If a serious vulnerability is found, immediately notifies the development team and develops a resolution plan.


</div>


Through this approach, an organization can identify and resolve potential security vulnerabilities before release, providing more secure software.

### 3.1.5.7 Method to Verify That Identified Risks Are Addressed Before Release of Supplied Software

> **ISO/IEC 18974**
> - Method to verify that identified risks will have been addressed before release of supplied software;
>
> **Self-Certification Checklist**
> - [ ] We have a method to verify that identified risks will have been addressed before release of Supplied Software;

Resolving the Known Vulnerabilities discovered by an SCA (Software Composition Analysis) tool before releasing Supplied Software is very important for ensuring the security level of the final product. This includes activities such as patching or removing vulnerable open source components, with the goal of preventing similar issues from occurring in the future.

#### Implementation Methods and Considerations

1. **Identify vulnerabilities using an SCA tool**:
    - Integrate the SCA tool into the CI/CD pipeline to continuously scan for vulnerabilities.
    - Perform a final scan before release to identify all Known Vulnerabilities.
2. **Define a vulnerability resolution process**:
    - Decide on a resolution method, such as applying a patch or removing the component, for each identified vulnerability.
    - Set priorities based on severity and resolve high-risk vulnerabilities first.
3. **Establish a resolution verification procedure**:
    - After applying a patch, perform a rescan to confirm that the vulnerability has been resolved.
    - When a component is removed, confirm that the corresponding functionality has been properly replaced.
4. **Final security approval procedure**:
    - After confirming that all high-risk vulnerabilities have been resolved, obtain final approval from the security lead.
    - Document any residual risk and establish a management plan.

#### Specific Examples

- When a Known Vulnerability (e.g., CVE-2017-5638) in the Apache Struts 2 framework is found by an SCA tool, upgrade to the latest patched version.
- When an open source library that is no longer maintained is found, remove the library and replace it with an alternative library.

#### Implementation Considerations

- **Automation**: Automate the scanning and result analysis of the SCA tool to improve efficiency.
- **Continuous monitoring**: Continue monitoring for and responding to new vulnerabilities even after release.
- **Documentation**: Document the vulnerability resolution process and results in detail for future reference.


#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (4) Vulnerability Resolution and Verification

- The business unit resolves the vulnerability in accordance with the established remediation plan.
- The vulnerability is resolved by removing the problematic open source software component or replacing it with a patched version, among other methods.
- IT uses an open source analysis tool to verify that the issue has been properly resolved.
- Security performs additional security testing on the resolved vulnerability to verify that it has been completely resolved.
- The verification result is documented and recorded.
- A review is conducted to confirm that all severe vulnerabilities have been resolved.
- If a vulnerability that is difficult to resolve remains, whether to approve it is reviewed by considering the business form and the extent of service exposure, among other factors.


</div>



Through this approach, an organization can effectively resolve Known Vulnerabilities before the release of Supplied Software and significantly improve the security level of the final product.

### 3.1.5.8 Method to Communicate Identified Risks to Third Parties

> **ISO/IEC 18974**
> - Method to export information about identified risks to third parties as appropriate.
>
> **Self-Certification Checklist**
> - [ ] We have a method to export information about identified risks to third parties as appropriate.

Security risks present in an organization's Supplied Software can affect not only the organization itself but also various stakeholders, such as customers who use the software, partners, and the open source community. Therefore, an organization must appropriately communicate identified risks to third parties so that risks can be managed jointly and the security of the overall software supply chain can be strengthened. This process must be carried out in a transparent and responsible manner, and must comply with relevant laws and contractual terms.

#### Implementation Methods and Considerations

1. **Risk assessment and classification**:
    - Assess the identified risk's severity, scope of impact, and likelihood of propagation to determine which third parties the information should be communicated to.
    - Information must be shared immediately for high-risk vulnerabilities that could result in personal information leakage, system failure, financial loss, or the like.
2. **Define information sharing criteria**:
    - Clearly define what information is to be shared and in what manner.
    - Information must be written concisely and clearly, and should include a non-technical explanation along with technical content.
    - Includes a description of the vulnerability, its impact, the resolution method, and contact information.
3. **Build communication channels**:
    - Build communication channels for safely sharing information with third parties.
    - Email, a customer portal, a security bulletin board, and the like can be used.
    - Apply encrypted communication, access permission management, data loss prevention technology, and the like for information security.
4. **Comply with legal and contractual obligations**:
    - Comply with relevant laws (e.g., personal information protection law) and contractual terms (e.g., confidentiality clauses) when sharing information.
    - Coordinate with the legal team to perform a legal review of information sharing.
5. **Assign an owner**:
    - Assign an owner who oversees the risk information sharing process.
    - The owner is responsible for information-sharing decisions, review of the information content, and communication with third parties.

#### Specific Examples

- **Open source community**:
    - Report vulnerabilities found in internally developed code to the relevant open source project and collaborate on patch development.
    - Consider using a Cybersecurity Vulnerability Information Sharing Program.
- **Customers**:
    - When a cybersecurity vulnerability occurs, notify customers immediately and inform them of the vulnerability's impact and resolution.
    - If necessary, provide remote support for customer systems to help with patch application.
- **Suppliers**:
    - When a vulnerability is found in software or hardware they have provided, inform customers of the fact and provide a patch or update.

#### Implementation Considerations

- **Timeliness**: Share information as quickly as possible so that third parties can take appropriate action.
- **Accuracy**: Provide accurate and reliable information.
- **Transparency**: Honestly disclose the severity and impact of the vulnerability.



#### Documentation Approach

Include the following content in the open source process. (Reference: [Open Source Process Template](../../../templates/2-process-template/))


<div class="pageinfo pageinfo-primary">


### (8) Customer and Third-Party Notification

The Open Source Program Manager generates an updated open source notice based on the SBOM in which the vulnerability has been resolved, and delivers it to the business unit.

1. Customer notification:

    The business unit notifies customers of the vulnerability resolution in the following ways:

    - Replaces the open source notice included with the product distribution.
    - Notifies customers directly by email or other means, as needed.
    - Redistributes a version of the Supplied Software in which the vulnerability has been resolved.
2. Third-party information disclosure:

    IT discloses risk information to third parties in the following ways:

    - Registers the revised open source notice and vulnerability-related information on the company's open source website.
    - Submits vulnerability information to a public vulnerability database (e.g., the NVD).
    - Notifies the open source project maintainer of the discovered vulnerability and the resolution method.
3. Notification content:

    The information provided to customers and third parties includes the following:

    - Vulnerability overview and identifier (e.g., CVE number)
    - Affected products and versions
    - The vulnerability's potential impact and CVSS score
    - Temporary response measures
    - Availability of a patch or update and how to apply it
    - Contact information for obtaining additional information


</div>
