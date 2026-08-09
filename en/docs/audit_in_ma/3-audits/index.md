# Chapter 3. Open Source Audits

> Explains why open source audits are performed, the criteria for deciding whether to commission one, and the inputs and outputs of the audit process.

---

LLMS index: [llms.txt](/llms.txt)

---

Every merger and acquisition (M&A) transaction differs, but the need to verify the impact of acquiring open source obligations remains constant across every deal. An open source audit is performed to understand how deeply the target uses and depends on open source software. It also provides insight into compliance issues, and further allows a look into the engineering practices of the target company.

## 3.1 Why Perform an Open Source Audit?

Open source licenses can impose constraints on how software is redistributed. These constraints may be incompatible with the acquirer's business, so they need to be uncovered early. Examples of how open source software affects the acquired asset include the following.

- Open source licenses typically impose obligations that must be fulfilled when distributing code. One example is the GNU General Public License (GNU GPL), which requires that derivative works or combined works also be provided under the same license. Other licenses require that specific notices be included in documentation, or place constraints on how a product may be promoted.

- Failing to meet open source license obligations can lead to litigation, costly redesigns, product recalls, and reputational damage.

## 3.2 Should You Commission an Open Source Audit?

A frequently asked question is whether an open source audit is even necessary. The answer depends on the company, the purpose of the acquisition, and the size of the source code. For example, in a smaller acquisition, some companies choose only to review the open source bill of materials (BoM) provided by the target (assuming one is provided) and discuss open source practices with the target's engineering leadership. Even when the purpose of the acquisition is talent acquisition, an audit can uncover undisclosed liabilities arising from past license obligations of an already-released product.

## 3.3 Inputs and Outputs

The audit process has one primary input and one primary output (Figure 4). The input to the process is the entire software stack subject to the ongoing merger and acquisition (M&A) transaction. This includes proprietary software, open source, and 3rd party software. The primary output at the end of the process is a detailed open source software bill of materials, which lists the following.

- All open source software used as components, their origin, and the identified license
- All open source snippets used in proprietary or 3rd party software, their source component, and the identified license

![Inputs and outputs of the due diligence process](fig4.jpg)

**Figure 4.** Inputs and outputs of the due diligence process. The full software stack, consisting of proprietary software, 3rd party software, and open source software, is taken as input, and after source code scanning and identification, an open source software bill of materials (BoM) is produced as output *(source: Linux Foundation, 2018)*
