# 0. Understanding OpenChain

LLMS index: [llms.txt](/llms.txt)

---

## 1. What Is the OpenChain Project?

Today, software continues to grow in scale and complexity. Developing a single piece of software can involve not only software built in-house but also a variety of software spanning the software supply chain, including open source, third-party software, and vendor SDKs.

If even a single organization within this complex software supply chain fails to comply with open source license obligations or fails to provide accurate information about its open source use, the enterprise distributing the final software has no choice but to fail at meeting its own open source license obligations. This can result in lawsuits and even the suspension of product sales.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 823px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/supplychain_hu_7af9bd5b7a71dad7.png" width="813" height="552">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>[OpenChain Open Source Software License Compliance General Public Guide]</center>

</p>
</figcaption>
</figure>


In December 2009, a lawsuit arose involving the open source project [Busybox](https://busybox.net/). Busybox is open source licensed under GPL-2.0 that is widely used in embedded systems, and 14 companies, including two South Korean companies, became subject to the lawsuit. A notable point in this case is that among the defendants were companies that were sued despite not developing the product themselves but only distributing it.

In such a complex software supply chain environment, it is very difficult for any single enterprise, no matter how excellent its processes are, to achieve perfect open source compliance on its own. Ultimately, for an enterprise to properly implement open source compliance, every member of the software supply chain must comply with license obligations and provide accurate open source information. This kind of trust must be built across the entire supply chain.

The [OpenChain](https://www.openchainproject.org/) project, part of the [Linux Foundation](https://www.linuxfoundation.org/), was founded on the belief that concisely and consistently defining the core requirements enterprises must meet for open source compliance, and having everyone comply with them, can build trust in open source licensing across the entire software supply chain.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 610px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/openchainlogo_hu_7581e73b0d768d82.png" width="600" height="79">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>[OpenChain Project Logo]</center>

</p>
</figcaption>
</figure>


At an open source conference in Europe in 2016, Dave Marr, an open source attorney at Qualcomm, emphasized exactly this point. To raise one enterprise's level of open source compliance, the compliance level of every member across the software supply chain must be raised. He further suggested that, to achieve this, leading enterprises that already have a solid understanding of open source and have established policies and processes should openly share their assets and know-how so that anyone could reference them. Conference attendees agreed with the idea that "open source compliance is not an area where enterprises can differentiate their profits. Enterprises want an appropriate level of risk management while investing minimal resources. That is why the more enterprises share their assets with one another, the more everyone can achieve compliance together with fewer resources." This is how the OpenChain project (then called a Work Group) began, with numerous global enterprises participating, including [Qualcomm](https://www.qualcomm.com/), [Siemens](https://www.siemens.com/), [Wind River](https://www.windriver.com/), [ARM](https://www.arm.com/), and [Adobe](https://www.adobe.com/).

The OpenChain project provides three main things to help enterprises more easily achieve open source compliance.

1. [OpenChain Specification](https://www.openchainproject.org/get-started/conformance)
2. [OpenChain Conformance Certification](https://certification.openchainproject.org/)
3. [Documentation Resources](https://www.openchainproject.org/resources)

Let's look at how enterprises can make use of each of these, one by one.

## 2. The OpenChain Specification and ISO/IEC Standards

The OpenChain Specification is a 10-page document that defines the core requirements for open source compliance. Version 1.0 of the OpenChain Specification was published in 2016. The OpenChain Specification is designed to be suitable for any enterprise, regardless of size or industry.

In 2020, version 2.1 of the specification was released, defining the six core requirements that enterprises must fulfill to achieve open source compliance, along with the list of materials needed to demonstrate them.

1. Program Establishment
2. Defining and Supporting Related Tasks
3. Reviewing and Approving Open Source Content
4. Creating and Delivering Compliance Artifacts
5. Understanding Open Source Community Engagement
6. Conformance to Specification Requirements

For an enterprise just starting out with open source compliance, a good strategy is to raise its maturity level by fulfilling these OpenChain Specification requirements one by one.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 604px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/spec_hu_14b92d21e27f4a59.png" width="594" height="775">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Source: https://github.com/OpenChain-Project/Specification/blob/master/Official/en/2.1/openchainspec-2.1.pdf></center>

</p>
</figcaption>
</figure>


In December 2020, this OpenChain Specification was formally registered as [ISO/IEC 5230:2020](https://www.iso.org/standard/81039.html), the international standard for open source compliance.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 681px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/iso_hu_b3d947295c1afb95.png" width="671" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Source: https://www.iso.org/standard/81039.html></center>

</p>
</figcaption>
</figure>


The OpenChain Specification, which had served as a de facto standard for the previous four years, was converted into the formal international standard ISO/IEC 5230:2020 — the first international standard to define open source compliance and process management. As a result, interest among global IT enterprises in complying with ISO/IEC 5230 is rising, and more enterprises are expected to require ISO/IEC 5230 compliance from their suppliers across the software supply chain.

In 2023, [ISO/IEC 18974](https://www.iso.org/standard/81039.html), a new standard for open source security assurance, was published. This standard is based on the OpenChain Security Assurance Specification and defines the core requirements for managing known security vulnerabilities in open source software. ISO/IEC 18974 covers the following key areas:

1. Identifying the core areas requiring security processes
2. How to assign roles and responsibilities
3. How to ensure the sustainability of the process

Like ISO/IEC 5230, ISO/IEC 18974 is concise and easy to understand, and it is backed by the global community, providing free reference materials and conformance resources.

Together, these two standards support organizations in effectively managing both license compliance and security assurance for open source software. Where ISO/IEC 5230 focuses on license compliance, ISO/IEC 18974 focuses on vulnerability management, making the two mutually complementary.



## 3. How to Certify to the ISO/IEC Standards

If an enterprise complies with all the requirements of both ISO/IEC 5230 and ISO/IEC 18974, it can be certified as having an open source program conforming to these standards. An open source program refers to the set of management systems — including policies, processes, and personnel — that an enterprise uses to carry out its open source compliance and security assurance activities.

The image below lists the item numbers required by ISO/IEC 5230. An enterprise that fulfills all these items can be recognized as having built a transparent and trustworthy open source governance system within the software supply chain.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 682px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/spec3111_hu_ca82823cea2e5897.png" width="672" height="440">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">



</p>
</figcaption>
</figure>


The [OpenChain project](https://www.openchainproject.org/) proposes three certification methods:

* Self-Certification
* Independent Assessment
* Third-Party Certification

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/certify_hu_6ec67eff1d183638.png" width="900" height="596">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i> https://www.openchainproject.org/get-started/conformance </i></center>

</p>
</figcaption>
</figure>


Let's look at each method.

### (1) Self-Certification

Self-certification is the method most recommended by the OpenChain project and has the advantage of incurring no cost. The OpenChain Project provides an [ISO/IEC 5230 self-certification website](https://openchainproject.org/checklist-iso-5230-2020) so that enterprises can verify on their own whether they comply with the OpenChain Specification. An enterprise's open source manager can sign up on this website and begin the online self-certification process. Self-certification proceeds by answering Yes/No questions, as shown below.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 846px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/question_hu_8cde8c4c95a4ad9f.png" width="836" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Source: https://certification.openchainproject.org/></center>

</p>
</figcaption>
</figure>


If an enterprise has built its open source compliance system well enough to answer Yes to every question in the OpenChain self-certification, it can submit the result on the website (Conforming Submission). After a brief question-and-answer verification process with the [Linux Foundation](https://www.linuxfoundation.org/), it can then declare ISO/IEC 5230 certification.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 877px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/sktannounce_hu_324168ab09a53f9c.png" width="867" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><Example: SK telecom's certification declaration - Source: https://www.openchainproject.org/featured/2021/09/08/sk-telecom></center>

</p>
</figcaption>
</figure>


By making this certification declaration, an enterprise is recognized within the global software supply chain as having an open source program that conforms to ISO/IEC 5230.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 850px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/announcelogo_hu_baf613e8a8938a49.png" width="840" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Enterprises that have declared conformant ISO/IEC 5230 programs, Source - https://www.openchainproject.org/  ></center>

</p>
</figcaption>
</figure>


The OpenChain project recommends the self-certification method. For reference, most enterprises that have declared OpenChain conformance have also adopted self-certification.

In addition, going through the self-certification process lets an enterprise determine what is lacking and what additional activities are needed. This guide explains, by major component — organization, policy, process, and so on — how to meet the requirements of ISO/IEC 5230 and ISO/IEC 18974.

For an enterprise that lacks the capability to make improvements on its own using only this guide, the independent assessment method can be considered.

### (2) Independent Assessment

In an independent assessment, an independent organization outside the enterprise inspects and evaluates the enterprise's open source compliance and security assurance status from an impartial standpoint. What distinguishes independent assessment is that it does not stop at producing an assessment report, but also provides consulting to address the gaps identified. (It does not, however, issue an official certificate.)

By receiving impartial assessment and consulting from an independent organization, an enterprise can raise its compliance and security assurance level, and through the iterative process of undergoing independent assessment again, refine its policies and build out its processes.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/independent2_hu_ff934ab02968f472.png" width="900" height="409">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Independent Compliance Assessment, Source - https://youtu.be/DEBd-g0Ab8E ></center>

</p>
</figcaption>
</figure>


Eventually, the enterprise reaches a level where it can obtain ISO/IEC 5230 and ISO/IEC 18974 certification, at which point it can move into the process of obtaining self-certification or third-party certification. In this way, independent assessment provides evaluation and consulting to raise an enterprise's open source compliance and security assurance level, supporting the enterprise in holding a conformant ISO/IEC 5230 and ISO/IEC 18974 program and obtaining certification.

Companies that provide independent assessment include [AlektoMetis](https://alektometis.com/) and [Source Code Control](https://sourcecodecontrol.co/), among others.

In South Korea, the [Conformance Group](https://openchain-project.github.io/OpenChain-KWG/subgroup/conformance/), a subgroup of the OpenChain Korea Work Group, is a community where enterprises discuss and share methods for achieving ISO/IEC 5230 and ISO/IEC 18974 conformance on their own. Anyone who is a member of the OpenChain Korea Work Group can participate and get help.

### (3) Third-Party Certification

An enterprise wishing to demonstrate a more reliable and transparent level of open source compliance and security assurance to buyers in the software supply chain can obtain a certificate from a third-party certification body and use it for promotional purposes. In addition, some buyers who demand stronger assurance of open source compliance and security may come to require third-party certification from their suppliers.

As of 2024, OpenChain's authorized third-party certification bodies are [ORCRO](https://orcro.co.uk/), [PWC](https://www.pwc.de/en/opensource), [TÜV SÜD](https://www.tuvsud.com/), [Synopsys](https://www.synopsys.com/), and [Bureau Veritas](https://group.bureauveritas.com/).

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/3rdpartycertifiers_hu_7c533f93b38ab71e.png" width="900" height="320">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Third-Party Certifiers, Source - https://www.openchainproject.org/partners ></center>

</p>
</figcaption>
</figure>


These bodies provide assessments to verify conformant ISO/IEC 5230 and ISO/IEC 18974 programs and issue certificates to enterprises that pass.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/pwc_hu_5bb61fd5d863abe9.png" width="900" height="331">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< PWC certification, Source - https://youtu.be/HslvXCM-4pQ ></center>

</p>
</figcaption>
</figure>


As of 2024, buyers or organizations that mandatorily require third-party certification are not yet common. However, some experts in the European automotive industry predict that it will not be long before ISO/IEC 5230 and ISO/IEC 18974 become mandatory for automotive software suppliers, much like [ASPICE](http://www.automotivespice.com/) (Automotive SPICE, an international standard process model for automotive software development).

In addition, detailed self-certification methods can be found in the following slides:

* [OpenChain Korea 9th Meeting - How to Self Certify](https://openchain-project.github.io/OpenChain-KWG/meeting/9th/OpenChain_Korea_20210311_howto.pptx)



## 4. OpenChain Resources

The [OpenChain project](https://www.openchainproject.org/) provides a variety of documentation resources that enterprises need to build a compliance program, including policy document templates and training materials. These materials are designed to support conformance with the OpenChain Specification and general open source compliance activities, and are provided under the CC-0 license so that anyone can use them freely.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 843px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/resource_hu_bf8f6802d2e8f11f.png" width="833" height="557">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< OpenChain Curriculum, Source - https://www.openchainproject.org/resources ></center>

</p>
</figcaption>
</figure>


Much of this guide was also written based on materials published by OpenChain. If an enterprise's open source manager needs policies, processes, or training materials, they should look to the OpenChain Resources first. These materials are also translated into Korean and published. The [OpenChain Korea Work Group](https://openchain-project.github.io/OpenChain-KWG/) leads this translation effort. Anyone interested can [participate](https://openchain-project.github.io/OpenChain-KWG/resource/) in the Korean translation.

The OpenChain project also provides additional resources by running various webinars and study groups:

1. Webinars: The OpenChain project regularly hosts webinars to share the latest trends and best practices in open source compliance and security. These webinars can be found on the [OpenChain website](https://openchainproject.org/webinars), where recordings are also available.

2. Training Materials: The OpenChain project provides a [comprehensive training curriculum](https://github.com/OpenChain-Project/Reference-Material) to help enterprises develop internal training programs. This material covers a range of topics, from the basic concepts of open source software to license compliance and security assurance.

By making use of these various resources, an enterprise can build and maintain a strong open source program that conforms to the ISO/IEC 5230 and ISO/IEC 18974 standards.


## 5. Trends in ISO/IEC Standard Adoption

Adoption of the ISO/IEC 5230 and ISO/IEC 18974 standards is showing a gradually expanding trend across the global software supply chain.

In early 2021, news emerged that a German automaker had begun requiring its parts suppliers to have an ISO/IEC 5230 compliance plan. In response, a European open source professor predicted that "it is clear that buyers in the software supply chain will increasingly require suppliers to comply with ISO/IEC 5230," adding that "in the automotive industry, it will come to occupy the same position as ASPICE."

Reflecting this outlook, in May 2021, [Scania](https://www.scania.com/), part of the Volkswagen Group, incorporated a requirement for ISO/IEC 5230 compliance into its own corporate standard (STD 4589) that suppliers must follow.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 323px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/scania_hu_2ffdfde30b765742.png" width="313" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>linkedin, May 2021</i></center>

</p>
</figcaption>
</figure>


Also, in July 2021, [Bosch](https://www.bosch.com/), an automotive and industrial technology company, declared that all of its group companies would have an ISO/IEC 5230-compliant program by the end of the year. The industry outlook is that it is only a matter of time before every automaker, and other industries as well, begin requiring ISO/IEC 5230 within their software supply chains.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 323px">
<img class="card-img-top" src="/docs/opensource_for_enterprise/0-openchain/bosch_hu_3bddac9870a960ef.png" width="313" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>linkedin, July 2021</i></center>

</p>
</figcaption>
</figure>


In 2023, ISO/IEC 18974, a new standard for open source security assurance, was published. This standard defines the core requirements for managing known security vulnerabilities in open source software. Together with ISO/IEC 5230, ISO/IEC 18974 supports organizations in effectively managing both license compliance and security assurance for open source software.

As of 2024, this trend is accelerating further. For example, [KT](https://www.kt.com/) announced in October 2024 that it had obtained ISO/IEC 18974 certification. This shows that South Korean enterprises, too, are actively adopting international standards for open source security management.

The activities of the [OpenChain Korea Work Group](https://openchain-project.github.io/OpenChain-KWG/) are also becoming more active. At its 22nd regular meeting held in June 2024, discussions covered the state of readiness for the ISO/IEC 18974 open source security standard and SBOM-based software supply chain management guidelines. This shows that South Korean enterprises are actively embracing the ISO/IEC 5230 and ISO/IEC 18974 standards.

This trend is expected to continue. As the complexity of the software supply chain increases and security threats grow, the importance of international standards such as ISO/IEC 5230 and ISO/IEC 18974 is likely to grow further. By complying with these standards, enterprises will be able to increase transparency in their open source use and effectively manage security risk.
