# 5. Training

LLMS index: [llms.txt](/llms.txt)

---

## 1. Training

No matter how excellent the policy and process an enterprise builds, they are useless if none of its employees pay any attention to them. For open source policy and process to work effectively within an enterprise, employee training is essential.

An enterprise must provide practical means, such as training and internal wikis, so that every program participant is aware that an open source policy exists within the organization and can carry out the necessary activities. Here, program participants refers to all employees involved in the enterprise's software development, distribution, and contribution activities, including software developers, release engineers, and quality engineers.

To this end, the ISO standards commonly require a documented procedure for communicating the open source policy, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.1.1.2 - A documented procedure that makes program participants aware of the existence of the open source policy (e.g., via training, internal wiki, or other practical communication method).<br>`A documented procedure that makes program participants aware of the existence of the open source policy (e.g., via training, internal wiki, or other practical communication method)`

</div>



<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



* 3.1.1.2: A documented procedure to make Program Participants aware of the Security Assurance policy.<br>`A documented procedure to make Program Participants aware of the Security Assurance policy.`

</div>


Many enterprises publish their open source policy document on an internal wiki site so that any employee can check what they need. In addition, they mandate open source policy training during new hire onboarding, and provide periodic training to program participants once a year or once every two years, so that every program participant is aware that the open source policy exists.

An enterprise must write up these methods and include them in the open source policy document, as in the example below.

```
5. Training and Assessment

All members holding a role defined in Chapter 4 must complete the advanced open source training course offered on the [Learning Portal]. This ensures familiarity with the open source policy, the related training policy, and how to look it up. Training records and assessment results are retained on the [Learning Portal] for at least 3 years.


```

An enterprise must make program participants aware of its open source policy, its open-source-related objectives, how participants can contribute to making the open source program effective, and the implications of failing to comply with program requirements. To this end, the enterprise must provide training, conduct assessments to confirm that program participants have correctly understood these points, and document and retain the assessment results.

The ISO standards commonly require documented evidence showing that program participants' awareness has been assessed, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.1.3.1 - Documented evidence of assessed awareness for the program participants - which should include the program's objectives, one's contribution within the program, and implications of program non-conformance.<br>`Documented evidence that the program participants' awareness of the following has been assessed: the program's objectives, how participants contribute within the program, and the implications of program non-conformance`

</div>



<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



* 3.1.3.1: Documented Evidence of assessed awareness for the Program Participants - which should include the Program's objectives, one's contribution within the Program, and implications of Program non-conformance.<br>`Documented evidence that the program participants' awareness of the following has been assessed: the program's objectives, how participants contribute within the program, and the implications of program non-conformance.`

</div>



Accordingly, an enterprise can include content such as the following example in its open source policy.

```
1. Purpose

(1) Purpose of the Policy 

This policy provides the following principles for the entire organization involved in software development, service, and distribution at OOO Corporation (hereinafter "the Company") to properly use open source software (hereinafter "open source").

1. Principles of open source compliance / security assurance
2. Principles for contributing to external open source projects
3. Principles for releasing internal projects as open source

These principles provide a way for every member of the Company to understand the value of open source, use open source correctly, and contribute to the open source community.

Every member of the Company can check the open source policy at the following link on the internal wiki: [internal_link]

(2) Consequences of Non-Compliance
Failure to comply with this policy may result in the following situations.

- The Company may receive external requests for open source license compliance.
- The Company may be forced to unintentionally disclose source code it developed.
- The Company may be sued by open source copyright holders.
- The Company may be fined for copyright infringement or breach of contract, or ordered to halt product sales.
- The Company's reputation may be damaged.
- The Company may breach a contract with a supplier and be subject to a claim for damages.
- The Company may be exposed to a serious security incident, causing substantial harm to the Company.

For these reasons, the Company regards violations of the open source policy seriously, and members or organizations that violate it may be subject to disciplinary action.

(3) How Members Can Contribute

Every member of the Company can contribute to the effectiveness of this policy and to improving the Company's compliance level by understanding the rationale and content of this policy and faithfully carrying out the required activities.

```

