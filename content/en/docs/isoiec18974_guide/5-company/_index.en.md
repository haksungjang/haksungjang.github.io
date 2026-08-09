---
title: "5. Implementation Considerations by Organizational Characteristics"
linkTitle: "5. Implementation Considerations by Organizational Characteristics"
weight: 50
type: docs
description: >
---

To effectively implement the ISO/IEC 18974 standard, a tailored approach that considers the organization's characteristics is necessary. This section describes in detail the approaches for large enterprises, small and medium-sized enterprises (SMEs), and startups, integration with existing security processes, and education and awareness programs.

## 5.1 Approaches by Large Enterprises, SMEs, and Startups

### 5.1.1 Large Enterprises

Large enterprises must manage complex organizational structures, diverse projects, and a wide range of technology stacks, so a systematic and comprehensive approach is essential. In addition, they must pay closer attention to compliance with legal and regulatory requirements, supply chain management, and protection of brand reputation.

- **Establishing a dedicated Open Source Program Office (OSPO)**: The OSPO functions as a central organization that establishes and manages the organization-wide open source strategy. The OSPO performs the following roles, which are important for ensuring consistent policies and processes.
    - Establishing and managing open source policy: Establishes and manages policies for open source use and contribution across the organization. Policies must reflect legal requirements, security guidelines, and the organization's business goals.
    - Managing open source compliance: Verifies compliance with open source licenses and resolves related issues.
    - Managing security vulnerabilities: Manages the process of identifying, assessing, and patching vulnerabilities in open source components.
    - Participating in open source communities: Contributes to open source projects and builds relationships with the community.

    **Success cases**: Large technology companies such as Google, Microsoft, and Facebook systematically manage their open source strategies through an OSPO. Through their OSPOs, these companies encourage open source use, contribute to communities, and manage legal and security risks at the same time.

- **Designating open source coordinators by department**: Designates an open source coordinator for each department or project team to ensure smooth communication with the OSPO. The coordinator complies with the guidelines provided by the OSPO and reports on the status of open source use within the department.
- **Adopting advanced tools and processes**: Adopts advanced Software Bill of Materials (SBOM) generation tools and vulnerability scanning solutions to manage large codebases and complex dependencies.
    - Example: Implements automated open source management using commercial tools such as WhiteSource, Black Duck, and Snyk. These tools quickly scan large codebases, generate accurate SBOMs, and provide diverse vulnerability information.
- **Managing a complex supply chain**: Builds a systematic process to track and manage open source use by various suppliers and partners.
    - Specifies open source security requirements in supplier contracts and verifies compliance through regular audits. Contract terms may include an obligation to provide an SBOM, sharing of vulnerability information, and allocation of responsibility in the event of a security incident.

**Table 5.1: Key Elements for ISO/IEC 18974 Implementation in Large Enterprises**

| Element | Description | Example |
| --- | --- | --- |
| Establishing an OSPO | Central organization for open source strategy and management | Google, Microsoft, Facebook |
| Designating departmental coordinators | Securing a communication channel between the OSPO and each department | Designating an open source Champion for each team |
| Using advanced tools | Automated SBOM generation and vulnerability scanning | WhiteSource, Black Duck, Snyk |
| Supply chain management | Specifying supplier security requirements | Including an SBOM provision obligation in contract terms |

### 5.1.2 Small and Medium-Sized Enterprises

SMEs have more limited resources than large enterprises, so an efficient implementation strategy is needed. The key is to choose cost-effective solutions, leverage the capabilities of existing teams, and, where necessary, seek help from outside experts.

- **Designating an open source lead within an existing team**: Instead of a dedicated OSPO, designates an open source security lead within the existing development or security team. The lead performs roles such as complying with open source policy, managing SBOMs, and checking vulnerabilities.
- **Using cloud-based open source management tools**: Considers cloud-based solutions to reduce initial investment costs and secure flexibility.
    - Example: Uses the open source management features provided by cloud-based collaboration platforms such as GitHub and GitLab. These platforms provide source code management, collaboration, build automation, and basic security scanning features.
- **Considering advice from outside experts**: Seeks advice from outside consultants or experts as needed to pursue efficient implementation.
    - Uses an open source security consulting firm to receive short-term technical support and training. Outside experts can provide specialized knowledge on SBOM generation, vulnerability scanning, and license compliance.
- **Choosing cost-effective solutions**: Optimizes costs by using open source tools or low-cost commercial solutions.
    - Example: Uses free or inexpensive tools such as OWASP Dependency-Check and Snyk Open Source. These tools provide basic SBOM generation and vulnerability scanning features and can be fully utilized even within an SME's budget.

**Table 5.2: Key Elements for ISO/IEC 18974 Implementation in SMEs**

