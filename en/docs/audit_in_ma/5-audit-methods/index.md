# Chapter 5. Audit Methods

> Explains the procedures and trade-offs of three audit methods: traditional audits, blind audits, and do-it-yourself (DIY) audits.

---

LLMS index: [llms.txt](/llms.txt)

---

When performing an open source audit, certain capabilities of a tool provide real value to the acquiring company. One of the most important is the ability to find open source code snippets mixed into the target company's proprietary code, and vice versa. Another is the ability to automatically filter false positives from audit results, minimizing the amount of manual work required.

There are three audit methods.

1. Traditional audit. The auditor has full access to all code and performs the audit remotely or on site.
2. Blind audit. The auditor performs the work remotely without ever seeing the source code.
3. Do-it-yourself (DIY) audit. The target company or acquiring company uses a tool to perform most of the actual audit work themselves, with the option for the audit firm to randomly verify the results.

## 5.1 The Traditional Audit Method

This method is called traditional because it is the original way of scanning source code for open source compliance. In a traditional audit, a compliance auditor from a third-party audit firm accesses the source remotely through a cloud system, or by visiting the site directly, and then performs a source code scan.

![The traditional audit method in an M&A transaction](fig5.jpg)

**Figure 5.** The traditional audit procedure in a merger and acquisition (M&A) transaction *(source: Linux Foundation, 2018)*

Figure 5 shows the audit procedure under the traditional audit method. Note that this procedure can vary slightly by service provider. A typical traditional audit procedure follows these steps.

- The auditor sends questions to the acquiring company to better understand the work.
- The acquiring company answers, helping the audit firm better grasp the scope and audit parameters.
- The auditor provides a quote based on the answers.
- The quote is agreed upon. Next, the parties sign a service agreement, a statement of work, a non-disclosure agreement, and so on. (The "Start" in Figures 5, 6, and 7 assumes the point at which all agreements have been signed, i.e., when the audit procedure actually begins.)
- The auditor is granted access to the target's code, either through a secure cloud upload or by visiting the company for an on-site audit.
- The auditor scans the target's source code, cleans up false positives, and evaluates the results.
- The auditor generates a report and delivers it to the client.
- The results are reviewed with the auditor and questions are answered, either by call or in person.

Most audit service providers adopt this method in common. You can get multiple bids for the same audit work and pick the one that best fits your requirements. Following this model requires the target company either to transfer the code to the auditor, or to allow the auditor to visit its office and complete the work on site.

## 5.2 Blind Audits

The blind audit method was pioneered by FOSSID AB, headquartered in Stockholm, to address the confidentiality requirements of M&A transactions. (Here, FOSSID AB refers to the company, and FOSSID refers to the tool itself.)

This company uses its own proprietary technology to perform audits and generate reports without ever seeing the source code. Figure 6 shows the blind audit procedure used by FOSSID AB, designed to keep source code confidential in M&A transactions. One key advantage of a blind audit is that the auditor can complete the review without accessing the source code. Furthermore, with enough care from the acquiring company, it can also provide a high level of confidentiality by keeping the auditor unaware of the target's identity. As far as the author is aware, no other company offering open source compliance services provides this audit method.

![The blind audit procedure for M&A transactions using FOSSID](fig6.jpg)

**Figure 6.** The blind audit procedure using FOSSID. The target company collects and sends only the digital signature of the software using a fingerprint collection tool, and FOSSID AB audits it by matching that signature against an open source database, without ever accessing the source code *(source: Linux Foundation, 2018)*

## 5.3 DIY Audits

A do-it-yourself (DIY) audit gives the acquiring company or the target company time-limited access to a compliance cloud tool so they can run the scan themselves. This allows the audit to be performed internally with full access to the knowledge base and all reporting functions. This approach is particularly attractive to companies with in-house staff experienced enough to interpret scan results and propose remediation procedures. For a company that goes through M&A procedures several times a year, it can quickly become the more cost-effective approach. The audit tool service provider can further secure the integrity of the audit by performing an independent certification to verify the results.

Figure 7 shows this audit method using FOSSID AB's tool. This approach has several advantages. Because it uses internal resources and does not depend on the availability of a third-party auditor, the audit can begin immediately when needed. This approach can shorten the schedule and reduce external cost factors. Because the audit is performed by someone with direct access to the code, all compliance issues can be handled immediately and fixes applied right away. Finally, the audit tool provider can verify the audit to ensure accuracy and completeness. As part of its DIY service, FOSSID AB randomly verifies X percent (X is determined as part of the quote agreement) of the files the target company decides to audit.

![The DIY audit procedure for M&A transactions using FOSSID](fig7.jpg)

**Figure 7.** The do-it-yourself (DIY) audit procedure using FOSSID. The target company performs the scan and audit itself on a time-limited instance of a dedicated web app, FOSSID AB independently verifies a portion of the audited files, and all data is deleted once the period ends *(source: Linux Foundation, 2018)*