Assessment is explained in more detail again below.

Open source training also includes content on the open source contribution policy. Even if an enterprise has created an open source contribution policy, if internal members are unaware that it exists, there is a risk that indiscriminate contribution activity could cause harm to both individuals and the company.

To address this, the ISO/IEC 5230 standard requires a documented procedure that makes all program participants aware of the existence of the open source contribution policy, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.5.1.3 - A documented procedure that makes all program participants aware of the existence of the open source contribution policy (e.g., via training, internal wiki, or other practical communication method).<br>`A documented procedure that makes all program participants aware of the existence of the open source contribution policy (e.g., via training, internal wiki, or other practical communication method)`

</div>


Accordingly, an enterprise must provide open source training so that all in-house developers are aware that the open source contribution policy exists.

Creating training materials from scratch can also be difficult for someone new to the role. To help with this difficulty, NCSOFT made its internal open source training materials available to anyone by publishing the lesson slides (PPT) and lecture scripts on GitHub.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/5-training/ncsofttraining_hu_99d8b656159f9e27.png" width="900" height="483">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>https://github.com/ncsoft/oss-basic-training</i></center>

</p>
</figcaption>
</figure>


Additionally, Kakao, a leading domestic platform company, has also made its open source training materials for in-house developers publicly available for anyone to view.


<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/5-training/kakaotraining_hu_2f60a795ba2987ca.png" width="900" height="507">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>http://t1.kakaocdn.net/olive/assets/opensource_guide_kakao.pdf</i></center>

</p>
</figcaption>
</figure>


If an enterprise has not yet created its own training materials, making use of the open source training materials from these leading enterprises is also a good approach.

## 2. Assessment

Once an enterprise has assigned an owner for each role, it must confirm that the assigned owner is qualified to perform the role based on education, training, and experience. Program participants with insufficient competency must also be given training to build sufficient competency. The enterprise must then assess whether each participant has the required competency and retain the results.

To this end, the ISO standards commonly require documented evidence that program participants' competency has been assessed, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.1.2.3 - Documented evidence of assessed competence for each program participant.<br>`Documented evidence of assessed competence for each program participant`

</div>



<div class="alert alert-warning" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 18974 - Security Assurance</div>



* 3.1.2.4 - Documented evidence of assessed competence for each Program Participant; <br>`Documented evidence of assessed competence for each Program Participant`

</div>


Accordingly, an enterprise must carry out training and assessment and retain the results, as follows.

1. The enterprise provides training so that each participant can acquire the necessary competencies.
2. An assessment is conducted based on the training content.
3. The assessment results are retained by the enterprise's training system or HR department.

When there are hundreds or more program participants, making delivering training difficult, using the enterprise's online training and assessment system is also a good approach.

Content such as this can be included in an enterprise's open source policy as follows.


```
4. Roles, Responsibilities, and Competencies

To ensure the effectiveness of this policy, the roles and responsibilities and the competencies required of the owner of each role are defined as follows.

The responsible organization/owner and the required competency level for each role are defined in [Appendix 1. Assigned Owners].


5. Training and Assessment

All members holding a role defined in Chapter 4 must complete the advanced open source training course offered on the [Learning Portal]. This ensures familiarity with the open source policy, the related training policy, and how to look it up. 

Training records and assessment results are retained on the [Learning Portal] for at least 3 years.


```


## 3. Open Source License Guide

To properly comply with open source licenses, one must accurately know the requirements of each open source license. However, since it is difficult for individual software developers to grasp all of this on their own, it is advisable for the Open Source Program Manager to summarize the requirements and cautions for common use cases of frequently used open source licenses and share them within the company.

The open source license guide should include the requirements for common open source license use cases, enabling development teams to properly comply with license obligations while using open source.

