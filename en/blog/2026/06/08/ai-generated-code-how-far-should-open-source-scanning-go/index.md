# AI-Generated Code: How Far Should Open Source Scanning Go?

> Examines whether AI-generated code needs snippet-level open source license scanning, laying out the decision criteria from public sources and distinguishing this from the security vulnerability angle.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert">


This post was written using Claude Code, and the key facts cited were cross-checked against public sources.
</div>


<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">Notice</div>


This post reflects the author's personal analysis and is not legal advice. The facts cited were verified against public sources, but specific matters should be reviewed by a lawyer or other qualified professional.
</div>


## One point to clarify first

It is hard to answer this question directly with a "yes" or "no." As I will explain point by point below, what determines the answer is not AI itself. AI coding increases the rate at which code fragments not declared as packages flow in, but it does not change the conditions under which license obligations arise. So rather than asking "does scanning still matter in the age of AI," it helps more to ask "under what conditions does snippet-level scanning become more important, and under what conditions does it become less important."

## Snippet scanning and SCA are different things

First, the terms need to be separated so the discussion doesn't get tangled.

| Category | What it looks at | How it catches code that came in |
|---|---|---|
| Dependency-level SCA | Components declared through a package manager | Manifests such as `package.json`, `pom.xml`, and build artifacts |
| Snippet-level matching | Fragments within the source code body | Code fragments that entered via copy-paste or AI generation |

Software Composition Analysis (SCA) refers broadly to the activity of identifying open source that has entered the code and managing its vulnerabilities and licenses. Most SCA looks at declared dependencies, as in the first row of the table above. Snippet-level matching is a separate feature found in only some commercial tools; it compares the source code body against a large number of open source projects to find the origin of fragments that are not declared as packages. What this post addresses is not SCA as a whole but this snippet matching.

## How much legal risk actually exists

Let's start with cases where AI code snippets led to license violation disputes.

