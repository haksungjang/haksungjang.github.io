# Chapter 9. Preparing for an Audit as a Target Company

> Covers how a target company can prepare in advance for an open source audit through its regular compliance activities.

---

LLMS index: [llms.txt](/llms.txt)

---

Passing an open source compliance audit is not difficult, provided you are prepared. But if you only start preparing after an acquiring company has shown interest, passing becomes difficult. These activities need to proceed alongside everyday business and development activities. The goal is to track every open source component the company uses and to honor the open source license obligations that arise from using those components. These same measures also help greatly when a company becomes the subject of a corporate transaction, because they reduce the risk of unexpected problems.

## 9.1 Know What Is in Your Code

Knowing what is in your code is the golden rule of compliance. You need to maintain a complete software inventory of every software component, including its origin and license information. This includes software components the organization built itself, open source components, and components originating from third parties. Most important is having a process to identify and track open source components. A complex compliance program is not always necessary, but five basic elements are required: policy, process, people, training, and tools.

### 9.1.1 Policy and Process

An open source compliance policy is a set of rules governing the management of open source software, covering both use and contribution. Process is the detailed specification of how the company implements these rules day to day. Compliance policies and processes govern various aspects of open source software, including use, contribution, auditing, and distribution.

![An example of an end-to-end open source compliance process](fig8.jpg)

**Figure 8.** An example of an end-to-end open source compliance process, going through the stages of identification, audit, resolution, review, approval, registration, documentation, verification, and disclosure *(source: Linux Foundation, 2018)*

Figure 8 shows an example compliance process. It represents the various stages each software component goes through as part of due diligence while building a product or software stack.

1. Identify all incoming source code.
2. Audit the source code.
3. Resolve issues found in the audit.
4. Complete the appropriate review.
5. Obtain approval for the open source usage.
6. Register the open source in the software inventory.
7. Update product documentation to reflect the open source usage.
8. Verify all steps prior to distribution.
9. Distribute the source code and perform final verification related to distribution.

The output of this process is an open source Bill of Materials (BOM). This BOM can be published together with a written offer that fulfills the legal obligations for the components it contains, along with the relevant copyright, license, and attribution notices. For a detailed discussion of the open source compliance process, refer to the free e-book *Open Source Compliance in the Enterprise*, published by the Linux Foundation.

### 9.1.2 People

At a large company, the open source compliance team is a multidisciplinary group made up of several members whose mission is to ensure open source compliance. The core team, often called the Open Source Review Board (OSRB), consists of representatives from engineering and product teams, one or more legal counsel, and a compliance officer. The extended team consists of a variety of members across departments such as documentation, supply chain, corporate development, IT, and localization, who contribute to compliance efforts on an ongoing basis. At a small company or startup, however, it can be as simple as a single engineering manager supported by legal counsel. Every company is different.

### 9.1.3 Training

Training is an essential component of a compliance program, helping employees clearly understand the policies governing open source software usage. The goal of providing open source and compliance training is to raise awareness of open source policy and strategy, and to build a shared understanding of the issues and facts of open source licensing. It should also address the business and legal risks that arise from including open source software in a product or software portfolio.

Both formal and informal training methods can be used. Formal methods include instructor-led training courses that require employees to pass a knowledge test to complete the course. Informal methods include webinars, brown bag seminars, and presentations delivered as part of new employee orientation sessions.

### 9.1.4 Tools

Open source compliance teams frequently use tools to automate source code audits, find open source code, and identify its licenses. These tools include compliance project management tools, software inventory tools, and source code and license identification tools.

## 9.2 Comply with Your Obligations

Whether intentionally or not, if you have shipped a product that includes open source software, you must comply with the various licenses governing those software components. This is why knowing what is in your code matters: having a complete Bill of Materials makes compliance far easier.

Complying is not a simple task, and it varies by product depending on the licenses and code structure involved. Broadly speaking, complying means the following.

1. Track every use of open source software.
2. Produce a finalized open source Bill of Materials for all software included in the shipping product image.
3. Fulfill the obligations of the open source licenses.
4. Repeat this process every time a software update is distributed.
5. Respond to compliance inquiries promptly and seriously.

## 9.3 Use the Latest Release for Security

One benefit of a comprehensive compliance program is that it becomes easier to find and replace products containing unsafe versions of open source components. Most source code scanning tools now offer the ability to flag disclosed security vulnerabilities in outdated software components. One important consideration when upgrading an open source component is to always confirm that the component retains the same license as the previous version, since open source projects have occasionally changed licenses at a major release.

Companies are encouraged to engage with open source project communities to avoid situations where they end up using a version with a security vulnerability. Actively participating in every open source project you use is neither reasonable nor feasible, so some level of prioritization is needed to identify the most important components. The level of engagement can range from subscribing to mailing lists and joining technical discussions, to contributing bug fixes and small features, to making major contributions. At minimum, it is beneficial for a company's developers working on a particular open source project to subscribe to and monitor that project's mailing list to receive reports on security vulnerabilities and available fixes.

## 9.4 Measure Your Compliance Efforts

The easiest and most effective first step any organization can take, regardless of size, is to participate in the OpenChain Project and achieve "OpenChain Conformant" status. This is done by answering a series of questions, either online or manually. The questions used for OpenChain conformance help confirm that an organization has established a process or policy for open source software compliance. OpenChain is an industry standard similar to ISO 9001. It leaves the precise implementation of process and policy to each individual organization and focuses on the "big picture." OpenChain conformance demonstrates that an open source compliance process or policy exists, and that additional details can be shared when a supplier or customer requests them. OpenChain is designed to build trust between organizations across global supply chains.

The Linux Foundation's Self-Assessment Checklist is a broad checklist that covers compliance best practices as well as the elements a compliance program needs in order to succeed. Companies can use this internal self-assessment checklist to evaluate their compliance against compliance best practices.