To this end, the ISO/IEC 5230 standard requires a documented procedure for handling common open source license use cases for the open source components within software to be distributed, as follows.

<div class="alert alert-success" role="alert"><div class="h4 alert-heading" role="heading">ISO/IEC 5230 - License Compliance</div>



* 3.3.2.1 - A documented procedure for handling the common open source license use cases for the open source components of the supplied software.<br>`A documented procedure for handling the common open source license use cases for the open source components of the supplied software`

</div>


To handle open source license use cases, a license guide organized by open source license is needed. For a general guide to open source licenses and a summary of license obligations, the [License Guide](https://www.olis.or.kr/license/licenseGuide.do) provided by the Korea Copyright Commission can be referenced.

The [Obligations by License](https://sktelecom.github.io/guide/use/obligation/) document within SK telecom's open source guide is also a good resource.


![SK Telecom's open source guide site explaining notice and modification obligations when redistributing GPL-2.0 source](sktlicenseguide.png)
[https://sktelecom.github.io/guide/use/obligation/gpl-2.0/](https://sktelecom.github.io/guide/use/obligation/gpl-2.0/)

An enterprise must provide the open source license guide in a location that members can easily access and reference.


## 4. Awareness-Raising Activities

To continuously raise program participants' awareness of open source license compliance and security assurance, the following activities are carried out:

### (1) Regular Newsletter Publication

- The Open Source Program Manager publishes an open-source-related newsletter once a month.
- The newsletter includes the latest open source trends, license compliance cases, security vulnerability information, and more.
- It is distributed by email to all program participants and also posted on the internal intranet.

### (2) Workshops and Seminars

- Open-source-related workshops or seminars are held quarterly.
- External experts are invited to give talks on open source licenses, security, and the latest technology trends.
- Program participants are encouraged to attend, and attendance records are kept.

### (3) Open Source Contribution Encouragement Program

- A program encouraging program participants to contribute to external open source projects is run.
- An incentive system for contribution activity is established, and outstanding contributors are selected and rewarded quarterly.
- Contribution activities are shared within the company and reflected in performance evaluations.

## 5. Measuring and Improving Training Effectiveness

To continuously measure and improve the effectiveness of the open source training program, the following activities are carried out:

### (1) Training Program Evaluation Metrics

- The training program is evaluated using the following quantitative and qualitative metrics:
  - Training completion rate
  - Assessment test scores
  - Reduction rate in the number of license compliance violations
  - Reduction rate in security vulnerability response time
  - Program participant satisfaction score

### (2) Feedback Collection and Analysis

- Feedback is collected from participants after every training program ends.
- Opinions on the training content, instructor, and training method are collected through an online survey.
- The collected feedback is analyzed to identify areas for improvement.

### (3) Establishing a Continuous Improvement Plan

- Based on the evaluation metric results and feedback analysis, a training program improvement plan is established semiannually.
- The Open Source Program Manager reports the improvement plan to the OSRB and obtains approval.
- The approved improvements are reflected in the next training program, and their effectiveness is monitored.

Through these activities, program participants' awareness of open source can be raised, and the effectiveness of the training program can be continuously improved.

## 6. Summary

By building the training, assessment, awareness-raising activities, and training-effectiveness measurement and improvement process described so far, an enterprise can satisfy the key requirements of the ISO/IEC 5230 and ISO/IEC 18974 standards. 

![Side-by-side clause comparison of ISO/IEC 5230 and ISO/IEC DIS 18974 with policy-awareness and training clauses (3.1.1.2, 3.1.2.3, 3.1.3.1, 3.5.1.3, etc.) highlighted in cyan](trainingno.png)


Through this training and assessment system, an enterprise can raise program participants' understanding of open source license compliance and security assurance and continuously improve their competency. In addition, through regular assessment and improvement activities, the effectiveness of the program can be continuously enhanced.

Ultimately, this will help raise an enterprise's level of open source management, minimize the legal risk arising from open source use, and strengthen its ability to respond to security vulnerabilities.
