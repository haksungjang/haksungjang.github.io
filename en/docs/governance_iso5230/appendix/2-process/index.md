# 2. Open Source Compliance Process (Sample)

LLMS index: [llms.txt](/llms.txt)

---

OOO Corporation (hereinafter "the Company") actively utilizes open source software (hereinafter "open source") while developing products and services that include software. The Company must carry out activities to comply with the obligations imposed by open source licenses when distributing software, and this is called open source compliance.

## 1. Process for Software Product Development/Distribution

The open source compliance process defines the procedures that must be performed to comply with open source license obligations at each development stage as the Company develops and distributes software products and services. All members involved in software product development/distribution comply with the following 10 steps of the open source compliance process.

![general-osc-process](general-osc-process.png)

### 1. Identification of Open Source<sub>Identification of Open Source</sub>
The development department complies with the following during the software design stage.

- While designing the software, identify the anticipated open source usage status and check the licenses.
- Check the obligations for each open source license. License-specific obligations can be found in the Company's open source license guide.
- Design the software considering the source code disclosure scope of each open source license.

The Open Source Program Manager writes and publishes a guide on the obligations, restrictions, and rights of major open source licenses so that development departments across the company can reference it.

The development department marks copyright and license notices in the source code in accordance with company rules. The Company's rules for copyright and license notation within source code can be found on the following page. : (insert_link)

When reviewing the adoption of new open source, the development department first identifies the license. It checks the license obligations, restrictions, and rights according to the Company's open source license guide. If the license is not covered by the Company's open source license guide, the department inquires with the Open Source Program Manager about whether adoption is possible and any precautions. The inquiry is made by creating a Jira Ticket.

The Open Source Program Manager analyzes the open source license obligations and guides the software development organization accordingly.

- If there are questions, advice is requested from the legal officer to provide clear guidance.
- Newly analyzed license information is reflected in the company-wide license guide.

### 2. Auditing Source Code<sub>Auditing Source Code</sub>

The development department provides the source code according to the infrastructure officer's guidance and requests an open source check.

The infrastructure officer performs the open source check using an open source analysis tool and generates the open source BOM.

The Open Source Program Manager reviews whether the open source license obligations can be met and whether there are open source license conflicts, and if there are issues, requests the development department to resolve them. Issues are created as Jira Tickets and assigned to the development department.

### 3. Resolving Issues<sub>Resolving Issues</sub>

The development department resolves all issues found during the source code auditing stage. It takes actions such as removing the problematic open source or replacing it with open source under a different license.

Once the development department resolves all identified issues, it resolves the Jira Ticket issue and requests a re-review.

### 4. Reviews<sub>Reviews</sub>

The Open Source Program Manager reviews whether all issues have been properly addressed. If necessary, the source code audit is performed again using the open source analysis tool.

### 5. Approval<sub>Approval</sub>

The Open Source Program Manager gives final approval or rejection of whether the open source compliance procedure was properly performed. In case of rejection, an explanation of the reason and a suggested method of correction are proposed to the development department.

### 6. Registration<sub>Registration</sub>

The Open Source Program Manager finalizes the BOM for tracking the list of open source used in each version of the software.

The infrastructure officer registers the finalized BOM in the system. The BOM includes the list of open source contained in the Supplied Software and the following information.

- The name and version of the product (or service) of the Supplied Software
- List of open source
  - Open source name / version
  - Open source license


### 7. Notices<sub>Notices</sub>

The Open Source Program Manager generates an open source notice to comply with the notice obligation. The open source notice includes the following items.

- Open source contact for open source-related inquiries
- Notice content for each open source
  - Copyright
  - Open source license name
  - Copy of the open source license
  - (if applicable) a Written Offer to obtain a copy of the source code

The Open Source Program Manager generates the open source notice and delivers it to the development department. If source code disclosure is required at this time, the department guides the development department on how to collect the source code to be disclosed.