| Element | Description | Example |
| --- | --- | --- |
| Using an existing team | Using existing personnel instead of a dedicated organization | Designating a lead within the development or security team |
| Cloud-based tools | Reducing initial costs and securing flexibility | Open source management features of GitHub, GitLab |
| Advice from outside experts | Short-term technical support and training as needed | Building an SBOM with the help of a consulting firm |
| Cost-effective solutions | Using free or inexpensive tools | OWASP Dependency-Check, Snyk Open Source |

### 5.1.3 Startups

Startups need a flexible approach that can respond to rapid growth and change. The key is to integrate security into the development process, actively use automation tools, and increase efficiency through fast decision-making.

- **Applying a simplified agile process**: Adopts a simplified approach that focuses on core requirements instead of a complex process.
    - Simplifies the open source use approval procedure and allows developers to choose open source components autonomously. However, important security or license-related matters must always be reviewed.
- **Integrating open source security management into the development process**: Integrates security checks into the existing development workflow rather than as a separate process (DevSecOps).
    - Adds SBOM generation and vulnerability scanning steps to the CI/CD pipeline. This allows security vulnerabilities to be automatically checked during the development process and resolved before code deployment.
- **Actively using automation tools**: Makes maximum use of automation tools for efficient management with limited personnel.
    - Example: Uses automation tools such as GitHub Actions and GitLab CI to automate SBOM generation and vulnerability scanning. These tools are relatively simple to configure and can be easily integrated into the development workflow.
- **Fast decision-making and execution**: Uses a flexible organizational structure to drive rapid decision-making and policy implementation.
    - Open source-related decisions are made quickly by the development team lead or the Chief Technology Officer (CTO). Advice from the legal or security team can be sought during the decision-making process, but decision-making speed should not be slowed down.

**Table 5.2: Key Elements for ISO/IEC 18974 Implementation in Startups**

| Element | Description | Example |
| --- | --- | --- |
| Agile process | Focus on core requirements, fast decision-making | Simplified use approval procedure |
| DevSecOps | Integrating security into the development workflow | Adding security checks to the CI/CD pipeline |
| Automation tools | Efficient management with limited personnel | GitHub Actions, GitLab CI |
| Fast decision-making | Using a flexible organizational structure | Responsibility of the development team lead or CTO |

**Success cases:**

- **Netflix**: Netflix developed an open source tool called "Security Monkey" to automate security in cloud environments. This encouraged developers to consider security more easily and contributed to reducing the burden on the security team.
- **Spotify**: Spotify succeeded in strengthening security while maintaining development speed by integrating security checks into its continuous deployment pipeline.

**Key considerations:**

- **Risk-based approach**: Rather than applying the same level of security management to all open source components, it is better to prioritize components with a higher level of risk.
- **Continuous learning**: Open source security threats are constantly changing, so it is necessary to continuously learn the latest trends and update security practices.
- **Community participation**: Participating in open source communities and collaborating with other organizations to help strengthen open source security is also a good approach.

## 5.2 Integration with Existing Security Processes

To successfully implement ISO/IEC 18974, smooth integration with existing security processes is essential. Integrating open source security management into the existing security system reduces redundant investment, increases efficiency, and achieves consistent security management.

1. **Analyzing current security policy**
    - **Reviewing existing policy**: Reviews the organization's existing security policies, such as information security policy, privacy policy, and risk management policy, to identify parts related to ISO/IEC 18974 requirements.
    - **Performing gap analysis**: Analyzes the differences between existing policy and ISO/IEC 18974 requirements and identifies parts that need to be supplemented.
    - **Integrating policy**: Adds open source security-related provisions to existing policy, or establishes a separate open source security policy and integrates it with existing policy.

    **Example**:

    - Adds a provision to the existing information security policy stating that "security review procedures must be followed when using open source software."
    - Adds a provision to the privacy policy stating that "encryption and access control measures must be strengthened when using open source components that process personal information."
2. **Using the DevSecOps framework**
    - **Integrating the CI/CD pipeline**: Integrates open source security management into the Continuous Integration/Continuous Delivery (CI/CD) pipeline to build a DevSecOps environment that considers security from the early stages of development.
    - **Automated security checks**: Automates steps such as Software Bill of Materials (SBOM) generation, license checking, and vulnerability scanning in the CI/CD pipeline.
    - **Feedback loop**: Provides rapid feedback of security check results to the development team so that fixes can be made.

    **Example**:

    - Uses CI/CD tools such as Jenkins, GitLab CI, and CircleCI to automate SBOM generation and vulnerability scanning steps.
    - Integrates Static Application Security Testing (SAST) tools such as SonarQube and Veracode into the CI/CD pipeline to check code quality and security vulnerabilities.
3. **Linking with the risk management process**
    - **Identifying risk**: Identifies risks arising from open source use (e.g., exploitation of vulnerabilities, license violations) and records them in the risk management register.
    - **Assessing risk**: Assesses the severity, likelihood of occurrence, and business impact of identified risks.
    - **Responding to risk**: Prepares and executes appropriate response measures (e.g., applying patches, mitigation measures, discontinuing use) according to the assessed risk.
    - **Monitoring risk**: Continuously monitors the effectiveness of the risk management plan and revises the plan as needed.

    **Example**:

    - Adds a risk item to the risk management register stating "use of open source components with severe vulnerabilities such as Log4Shell."
    - Assesses the likelihood of occurrence of the corresponding risk as "medium" and severity as "high," and establishes a response plan of "applying a patch within 24 hours of vulnerability discovery."
