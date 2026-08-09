# 4. Comparison and Integration with ISO/IEC 5230

LLMS index: [llms.txt](/llms.txt)

---

This chapter compares and analyzes ISO/IEC 5230 for open source compliance management and ISO/IEC 18974 for open source security assurance, and presents a way to integrate the two standards to build a more effective open source management system.

## 4.1 Similarities and Differences

ISO/IEC 5230 and ISO/IEC 18974 are both international standards for open source management, but they differ in their main objectives, scope of application, and core requirements. It is important to understand both standards and apply them appropriately to the organization's circumstances.

**Table 4.1: Main Similarities Between ISO/IEC 5230 and ISO/IEC 18974**

| Similarity | Description |
| --- | --- |
| International standards for open source management | Both standards aim at the effective management of open source software. |
| Based on the Linux Foundation's OpenChain project | Both standards were developed based on the output of the OpenChain project. |
| Improvement of an organization's open source processes | Both standards help organizations improve their open source management processes and raise their maturity. |
| Self-certification option | Both standards allow organizations to confirm their compliance through self-assessment. |
| Emphasis on continuous improvement | Both standards encourage continuous improvement of open source management processes. |

**Table 4.2: Main Differences Between ISO/IEC 5230 and ISO/IEC 18974**

| Category | ISO/IEC 5230 | ISO/IEC 18974 |
| --- | --- | --- |
| Main focus | Open source license compliance | Open source security assurance |
| Scope of application | License obligations, notice requirements, copyright attribution, source code disclosure obligations, etc. | Vulnerability management, SBOM (Software Bill of Materials) management, patch management, security review, etc. |
| Main audience | Legal team, compliance officers, license managers | Security team, development team, OSPO (Open Source Program Office) |
| Core requirements | - License identification and analysis <br> - Compliance with license obligations <br> - Fulfillment of notice obligations <br> - Copyright attribution | - Identification and assessment of vulnerabilities <br> - Establishing and executing a vulnerability response plan <br> - Establishing and complying with a security policy <br> - SBOM management |
| Management targets | Open source licenses, copyrights, patents | Security vulnerabilities, malicious code, and outdated dependencies in open source components |
| Main activities | - License review and analysis <br> - Confirming compliance with license obligations <br> - Fulfilling notice obligations <br> - Legal risk management | - Vulnerability scanning and analysis <br> - Applying security updates and patches <br> - Incident response <br> - Open source security audits |
| Goal | Reduced legal liability, prevention of license disputes, maintaining compliance | Reduced security risk, improved software reliability, safe software development |
| Management tools | - License scanning tools (e.g., FOSSology, ScanCode) <br> - Compliance management systems | - Vulnerability scanners (e.g., OWASP Dependency-Check, Snyk) <br> - SBOM management tools (e.g., SPDX Tools, CycloneDX) <br> - Security information and event management (SIEM) systems |
| How license compliance is ensured | - Building an open source license review process <br> - Providing open source usage guidelines <br> - Training on compliance with license obligations <br> - Establishing a resolution procedure for license violations | Not applicable |
| How security vulnerabilities are managed | Not applicable | - Using vulnerability scanning tools <br> - Assessing vulnerabilities and prioritizing them <br> - Applying patches or mitigation measures <br> - Periodically reviewing the vulnerability management process |

**How does ISO/IEC 5230 ensure license compliance?**

To ensure open source license compliance, ISO/IEC 5230 requires the following.

- **License identification process**: The organization must accurately identify the licenses of all open source components it uses. This can be done using license identification tools or by manually reviewing the code.
- **Compliance with license obligations**: The organization must comply with all obligations of the identified licenses. For example, if the organization uses a component under the GPL (GNU General Public License), it may be required to disclose its source code.
- **Fulfillment of notice obligations**: The organization must notify users of the license information for open source components. This can be done by including notice text within the software product or by providing a separate license file.

**How does ISO/IEC 18974 manage security vulnerabilities?**

To manage open source security vulnerabilities, ISO/IEC 18974 requires the following.

- **Using vulnerability scanning tools**: The organization must periodically scan open source components for known vulnerabilities using automated vulnerability scanning tools.
- **Assessing vulnerabilities and prioritizing them**: For each vulnerability found, the organization must assess its severity, impact, and exploitability, and determine a response priority.
- **Applying patches or mitigation measures**: According to priority, the organization must apply patches to vulnerabilities or implement mitigation measures (e.g., changing firewall settings, modifying code).
- **Periodically reviewing the vulnerability management process**: The organization must periodically review the effectiveness of the vulnerability management process and improve it as needed.

## 4.2 The Complementary Relationship Between the Two Standards

ISO/IEC 5230 (open source license compliance) and ISO/IEC 18974 (open source security assurance) are independent standards, but when an organization implements them together, it can create a synergistic effect in open source management. Understanding the areas each standard covers and leveraging their complementary relationship makes it possible to build a stronger open source management system.

1. **Building an integrated open source management system**
    - **Legal risk management (ISO/IEC 5230)**: Compliance with open source licenses reduces the likelihood of legal disputes such as copyright and patent infringement.
    - **Security risk management (ISO/IEC 18974)**: Managing the risk of vulnerabilities and malicious code infection in open source components reduces the likelihood of security incidents.
    - **Integrated management**: Rather than managing legal risk and security risk separately, building an integrated system improves efficiency.