The development department encloses the open source notice when distributing the product. For products with a screen, measures are taken so users can check it through a menu. (e.g., App > Menu > Settings > Copyright Information > Open Source Licenses)

If the development department has used open source under a license that requires source code disclosure, such as GPL or LGPL, it checks the scope of source code disclosure and collects the source code to be disclosed.

- The source code collected to comply with license obligations such as GPL and LGPL must match the source code that composes the binary installed on the product. That is, building the collected source code must produce the same binary as the one installed on the product.

### 8. Pre-Distribution Verifications<sub>Pre-Distribution Verifications</sub>

The development department submits the following artifacts to demonstrate that open source compliance activities were properly performed.

1. The final open source notice included in the product
2. Materials confirming that the open source notice is included in the product (e.g., a screen capture image showing the open source notice)
3. (if applicable) the source code to be disclosed (submitted compressed into a single file)

The Open Source Program Manager reviews the materials submitted by the development department to confirm there are no issues.

### 9. Distribution<sub>Distribution</sub>

The Open Source Program Manager submits the compliance artifacts submitted by the development department to the infrastructure officer.

The infrastructure officer registers the compliance artifacts on the Company's open source distribution site.

### 10. Final Verifications<sub>Final Verifications</sub>

The Open Source Program Manager conducts a comprehensive check, including whether the compliance artifacts were properly registered on the Company's open source portal without issues and whether they can be downloaded externally without problems.

## 2. External Inquiry Response Process
Responding quickly and accurately to external open source compliance inquiries can greatly reduce the risk of escalation to litigation. To this end, the Company complies with the following process to respond to external open source compliance inquiries.

![general-inquiry-process](general-inquiry-process.png)

### 1. Acknowledge<sub>Acknowledge</sub>
Upon receiving an inquiry, the Open Source Program Manager immediately notifies the requester that the inquiry has been received. At this time, the expected date of action is also communicated. Since it is important to accurately understand the requester's intent, additional clarification is requested if the inquiry is unclear.

The main types of inquiries and requests that require a response are as follows.

- Inquiries about whether open source is used in a specific product or service
- Requests for source code under a GPL or LGPL license mentioned in a Written Offer
- Requests for explanation and source code disclosure for open source found in a product but not specified in the open source notice
- Requests to provide files missing from source code disclosed under GPL, LGPL, and similar obligations, and how to build it
- Requests for copyright attribution

The Open Source Program Manager creates a Jira Issue for the received request and records all response activities in detail.

### 2. Inform<sub>Inform</sub>

The Open Source Program Manager informs the requester that the Company is faithfully performing open source compliance and is investigating the requester's inquiry. It is advisable to notify the requester whenever there is an update to the progress of the internal investigation.

### 3. Investigate<sub>Investigate</sub>

The Open Source Program Manager conducts an internal investigation of the request. Whether the compliance process was properly performed for the version of the product in question is confirmed through the BOM and documented review history. Advice is requested from the legal officer if needed.

If confirmation is needed from a specific development department, the Open Source Program Manager requests the development department to investigate. The development department that receives the investigation request immediately checks whether there is a problem with the compliance artifacts and reports the results to the Open Source Program Manager.

### 4. Report<sub>Report</sub>

The open source compliance officer completes the internal investigation within the expected action date and notifies the requester of the results.

- If the requester's inquiry was a mistaken claim due to a misunderstanding, the requester is notified of this without further action, and the case is closed.
- If the issue is confirmed, the requester is informed of the exact method and timing for fulfilling the obligations of the relevant open source license.

### 5. Rectify<sub>Rectify</sub>

If an actual compliance problem is found during the internal investigation, the relevant development department performs all procedures necessary to resolve the compliance issue.

### 6. Report<sub>Report</sub>

After the problem is resolved, the requester is notified immediately, and the best available method to confirm the resolution is provided.

### 7. Improve<sub>Improve</sub>

When a compliance problem occurred, the case is reviewed at an OSRB meeting, the circumstances leading to the problem are identified, and the process is improved to prevent recurrence.
