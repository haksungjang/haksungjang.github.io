---
title: "Enterprise Open Source Compliance Guide Using OpenChain"
linkTitle: "OpenChain Guide"
weight: 20
description: >
  The OpenChain specification is the only international standard (ISO) for open source compliance. This guide explains how enterprises can use it to raise their level of open source compliance.
---

{{% pageinfo %}}
The National IT Industry Promotion Agency (NIPA) sponsored this work, and Open UP conducted the research to produce a guide explaining what enterprises need to comply with the OpenChain specification, the international standard for open source compliance. : [Enterprise Open Source Governance OpenChain 2.0 Guide](https://www.oss.kr/oss_guide/show/7050bff0-d06b-43f0-99a6-9975afcd486f)

Here, we are writing the manuscript for a revised edition of this guide.
{{% /pageinfo %}}

##  Chapter 1. What Is OpenChain?

Today, software continues to grow in scale and complexity. Developing a single piece of software can involve not only software developed in-house but also open source, third-party software<sub>3rd party software</sub>, vendor SDKs, and other software spanning the software supply chain.

If even one organization among the many in this complex software supply chain fails to comply with open source license obligations or fails to provide correct open source usage information, the company distributing the final software has no choice but to fail to meet its open source license obligations. This can result in being sued and having product sales halted.

{{< imgproc supplychain Fit "900x600" >}}
<center>[OpenChain Open Source Software License Compliance General Public Guide]</center>
{{< /imgproc >}}

In December 2009, there was a lawsuit related to the open source project Busybox. Busybox is open source software licensed under GPL-2.0 that is widely used in embedded systems, and 14 companies, including two Korean companies, were named as defendants in the lawsuit. What is notable about this case is that it included companies that had only distributed the product without developing it themselves, and they were still sued.

In such a complex software supply chain environment, it is very difficult for any single company to achieve perfect open source compliance on its own, no matter how excellent its processes are. Ultimately, for a company to properly carry out open source compliance, every member of the software supply chain must comply with license obligations and provide correct open source information. This kind of trust must be built across the entire supply chain.

The Linux Foundation's [OpenChain](https://www.openchainproject.org/) project was founded on the belief that concisely and consistently defining the key requirements companies must meet for open source compliance, and having everyone comply with them, can build trust in open source licensing across the entire software supply chain.

{{< imgproc openchainlogo Fit "600x450" >}}
<center>[OpenChain Project Logo]</center>
{{< /imgproc >}}

At an open source conference in Europe in 2016, Dave Marr<sub>Dave Marr</sub>, an open source lawyer at Qualcomm, emphasized exactly this point. To raise a company's level of open source compliance, the open source compliance level of every member within the software supply chain must be raised. He also suggested that, to achieve this, advanced companies that already have a sufficient understanding of open source and have already established policies and processes should make their assets and know-how public so that anyone could reference them. Conference attendees resonated with the idea that "open source compliance is not an area where companies can differentiate their competitive advantage. Companies want an appropriate level of risk management while investing minimal resources. That is why the more companies share their assets with one another, the more everyone can achieve compliance together with fewer resources." That is how the OpenChain project (then called a Work Group) began, with many global companies such as Qualcomm, Siemens, Wind River, ARM, and Adobe participating.

The OpenChain project provides three main things to help companies achieve open source compliance more easily.

1. OpenChain Specification[^specification]
2. OpenChain Conformance Certification[^question]
3. Documentation Resources[^resource]

[^specification]: OpenChain Specification - https://www.openchainproject.org/contribute-to-the-standard
[^question]: OpenChain Self-Certification website - https://certification.openchainproject.org/
[^resource]: OpenChain Resources - https://www.openchainproject.org/resources


Let's look at how companies can make use of each of these, one by one.

### 1. OpenChain Specification

The OpenChain Specification is a 10-page document that defines the key requirements for open source compliance. Version 1.0 of the OpenChain Specification was released in 2016. The OpenChain Specification is designed to be suitable for all companies regardless of their size or industry.

In April 2019, version 2.0 of the specification was released, defining six key requirements that companies must fulfill to achieve open source compliance, along with the list of evidence needed to demonstrate them.

1. Establishing a Program
2. Defining and Supporting Relevant Tasks
3. Reviewing and Approving Open Source Content
4. Creating and Delivering Compliance Artifacts
5. Understanding Open Source Community Engagement
6. Complying with Specification Requirements

For a company just starting out with open source compliance, a good strategy is to raise its level by meeting these OpenChain Specification requirements one by one.

{{< imgproc spec Fit "1200x900" >}}
<center>< Source: https://github.com/OpenChain-Project/Specification/blob/master/Official/en/2.1/openchainspec-2.1.pdf></center>
{{< /imgproc >}}

In December 2020, the OpenChain Specification was officially registered as the international standard[^ISO] for open source compliance.

[^ISO]: ISO/IEC 5230 : https://www.iso.org/standard/81039.html


{{< imgproc iso Fit "900x600" >}}
<center>< Source: https://www.iso.org/standard/81039.html></center>
{{< /imgproc >}}


The OpenChain Specification, which had been the de facto standard for the past four years, was converted into the official international standard ISO/IEC 5230:2020, the first international standard to define open source compliance and process management. As a result, interest among global IT companies in complying with ISO/IEC 5230 is growing, and it is expected that more companies will require their suppliers in the software supply chain to comply with ISO/IEC 5230.

How to comply with each requirement in the OpenChain Specification is covered in detail in ["Chapter 2. How to Comply with the OpenChain Specification"](#chapter-2-how-to-conform-to-the-openchain-specification).

### 2. OpenChain Conformance Certification

If a company complies with all the requirements in the OpenChain Specification, it can be certified as having an open source program conforming to OpenChain. An open source program refers to a set of management systems, such as policies, processes, and personnel, that a company uses to carry out open source compliance activities. This section explains the certification methods and conformance declaration.

The OpenChain project proposes three certification methods.
* Self-Certification
* Independent Assessment
* Third-Party Certification

Let's look at each method.

#### Self-Certification

Self-certification is the method most recommended by the OpenChain project, and it has the advantage of incurring no cost. OpenChain provides a self-certification website[^question] so that companies can check for themselves whether they comply with the OpenChain Specification. A company's open source manager can sign up on the OpenChain self-certification website and start the online self-certification process. Self-certification proceeds by answering Yes/No questions, as shown below.


{{< imgproc question Fit "900x600" >}}
<center>< Source: https://certification.openchainproject.org/></center>
{{< /imgproc >}}


If a company has built a solid open source compliance system and can answer Yes to every item on the OpenChain self-certification questionnaire, it can submit these results on the website<sub>Conforming Submission</sub>. After that, following a simple Q&A verification process from the Linux Foundation, the company can make an OpenChain conformance declaration.

{{< imgproc announce Fit "900x600" >}}
<center><Example: LG Electronics conformance declaration - Source: https://www.openchainproject.org/featured/2021/02/08/lg-openchain-iso-5230></center>
{{< /imgproc >}}

Once a company makes an OpenChain conformance declaration, it is recognized as having an open source program that conforms to OpenChain, and at the same time, it can register its logo on the OpenChain project's website.

{{< imgproc organization Fit "900x600" >}}
<center>< Companies that have declared an ISO/IEC 5230 conforming program, Source - https://www.openchainproject.org/  ></center>
{{< /imgproc >}}

Companies with an OpenChain conforming program are granted the right to use the OpenChain logo.

{{< imgproc certilogo Fit "900x600" >}}
<center>< OpenChain Logo, Source - https://www.openchainproject.org/ ></center>
{{< /imgproc >}}

A company recognized in this way as having an OpenChain conforming program can demonstrate that it is faithfully carrying out open source compliance within the software supply chain. The OpenChain project recommends the self-certification method. For reference, most companies that have made an OpenChain conformance declaration have also adopted the self-certification method.

Through self-certification, a company can determine what is lacking and what additional activities are needed. To address these gaps, it can refer to the methods for complying with the OpenChain Specification explained in Chapter 2. Companies that lack the capacity to make these improvements on their own can consider the independent assessment method.

#### Independent Assessment

In an independent assessment, an independent organization external to the company inspects and evaluates the company's open source compliance status from a fair, impartial perspective. It differs from self-certification and third-party certification in that it does not issue any certificate. A distinguishing feature of independent assessment is that it does not stop at producing an assessment report but also provides consulting to address the gaps that are identified.

Through the iterative process of receiving a fair assessment and consulting from an independent organization to raise its compliance level, and then undergoing independent assessment again, a company can refine its policies and build out its processes.


{{< imgproc independent2 Fit "900x1200" >}}
<center>< Independent Compliance Assessment, Source - https://youtu.be/DEBd-g0Ab8E ></center>
{{< /imgproc >}}

Eventually, the company reaches a level where it can obtain OpenChain certification. At that point, it can begin the process of pursuing self-certification or third-party certification. In this way, OpenChain's independent assessment provides evaluation and consulting to raise a company's level of open source compliance, supporting the company in obtaining an OpenChain conforming program and certification.

Companies that provide independent assessment include [AlektoMetis](https://alektometis.com/)[^AlektoMetis] and [Source Code Control](https://sourcecodecontrol.co/)[^SourceCodeControl], among others.

[^AlektoMetis]: AlektoMetis - https://alektometis.com/, 
[^SourceCodeControl]: Source Code Control - https://sourcecodecontrol.co/

In Korea, NIPA's [Open UP](https://www.oss.kr/open_up_intro)[^openup] offers a similar program free of charge to domestic companies through the [Open Source Software Utilization Support Program](https://www.oss.kr/news/show/49e410fb-604d-4d35-ba25-8286b5f2c50d)[^program].

[^openup]: Open UP - https://www.oss.kr/open_up_intro
[^program]: Open Source Software Utilization Support Program - https://www.oss.kr/news/show/49e410fb-604d-4d35-ba25-8286b5f2c50d

{{< imgproc openup2 Fit "900x600" >}}
<center>< Open UP key tasks, Source - https://www.oss.kr/open_up_task ></center>
{{< /imgproc >}}


#### Third-Party Certification

If a company wants to demonstrate a more reliable and transparent level of open source compliance to buyers in the software supply chain, it can obtain a certificate from a third-party certification body and use it for promotion. In addition, some buyers who demand more robust reliability in open source compliance are expected to eventually require third-party certification from their suppliers<sub>Supplier</sub>.

As of April 2021, OpenChain's authorized third-party certification bodies are [ORCRO](https://orcro.co.uk/)[^ORCRO], [PWC](https://www.pwc.de/en/opensource)[^PWC], and [TÜV SÜD](https://www.tuvsud.com/)[^TUVSUD].

[^ORCRO]: ORCRO- https://orcro.co.uk/
[^PWC]: PWC - https://www.pwc.de/en/opensource
[^TUVSUD]: TÜV SÜD - https://www.tuvsud.com

{{< imgproc 3rdparty Fit "900x600" >}}
<center>< Third-Party Certifiers, Source - https://www.openchainproject.org/partners ></center>
{{< /imgproc >}}

These bodies provide assessments to verify an ISO/IEC 5230 conforming program and issue certificates to companies that pass.

{{< imgproc pwc Fit "900x600" >}}
<center>< PWC certification, Source - https://youtu.be/HslvXCM-4pQ ></center>
{{< /imgproc >}}


As of April 2021, there does not yet appear to be any buyer or organization that mandatorily requires third-party certification. However, some experts in the European automotive industry predict that it will not be long before ISO/IEC 5230, like [ASPICE](http://www.automotivespice.com/)<sub>Automotive SPICE</sub>[^aspice] (an international standard process model for automotive software development), becomes mandatory for automotive software suppliers.

[^aspice]: ASPICE: International standard process model for automotive software development - http://www.automotivespice.com

### 3. Documentation Resources

The OpenChain project provides a variety of documentation resources, such as policy document templates and training materials, that companies need to build a compliance program. These resources are designed to support compliance with the OpenChain Specification and general open source compliance activities, and they are provided under the CC-0 license so that anyone can use them freely.

{{< imgproc resource Fit "900x600" >}}
<center>< OpenChain Curriculum, Source - https://www.openchainproject.org/resources ></center>
{{< /imgproc >}}

Much of the content in this guide was also written based on materials published by OpenChain. If a company's open source manager needs policies, processes, or training materials, we recommend checking OpenChain Resources first. These materials are also being translated into Korean and published. The [OpenChain Korea Work Group](https://openchain-project.github.io/OpenChain-KWG/)[^KWG] is leading this translation work. Anyone interested can [participate](https://openchain-project.github.io/OpenChain-KWG/resource/) in the Korean translation[^translate].

[^KWG]: OpenChain Korea Work Group - https://openchain-project.github.io/OpenChain-KWG/

[^translate]: Korean translation work - https://openchain-project.github.io/OpenChain-KWG/resource/

Chapter 2 explains in detail how to comply with each requirement of the OpenChain Specification.

## Chapter 2. How to Conform to the OpenChain Specification

The OpenChain Specification defines the core requirements for open source compliance. A company that fully conforms to the OpenChain Specification and declares that it has an OpenChain Conformant Program can demonstrate trust within the supply chain through which it distributes its software solutions.

This chapter describes in detail the six major requirements a company must satisfy to conform to OpenChain Specification version 2.1, along with how to meet each one. Note that version 2.1 of the OpenChain Specification is the version registered as [ISO/IEC 5230](https://www.iso.org/standard/81039.html)[^iso].

[^iso]: ISO/IEC 5230 - https://www.iso.org/standard/81039.html

### 1. Program foundation

A company that develops and distributes software using open source must create policies and processes for managing open source, and allocate the personnel and resources needed for them appropriately. As mentioned in the previous chapter, an open source program refers to the set of management systems — policies, processes, personnel, and so on — that a company uses to carry out open source compliance activities, and the first requirement of the OpenChain Specification is to establish this open source program.

#### 1-1. Policy

The first requirement is that a documented open source policy must exist. Section 3.1.1 of OpenChain Specification version 2.1 defines the requirement for the policy and its verification material as follows.

{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.1.1 Policy

3.1.1 Policy

A written open source policy shall exist that governs open source license compliance of the supplied software. The policy shall be internally communicated.

Verification Material(s)

* 3.1.1.1 A documented open source policy
* 3.1.1.2 A documented procedure that makes program participants aware of the existence of the open source policy (e.g., via training, internal wiki, or other practical communication method)

---

A written open source policy shall exist that governs open source license compliance of the supplied software. The policy shall be internally communicated.

Verification Material(s):  

* 3.1.1.1 A documented open source policy.
* 3.1.1.2 A documented procedure that makes program participants aware of the existence of the open source policy (e.g., via training, internal wiki, or other practical communication method).

{{% /alert %}}

Let's look at how a company should meet this requirement, organized by the questions asked in [OpenChain self-certification](https://certification.openchainproject.org/)[^question].

| 1.a  | Do you have a documented policy that governs open source license compliance of the Supplied Software distribution? |
|---|:---|
|  | Do you have a documented policy that governs open source license compliance of the Supplied Software distribution? |


What must a company prepare in order to answer YES to this question? First, it must establish and document an open source policy. The open source policy includes the following:
* A policy for creating and distributing software products and services using open source
* A policy for contributing to external open source communities
* A policy for releasing the company's own software as open source

For reference, this guide provides a sample open source policy document that satisfies the requirements of the OpenChain Specification in "[Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy)." A company can modify this sample policy to fit its own business strategy and environment.

| 1.b  | Do you have a documented procedure that communicates the existence of the open source policy to all Software Staff? (e.g., via training, internal wiki, or other practical communication method) |
|---|:---|
|  | Do you have a documented procedure that communicates the existence of the open source policy to all Software Staff? (e.g., via training, internal wiki, or other practical communication method) |


A company must provide practical means, such as training and an internal wiki, so that all program participants are aware that an open source policy exists within the organization and can carry out the necessary activities. Here, program participants means all employees involved in developing, distributing, and contributing the company's software, including software developers, release engineers, and quality engineers.

Many companies publish their open source policy document on an internal wiki site so that any employee can check what is needed. In addition, they make training on the open source policy mandatory during new-hire orientation, and provide periodic training to program participants every year or every two years, so that all program participants remain aware that the open source policy exists. In other words, a company must include these methods in the open source policy document, written as in the example below.

~~~
1. Training and Assessment

All participants in software distribution must take the mandatory open source
training provided on [Learning Portal] every year. 
This ensures familiarity with the open source policy, related training policy, and 
how to look it up. Training records are retained in [Learning Portal]. 
~~~


#### 1-2. Competence

This section defines the requirement for the competence that program participants must have. Section 3.1.2 of OpenChain Specification 2.1 defines the requirement for competence and its verification material as follows.

{{% alert title="OpenChain Specification version 2.1, " color="success" %}}


3.1.2 Competence

The organization shall: 
* Identify the roles and the corresponding responsibilities of those roles that affect the performance and effectiveness of the program.
* Determine the necessary competence of program participants fulfilling each role.
* Ensure that program participants are competent on the basis of appropriate education, training, and/or experience.
* Where applicable, take actions to acquire the necessary competence.
* Retain appropriate documented information as evidence of competence.

Verification Material(s):

* 3.1.2.1 A documented list of roles with corresponding responsibilities for the different participants in the program.
* 3.1.2.2 A document that identifies the competencies for each role.
* 3.1.2.3 Documented evidence of assessed competence for each program participant.

---

3.1.2 Competence

The organization shall
* Identify the roles and the corresponding responsibilities of those roles that affects the performance and effectiveness of the program;
* Determine the necessary competence of program participants fulfilling each role
* Ensure that program participants are competent on the basis of appropriate education, training, and/or experience;
* Where applicable, take actions to acquire the necessary competence; and
* Retain appropriate documented information as evidence of competence.

Verification Material(s):

* 3.1.2.1 A documented list of roles with corresponding responsibilities for the different participants in the program.
* 3.1.2.2 A document that identifies the competencies for each role.
* 3.1.2.3 Documented evidence of assessed competence for each program participant.

{{% /alert %}}

Let's look at how a company should meet this requirement, organized by the questions asked in [OpenChain self-certification](https://certification.openchainproject.org/)[^question].

| 1.c  | Have you identified the roles and the corresponding responsibilities that affect the performance and effectiveness of the Program? |
|---|:---|
|  | Have you identified the roles and the corresponding responsibilities that affect the performance and effectiveness of the Program? |


A company must define what roles are needed for an open source program to be effective and produce results, and what responsibilities each role must carry out. The general roles typically needed for an open source program are as follows:
* Open source program manager
* Legal
* Infrastructure
* Security
* Development culture
* Quality
* Software development department
* OSPO[^OSPO]
* OSRB[^OSRB]

[^OSPO]: OSPO - Open Source Program Office
[^OSRB]: OSRB - Open Source Review Board

It is not necessary to establish all of the above roles from the outset. A company just getting started can begin with a single person serving as the open source program manager.

A document that specifies the general responsibilities for each role is provided in "[Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy)," under "[4. Roles, Responsibilities, and Competence](#4-roles-responsibilities-and-competencies3121)."

| 1.d  | Have you identified and documented the competencies required for each role? |
|---|:---|
|  | Have you identified and documented the competencies required for each role? |



Once each role and its responsibilities have been defined, a company must define the competencies required of the person filling that role. This is likewise covered in "[Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy)," under "[4. Roles, Responsibilities, and Competence](#4-roles-responsibilities-and-competencies3121)," so please refer to it.

| 1.e  | Have you documented evidence of assessed competence for each Program participant? |
|---|:---|
|  | Have you documented evidence of assessed competence for each Program participant? |

A company must designate a person responsible for each role and confirm that the designated person is qualified to perform that role on the basis of education, training, and experience. Where necessary, it must also provide training so that program participants can acquire sufficient competence. The company must then assess whether each participant has the required competence and retain the results.
1. The company provides training so that each participant can acquire the necessary competence.
2. It conducts an assessment based on the training content.
3. The assessment results are retained by the company's training system or HR department.

If there are hundreds or more program participants, making it difficult to provide training directly, using the company's online training and assessment system is also a good approach.

Content such as the following can be included in the company's open source policy to reflect this.

~~~

4. Roles, Responsibilities, and Competence
To ensure the effectiveness of this policy, the roles and responsibilities, and the 
competence required of the person in charge of each role, are defined as follows. 
The organization/person in charge of each role and the required competence level 
are defined in "Appendix 1. Personnel in Charge." 

5. Training and Assessment
All members responsible for each role defined in Section 4 must take the open 
source training provided on [Learning Portal]. 
Training records and assessment results are retained on [Learning Portal] for at 
least three years. 
~~~

#### 1-3. Awareness 

Next, the OpenChain Specification requires that program participants be aware of the company's open source policy and its implications, as follows.


{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.1.3 Awareness

The organization shall ensure that the program participants are aware of:

* The open source policy
* Relevant open source objectives
* Their contribution to the effectiveness of the program
* The implications of not following the Program's requirements

Verification Material(s): 

* 3.1.3.1 Documented evidence of assessed awareness for the program participants, which should include the program's objectives, one's contribution within the program, and the implications of program non-conformance

---

3.1.3 Awareness
The organization shall ensure that the program participants are aware of:
* The open source policy;
* Relevant open source objectives;
* Their contribution to the effectiveness of the program; and
* The implications of not following the Program’s requirements.

Verification material(s):

* 3.1.3.1 Documented evidence of assessed awareness for the program participants - which should include the program’s objectives, one’s contribution within the program, and implications of program non-conformance.

{{% /alert %}}

In this regard, the question asked in [OpenChain self-certification](https://certification.openchainproject.org/)[^question] is as follows.

| 1.f<br>  | Do you have evidence documenting the awareness of your personnel of the following topics?<br> i - The open source policy and where to find it; <br>ii - The relevant open source objectives; <br>iii - The contributions expected to ensure the effectiveness of the Program; <br>iv - The implications of failing to follow the Program requirements. |
|---|:---|
|  | Do you have evidence documenting the awareness of your personnel of the following topics?  <br>i - The open source policy and where to find it;  <br>ii - The relevant open source objectives;  <br>iii - The contributions expected to ensure the effectiveness of the Program;  <br>iv - The implications of failing to follow the Program requirements. |

A company must make program participants aware of the company's open source policy, the open source-related objectives, how participants can contribute to making the open source program effective, and the implications of failing to meet the program's requirements. To this end, the company provides training and conducts an assessment to confirm that program participants have gained the correct awareness. The assessment results are documented and retained.

Content such as the example below can be included in the company's open source policy for this purpose.

~~~
1. Purpose
  (1) Purpose of the policy
    This policy provides the following principles so that the entire organization 
    involved in software development, services, and distribution at the company 
    can make proper use of open source. 

    1) Principles for carrying out compliance with respect to open source licenses
    2) Principles for contributing to external open source projects
    3) Principles for releasing internal projects as open source
   
   These principles give all members of the company a way to understand the value 
   of open source, use open source correctly, and contribute to open source 
   communities.

  (2) Implications of non-compliance
   Failure to comply with this policy may result in the following situations.  
   * Receiving demands for open source license compliance from outside parties.
   * Being forced to release the company's source code against its wishes.
   * Facing legal action from open source copyright holders.
   * Being fined for copyright infringement or breach of contract, or being 
     ordered to stop selling products.
   * Loss of the company's reputation. 
   * Being held liable for damages due to breach of contract with a supplier.
  For these reasons, the company regards violations of the open source policy as 
  serious, and members or organizations that violate it may be subject to 
  disciplinary action.

  (3) How members can contribute
    All members can contribute to the effectiveness of the policy and to raising 
    the company's level of compliance by understanding the rationale and content 
    of this policy and faithfully carrying out the required activities.

~~~

A company must also establish a training and assessment policy so that program participants become aware of the open source policy. An example of this is provided in "[Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy)," under "[5. Training and Assessment](#5-training-and-evaluation)."

#### 1-4. Program Scope

A company must decide which organizations or products within the company the open source program applies to, and a procedure is needed for making that decision. Section 3.1.4 of OpenChain Specification 2.1 defines the requirement for the program's scope and its verification material as follows. 


{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.1.4 Program scope

Different programs may be governed by different levels of scope. For example, a program could govern a single product line, an entire department, or an entire organization. Accordingly, each program must precisely state its scope.

Verification Material(s):

* 3.1.4.1 A written statement that clearly defines the scope and limits of the program

---

3.1.4 Program scope  

Different programs may be governed by different levels of scope. For example, a program could govern a single product line, an entire department or an entire organization. The scope designation needs to be declared for each program.

Verification material(s):
* 3.1.4.1 A written statement that clearly defines the scope and limits of the program.

{{% /alert %}}

In this regard, the question asked in [OpenChain self-certification](https://certification.openchainproject.org/)[^question] is as follows.


| No | Self-certification question |
|---|:---|
| 1.h | Do you have a written statement clearly defining the scope and limits of the Program? |
| 1.h | Do you have a written statement clearly defining the scope and limits of the Program? |

A single open source program does not necessarily have to apply to the entire company. The scope can be set differently depending on the characteristics of each organization and product within the company. Different open source programs can apply by organization or by product. Likewise, an organization that does not distribute software at all can be excluded from the scope of the open source program. A company can define the scope and limits of the open source program clearly, taking into account the characteristics of its organizations and products, and state this in the open source policy.

| No | Self-certification question |
|---|:---|
| 1.g | Do you have a process for determining the scope of your Program? |
| 1.g | Do you have a process for determining the scope of your Program? |

In addition, situations may arise in which the scope of the program must be determined or revised as the company's organizations, products, and services change to fit the business environment. A company must prepare a process for responding to this, as in the example below.

1. When starting a new project, the open source program manager determines whether that project falls within the scope of the program. 
2. If it is determined to fall within scope, a proposal to bring the project into the scope of the program is submitted to the OSRB[^OSRB].
3. If the OSRB accepts the proposal, the scope of the program is revised accordingly. 
4. In addition, if the open source program manager determines that a review of the program's scope is needed, they can initiate a review of the program's scope through the same process.

To this end, content such as the following is included in the open source policy. 

~~~
2. Scope
This policy applies to the following three areas.

1) It applies to all products the company provides or distributes externally. 
   However, using open source solely for internal purposes is not within the 
   scope of this policy.
2) It applies when a member contributes to an external open source project.
3) It applies when internal code is released as open source.

The scope can be changed to fit the company's business environment, and the 
procedure for doing so is as follows. 

1) When the open source program manager determines that a change to the policy's 
   scope is needed due to changes in the company's business environment, such as 
   a new business or organizational restructuring, a proposal for the change is 
   submitted to the OSRB. 
2) The OSRB approves an appropriate level of scope change. 
3) The OSRB revises the open source policy to change the scope of the policy. 

~~~

This guide provides an example of specifying the program scope in "[Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy)," under "[2. Scope](#2-scope3141)."


#### 1-5. License Obligations

Using open source requires complying with the obligations imposed by each license. Section 3.1.5 of OpenChain Specification 2.1 requires a review process for determining the obligations imposed by each open source license, as follows. 


{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.1.5 License obligations

A process shall exist for reviewing the identified licenses to determine the obligations, restrictions, and rights granted by each license.

Verification Material(s)

* 3.1.5.1 A documented procedure for reviewing and recording the obligations, restrictions, and rights granted by each identified license

---

3.1.5 License obligations

A process shall exist for reviewing the identified licenses to determine the obligations, restrictions and rights granted by each license.

Verification material(s):

* 3.1.5.1 A documented procedure to review and document the obligations, restrictions and rights granted by each identified license.

{{% /alert %}}

In this regard, the question asked in [OpenChain self-certification](https://certification.openchainproject.org/)[^question] is as follows.

| 1.i | Do you have a process for reviewing open source license obligations, restrictions and rights? |
|---|:---|
|  | Do you have a process for reviewing open source license obligations, restrictions and rights? |

To determine whether an open source component can be used, a company must first identify what license the open source it intends to use is under, and confirm the obligations that license requires. It must review and record whether open source was used, what the license is, and what obligations each license imposes. An example procedure for this is as follows. 

1. The open source program manager makes a preliminary assessment of the license according to the criteria defined in the open source policy. 
2. If there is any question, the open source program manager requests advice from an external legal expert. 
3. All internal and external decision results and the supporting rationale are retained. 

A company's open source program manager should prepare a summary of open source license obligations so that the obligations, restrictions, and rights granted by the major open source licenses can be easily understood, and include it in the open source policy so that anyone can view it. The [License Guide](https://www.olis.or.kr/license/licenseGuide.do)[^copyrightguide] provided by the Korea Copyright Commission can be used as a reference. The [Obligations by License](https://sktelecom.github.io/guide/use/obligation/)[^sktobligation] document in SK telecom's open source guide is also a good example.

[^copyrightguide]: Korea Copyright Commission License Guide - https://www.olis.or.kr/license/licenseGuide.do
[^sktobligation]: Obligations by License in SK telecom's open source guide - https://sktelecom.github.io/guide/use/obligation/

The "documented procedure to review and document the obligations, restrictions and rights granted by each identified license" required here corresponds to "[Appendix 2. Sample Open Source Compliance Process](#appendix-2-sample-open-source-compliance-process)," [1. Open Source Identification Stage](#1-identification-of-open-source).

### 2. Relevant Tasks Defined and Supported

For an open source program to operate effectively, sufficient resources and staffing must be allocated. This section defines the requirements for this.

#### 2-1. Access

Section 3.2.1 of OpenChain Specification 2.1 first defines the requirements and verification materials for maintaining a process that effectively responds to external inquiries.

{{% alert title="OpenChain Specification Version 2.1, " color="success" %}}

3.2.1 Access

Maintain a process to effectively respond to external open source inquiries. Publicly identify a means by which a third party can make an open source compliance inquiry.

Verification material(s):

* 3.2.1.1 Publicly visible method that allows any third party to make an open source license compliance inquiry (e.g., via a published contact email address, or the Linux Foundation's Open Compliance Directory).
* 3.2.1.2 An internal documented procedure for responding to third party open source license compliance inquiries.

{{% /alert %}}


The questions required by [OpenChain self-certification](https://certification.openchainproject.org/)[^question] on this topic, along with response strategies, are as follows.

| 2.a  | Have you assigned individual(s) responsible for receiving external open source compliance inquiries ("Open Source Liaison")? |
|---|:---|
|  |  |

Customers and open source copyright holders sometimes raise open-source-related inquiries, requests, and claims with a company regarding products or services developed using open source. The main types of external inquiries and requests are as follows.

* Inquiries about whether open source is used in a specific product or service
* Requests for source code under GPL or LGPL licenses referenced in a Written Offer
* Requests to explain and disclose source code for open source found in a product but not listed in the open source notice
* Requests for missing files or build instructions for source code disclosed under obligations such as GPL or LGPL
* Requests for copyright attribution

A company must designate a person responsible for handling these external inquiries. This role is typically filled by the open source program manager.

| 2.b  | Is the Open Source Liaison function publicly identified (e.g. via an email address and/or the Linux Foundation's Open Compliance Directory)? |
|---|:---|
|  |  |

There are cases where an external open source developer wants to contact a company's representative to discuss an open source compliance issue but cannot find a way to reach them, and ends up filing a legal claim directly. To prevent this, a company must always publicly disclose a contact method through which a third party can make open-source-related inquiries and requests.

There are two ways a company can provide an external contact method for open-source-related inquiries: (1) publishing the email address of the company's open source program manager, or (2) using the Linux Foundation's [Open Compliance Directory](https://compliance.linuxfoundation.org/references/open-compliance-directory/)[^directory]. Another option is to include the representative email address of the company's open source program office in the open source notice distributed with the product or service.

[^directory]: Open Compliance Directory - https://compliance.linuxfoundation.org/references/open-compliance-directory/

The Linux Foundation created the Open Compliance Directory as a space where companies can publish contact information for their open source representatives.

{{< imgproc directory Fit "900x600" >}}
<center>< Image source: https://compliance.linuxfoundation.org/references/open-compliance-directory/ ></center>
{{< /imgproc >}}

A company's open source representative registers the company's contact information using "Add an Organization." External developers can submit open-source-compliance-related inquiries and requests through "Request a Contact." This lets open source developers easily find the contact point information for a given company, and resolve open source compliance issues by discussing them with the company's open source representative before resorting to a legal claim. Registering company information and a contact method in the Open Compliance Directory is one way to reduce litigation risk.

Let's look at the next self-certification question.

| 2.c  | Do you have a documented procedure that assigns responsibility for receiving and responding to open source compliance inquiries? |
|---|:---|
|  |  |

To avoid being taken to court over an external claim, a company must respond to external inquiries and requests as quickly and accurately as possible. To this end, the company must have a process in place to respond to external open source inquiries quickly and effectively.

The following example wording can be incorporated into the open source policy to reflect the above.

~~~

1. External Inquiry Response
(1) Responsibility for External Inquiry Response
Responding to external open source compliance inquiries and requests is the 
responsibility of the open source program manager. 

The open source program manager may assign all or part of the handling of an 
inquiry to the appropriate personnel within [Company]. Legal counsel is 
consulted when necessary.
Anyone who receives an external open source compliance inquiry must notify the 
open source program manager so that a prompt response can be made. 

(2) Publishing Contact Information
The open source program manager publicly provides contact information so that 
external parties can make open-source-related inquiries and requests.

* Provide a contact email address in the open source notice. 
* Register contact information in the Linux Foundation's Open Compliance Directory.

(3) External Inquiry Response Procedure
Responding to external open source compliance inquiries quickly and accurately 
significantly reduces the risk of escalation to litigation. To this end, the 
company follows the external inquiry response procedure defined in the open 
source compliance process when responding to external open source compliance 
inquiries. 

~~~

This guide also provides an example of the general procedure for responding to open source compliance inquiries in "[2. External Inquiry Response Process](#2-external-inquiry-response-process)" of "[Appendix 2. Sample Open Source Compliance Process](#appendix-2-sample-open-source-compliance-process)".


#### 2-2. Effectively Resourced

Section 3.2.2 of OpenChain Specification 2.1 defines the requirements and verification materials for resourcing the effective operation of an open source program, as follows.

{{% alert title="OpenChain Specification Version 2.1, " color="success" %}}

3.2.2 Effectively resourced

Identify and Resource Program Task(s):

* Assign accountability to ensure the successful execution of program tasks.
* Program tasks are sufficiently resourced:
  * Time to perform the tasks have been allocated; and
  * Adequate funding has been allocated.
* A process exists for reviewing and updating the policy and supporting tasks;
* Legal expertise pertaining to open source license compliance is accessible to those who may need such guidance; and
* A process exists for the resolution of open source license compliance issues.

Verification material(s):
* 3.2.2.1 Document with name of persons, group or function in program role(s) identified.
* 3.2.2.2 The identified program roles have been properly staffed and adequate funding provided.
* 3.2.2.3 Identification of legal expertise available to address open source license compliance matters which could be internal or external.
* 3.2.2.4 A documented procedure that assigns internal responsibilities for open source compliance.
* 3.2.2.5 A documented procedure for handling the review and remediation of non-compliant cases.

{{% /alert %}}

Let's look at each question required by [OpenChain self-certification](https://certification.openchainproject.org/)[^question] on this topic, along with how to satisfy it.

| 2.d | Have you documented the persons, group or function supporting the Program role(s) identified? |
|---|:---|
| |  |

A company must list the roles of each program participant and their corresponding responsibilities, and designate the person or organization responsible for each role. This must be documented and included in the open source policy document so that anyone can view it. See the example below.

~~~
4. Roles, Responsibilities, and Competencies
To ensure the effectiveness of this policy, the roles, responsibilities, and 
competencies required of each role's owner are defined as follows. 

The organization/person responsible for each role and the required competency 
level are defined in [Appendix 1. Status of Personnel]. The open source 
program manager periodically updates this list to reflect the company's 
business situation. 
~~~

Let's look at the next self-certification question.

| 2.e | Have the identified Program roles been properly staffed and has adequate funding provided? |
|---|:---|
|  |  |

A company must provide sufficient resources so that the open source program can function smoothly. Personnel filling each role in the program must be properly staffed, and adequate budget and working time must be guaranteed. If this is not the case, a procedure to remedy it must be in place. The following example wording can be added to the open source policy document.

~~~
4. Roles, Responsibilities, and Competencies

The head of the organization responsible for each role designates a person 
within the organization and allocates the appropriate time and budget for 
that person to fulfill the role. If a role's owner does not receive adequate 
support while performing the role, they must raise the issue with the open 
source program manager. The open source program manager discusses the 
resolution with the relevant organization head. If the issue is not properly 
resolved, the open source program manager may request that the OSRB resolve 
it. The OSRB shares the issue with the head of the higher-level organization 
and requests a resolution. 

~~~


| 2.f | Is legal expertise pertaining to internal and external open source compliance identified? |
|---|:---|
|  |  |

When a program participant needs a legal review to resolve an issue, the company must provide a way to request legal advice. This is provided primarily through the company's in-house legal team, and for particularly contentious issues, an external law firm with open source legal expertise may be engaged. An example of the open source policy for this is as follows.

~~~

4. Roles, Responsibilities, and Competencies

(2) Open Source Program Manager
* The open source program manager provides a way for members to obtain 
  legal advice related to open source. 
* The open source program manager decides whether to engage an external 
  law firm. The open source program manager evaluates and reviews the 
  effectiveness and appropriateness of external legal counsel annually.

~~~

For reference, the OpenChain Project provides, through its partner program, a list of global law firms that offer open-source-related legal advice.

{{< imgproc partners Fit "900x600" >}}
<center>< https://www.openchainproject.org/partners ></center>
{{< /imgproc >}}

Law firms registered as OpenChain partners meet the requirements set by the OpenChain Project, and Bae, Kim & Lee LLC is the only firm registered from South Korea.


| 2.g | Do you have a documented procedure assigning internal responsibilities for Open Source compliance? |
|---|:---|
|  |  |

A procedure must exist for assigning internal responsibility for open source compliance. This is the role of the open source program manager, who must identify issues and appropriately assign them to the owner of each role. To this end, a company can describe this in the open source policy document as follows.

~~~

4. Roles, Responsibilities, and Competencies

(2) Open Source Program Manager

The open source program manager bears overall responsibility for the 
company's open source program. To ensure open source compliance for 
products and services that use open source, the manager is responsible for 
the following.

* Defining the roles required for open source compliance, and designating 
  the organization and person responsible for each role. Consulting with 
  the OSRB as needed.

~~~


| 2.h | Do you have a documented procedure for handling review and remediation of non-compliant cases? |
|---|:---|
|  |  |

When a compliance non-conformance issue is raised, a company must document a procedure for reviewing and responding to it promptly. The following example can be referenced and included in the open source policy.

~~~
1. Open Source Use

(5) Compliance Issue Remediation Procedure
When a compliance issue is raised, the open source program manager responds 
promptly by carrying out the following procedure. 

1. Acknowledge receipt of the inquiry and specify an appropriate resolution 
   time.
2. Confirm whether the issue actually points to a real problem. (If not, 
   notify the person who raised the issue that it is not a problem.)
3. If it is a real problem, prioritize it and decide on an appropriate 
   response.
4. Carry out the response and, if necessary, update the open source 
   compliance process accordingly.
5. Preserve the above records using Jira Tracker.
~~~

### 3. Open Source Content Review and Approval


#### 3.1 BOM (Bill of Materials)

Section 3.3.1 of OpenChain Specification Version 2.1 defines the requirements and verification materials for the BOM (Bill of Materials) as follows.


{{% alert title="OpenChain Specification Version 2.1, " color="success" %}}

3.3.1 Bill of Materials

A process shall exist for creating and managing a bill of materials that includes each open source component (and its identified licenses) from which the supplied software is comprised.

Verification Material(s):

* 3.1.1.1  A documented procedure for identifying, tracking, reviewing, approving, and archiving information about the collection of open source components from which the supplied software is comprised.
* 3.3.1.2 Open source component records for the supplied software that demonstrates the documented procedure was properly followed.

{{% /alert %}}

The questions required by [OpenChain self-certification](https://certification.openchainproject.org/)[^question] on this topic, along with response strategies, are as follows.

| 3.a  | Do you have a documented procedure for identifying, tracking and archiving information about the collection of open source components from which a Supplied Software release is comprised? |
|---|:---|
|  |  |

The most basic open source compliance activity is understanding the status of open source included in supplied software. A process must be established for identifying the open source and its licenses contained in supplied software, and for creating and managing a BOM (Bill of Materials) that holds this information. This is because knowing which open source is included in each version of supplied software is necessary to comply with the obligations each open source license requires when the software is distributed.

All open source must be reviewed and approved before being integrated into supplied software. A prior review must confirm not only the open source's function and quality but also whether it meets sourcing and licensing requirements. This requires a request-for-review → review → approval process. [Appendix 2. Sample Open Source Compliance Process](#appendix-2-sample-open-source-compliance-process) describes the entire process a company follows for open source compliance. The BOM is created and managed through the steps from [1. Identification of Open Source](#1-identification-of-open-source) through [6. Registration](#6-registration).

In addition, every step and outcome of this open source compliance process must be documented. Using an issue tracking system such as Jira or Bugzilla, rather than email, documents this process more efficiently.

| 3.b  | Do you have open source component records for each Supplied Software release which demonstrates the documented procedure was properly followed? |
|---|:---|
|  |  |

The list of open source included in supplied software must be documented and archived. [SW360](https://projects.eclipse.org/proposals/sw360)[^sw360], an open source project sponsored by the Eclipse Foundation, provides a feature for tracking the list of open source included per supplied software. See [Appendix 3. Open Source Tools](#appendix-3-open-source-tools) for how to use SW360.

[^sw360]: SW360 - https://projects.eclipse.org/proposals/sw360

This guide provides an example of a BOM usage policy in [6. Open Source Use](#6-using-open-source) under "[Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy)".


#### 3.2 License Compliance

Section 3.3.2 of OpenChain Specification Version 2.1 defines the requirements and verification materials for license compliance as follows.

{{% alert title="OpenChain Specification Version 2.1, " color="success" %}}

3.3.2 License Compliance

The program shall be capable of managing common open source license use cases encountered by program participants for supplied software, which may include the following use cases (note that the list is neither exhaustive, nor might all of the use cases apply):

- Distributed in binary form;
- Distributed in source form;
- Integrated with other open source such that it triggers additional licensing obligations;
- Contains modified open source;
- Contains open source or other software under an incompatible license interacting with other components within the Supplied Software; and/or
- Contains open source with attribution requirements.

Verification Material(s):

* 3.3.2.1 A documented procedure for handling the common open source license use cases for the open source components of the supplied software.

{{% /alert %}}

The questions required by [OpenChain self-certification](https://certification.openchainproject.org/)[^question] on this topic, along with response strategies, are as follows.

| 3.c  | Have you implemented a procedure that handles at least the following common open source license use cases for the open source components of each supplied Supplied Software release?<br><br>i - distributed in binary form;<br>ii - distributed in source form;<br>iii - integrated with other open source such that it may trigger copyleft obligations;<br>iv - contains modified open source;<br>v - contains open source or other software under an incompatible license interacting with other components within the Supplied Software;<br>vi - contains open source with attribution requirements. |
|---|:---|
|  |  |

To properly comply with open source licenses, one must accurately understand the requirements of each license. However, since it is difficult for individual software developers to grasp all of this on their own, it is advisable for the open source lead to compile the requirements and precautions for common use cases of frequently used open source licenses and share them internally. For a general guide to open source licenses and a summary of license obligations, see the [Open Source Software License Guide](https://www.oss.kr/oss_license)[^nipa-license] provided by NIPA. SK telecom's open source license guide[^gpl], which analyzes license obligations by software use case, is also a good example.

[^nipa-license]: NIPA Open Source Software License Guide - https://www.oss.kr/oss_license

[^gpl]: SK telecom Open Source License Guide - https://sktelecom.github.io/guide/use/obligation/gpl-2.0/

The identification, inspection, issue-resolution, review, and approval stages of the open source compliance process in [Appendix 2. Sample Open Source Compliance Process](#appendix-2-sample-open-source-compliance-process) make it possible to handle common open source license use cases for the open source components of supplied software.

Source code scanning tools can be used at the identification and inspection stage. These range from free, open-source-based tools to commercial tools, and each has its own strengths, but none provides complete functionality that resolves every problem on its own. A company must therefore choose a tool suited to its product's characteristics and requirements. Many companies use these automated source code scanning tools alongside manual review. The Linux Foundation's FOSSology[^fossology] project is an openly released source code scanning tool that companies can use easily and free of charge. See [Appendix 3. Open Source Tools](#appendix-3-open-source-tools) for how to use it.

[^fossology]: FOSSology - http://fossology.org/

### 4. Compliance artifact creation and delivery

#### 4.1 Compliance Artifacts

Section 3.4.1 of OpenChain Specification version 2.1 defines the following requirements and verification materials for compliance artifacts.

{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.4.1 Compliance artifacts

A process shall exist for creating the set of compliance artifacts for the supplied software.

Verification Materials(s):

* 3.4.1.1 A documented procedure that describes the process under which the compliance artifacts are prepared and distributed with the supplied software as required by the identified licenses.
* 3.4.1.2 A documented procedure for archiving copies of the compliance artifacts of the supplied software - where the archive is planned to exist for a reasonable period of time (determined by domain, legal jurisdiction and/or customer contracts) since the last offer of the supplied software; or as required by the identified licenses (whichever is longer). Records exist that demonstrate the procedure has been properly followed.

---

3.4.1 Compliance artifacts

A process shall exist for creating the set of compliance artifacts for the supplied software.

Verification Materials(s):

* 3.4.1.1 A documented procedure that describes the process under which the compliance artifacts are prepared and distributed with the supplied software as required by the identified licenses.
* 3.4.1.2 A documented procedure for archiving copies of the compliance artifacts of the supplied software - where the archive is planned to exist for a reasonable period of time (determined by domain, legal jurisdiction and/or customer contracts) since the last offer of the supplied software; or as required by the identified licenses (whichever is longer). Records exist that demonstrate the procedure has been properly followed.

{{% /alert %}}

Regarding this, the questions required by [OpenChain Self Certification](https://certification.openchainproject.org/)[^question] and the corresponding responses are as follows.

| 4.a  | Do you have a documented procedure that describes a process that ensures the Compliance Artifacts are distributed with Supplied Software as required by the Identified Licenses? |
|---|:---|
|  | Do you have a documented procedure that describes a process that ensures the Compliance Artifacts are distributed with Supplied Software as required by the Identified Licenses? |

The previous chapter noted that the most fundamental open source compliance activity is identifying the open source components included in the supplied software. This is done precisely to correctly satisfy open source license requirements, which are at the core of open source compliance. In other words, a process must be established for creating the set of compliance artifacts for the open source components included in the supplied software.

Compliance artifacts are broadly divided into two categories.

1. Open source notice: a document that provides the full text of open source licenses and copyright information
2. Source code package to be disclosed: a package that collects the source code to be disclosed in order to fulfill the obligations of open source licenses—such as the GPL and LGPL—that require source code disclosure

This guide provides an example of a policy for creating compliance artifacts in [6. Open Source Usage](#6-using-open-source) of [Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy).

Compliance artifacts must be provided together when the supplied software is distributed. Compliance artifacts are created and distributed through the notice, pre-distribution review, and distribution stages of [Appendix 2. Sample Open Source Compliance Process](#appendix-2-sample-open-source-compliance-process).

| 4.b  | Do you archive copies of the Compliance Artifacts of the Supplied Software? |
|---|:---|
|  | Do you archive copies of the Compliance Artifacts of the Supplied Software? |

| 4.c  | Are the copies of the Compliance Artifacts archived for at least as long as the Supplied Software is offered or as required by the Identified Licenses (whichever is longer)? |
|---|:---|
|  | Are the copies of the Compliance Artifacts archived for at least as long as the Supplied Software is offered or as required by the Identified Licenses (whichever is longer)? |

When distributing supplied software, if it is difficult to include the source code package to be disclosed, this requirement can instead be satisfied by providing a written offer to supply the source code for at least three years. A written offer is typically provided through the product's user manual, and an example is as follows.

> The software included in this product contains copyrighted software that is licensed under the GPL. A copy of that license is included in this document on page X. You may obtain the complete Corresponding Source code from us for a period of three years after our last shipment of this product, which will be no earlier than 2011-08- 01, by sending a money order or check for $5 to:
>
> GPL Compliance Division  
> Our Company  
> Any Town, US 99999  
>   
> Please write“source for product Y” in the memo line of your payment.  
> You may also find a copy of the source at http://www.example.com/sources/Y/.  
> This offer is valid to anyone in receipt of this information.

_<center>< Source: SPLC Guide to GPL Compliance ></center>_

Therefore, compliance artifacts must be retained for at least three years, and a process for doing so must be established. Some companies build their own websites (e.g., http://opensource.lge.com/) so that external customers can download the open source notice and the source code package to be disclosed for the supplied software at any time.


### 5. Understanding open source community engagements

#### 5.1 Contributions

Section 3.5.1 of OpenChain Specification version 2.1 defines the following requirements and verification materials for compliance artifacts.


{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.5.1 Contributions

If an organization considers contributions to open source projects, then
- a written policy shall exist that governs contributions to open source projects;
- the policy shall be internally communicated; and
- a process shall exist that implements the policy

Verification Materials(s):

If an organization permits contributions to open source projects, then the following shall exist:
- 3.5.1.1 A documented open source contribution policy;
- 3.5.1.2 A documented procedure that governs open source contributions; and
- 3.5.1.3 A documented procedure that makes all program participants aware of the existence of the open source contribution policy (e.g., via training, internal wiki, or other practical communication method).

---

3.5.1 Contributions

If an organization considers contributions to open source projects, then
- a written policy shall exist that governs contributions to open source projects;
- the policy shall be internally communicated; and
- a process shall exist that implements the policy

Verification Materials(s):

If an organization permits contributions to open source projects, then the following shall exist:

- 3.5.1.1 A documented open source contribution policy;
- 3.5.1.2 A documented procedure that governs open source contributions; and
- 3.5.1.3 A documented procedure that makes all program participants aware of the existence of the open source contribution policy (e.g., via training, internal wiki, or other practical communication method).


{{% /alert %}}

Regarding this, the questions required by [OpenChain Self Certification](https://certification.openchainproject.org/)[^question] and the corresponding responses are as follows.

| 5.a  | Do you have a policy that governs contributions to open source projects on behalf of the organization? |
|---|:---|
|  | Do you have a policy that governs contributions to open source projects on behalf of the organization? |


Global software companies value not only using open source to build products and services, but also the strategic value that can be created by contributing to open source projects. However, approaching this without a sufficient understanding of the open source project ecosystem and how communities operate, and without a strategy, can unexpectedly damage the company's reputation and create legal risk. Therefore, it is important for companies to establish a strategy and policy for participating in and contributing to open source projects.

For a policy on open source contributions, see [7. Open Source Contributions](#7-contributing-to-open-source) of [Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy).

| 5.b  | Do you have a documented procedure that governs Open Source contributions? |
|---|:---|
|  | Do you have a documented procedure that governs Open Source contributions? |

If a company has a policy that permits contributions to external open source projects, it must also have a documented procedure that governs how in-house developers can contribute to external projects. The [Open Source Contribution Process](https://sktelecom.github.io/guide/contribute/process/)[^skt-contribution] published by SK telecom is a good example.

[^skt-contribution]: SK telecom Open Source Contribution Process - https://sktelecom.github.io/guide/contribute/process/

| 5.c  | Do you have a documented procedure that makes all Software Staff aware of the existence of the Open Source contribution policy? |
|---|:---|
|  | Do you have a documented procedure that makes all Software Staff aware of the existence of the Open Source contribution policy? |

Even if an open source contribution policy has been created, it becomes useless if internal members are unaware of its existence. A procedure is needed to make all in-house developers aware of the existence of the open source contribution policy. Communicate the open source contribution policy in parallel with the open source policy communication activity described in 3.1.1.2.


### 6. Adherence to the specification requirements

#### 6.1 Conformance

Section 3.6.1 of OpenChain Specification version 2.1 defines the following requirements and verification materials for conformance.

{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.6.1 Conformance

In order for a program to be deemed OpenChain conformant, the organization shall affirm that the program satisfies the requirements presented in this document.

Verification Materials(s):

* 3.6.1.1 A document affirming the program specified in §3.1.4 satisfies all the requirements of this document.

----------------

3.6.1 Conformance

In order for a program to be deemed OpenChain conformant, the organization shall affirm that the program satisfies the requirements presented in this document.

Verification Materials(s):

* 3.6.1.1 A document affirming the program specified in §3.1.4 satisfies all the requirements of this document.

{{% /alert %}}

Regarding this, the questions required by [OpenChain Self Certification](https://certification.openchainproject.org/)[^question] and the corresponding responses are as follows.

| 6.a  | Do you have documentation confirming that your Program meets all the requirements of this specification? |
|---|:---|
|  | Do you have documentation confirming that your Program meets all the requirements of this specification? |

A company that satisfies all the requirements of OpenChain Specification 2.1 can notify the Linux Foundation, undergo the verification process, obtain ISO/IEC 5230 conformance certification, and declare it. If even one requirement is not met, the company cannot be considered conformant with ISO/IEC 5230.

If all the requirements of the OpenChain Specification are satisfied, this can be stated in the policy document as conformant with OpenChain, as in [10. OpenChain](#10-openchain) of [Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy).

#### 6.2 Duration

Section 3.6.2 of OpenChain Specification version 2.1 defines the following requirements and verification materials for duration.

{{% alert title="OpenChain Specification version 2.1, " color="success" %}}

3.6.2 Duration

A program that is OpenChain conformant with this version of the specification shall last 18 months from the date conformance validation was obtained. The conformance validation registration procedure can be found on the OpenChain project's website.

Verification Materials(s):

* 3.6.2.1 A document affirming the program meets all the requirements of this document, within the past 18 months of obtaining conformance validation.

---

3.6.2 Duration

A program that is OpenChain conformant with this version of the specification shall last 18 months from the date conformance validation was obtained. The conformance validation registration procedure can be found on the OpenChain project's website.

Verification Materials(s):

* 3.6.2.1 A document affirming the program meets all the requirements of this document, within the past 18 months of obtaining conformance validation.

{{% /alert %}}

Regarding this, the questions required by [OpenChain Self Certification](https://certification.openchainproject.org/)[^question] and the corresponding responses are as follows.

| 6.b  | Do you have documentation confirming that your Program conformance was reviewed within the last 18 months? |
|---|:---|
|  | Do you have documentation confirming that your Program conformance was reviewed within the last 18 months? |

It is important for a company to continue maintaining compliance activities even after declaring conformance with OpenChain. Article 3.6.2.1 of OpenChain Specification version 2.1 requires that, even after declaring OpenChain conformance, the company continue to comply with all the requirements of OpenChain Specification version 2.1 without change for at least 18 months.

A company must maintain a state of continuous conformance for at least 18 months after declaring OpenChain conformance, and if it does so, it can state in a document that it has continued to meet OpenChain for 18 months or more, as in [10. OpenChain](#10-openchain) of [Appendix 1. Sample Open Source Policy](#appendix-1-sample-open-source-policy).

It is also a good idea to use a website, as SK telecom does, to communicate this externally.

{{< imgproc iso5230-skt Resize "700x" >}}
<center><i>https://sktelecom.github.io/compliance/iso5230/ </i></center>
{{< /imgproc >}}

## Appendix 1. Sample Open Source Policy

### 1. Purpose

#### (1) Purpose of the Policy<sub>(3.1.3.1)</sub>

This policy provides the following principles so that all organizations within [Company Name] Inc. (hereinafter the "Company") involved in software development, services, and distribution can properly use open source software (hereinafter "open source").

1. Principles for performing compliance activities that take open source licenses into account
2. Principles for contributing to external open source projects
3. Principles for releasing internal projects as open source

These principles give every member of the Company a way to understand the value of open source, use open source correctly, and contribute to the open source community.

All members of the Company can find the open source policy at the following link on the internal wiki: [internal_link]<sub>(3.1.1.1)</sub>

#### (2) Impact of Non-Compliance
Failing to comply with this policy can result in the following situations.

- The Company may receive external demands for open source license compliance.
- The Company may be forced to release source code it developed against its wishes.
- The Company may be sued by open source copyright holders.
- The Company may be fined for copyright infringement and breach of contract, or ordered to stop selling its products.
- The Company's reputation may suffer.
- The Company may breach contracts with suppliers and face damage claims.

For these reasons, the Company treats violations of this open source policy seriously, and members or organizations that violate it may be subject to disciplinary action.

#### (3) How Members Can Contribute

All members of the Company can contribute to the effectiveness of this policy and to raising the Company's compliance level by understanding the rationale and content of this policy and faithfully carrying out the required activities.

### 2. Scope<sub>(3.1.4.1)</sub>
This policy applies to the following three areas.

1. Applies to [all products the Company provides or distributes externally]. However, using open source solely for internal purposes is not within the scope of this policy.
2. Applies when members contribute to external open source projects.
3. Applies when internal code is released as open source.

The scope may change to fit the Company's business environment, following this procedure:

1. When the Open Source Program Manager determines that a change in the policy's scope is needed due to changes in the Company's business environment, such as a new business or organizational restructuring, they submit a proposal for the change to the OSRB.
2. The OSRB approves an appropriate level of change to the scope.
3. The OSRB revises the open source policy to change its scope.


### 3. Terms
* BOM (Bill of Materials)
* Software distribution participant: Refers to all employees involved in the Company's development, distribution, and contribution of software, including software developers, deployment engineers, and quality engineers.
* ...

### 4. Roles, Responsibilities, and Competencies<sub>(3.1.2.1)</sub>
  To ensure the effectiveness of this policy, the following roles, responsibilities, and the competencies required of each role's owner are defined.

 The organization/owner responsible for each role and the required competency level are defined in [Appendix 1. Role Assignments].<sub>(3.1.2.2)</sub>
 
* The Open Source Program Manager periodically updates this list to reflect the Company's business situation.<sub>(3.2.2.1)</sub>
* The head of the organization responsible for each role designates an owner within the organization and allocates the time and budget needed for the owner to faithfully perform the role.<sub>(3.2.2.2)</sub>
  * If an owner does not receive adequate support while performing their role, they must raise the issue with the Open Source Program Manager.
  * The Open Source Program Manager discusses resolution of the issue with the relevant organization head. If it is not resolved adequately, the Open Source Program Manager may request the OSRB to resolve it.
  * The OSRB shares the issue with the head of the higher-level organization and requests resolution.

#### (1) OSRB
The OSRB<sub>Open Source Review Board</sub> is a body composed of the Open Source Program Manager and the heads of related organizations — such as the Legal, Patent, Development, and Infrastructure teams — formed to ensure the Company's open source compliance.

* Creates policies and processes for open source compliance and defines the roles and responsibilities within the Company for carrying them out.
* When an open source compliance issue arises within the Company, discusses resolution options and prepares a response.
* When necessary, reports issues to executives and receives feedback on risk mitigation measures.

#### (2) Open Source Program Manager
The Open Source Program Manager has overall responsibility for the Company's open source program. To ensure open source compliance for products and services that use open source, this role is responsible for the following.<sub>(3.2.2.4)</sub>

- Defines the roles needed for open source compliance and designates the organization and owner responsible for each role, consulting the OSRB as needed.
- Organizes and evaluates open source compliance training.
- Serves as chair of the OSRB and directs its activities.
- Responds to external inquiries and requests related to open source use and compliance.
- Reviews and approves requests to use open source.
- Maintains open source BOM records.
- Provides members with a way to obtain legal advice related to open source.<sub>(3.2.2.3)</sub>
- Maintains a repository for open source notices and released source code.

#### (3) OSPO
The OSPO<sub>Open Source Program Office</sub> supports and fosters the growth of open source activities both inside and outside the Company.

- Establishes, improves, and disseminates the open source policy.
- Provides guidance for contributing code to external open source projects.
- Provides guidance for releasing internal projects as open source.
- Develops and operates the open source portal.
- Develops and selects open source tools.
- Sponsors open source project events.
- Manages relationships with the open source community.

#### (4) Legal
Legal provides advice on legal risks that may arise in the course of using open source, and on ways to mitigate them, including interpreting open source licenses and obligations.

- Provides advice on license and intellectual property issues, including conflicts arising from incompatible open source licenses.
- When contributing to external open source projects, reviews the necessary legal matters, including the open source license and any CLA<sub>Contributor License Agreement</sub>.

#### (5) IT Infrastructure
IT Infrastructure operates and automates open source analysis tools and builds systems to ensure that license analysis is performed smoothly for all software to be distributed.

- Operates open source license analysis tools.
- Integrates with the DevOps environment to automate license analysis.
- Builds the systems and processes needed to perform license analysis on all software to be distributed.
- Obtains and maintains an open source BOM for all software to be distributed.

#### (6) Security
Security operates open source vulnerability analysis tools and builds systems to ensure that vulnerability analysis is performed smoothly for all software to be distributed.

- Operates open source vulnerability analysis tools.
- Integrates with the DevSecOps environment to automate open source vulnerability analysis.
- Builds the systems and processes needed to perform open source vulnerability analysis on all software to be distributed.

#### (7) Developer Culture
Developer Culture supports internal developers in actively using open source and participating in internal and external communities so they can adopt advanced development practices.

- Encourages participation in the open source community.
- Fosters a culture in which active participation in external open source projects is recognized as an internal achievement.
- Builds a development culture that makes the Company attractive to open source developers.

#### (8) Quality
The organization responsible for quality, such as QA, verifies that open source license obligations were properly fulfilled when software is distributed.

- Verifies that open source compliance activities were performed at the appropriate stage of the development process.
- Verifies that deliverables were generated as required by the open source licenses.
- Verifies that the open source notice and any source code to be released are provided together when software is distributed.
- If an issue is found, notifies the software development/distribution organization and directs it to fix the issue immediately.


### 5. Training and Evaluation
Every software distribution participant must complete the mandatory open source training provided on the [Learning Portal] each year. This ensures they are familiar with the open source policy, related training policies, and how to look them up. Training records are kept in the [Learning Portal].<sub>(3.1.1.2)<sub>

All members holding a role defined in Section 4 must complete the advanced open source training course provided on the [Learning Portal]. Training records and evaluation results are kept in the [Learning Portal] for at least three years.<sub>(3.1.2.3)</sub>

### 6. Using Open Source

Developing and distributing products and services using open source requires complying with the obligations each open source license imposes. The activities for doing so are called open source compliance.

To carry out open source compliance correctly, software development/distribution organizations must comply with the following.<sub>(3.3.1.1)</sub>

* Every step of the open source compliance process is recorded and kept in Jira Tracker.

#### (1) Identifying Open Source and Reviewing License Obligations

When adopting open source in product or service development, first identify what license applies to it, then review and confirm the obligations the license requires.

The Company's [Open Source License Guide] includes a list of major open source licenses and explains, for each license, the obligations it imposes by the following distribution forms.<sub>(3.3.2.1)</sub>

- Binary form
- Source form
- Strong/weak copyleft
- SaaS-based delivery
- Whether the code was modified
- Whether attribution-required open source is included, and so on.

Software development/distribution organizations may refer to this guide when reviewing open source license obligations. If a license not covered in this guide needs to be reviewed, contact the Open Source Program Manager.

#### (2) License-Aware Design

Understand how open source components are combined and design the software architecture so that the Company's own code is not affected by open source license obligations.

The Company's [Open Source License Guide] explains the scope of source code disclosure required by each open source license and design approaches for preventing disclosure of the Company's own code.

#### (3) Generating Open Source Compliance Deliverables
The most basic open source compliance activity is identifying the open source contained in software to be distributed. This is essential to properly meeting open source license requirements, which is the core of open source compliance. In other words, a set of compliance deliverables must be generated for the open source contained in software to be distributed.<sub>(3.4.1.1)</sub>

Open source compliance deliverables fall into two broad categories.

1. Open source notice: a document providing the full text of open source licenses and copyright information.
2. Source code package to be released: a package of source code compiled for release to fulfill the obligations of open source licenses that require source code disclosure, such as the GPL and LGPL.

To compile, distribute, and store these compliance deliverables, comply with the following.<sub>(3.4.1.2)</sub>

- Compile the open source notice or the source code package to be released as required by the conditions of each license. For example, if a license requires the full license text to be included, providing only a link is not sufficient.
- Store the compiled deliverables in a dedicated repository.
- When the source code to be released is provided under a written offer, publish a download link so the repository of compiled deliverables can be accessed externally.
  
The Company's open source compliance process can be used to issue the open source notice and compile the source code package to be released.

#### (4) Generating an Open Source BOM (Bill of Materials)
An inventory of the open source contained in software to be distributed (BOM: Bill of Materials) must be generated and managed.<sub>(3.3.1.2)</sub>

The Company's open source compliance process can be used, together with open source tools, to generate and retain the open source BOM.

#### (5) Compliance Issue Resolution Procedure

When a compliance issue is raised, the Open Source Program Manager follows the procedure below to respond promptly.<sub>(3.2.2.5)</sub>

1. Acknowledge receipt of the inquiry and specify a reasonable resolution time.
2. Determine whether the issue actually points to a real problem. (If not, inform the person who raised it that it is not an issue.)
3. If it is a real problem, set a priority and decide on an appropriate response.
4. Carry out the response and, if necessary, revise the open source compliance process accordingly.
5. Record and retain the above using Jira Tracker.

### 7. Contributing to Open Source
The Company encourages participation and contribution to external open source projects to create business value through open source. In this process, however, care must be taken to avoid unintentionally exposing the Company's intellectual property or infringing the rights of third parties. To that end, members of the Company must comply with the following when contributing to external open source projects.<sub>(3.5.1.1)</sub>

#### (1) Review Request and Approval

From a copyright standpoint, contributing to open source means granting an open source project the right to modify, use, and distribute your work. In some cases, you may even need to assign your copyright to the open source project. Generally, however, the copyright in a work created during employment belongs to the employer. That is, works created by Company members belong to the Company. If a member contributes such a work to open source on their own judgment, it can create an unnecessary copyright infringement issue.

Therefore, if you wish to contribute to an open source project, follow the review request and approval procedure defined in the open source contribution process before making your first contribution.

However, for the following simple cases, the risk of copyright infringement is low, so members may contribute at their own discretion without going through the review procedure.

- Small code snippets of 10 lines or fewer
- Questions and answers on Stack Overflow
- Maintenance activity on GitHub, such as creating issues, reviewing/approving pull requests, and the like

#### (2) Contribute Only Code You Have the Right to Contribute
You must contribute only code you have the right to contribute — that is, code you wrote yourself. Do not contribute a third party's code without authorization.

#### (3) Caution Against Intellectual Property Exposure
Do not contribute code or documents that risk exposing the Company's intellectual property, such as sensitive information or patents.

* If the code you intend to contribute includes a Company patent, confirm whether that patent may be contributed to the project under the open source license. If anything is unclear, contact the OSPO.

#### (4) Caution When Signing a CLA
Some open source projects require every contributor to sign a CLA<sub>Contributor License Agreement</sub>. This is an agreement seeking contributors' consent to reduce copyright disputes that can arise when a project manages works from many contributors. Projects led by large companies typically require a signed CLA.

CLAs vary by project but generally include agreement to the following.

- I (or my employer) have the right to contribute my contribution to the project. (That is, I am the author of the contribution.)
- I (or my employer) grant the project the right to modify, distribute, and manage my contribution.
- I (or my employer) will not revoke the granted rights.
- I (or my employer) grant the project the right to change the license in the future as needed.

In rare cases, some CLAs also require agreement to the following condition.

- I (or my employer) assign my copyright in the contribution to the project or the organization managing the project at the time of contribution.

To protect its intellectual property, the Company does not permit contributions to open source projects that require assignment of copyright. To make this determination, if the open source project a member wishes to contribute to requires a signed CLA, the member must request a review from the OSPO before signing.

#### (5) Copyright Notice

The intellectual property in works a member creates during their employment belongs to the Company by default. Therefore, when contributing code to an external open source project, members must include the Company's copyright notice.

When contributing one or more files, mark the copyright and license at the top of each file as follows.

~~~
Copyright (c) {$year} {$Company}
SPDX-License-Identifier: {$SPDX_license_name}
~~~
Here, $SPDX_license_name is set according to the license policy of the open source project in question.

However, if you are only modifying existing code for purposes such as a bug fix, there is no need to add a copyright notice for that modification.

#### (6) Use Your Company Email
When contributing to open source projects, use your Company email rather than a personal email address. This (1) gives members a sense of responsibility for communicating with the community on the Company's behalf, and (2) helps improve the Company's recognition as an organization that actively contributes to the open source community.

### 8. Releasing Open Source

The Company values collaboration with the open source community and encourages releasing internal software as open source projects. However, there are several rules that must be followed to protect the Company's intellectual property and prevent unintentional copyright infringement.

#### (1) Approval
From a copyright standpoint, releasing something as open source means granting everyone the right to modify, use, and distribute the work through an open source license. Generally, the copyright in a work created during employment belongs to the employer. That is, works created by Company members belong to the Company. If a member releases such a work as open source on their own judgment, it can create an unnecessary copyright infringement issue.

Therefore, if you wish to release software as open source, follow the review request and approval procedure set out in the Company's open source release policy.

If anything about the release process seems undesirable, do not hesitate to contact the OSPO.

#### (2) Release Only Code You Have the Right to Release

One of the worst situations that can arise with an open source project is legally problematic code being included in it. Code the Company has no right to distribute, or code that infringes another company's IP such as a patent, can create legal problems. Therefore, when preparing code for release, verify the origin of every piece of code and remove anything that could be problematic.

#### (3) Caution Against Intellectual Property Exposure
Do not release code or documents that risk exposing the Company's intellectual property, such as sensitive information or patents.

If the code you intend to release includes a Company patent, confirm whether that patent may be released under the open source license. If anything is unclear, contact the OSPO.

#### (4) Release Useful Code
To become a successful project, the code must also be useful to others. If a similar project already exists, participate in the existing project rather than creating a new one.

The open source project you plan to release should be expected to (1) provide differentiated value to the open source community, (2) solve a problem the community has not yet solved, and (3) attract positive attention by showcasing our technical capabilities.
* Do not release code as open source if it could not be used in an actual product or service.
* Do not release code that addresses a problem the open source community has already solved. In such cases, contribute to the existing open source project instead.

#### (5) Secure Resources
Secure the resources needed for the project, including developers.

* In the early stages, a similar level of developer effort is needed as for a typical internal project.
* Developers are needed who can review external contributions promptly.
* The Legal and Marketing teams also have roles to play.
* Secure a budget for the infrastructure needed to maintain and manage the project. This includes tools for project hosting, such as GitHub.

If an environment with sufficient resource support cannot be established, do not release the project as open source.

#### (6) Use Your Company Email
When releasing open source, use your Company email rather than a personal email address. This (1) gives members a sense of responsibility for communicating with the community on the Company's behalf, and (2) helps improve the Company's recognition as an organization that actively releases projects to the open source community.

### 9. Responding to External Inquiries

#### (1) Responsibility for Responding to External Inquiries
The Open Source Program Manager is responsible for responding to external inquiries and requests regarding open source compliance.<sub>(3.2.1.2)</sub>

* The Open Source Program Manager may assign all or part of the handling of an inquiry to an appropriate person within the Company. When necessary, they consult Legal to handle it.
* Anyone who receives an external inquiry about open source compliance must notify the Open Source Program Manager so a prompt response can be made.

#### (2) Publishing Contact Information
The Open Source Program Manager publicly provides contact information so external parties can make open source-related inquiries and requests.<sub>(3.2.1.1)</sub>

* Provide a reachable email address in the open source notice.
* Register contact information with the Linux Foundation's Open Compliance Directory.

#### (3) External Inquiry Response Procedure
Responding to external open source compliance inquiries promptly and accurately can greatly reduce the risk of escalation to litigation. To that end, the Company follows the external inquiry response procedure defined in its open source compliance process when responding to external open source compliance inquiries.<sub>(3.2.1.2)</sub>

### 10. OpenChain
The Company supports the spirit of the Linux Foundation's OpenChain project and actively participates in it to improve the level of open source compliance across the software supply chain.

- By applying this open source policy, the Company ensures conformance with ISO/IEC 5230:2020 as of October 1, 2021.<sub>(3.6.1.1)</sub>
- The Company ensures that it meets all requirements of OpenChain Specification version 2.1, ISO/IEC 5230:2020, for at least 18 months after obtaining conformance certification.<sub>(3.6.2.1)</sub>
- The Company reviews conformance at intervals of at least 18 months and revises and updates the policy as needed.


### Appendix 1. Role Assignments

| No | Role | Responsibility | Required Competency | Responsible Organization | Owner | 
|---|:---|:---|:---|:---|:---|
| 1 | Open Source Program Manager | Has overall responsibility for the Company's open source program. | 1. Understanding of the software development process<br>2. Understanding of intellectual property related to open source licenses, including copyright and patents<br>3. Expert knowledge of open source compliance<br>4. Open source development experience<br>5. Communication skills  | CTO | [Name] |
| 2 | Legal | Interprets open source licenses and obligations. Provides advice on mitigating legal risks that may arise in using open source, including fulfilling those obligations. | 1. Basic knowledge of the open source ecosystem<br>2. Expert knowledge of software copyright<br>3. Expert knowledge of open source licenses | Legal Team | [Name] | 
| 3 | Infrastructure | Operates and automates open source analysis tools and builds systems to ensure license analysis is performed smoothly for all software to be distributed. | 1. Basic knowledge of the open source compliance process<br>2. Understanding of open source license analysis tools<br>3. Expert knowledge of IT infrastructure | IT Infrastructure Team | [Name] | 
| 4 | Security | Operates open source vulnerability analysis tools and builds systems to ensure vulnerability analysis is performed smoothly for all software to be distributed. | 1. Basic knowledge of the open source compliance process<br>2. Understanding of open source license analysis tools<br>3. Expert knowledge of security | Security Team | [Name] | 
| 5 | Developer Culture | Supports internal developers in actively using open source and participating in internal and external communities to adopt advanced development practices.  | 1. Understanding of the software development process<br>2. Basic knowledge of open source compliance<br>3. Understanding of the open source policy | DR | [Name] | 
| 6 | Development Team | Software development/distribution organizations comply with the open source policy and process for the proper use of open source.  | 1. Understanding of the software development process<br>2. Basic knowledge of open source compliance<br>3. Understanding of the open source policy<br>4. Basic knowledge of open source licenses | Development Team | All members |

## Appendix 2. Sample Open Source Compliance Process

Company OOO (hereinafter referred to as the "Company") actively uses open source software (hereinafter "open source") while developing products and services that include software. The Company must carry out activities to comply with the obligations imposed by open source licenses when distributing software, and this is called open source compliance.

### 1. Process for Software Product Development/Distribution

The open source compliance process defines the procedures that must be followed at each development stage for the Company to comply with open source license obligations while developing and distributing software products and services. All members involved in software product development/distribution follow the following 10-step open source compliance process.

{{< imgproc general-osc-process Fit "1200x1200" >}}
{{< /imgproc >}}

#### 1. Identification of Open Source
The development department follows the items below during the software design stage.

- While designing software, identify predictable open source usage and check the licenses.
- Check the obligations for each open source license. The obligations for each license can be found in the Company's Open Source License Guide.
- Design the software considering the source code disclosure scope of each open source license.

The open source program manager writes and publishes a guide on the obligations, restrictions, and rights of major open source licenses so that development departments across the Company can refer to it.

The development department marks copyright and license notices in the source code according to Company rules. The Company's rules for copyright and license notices in source code can be found on the following page. : (insert_link)

When the development department considers adopting new open source, it first identifies the license. It checks the license obligations, restrictions, and rights according to the Company's Open Source License Guide. If the license is not covered in the Company's Open Source License Guide, it inquires with the open source program manager about whether adoption is possible and any precautions. The inquiry is made by creating a Jira Ticket.

The open source program manager analyzes the open source license obligations and provides guidance to the software development organization.

- If there is any question, request advice from the legal department to provide clear guidance.
- Reflect newly analyzed license information in the company-wide license guide.

#### 2. Auditing Source Code

The development department provides the source code as instructed by the infrastructure team and requests an open source check.

The infrastructure team performs the open source check using an open source analysis tool and generates the open source BOM.

The open source program manager reviews whether the open source license obligations can be complied with and whether there are open source license conflicts, and if there are issues, requests the development department to resolve them. Issues are created as Jira Tickets and assigned to the development department.

#### 3. Resolving Issues

The development department resolves all problems found during the source code audit stage. It takes actions such as removing the open source in question or replacing it with open source under a different license.

Once the development department resolves all issues found, it resolves the Jira Ticket issue and requests a re-review.

#### 4. Reviews

The open source program manager reviews whether all issues have been properly addressed. If necessary, it performs the source code audit again using the open source analysis tool.

#### 5. Approval

The open source program manager gives final approval or rejection as to whether the open source compliance procedure was properly carried out. In case of rejection, it explains the reason and proposes a way to fix it to the development department.

#### 6. Registration

The open source program manager finalizes the BOM for tracking the open source usage list by software version.

The infrastructure team registers the finalized BOM in the system. The BOM includes the list of open source included in the distributed software and the following information.

- Product (or service) name and version of the distributed software
- Open source list
  - Open source name / version
  - Open source license


#### 7. Notices

The open source program manager creates open source notices to comply with the notice obligation. The open source notices include the following.

- Open source contact for open source-related inquiries
- Notice content for each open source
  - Copyright
  - Open source license name
  - Open source license copy
  - (if applicable) Written Offer for obtaining a copy of the source code

The open source program manager creates the open source notices and delivers them to the development department. If source code disclosure is required, it guides the development department on how to collect the source code to be disclosed.

The development department includes the open source notices with the product at the time of distribution. For products with a screen, it ensures the user can check the notices through a menu. (e.g., App > Menu > Settings > Copyright Information > Open Source Licenses)

If the development department has used open source under a license that requires source code disclosure, such as GPL or LGPL, it checks the scope of source code disclosure required and collects the source code to be disclosed.

- The source code collected to comply with obligations under licenses such as GPL and LGPL must match the source code that makes up the binary included in the product. That is, building the collected source code must produce the same binary as the one included in the product.

#### 8. Pre-Distribution Verifications

The development department submits the following deliverables to demonstrate that the open source compliance activities were properly performed.

1. The final open source notices included in the product
2. Materials confirming that the open source notices are included in the product (e.g., a screenshot showing the open source notices)
3. (if applicable) Source code to be disclosed (submitted compressed into a single file)

The open source program manager reviews the materials submitted by the development department to check for any issues.

#### 9. Distribution

The open source program manager submits the compliance deliverables submitted by the development department to the infrastructure team.

The infrastructure team registers the compliance deliverables on the Company's open source distribution site.

#### 10. Final Verifications

The open source program manager performs a comprehensive check, such as confirming that the compliance deliverables were registered without issue on the Company's open source portal and that they can be downloaded from outside without issue.

### 2. External Inquiry Response Process
Responding to external open source compliance inquiries quickly and accurately can greatly reduce the risk of the matter escalating to litigation. To this end, the Company follows the process below for responding to external open source compliance inquiries.

{{< imgproc general-inquiry-process Fit "1200x900" >}}
{{< /imgproc >}}

#### 1. Acknowledge
The open source program manager notifies the requester immediately upon receiving an inquiry that it has been received. At this time, it also informs the requester of the expected resolution date. Since it is important to accurately understand the requester's intent, if the inquiry is unclear, it requests additional clarification.

The main types of inquiries and requests that require a response are as follows.

- Inquiries about whether open source is used in a specific product or service
- Requests for source code under GPL or LGPL licenses mentioned in a Written Offer
- Requests for an explanation and source code disclosure for open source found in the product but not listed in the open source notices
- Requests for missing files and build instructions for source code disclosed under obligations such as GPL or LGPL
- Requests for copyright notices

The open source program manager creates a Jira Issue for the received request and records the entire response process in detail.

#### 2. Inform

The open source program manager informs the requester that the Company is faithfully carrying out open source compliance and that the requester's inquiry is being investigated. It is good practice to notify the requester whenever there is an update on the progress of the internal investigation.

#### 3. Investigate

The open source program manager conducts an internal investigation into the request. It checks whether the compliance process was properly carried out for the product version in question through the BOM and documented review history. If necessary, it requests advice from the legal department.

If the matter requires confirmation from a specific development department, the open source program manager requests the development department to investigate. The development department that receives the investigation request immediately checks whether there is a problem with the compliance deliverables and reports the results to the open source program manager.

#### 4. Report

The open source compliance officer completes the internal investigation within the expected resolution date and informs the requester of the results.

- If the requester's inquiry was a mistaken claim due to a misunderstanding, the Company informs the requester of this without further action and closes the matter.
- If the problem is confirmed, the Company informs the requester of the correct method and timing for fulfilling the obligations of the relevant open source license.

#### 5. Rectify

If an actual compliance problem is found during the internal investigation, the relevant development department carries out all procedures necessary to resolve the compliance problem.

#### 6. Report

Once the problem is resolved, the Company immediately notifies the requester and provides the best available means to confirm that the problem has been resolved.

#### 7. Improve

If there was a compliance problem, the case is reviewed at an OSRB meeting to identify how the problem occurred, and the process is improved so that the problem does not recur.

## Appendix 3. Open Source Tools

Open source compliance activities require not only policies, processes, and training materials but also various tools and systems for source code scanning, dependency analysis, open source BOM management, and more. For this reason, many companies invest significant resources in adopting and operating such tools and systems. Companies that are just starting out with open source compliance in particular face difficulties not only in terms of process but also cost.

To address this difficulty, the [Open Source Tooling Group](https://github.com/Open-Source-Compliance/Sharing-creates-value)[^toolinggroup] was launched in June 2019, led by open source compliance tooling experts from companies participating in the OpenChain project, including Siemens, Bosch, Toshiba, Fujitsu, and Hitachi.

[^toolinggroup]: Open Source Tooling Group - https://github.com/Open-Source-Compliance/Sharing-creates-value


The Open Source Tooling Group was formed so that open source experts from various companies can work together to solve issues and share the results, reducing open source compliance costs and producing high-quality compliance deliverables.

Specifically, it aims to build an integrated (turn-key) open source tool chain using existing open source projects such as FOSSology, SW360, ORT, Software Heritage, ClearlyDefined, and SPDX, and to make it freely available for any company to use.

This section introduces FOSSology and SW360 and briefly explains how to use them.

### 1. FOSSology

Source code scanning tools can be used to detect the open source and license information included in software for open source compliance purposes.

{{< imgproc fossology1 Fit "900x600" >}}
<center>< https://www.fossology.org/ ></center>
{{< /imgproc >}}

The Linux Foundation's FOSSology project developed such a scanning tool and released it as open source so that anyone can use it freely.

#### Key Features

FOSSology is a web-based program that lets users log in to the website and upload individual files or software packages. FOSSology detects license text and copyright information in the uploaded files. It is a good tool for developers to check what license and copyright applies to the open source they want to use. FOSSology scans every file in the open source package uploaded by the developer, automatically detects license-related text and copyright information in each file, and generates a report. For more details on FOSSology's key features, see the following page. : [https://www.fossology.org/features/](https://www.fossology.org/features/)

#### Installation

To use FOSSology within a company, a FOSSology server must be set up in-house. This requires installing FOSSology on a Linux-based server system. FOSSology can be installed in the following three ways.

1. Using Docker
2. Using Vagrant and VirtualBox
3. Installing by building from source

This section describes the simplest method, using Docker.

FOSSology publishes a containerized Docker image through Docker Hub. : [https://hub.docker.com/r/fossology/fossology](https://hub.docker.com/r/fossology/fossology)

The pre-built Docker image can be run with the following command.

```text
$ docker run -p 8081:80 fossology/fossology
```

The Docker image can be accessed with the following URL and account information. : http://\[IP\_OF\_DOCKER\_HOST\]:8081/repo

* Username : fossy
* Passwd : fossy

For more details on installation, see the following page. : [https://github.com/fossology/fossology/blob/master/README.md](https://github.com/fossology/fossology/blob/master/README.md)

#### Test Server

If setting up a system to install FOSSology is difficult, the test server provided by the FOSSology Project can be used. The FOSSology project provides an environment for testing. (The test server may be discontinued without notice.)

Users can access the FOSSology test server with the following account to try out FOSSology's features.

{{< alert  >}}
Test server URL: [https://fossology.osuosl.org/](https://fossology.osuosl.org/)

* Username: fossy
* Password: fossy
{{< /alert  >}}

![](../fossology2.png)

#### Basic Workflow

The basic usage procedure for FOSSology is as follows.

* To check the license and copyright information of the open source to be used, compress the open source's source code into a single file and upload it to FOSSology.
* To do this, select Menu &gt; Upload &gt; From File.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/Oywr9jqM09g1SfxfZ-2HERmYA_8)

* Select the file to upload and click the Upload button.
* Once the upload is complete, the Job Agent automatically performs the analysis.
* The analysis status can be checked at Menu &gt; Jobs &gt; My Recent Jobs.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/9IKts-8lH7YK_Dat124-hEw_q4I)

* Once the analysis is complete, the results can be checked at Menu &gt; Browse.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/C62vBvaVNeBLAqrRrx-XKoeuMhg)

* Selecting an individual file shows the license-related text detected by FOSSology.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/9idwgtBqNj7YAl7Wg0i98QJ5b4w)

* At Menu &gt; Browser &gt; select a file or directory &gt; Copyright/Email/Url/Author, you can see the Copyright/Email/Url/Author information detected by FOSSology.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/NrjeCqal75rJ1bwGLPPmjhBEn4Q)

After checking whether the results analyzed by FOSSology are valid, users can exclude any incorrectly detected items from the analysis results. FOSSology calls this the Clearing process; for more details, see the following page. : [https://www.fossology.org/get-started/basic-workflow/](https://www.fossology.org/get-started/basic-workflow/)

Using the method above, you can easily check the license and copyright information of the open source you want to use.


### 2. SW360

Companies that develop and distribute products including open source must collect and track information such as the version and license of the open source used in each product and release version. This allows the company to carry out proper open source compliance activities.

In particular, when a security vulnerability is reported for a specific open source version in the [NVD](https://nvd.nist.gov/vuln)[^nvd]<sub>National Vulnerability Database</sub>, if the company cannot trace which products use that version, the company will not know which products need the security patch applied, and its products will inevitably remain exposed to the security vulnerability.

[^nvd]: NVD : NATIONAL VULNERABILITY DATABASE - https://nvd.nist.gov/vuln

As such, tracking open source information is essential. Companies build their own systems for this or purchase commercial services. SW360 is an open source project sponsored by the Eclipse Foundation that provides a web application and repository for collecting and tracking software BOM information.

{{< imgproc sw3601 Fit "900x600" >}}
<center>< https://www.eclipse.org/sw360/ ></center>
{{< /imgproc >}}

#### Key Features

SW360 provides a web-based UI, and its key features are as follows.

* Tracking components used in products
* Security vulnerability assessment
* License obligation management
* Generating legal documents such as notices

![https://www.eclipse.org/sw360/](https://lh3.googleusercontent.com/MPrOy70nOVSCRiorql9Momzi18lG66Liqttyutjwc9LAhVUwqmVf8xyeEkg085Pm1OYxwPRzyh68Th93ZlKA3fjG5_PnsBQijwUGkRa7o72h8Jco_7BcIwfoR7FGu8hsZA8n5ASq)

#### Installation

SW360 is composed as follows.

* Frontend : Liferay-(Tomcat-)based portal application
* Backend : Tomcat-based thrift service
* Database : CouchDB

For details on the project structure and the software required for installation, see the Required software section of the README. : [https://github.com/eclipse/sw360/blob/master/README.md](https://github.com/eclipse/sw360/blob/master/README.md)

SW360 offers the following three installation methods. Users can choose one of these to install.

1. Vagrant-based installation: Vagrant is a tool for managing virtualization instances, and sw360vagrant provides an environment for deploying SW360 all at once. : [https://github.com/sw360/sw360vagrant](https://github.com/sw360/sw360vagrant)
2. The SW360 components can be installed individually. : [https://github.com/eclipse/sw360](https://github.com/eclipse/sw360)
3. It can be deployed via Docker. : [https://github.com/sw360/sw360chores](https://github.com/sw360/sw360chores)

This section introduces the Vagrant-based installation and deployment method on a CentOS 7.6 system. For more details, see the README. : [https://github.com/sw360/sw360vagrant/blob/master/README.md](https://github.com/sw360/sw360vagrant/blob/master/README.md)

##### 1) Prerequisites

To install SW360 on a vagrant box, openjdk, VirtualBox, and Vagrant must be installed. First, install openjdk 1.8.0.

```text
$ yum install java-1.8.0-openjdk
$ java -version
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-b12)”
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

Install VirtualBox.

```text
$ sudo wget https://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo -P /etc/yum.repos.d
$ sudo yum install VirtualBox-5.2
```

If a "kernel module is not loaded" error occurs when installing VirtualBox on CentOS 7, install kernel-devel to resolve it and then reinstall VirtualBox.

```text
$ sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
$ sudo yum install dkms
$ sudo yum install kernel-devel
# reboot
$ sudo /sbin/vboxconfig
$ systemctl status vboxdrv
● vboxdrv.service - VirtualBox Linux kernel module
   Loaded: loaded (/usr/lib/virtualbox/vboxdrv.sh; enabled; vendor preset: disabled)
   Active: active (exited) since Wed 2020-02-19 09:06:02 KST; 20min ago
```

Install Vagrant and the vagrant-aws plugin.

```text
$ sudo yum install https://releases.hashicorp.com/vagrant/2.2.6/vagrant_2.2.6_x86_64.rpm 
# Install the vagrant-aws plugin
$ vagrant plugin install vagrant-aws
```

Then, clone the sw360vagrant code.

```text
$ git clone https://github.com/sw360/sw360vagrant.git
```

##### 2) Downloading Dependencies

To reduce the time it takes to build the Vagrant box, download the dependency packages in advance.

```text
$ cd sw360vagrant
$ ./download-packages.sh
```

This downloads the following packages into the ./shared/package folder.

* Liferay 7.2.1 CE GA2 with Tomcat (9.0.17)
* Postgresql-42.2.9 ODBC client for Java as \*.jar file
* 11 \*.jar files required by SW360
* Thrift 0.11
* A box image from Ubuntu 16.04 LTS (xenial-server-cloudimg-amd64-vagrant.box)

##### 3) Building the Base Box

Now build the base box with the following command.

```text
$ cd generate-box
$ ./generate_box.sh
```

This step can take tens of minutes.

##### 4) Running the Box

Run the box with the following command.

```text
# If you have built a vagrant box from this directory earlier, you will have to destroy it first via
$ vagrant destroy
$ cd ../sw360-single
$ vagrant up
```

Running the box configures Liferay, PostgreSQL, and CouchDB. If it runs without issue, the Liferay screen can be accessed at [https://localhost:8443/](https://localhost:8443/).

![](https://lh6.googleusercontent.com/leof_ntxQlxjDeD91E7ZfwWY0ftUlD0D_L58AkeNJb_bEFFzKvuL28yzb4iIA6-bAuSfQydo-gVBlnn5EVGGBKcPh0-6Y7p2Qbar74qpB4uwa_nibrV535NJwEIpWXZPFeNUSRd-)

##### 5) Deploying the SW360 Layout

The last step is to deploy the SW360 layout in Liferay. This step is not yet automated and must be performed manually by an administrator. Access [https://localhost:8443/](https://localhost:8443/) and log in with the following account.

* id : [setup@sw360.org](mailto:setup@sw360.org)
* pw : sw360fossy

Then follow the instructions on the following site to deploy the layout. [https://github.com/eclipse/sw360/wiki/Deploy-Liferay7](https://github.com/eclipse/sw360/wiki/Deploy-Liferay7)

Once the deployment is complete, you will see a screen like the following.

![](https://lh5.googleusercontent.com/INu1-WWi1-SA9P61IMNlgZhugTXbiwbSKUOu2eWq_d5sIIp8NfqxQntwId41ZDmTG6_5Ope8GdU1J2S0adaJDolM09dtfkwIbOE2gTDC4MZXMxhX9kN28E4Yj8a3deBUHBL7yCqj)

#### Basic Workflow

##### 1) Registering Licenses

When SW360 is first installed, commonly used open source licenses must be registered first. A license includes the following information.

* Full Name
* Short Name
* License Type
* GPL-2.0 Compatibility (e.g., yes, no)
* License Text

Selecting Menu &gt; Licenses &gt; Add License opens the Create License screen shown below.

![](https://lh6.googleusercontent.com/8bn6z_39PK5WrjP7mzhHrTwfM5PU19QT3TiQnAatOYywVwcGLJGFMmMgMkzh4CKAPM0SOOy7VDoboaj9OKpD1QEZv6KWOeWxZfqGA_2geYrYOBm2kOVzrNOmGPVK-8hzJvBZ-klT)

Registering licenses one by one this way can be quite tedious. Fortunately, SW360 provides a function to import the SPDX License List all at once. Click Menu &gt; Admin &lt; Import SPDX Information.

![](https://lh5.googleusercontent.com/d8ZK-dD34z1yKZn-szPNrN7iT4zg1EQnKnAv4QcPslSR0-laETy37ArojuweqSsxpWuvGXtdF5FabiWk57So-bD_iiEx7eVIR6tWDsYO2SkaCdlKr6ELDN9y_NdkqWFbQgRF2lXN)

The SPDX License List will then be automatically registered. At Menu &gt; Licenses, you can confirm that 338 licenses have been registered.

![](https://lh6.googleusercontent.com/Ucjuo09uJKhEhACZ90y98PszgSiCGtlDotH8mbTXJ2ePnF3TquzNX2yWzOCENTKNk1UjMJhyFgHxTCH6lxvZJg1l07M0hCc-v-14loAJ0efUU9V9hqS9mUabAT9QNysYL8E2tgIf)

##### 2) Registering Components and Releases

In SW360, a Component is a unit of software. This can cover various forms of software, including the following.

* Open source software
* Libraries
* 3rd party software

A Component includes the following information.

* Component Name
* Main Licenses
* Categories (e.g., Library, Cloud, Mobile, ...)
* Component Type (e.g., OSS, Internal, InnerSource, Service, Freeware)
* Default Vendor
* Homepage URL

A Release is a unit that refers to one version of a Component. Accordingly, one Component can have multiple Releases. A Release is created and managed under a Component.

A Release includes the following information.

* Component Name
* Version
* License
* Download URL
* CPE ID (e.g., cpe:2.3:a:apache:maven:3.0.4)

For example, to register zlib-1.2.8, first register zlib as a Component, and then register zlib 1.2.8 as a Release. Selecting Menu &gt; Components &gt; Add Component opens the Create Component screen, where information about zlib can be registered.

![](https://lh6.googleusercontent.com/0a3ecmmFzumTZTaoWCOZPKkQIZLJwbPoAaduCTfwQMH_N67DPaMpTkerA4LOynwkl_nLkNT-pRh-rKzj4XHtBjoTkVMW9g06Rywryk3wbAj-Y3ONDg16VcGepMEm7m7Y8M3iDWyH)

Once the Component is created, information about the zlib-1.2.8 version can be registered at Components &gt; Releases &gt; Add Release.

![](https://lh4.googleusercontent.com/ynUEB5-rGVYDirFghLx2v3tUt-uh-WL3YTN0siaGZWBrWQKYnIiV3B04mvdv3nZUW7t_U2Gl8msV_es1X181uq95YAp1bnqa0e3QLshhd1zhqk6z8ubPeEfo74cKdwho95_NyI1J)

Having registered versions 1.2.8 and 1.2.11 as separate Releases under the zlib Component, the Release Overview screen shows the following two Releases.

![](https://lh3.googleusercontent.com/GxgMJQbNjRBNxMTMBvqEXNFNElXGXoCnaksCMs46ydREIrqrj7dFxMK0YkvjviHYMCiHY07xlR-Xixpa_C5nMFLzih0dXZAtv-6yKg4RdADJxr5qmDwhAEopVOaVNqzVWc3gMpLq)

SW360 provides a function to import a large number of Component records at once. At Menu &gt; Admin &gt; Import / Export, you can enter Component information into the CSV template and import it.

![](https://lh5.googleusercontent.com/VInFwWAV-1lG1E7zFQPvn1GIlYPPY5ToGbSa49Brg7XuB-AwyCEHA9han0EUij1KX3c8aN2UZ1mKkN-5Y4BNv8LOV3O5YoypLQ7EF43QFPAU9L18XT57Ec5eoneswtGtt3rMSPoQ)

Note that, as of February 2020, this function may not yet work reliably.

##### 3) Creating a Project

A Project refers to a single product. Depending on the business type, it could be a product, a service, or software. The Components/Releases used in the product are registered and managed under a Project.

When creating a Project, the following information is registered.

* Project Name
* Version
* Project type (e.g., Product, Customer Project, Service, Internal Project, InnerSource)

A Project can be created via Menu &gt; Projects &gt; Add Project.

![](https://lh6.googleusercontent.com/6gNtLci53U6zaU6Th5SHousuZ4VUijzuYjiJJlB0R6JwiHG4ggjb0RcnRYDkZCBhE2dMP2gGbT4qmB2FE5O8EW8hTfv1lgM4_XN0vzQUkttfTbX2cF0aNftHYuUy9EXczT2LzLO5)

Once the Project is created, the included Releases or sub-Projects are registered. Selecting the Project at Menu &gt; Projects lets you register Linked Projects and Linked Releases under "Linked Releases and Projects."

![](https://lh4.googleusercontent.com/ZjD7r7EzxfdQ4bhw4ODsChydb6Vgqj1m4Ad0cWlYtyYXO40MCbPpTHHcy-wJmbHeA_FxTa66Mpza6-9ohu0e93b7BaGb7Zc9soTA3mGCHGnyGURukRUnJS_duI7T8IL2aTgMFzjB)

The following screen shows the state after OpenSSL 1.0.1 and zlib 1.2.8 have been registered as Linked Releases in the SuperCalc Project.

![](https://lh3.googleusercontent.com/tZCshPwxtukNLvfL-f-LfNOH-4ATof0bIGxpghVKXQ9QMBgoc_t0ROJMYafS9V4PuRaOOEW9zp25yk0gFA_kcaoRN83UKwUaFhaXxSWg7xPWvsYoJ_-pZkROkey1mYVTqGxKsCRu)

##### 4) Security Vulnerability Management

SW360 can automatically check whether there is a security vulnerability for a registered Release. To do this, SW360 provides a function to schedule periodic collection of CVE information. At Menu &gt; Admin &gt; Schedule, you can set the CVE SEARCH information to be collected every 24 hours.

![](https://lh5.googleusercontent.com/V2AJbexZqJJqwFYD1kFpjdZ7zVM9PCd-I_6MSBu3djO2Gi6gQxxQpKoqqsETxDaSkpDXOKFOp9h0Fps1xYHEphesVX9ECwBwnSX5cWdziXoohh-CMmqRh_wVkwUD8dZE9w1raJRk)

Once this schedule is set, SW360 collects CVE information from the CVE Search site ([https://cve.circl.lu/](https://cve.circl.lu/)) at the scheduled time. The collected CVE information can be checked at Menu &gt; Vulnerabilities.

![](https://lh3.googleusercontent.com/dpIMyX7qCMdnibNihuL6RBSKg2fEckbOBPWJEtw08mY4quhv6Hh3BlgFIeydPOS6N8rF6ZSs4hpZgBGcXbcJI9saFDyfv4i-TCvxV5z-4LD9ZXpKah0jQU45j3iibxFpYoa7Hj9u)

Once the vulnerability information has been collected, you can check whether the created Project has any security vulnerabilities. The SuperCalc Project created above shows 85 reported security vulnerabilities.

![](https://lh5.googleusercontent.com/lGeLbWHIBk6y2OSOXskcp4A2c5od0eTH6n7U5YG0p4cwTrrX02b6TpeRqJ7VXg5aUE7qDP2X2f8o4Rj1JsPHhZ-CUdLiy80O532Cgw-h_P9r-jHdL61QaXhFOPxIjTlX1cg9XPk5)

By registering and managing software developed and distributed by a company in SW360 this way, it becomes possible to manage the risk not only of open source compliance but also of security vulnerabilities.

SW360 also provides most of its functions as a REST API in addition to the Web Interface above, enabling integration with other tools such as FOSSology. : [https://github.com/eclipse/sw360/wiki/Dev-REST-API](https://github.com/eclipse/sw360/wiki/Dev-REST-API)

In other words, integrating source code scanning tool analysis results into SW360 as part of DevOps, thereby automating Component and Release registration, would greatly increase efficiency.