4. **Updating the incident response plan**
    - **Adding open source-related scenarios**: Adds open source-related scenarios (e.g., exploitation of vulnerabilities, license violations) to the existing incident response plan.
    - **Defining response procedures and responsible parties**: Clearly defines the response procedure and responsible party for each scenario.
    - **Training and simulation**: Conducts regular training and simulations to improve response capability in the event of an open source-related security incident.
    - **Reviewing insurance enrollment**: Considers enrolling in cyberattack insurance to prepare for open source-related legal liability (e.g., copyright infringement lawsuits).

    **Example**:

    - Adds a scenario to the incident response plan stating "a zero-day vulnerability is discovered in an open source component," and clearly defines the response procedure and responsible party.
    - Includes a scenario exploiting an open source vulnerability during penetration testing exercises to check response capability.

**Table 5.3: Methods for Integration with Existing Security Processes**

| Integration Area | Description | Execution Example |
| --- | --- | --- |
| Policy | Adding open source-related provisions or establishing a separate policy | Adding a provision to "comply with security review procedures when using open source software" |
| DevSecOps | Integrating security checks into the CI/CD pipeline | Installing the OWASP Dependency-Check plugin in Jenkins |
| Risk management | Recording open source-related risks in the risk management register | Adding a risk item for "severe vulnerabilities such as Log4Shell" |
| Incident response | Adding open source-related scenarios | Adding a scenario for "when an open source zero-day vulnerability is discovered" |

## 5.3 Education and Awareness Programs

Understanding and participation across the entire organization is essential for effective ISO/IEC 18974 implementation. Education and awareness programs should support organization members in recognizing the importance of open source security and fulfilling their own roles and responsibilities.

1. **Developing tailored education programs by audience**
    - **Developers**: Provides education on secure coding practices, major open source licenses, and vulnerability response methods.
        - Example: Provides security training courses such as OWASP Top 10 and SANS Top 25, and trains developers on how to find security vulnerabilities during code review.
    - **Security team**: Provides education on open source security audits, incident response procedures, and the latest security threat trends.
        - Example: Strengthens practical capability through penetration testing exercises and breach incident analysis workshops.
    - **Legal team**: Provides education on types of open source licenses, legal liabilities and obligations, and related laws.
        - Example: Provides legal lectures on major open source licenses such as the GNU General Public License (GPL), Apache License, and MIT License.
    - **Executive management**: Provides education on the need for open source security investment, Return on Investment (ROI), and risk management.
        - Example: Supports participation in open source security-related workshops or seminars and provides investment effectiveness analysis reports.
2. **Using various education methods**
    - **Building an online learning platform**: Provides a learning environment not restricted by time or place.
        - Example: Uses online education platforms such as Coursera and Udemy, or builds an in-house Learning Management System (LMS).
    - **Running workshops and hands-on sessions**: Provides practice-centered learning opportunities through real cases.
        - Example: Conducts web application security vulnerability diagnosis workshops using tools such as OWASP ZAP and Burp Suite.
    - **Seminars inviting outside experts**: Provides opportunities to share the latest trends and best practices and to acquire specialized knowledge.
3. **Continuous awareness-raising activities**
    - **Running an internal newsletter or blog**: Regularly shares the latest open source security news, vulnerability information, and success cases.
    - **Conducting in-house security campaigns**: Conducts campaigns that emphasize the importance of open source security and encourage member participation.
    - **Running a "Security Champions" program**: Trains personnel in each team to lead the security culture and encourages security-related activities.
4. **Building an evaluation and feedback system**
    - **Measuring education effectiveness**: Sets Key Performance Indicators (KPIs) to measure the effectiveness of education programs and evaluates them regularly. (e.g., education completion rate, evaluation of security knowledge improvement)
    - **Collecting feedback**: Collects and analyzes feedback on education programs and uses it to improve programs.
    - **Reflecting improvements**: Continuously improves the content, methods, and frequency of education programs based on evaluation results and feedback.

**Table 5.4: Elements of Education and Awareness Programs**

| Element | Description | Example |
| --- | --- | --- |
| Education by audience | Tailored education for developers, security team, legal team, executive management | Secure coding education for developers |
| Various education methods | Using online lectures, workshops, seminars, etc. | Penetration testing exercises, legal advice |
| Continuous awareness-raising | Newsletter, in-house campaigns, Security Champions | Publishing a monthly security newsletter |
| Evaluation and feedback | Measuring education effectiveness, reflecting feedback | Education satisfaction survey, KPI achievement rate evaluation |