2. **Process synergy**
    - **Using an SBOM (Software Bill of Materials)**: An SBOM can be used to manage license information and security vulnerability information together. Recording both license information and vulnerability information in the SBOM makes it possible to grasp the legal and security risks of each component at the same time.
    - **Integrating documentation and training programs**: Efficiency can be improved by integrating open source policies, license compliance procedures, and security guidelines into a single document and jointly operating training programs.
3. **Optimizing organizational structure**
    - **Using an OSPO (Open Source Program Office)**: An OSPO can be used to manage the requirements of both standards in an integrated way. The OSPO oversees open source policy development, process management, and tool adoption, and facilitates cooperation between the legal and security teams.
    - **Strengthening cooperation between the legal and security teams**: The legal team assesses the legal risks related to open source licenses, and the security team analyzes the security vulnerabilities of open source components. The two teams work together to conduct a comprehensive risk assessment of open source use and develop appropriate response measures.
4. **Strengthening supply chain management**
    - **Considering both standards together when evaluating suppliers**: When receiving software from a supplier, both ISO/IEC 5230 and ISO/IEC 18974 are used as criteria for evaluating the supplier's open source management system. This helps raise the level of open source management across the entire supply chain.
    - **Specifying contract terms**: Supply contracts specify requirements related to open source license compliance and security, and require suppliers to comply with them.

**Table 4.3: The Complementary Relationship Between ISO/IEC 5230 and ISO/IEC 18974**

| Area | ISO/IEC 5230 (License Compliance) | ISO/IEC 18974 (Security Assurance) | Synergistic Effect |
| --- | --- | --- | --- |
| Risk management | Legal risk management | Security risk management | Integrated management of legal and security risk |
| Information management | License information | Vulnerability information | Integrated information management through the SBOM |
| Organizational structure | Led by the legal team | Led by the security team | Strengthened cooperation through the OSPO |
| Supply chain management | License compliance contracts | Security requirement contracts | Improved management level across the supply chain |

## 4.3 Integrated Implementation Strategy

ISO/IEC 5230 (open source license compliance) and ISO/IEC 18974 (open source security assurance) each address a different aspect, but an organization can implement both standards in an integrated way to create a synergistic effect. This section presents concrete strategies and action plans for effectively integrating the two standards.

1. **Adopting a phased approach**
    - **Implementing ISO/IEC 5230 first**: Implement ISO/IEC 5230 first to build a basic license compliance system. This helps reduce the legal risk associated with open source use and establish a compliance culture within the organization.
    - **Adding ISO/IEC 18974**: After implementing ISO/IEC 5230, introduce ISO/IEC 18974 to strengthen the security management system. This helps effectively manage vulnerabilities in open source components and strengthens the security of the software supply chain.
    - **Establishing an integrated roadmap**: An integrated roadmap can also be established to consider both standards at once and implement them in parallel. In this case, both legal and security aspects can be considered from the initial stage to build a balanced open source management system.
2. **Leveraging common elements**
    - **Integrating policies and processes**: Elements commonly required by both standards, such as the open source usage policy, the SBOM (Software Bill of Materials) management process, and training programs, are integrated and managed together. This helps reduce duplicated work and improve management efficiency.
    - **Integrating tools**: License scanning tools and vulnerability scanning tools are integrated, or tools that allow SBOM data to be shared are used to facilitate information sharing.
3. **Integrating organizational structure and roles**
    - **Using an OSPO (Open Source Program Office)**: Open source-related activities are managed in an integrated way centered on the OSPO. The OSPO is composed of experts from various departments, including legal, security, and development, and supports comprehensive decision-making about open source use.
    - **Clarifying responsibilities and authority**: The responsibilities and authority of each role (e.g., legal team, security team, development team) are clearly defined, and a collaborative framework is established.
4. **Continuous cooperation and information sharing**
    - **Regular meetings**: Regular meetings between the legal, security, and development teams share the latest open source information, threat trends, and issues.
    - **Information sharing platform**: An information sharing platform (e.g., an internal wiki, a collaboration tool) is built where open source-related information can be shared and discussed.
    - **Education and training**: Training programs on open source licensing and security are jointly developed and delivered to all employees.

**Table 4.4: Integrated Implementation Strategy for ISO/IEC 5230 and ISO/IEC 18974**

| Strategy | Description | Action Plan |
| --- | --- | --- |
| Phased approach | Implement ISO/IEC 5230 first, then ISO/IEC 18974 | Step 1: Satisfy the ISO/IEC 5230 requirements 
Step 2: Add the ISO/IEC 18974 requirements |
| Leveraging common elements | Sharing policies, processes, and tools | Integrating the SBOM generation process, integrating training programs |
| Integrating organizational structure | Managing centered on the OSPO | Composing the OSPO with legal, security, and development experts |
| Continuous cooperation and information sharing | Regular meetings, building an information sharing platform | Strengthening cross-team collaboration, improving information accessibility |
