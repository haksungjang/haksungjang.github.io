---
title: "Chapter 4. Estimating Audit Scope"
linkTitle: "4. Estimating Audit Scope"
weight: 40
type: docs
description: >
  Explains the code size and characteristics an auditor must understand to produce an audit
  estimate, and how urgency affects cost.
---

The size, scope, and cost of an audit vary by transaction, and generally increase as the size and complexity of the source code grow. To provide an estimate (cost and duration) for an open source audit, the auditor needs to gain some understanding of the codebase's size and characteristics, as well as the project's urgency.

The first questions an auditor asks relate to code metrics: the size of the source codebase, the number of lines of source code, and the number of files to be audited. The auditor also asks whether the codebase consists solely of source code, or whether it also includes binary files, configuration files, documentation, and other file types. Knowing the file extensions subject to audit can also be helpful to the auditor.

Mature companies generally keep records of the open source components and versions used in their products and projects. This information greatly helps the auditor gauge the expected workload.

Because discussions of audit cost occur early in the process based on size and scope, the acquirer may not have access to all the information described above. At a minimum, the auditor needs to know the number of files to be scanned before proceeding, and any additional information helps refine the estimate further. Once the auditor has gathered enough information to understand the scope of work, urgency also needs to be determined, since it significantly affects the cost of the audit.