The most widely known case is the Copilot class action lawsuit that open source developers filed against GitHub, Microsoft, and OpenAI in November 2022. In May 2023, the copyright infringement claim was dismissed for lack of concrete evidence of copying, and in July 2024, the claim under Section 1202(b) of the Digital Millennium Copyright Act (DMCA) was also dismissed. This section prohibits removing copyright management information attached to an original work, and the court did not accept the claim on the grounds that the Copilot output was not sufficiently identical to the original <a id="a2-ref-1"></a>[A2](#a2). Of the 22 claims originally filed, two remain: open source license violation and breach of contract <a id="a2-ref-2"></a>[A2](#a2)·<a id="a3-ref-1"></a>[A3](#a3).

This carries facts that can be read in two directions.

On one hand, the defendants in disputes so far have all been vendors that built the AI tools, and no publicly reported case exists of an adopting company being sued solely for using AI-generated code <a id="c1-ref-1"></a>[C1](#c1). Also, in September 2023, Microsoft announced through its Copilot Copyright Commitment that it would cover defense costs and damages if a paying commercial customer is sued by a third party over intellectual property arising from Copilot output. This comes with the condition that the customer must not disable the product's built-in filtering features and must not intentionally generate infringing content <a id="b1-ref-1"></a>[B1](#b1)·<a id="c5-ref-1"></a>[C5](#c5).

On the other hand, the legal question has not been settled. The DMCA issue above has gone up to the Ninth Circuit Court of Appeals as an interlocutory appeal — where a specific issue is contested in a higher court before the trial court's judgment — and as of June 2026, no ruling has come down, and the trial court proceedings remain paused <a id="a1-ref-1"></a>[A1](#a1). The absence of reported precedent does not mean there is no risk.

## When do license obligations arise

One distinction needs to be made here. Whether you get sued and whether you have an obligation to comply with a license are different questions. Even if no one files a lawsuit, the obligation to comply with an open source license remains. And when that obligation is triggered matters.

The copyleft obligation of GPL-family licenses, which requires disclosing source code, arises when software is distributed. Merely running software internally is use, not distribution, so no obligation arises <a id="c3-ref-1"></a>[C3](#c3)·<a id="c4-ref-1"></a>[C4](#c4). Pure SaaS that does not deliver code is likewise outside GPL obligations for the same reason. Two caveats apply here.

- AGPL is a stricter license that treats even providing a network service as distribution. If you use a component licensed under AGPL, the source disclosure obligation arises even if you provide it only as a service without directly delivering the code <a id="c3-ref-2"></a>[C3](#c3). Such components can be managed by excluding them through internal policy.
- "Internal" must mean use limited to the company's own employees, and if distribution occurs later — through an acquisition or open-sourcing — the issue arises at that point.

Whether short code is even copyrightable is also worth examining. A few lines of functional code may be too trivial an amount of copying to pursue (de minimis), or may fall outside protection because there is effectively only one way to express it (merger doctrine) <a id="a4-ref-1"></a>[A4](#a4)·<a id="a5-ref-1"></a>[A5](#a5). That said, this is a case-by-case determination, and longer, creative code blocks are protected, so it is hard to say all snippets are free to use.

In practice, it is common for small fragments to come with obligations attached. Code from Stack Overflow, which developers frequently copy, is licensed under CC BY-SA, carrying attribution and share-alike obligations. According to one study, the proportion of GitHub projects that used this code in compliance with the license was at most 1.8% <a id="c6-ref-1"></a>[C6](#c6). This means even small fragments can carry license obligations, and that obligation is widely not observed.

## Do standards require snippet scanning

OpenChain ISO/IEC 5230, the international standard for open source license compliance, focuses on defining where the compliance process sits, how roles and responsibilities are allocated, and how the process is sustained <a id="a6-ref-1"></a>[A6](#a6). It is a non-prescriptive standard that sets what must be achieved while leaving the specific method to the organization, so it does not mandate a particular technique such as snippet scanning <a id="a6-ref-2"></a>[A6](#a6)·<a id="a7-ref-1"></a>[A7](#a7). What the standard requires is identifying third-party components and maintaining a list of them — a Software Bill of Materials (SBOM). What matters for meeting the standard is grasping which components entered the code; it does not require analyzing the origin of every single code fragment. In fact, many widely used SCA tools on the market operate at the dependency level only, without snippet matching.

This fact can be read two ways. It means the standard can be met without snippet scanning, since the standard does not require it, and at the same time it means an area remains that the standard does not cover. Dependency-level scanning cannot see fragments that were copied or AI-generated without being declared as a package. Snippet matching is the feature that fills exactly that gap, and some organizations perform it for more thorough intellectual property management.

## Under what conditions does it become more important

How much weight snippet scanning deserves depends on two conditions a company faces.

First, whether the company delivers code or binaries directly to customers. When code leaves the company — as with on-premises installed products, mobile apps, SDKs, or embedded device firmware — this counts as distribution and can trigger copyleft obligations. Pure SaaS that does not deliver code carries a smaller burden.

Second, whether the company undergoes external verification — situations where someone outside the company actually checks the origin of the code, such as M&A due diligence, a large customer's security audit, regulatory requirements, or an SBOM submission that demands snippet-level detail.

The more these two overlap, the greater the chance that a latent obligation surfaces as an actual cost. Even if code is delivered, if there is no verification trigger, the risk stays latent, and if code is not delivered, the obligation itself rarely arises. Neither condition has anything to do with whether AI is used. AI coding is a factor that increases the inflow volume once a condition holds, not a factor that creates the condition.

## Looking at it by company condition

Placing the two conditions above on two axes yields four quadrants.

![A quadrant chart with two axes: whether code is delivered outside the company, and whether it undergoes external verification. Snippet scanning matters most only when both apply; when code is not delivered, it matters little regardless of verification](./snippet-decision-matrix.png)

**Figure 1.** How much weight snippet scanning deserves, by condition

The top-right quadrant carries the greatest burden: code leaves the company, creating a license obligation, and there is also a trigger — such as M&A due diligence or a customer audit — that actually looks into that obligation. In the top-left, even if an obligation arises, there is no one to check it, so it stays latent. In the bottom two quadrants, there is no distribution at all, so an obligation rarely arises to begin with.

This diagram is a starting point for judgment, not a definitive answer. Even within the same quadrant, the choice can vary depending on the nature of the code involved, the types of licenses used, and the company's risk tolerance.

## Embedded software is a different case

Everything so far has assumed software built through a package manager. Software that runs as embedded or firmware code — routers, set-top boxes, IoT devices, automotive controllers — is a different case. It is mostly written in C/C++, and open source is often copied in as raw source directly into the project without a manifest. In this case, dependency-level SCA has no manifest to read and can barely see the open source at all.

One distinction is needed. For large components brought in wholesale, such as the Linux kernel or BusyBox, the company is usually aware it is using them. That is not a discovery problem but a matter of whether the source disclosure obligation is being met. Where snippet scanning is needed is different: small code fragments pulled in bits and pieces from various open source projects that no one has listed anywhere. Finding these fragments, which dependency-level SCA cannot see, is the job of snippet scanning.

So in embedded software, snippet scanning is not a conditional supplement but closer to a basic means of finding undeclared open source fragments.

## Filtering code before it comes in

Apart from scanning after the fact, there is also a way to block problem code before it comes in. GitHub Copilot has a setting that blocks suggestions matching public code verbatim. Suggestions that match public code exactly at a certain length (on average, roughly 150 characters) or longer are simply not shown <a id="b2-ref-1"></a>[B2](#b2)·<a id="c2-ref-1"></a>[C2](#c2). GitHub has stated that verbatim duplication over 150 characters occurs at about the 1% level, though independent studies report higher figures depending on context. Either way it is not zero, but turning on this setting reduces the inflow of fragments with unclear provenance. It costs almost nothing, and it is also a precondition for the vendor indemnification discussed earlier.

This setting overlaps in purpose with after-the-fact snippet scanning. One finds fragments after they come in; the other blocks them before they come in. Which of the two to use, and to what extent, is a matter to decide by weighing the conditions above together with cost.

Putting the inflow paths and inspection methods covered so far in one place looks like this.

![Three paths through which code enters, and the methods that catch each one. Code declared through a package manager is caught by dependency-level SCA, but fragments that entered via copy-paste or AI generation, and embedded code copied in as raw source without a manifest, are caught only by snippet matching](./code-inflow-coverage.png)

**Figure 2.** Code inflow paths and the methods that catch them

Where the blind spot of dependency-level SCA lies, and how snippet matching fills that spot, is the starting point for this judgment.

## Criteria for the decision

There is a reason this decision is not simple. Snippet matching is effectively the only way to find code fragments that entered without being declared as a package, whether copied or AI-generated. Neither dependency-level SCA nor code-filtering settings catch all of those fragments. So a small residual area remains that only snippet matching fills. Yet at many companies, that small area rarely translates into actual loss, and snippet scanning costs tool spend and review effort. In the end, this comes down to deciding whether to spend that much to guard against this small risk.

There are four points to examine when making this decision.

- **Does the company send code outside the organization?** — The more it does, the greater the room for a copyleft obligation to actually arise.
- **Does the company undergo external verification?** — M&A due diligence or a customer audit can surface an obligation that had been buried until then.
- **How much license risk is the company willing to accept?** — There is no reported litigation precedent, but the legal question is not settled either. How to weigh this uncertainty is up to the company to decide.
- **Are other inspection measures already in place?** — If dependency-level SCA, an AI tool setting that blocks suggestions matching public code verbatim, and a policy excluding AGPL components are already running, the additional share that snippet scanning would catch shrinks accordingly.

One more point is worth adding. Snippet scanning does not have to be decided as an all-or-nothing choice, always on or never done. The occasions when an outside party actually looks into code provenance are largely predictable: M&A due diligence or a large customer's audit. So one option is to run only dependency scanning and the blocking setting normally, and undergo a one-time snippet scan when such an occasion is anticipated.

Weighing the four points above and this operating approach against your own company's situation, the answer to how much weight to give snippet scanning will differ from company to company. The exception is embedded software built without a manifest. There, snippet scanning is not a conditional supplement but a basic means of finding undeclared open source fragments.

## Security vulnerabilities are a separate matter

Everything up to this point has been about licensing. Security vulnerabilities are a different axis, and the conditional conclusions above should not simply be applied here. If vulnerable open source is present in the code, it is dangerous whether or not it is distributed and whether or not it is audited, because even code that stays internal-only or sits in a pure SaaS backend is exposed to attack. So vulnerability inspection is broadly needed at nearly every company.

Tools handling security inspection fall broadly into two kinds.

- **Dependency-level SCA** — Looks at the name and version of declared open source libraries and checks them against known vulnerability (CVE) lists <a id="d1-ref-1"></a>[D1](#d1). Known vulnerabilities in libraries that AI pulled in are caught here.
- **SAST (static analysis)** — Finds risky coding patterns in the source code itself, regardless of where the code came from. This is where the primary security risk of AI code lies. One study found vulnerabilities in about 40% of 1,689 programs generated by Copilot <a id="d2-ref-1"></a>[D2](#d2).

Whether code was copied in or generated by AI, security vulnerability inspection is no different from any other code. SAST catches risky coding patterns in the code itself, and dependency-level SCA catches known vulnerabilities in libraries that were pulled in. Snippet scanning is a feature for finding license origin, so it is not a tool used for security inspection.

One exception worth noting: the rare case where code with a known vulnerability was copied in verbatim, yet it triggers no SAST pattern and appears in no dependency list. Catching this requires not the snippet feature that finds license origin, but an inspection that directly compares a vulnerable-code signature built from a CVE patch against your own code — vulnerable code clone detection <a id="d3-ref-1"></a>[D3](#d3). Academic tools and some commercial tools provide this.

## Sources

<a id="a1"></a>**A1.** BakerHostetler (2025). *Doe v. GitHub, Inc. — The Copilot Litigation*. <https://www.bakerlaw.com/the-copilot-litigation/> (accessed: 2026-06-08). — Claim-by-claim progress of the Copilot class action and its status pending before the Ninth Circuit Court of Appeals. <a href="#a1-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="a2"></a>**A2.** Claburn, T. (2024). *Judge dismisses DMCA copyright claim in GitHub Copilot suit*. The Register, 2024-07-08. <https://www.theregister.com/2024/07/08/github_copilot_dmca/> (accessed: 2026-06-08). — Dismissal of the DMCA §1202(b) claim; 2 of the original 22 claims remain (license violation, breach of contract). <a href="#a2-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="a3"></a>**A3.** Pearl Cohen (2024). *Copyright Claims Against GitHub, Microsoft, and OpenAI Largely Dismissed*. <https://www.pearlcohen.com/copyright-claims-against-github-microsoft-and-openai-largely-dismissed/> (accessed: 2026-06-08). — Overview of the dismissal of most claims and the claims that remain. <a href="#a3-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="a4"></a>**A4.** Goldstein Patent Law. *Understanding the Copyright Merger Doctrine*. <https://www.goldsteinpatentlaw.com/copyright-merger-doctrine/> (accessed: 2026-06-08). — The merger doctrine, which denies copyrightability to functional code. <a href="#a4-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="a5"></a>**A5.** NYU Journal of Intellectual Property & Entertainment Law. *Clarifying the De Minimis Doctrine in Copyright Law*. <https://jipel.law.nyu.edu/clarifying-the-de-minimis-doctrine-in-copyright-law/> (accessed: 2026-06-08). — The de minimis doctrine, which does not treat trivial copying as infringement. <a href="#a5-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="a6"></a>**A6.** OpenChain Project. *OpenChain ISO/IEC 5230 — License Compliance*. <https://openchainproject.org/license-compliance> (accessed: 2026-06-08). — That the standard defines process and roles but does not mandate a specific technique such as snippet scanning. <a href="#a6-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="a7"></a>**A7.** ISO. *ISO/IEC 5230:2020 — Information technology — OpenChain Specification*. <https://www.iso.org/standard/81039.html> (accessed: 2026-06-08). — Bibliographic information for the standard text. <a href="#a7-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="b1"></a>**B1.** Microsoft (2023-09-07). *Microsoft announces new Copilot Copyright Commitment for customers*. <https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/> (accessed: 2026-06-08). — Intellectual property indemnification for paying commercial customers and the condition of keeping the built-in filtering feature enabled. <a href="#b1-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="b2"></a>**B2.** GitHub. *GitHub Copilot* (product page). <https://github.com/features/copilot> (accessed: 2026-06-08). — The existence and operation of the setting that blocks matches with public code. <a href="#b2-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="c1"></a>**C1.** TechTarget. *AI lawsuits explained: Who's getting sued?*. <https://www.techtarget.com/whatis/feature/AI-lawsuits-explained-Whos-getting-sued> (accessed: 2026-06-08). — Evidence that lawsuit defendants have been concentrated among vendors, with no reported cases of adopting companies being sued. <a href="#c1-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="c2"></a>**C2.** Microsoft Community Hub. *Demystifying GitHub Copilot Security Controls*. <https://techcommunity.microsoft.com/blog/azuredevcommunityblog/demystifying-github-copilot-security-controls-easing-concerns-for-organizational/4468193> (accessed: 2026-06-08). — The roughly 150-character match threshold for the public-code-match blocking setting and the roughly 1% duplication rate. <a href="#c2-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="c3"></a>**C3.** Mend.io. *The SaaS Loophole In GPL Open Source Licenses*. <https://www.mend.io/blog/the-saas-loophole-in-gpl-open-source-licenses/> (accessed: 2026-06-08). — The distribution trigger for copyleft, why internal use and SaaS do not qualify, and the AGPL Section 13 exception. <a href="#c3-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="c4"></a>**C4.** Revenera. *Understanding the SaaS Loophole in GPL*. <https://www.revenera.com/blog/software-composition-analysis/understanding-the-saas-loophole-in-gpl/> (accessed: 2026-06-08). — Additional support on the distribution trigger and the SaaS exception. <a href="#c4-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="c5"></a>**C5.** TechTarget. *Microsoft Copilot Copyright Commitment explained*. <https://www.techtarget.com/searchenterprisedesktop/tip/Microsoft-Copilot-Copyright-Commitment-explained> (accessed: 2026-06-08). — Additional support on the scope and conditions of the indemnification. <a href="#c5-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="c6"></a>**C6.** Baltes, S. & Diehl, S. (2019). *Usage and Attribution of Stack Overflow Code Snippets in GitHub Projects*. Empirical Software Engineering, arXiv:1802.02938. <https://arxiv.org/abs/1802.02938> (accessed: 2026-06-08). — An empirical study finding that the rate of license-compliant use of Stack Overflow code (CC BY-SA) in GitHub projects was at most 1.8%. <a href="#c6-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="d1"></a>**D1.** Cycode. *What Is Software Composition Analysis (SCA)?*. <https://cycode.com/blog/what-is-software-composition-analysis-sca/> (accessed: 2026-06-08). — How SCA finds vulnerabilities by checking components and versions against CVE/NVD. <a href="#d1-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="d2"></a>**D2.** Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2022). *Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions*. IEEE S&P 2022, arXiv:2108.09293. <https://arxiv.org/abs/2108.09293> (accessed: 2026-06-08). — Vulnerabilities in about 40% of 1,689 programs generated across 89 scenarios. <a href="#d2-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

<a id="d3"></a>**D3.** Kim, S., Woo, S., Lee, H., & Oh, H. (2017). *VUDDY: A Scalable Approach for Vulnerable Code Clone Discovery*. IEEE S&P 2017. <https://seulbae-security.github.io/pubs/vuddy-sp17.pdf> (accessed: 2026-06-08). — The problem of vulnerabilities propagating through copied code and copies remaining unpatched even after an upstream patch, and detection of this. <a href="#d3-ref-1" onclick="event.preventDefault(); history.back(); return false;" title="Return to text">↩</a>

---

*Research as of: 2026-06-08*
