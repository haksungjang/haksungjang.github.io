# Chapter 11. Recommended Compliance-Related Development Practices

> Summarizes development practices that reduce compliance issues, and mistakes that must be avoided.

---

LLMS index: [llms.txt](/llms.txt)

---

Detailed recommendations on how to establish development practices that support open source license compliance activities are already available in a number of publications. This chapter briefly touches on the most important of these practices. Following them can eliminate a substantial share of commonly occurring compliance issues.

## 11.1 Recommended Practices

- Request approval for using open source software before committing code to a product repository.
- Request approval before linking proprietary code to an open source library or vice versa, unless the license of that library code has already been pre-approved under company policy.
- For every file you modify, update a changelog with a one-line description of the date of change, the author, and the change applied.
- Document the interface between the code you write and the open source software. This helps others understand the interaction and clarify compliance-related concerns.
- Save the web page describing the license of a source code package as a PDF, to record the state of the project at the time of download.
- Keep an unmodified copy of the package, along with its license information, in a backup location.
- When upgrading an open source software component, verify that the license has not changed. Licenses can change between versions.
- Verify that the license of a source code package matches what is described on the project's website. If there is a discrepancy, contact the project to clarify it.

## 11.2 Mistakes to Avoid

- Do not remove or alter existing license or copyright information. All such information must be kept intact.
- Do not rename open source components.
- Do not copy and paste open source code into proprietary or 3rd party source code, or vice versa, without prior approval.
- Do not commit open source or 3rd party source code to an internal product source tree without prior approval.
- Do not merge or mix source code that came in under different licenses without proper approval.
- Do not discuss compliance practices with individuals outside the company.
