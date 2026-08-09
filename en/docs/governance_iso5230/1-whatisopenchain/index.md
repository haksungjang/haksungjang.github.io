# 1. Understanding ISO/IEC 5230

LLMS index: [llms.txt](/llms.txt)

---

## What is ISO/IEC 5230?

ISO/IEC 5230 is a specification created by the Linux Foundation's OpenChain Project that defines the minimum core requirements for ensuring trustworthy open source compliance across the software supply chain.

Today's software keeps growing in scale and complexity. Building a single piece of software can involve not only software developed in-house but also a wide range of software from across the supply chain, including open source, third-party software, and vendor SDKs.

If even one organization in this complex software supply chain fails to comply with its open source license obligations or fails to provide accurate information about its open source usage, the company distributing the final software has no choice but to fail at open source license compliance as well. This can result in lawsuits that force the company to halt sales of its product.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 823px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/supplychain_hu_7af9bd5b7a71dad7.png" width="813" height="552">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>[OpenChain Open Source Software License Compliance General Public Guide]</center>

</p>
</figcaption>
</figure>


In December 2009, there was a lawsuit involving the open source project Busybox. Busybox is a GPL-2.0-licensed open source project widely used in embedded systems, and 14 companies, including two Korean companies, were named as defendants. What stood out about this case is that even companies that had not developed the product themselves, but had merely distributed it, were sued.

In such a complex software supply chain environment, it is extremely difficult for any single company, no matter how excellent its processes are, to achieve complete open source compliance on its own. In the end, for a company to properly implement open source compliance, every participant in the software supply chain must comply with license obligations and provide accurate open source information. This kind of trust must be built across the entire supply chain.

The Linux Foundation's [OpenChain](https://www.openchainproject.org/) project was founded on the belief that if the core requirements a company must meet for open source compliance are defined concisely and consistently, and everyone complies with them, trust regarding open source licensing can be built across the entire software supply chain.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 610px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/openchainlogo_hu_7581e73b0d768d82.png" width="600" height="79">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>[OpenChain Project Logo]</center>

</p>
</figcaption>
</figure>


At an open source conference in Europe in 2016, Dave Marr, an open source attorney at Qualcomm, emphasized exactly this point. To raise a company's level of open source compliance, the level of open source compliance of every participant in the software supply chain must be raised. He also suggested that, to achieve this, advanced companies that already understand open source well and have established policies and processes could open up their assets and know-how so that anyone could reference them. Conference attendees agreed with the idea that "open source compliance is not an area where companies can differentiate their competitive advantage. Companies want an adequate level of risk management while investing minimal resources. That is why the more companies share their assets with one another, the more everyone can achieve compliance with fewer resources." That is how the OpenChain project (then a Work Group) began, with the participation of numerous global companies including Qualcomm, Siemens, Wind River, ARM, and Adobe.

The OpenChain project provides companies with three main things to make it easier to achieve open source compliance.

1. The OpenChain Specification[^specification]
2. OpenChain Conformance Certification[^question]
3. Reference materials[^resource]

[^specification]: OpenChain Specification - https://www.openchainproject.org/get-started/conformance
[^question]: OpenChain self-certification website - https://certification.openchainproject.org/
[^resource]: OpenChain reference materials - https://www.openchainproject.org/resources

Let's look at how companies can use each of these.

## The OpenChain Specification and ISO/IEC 5230

The OpenChain Specification is a 10-page document that defines the core requirements for open source compliance. OpenChain Specification version 1.0 was released in 2016. The OpenChain Specification is designed to be applicable to any company, regardless of its size or industry.

Version 2.1 of the specification was released in 2020, and it defines six core requirements that a company must fulfill to achieve open source compliance, along with a list of the evidence needed to demonstrate each.

1. Establishing the program
2. Defining and supporting relevant roles
3. Reviewing and approving open source content
4. Creating and delivering compliance artifacts
5. Understanding engagement with open source communities
6. Complying with the specification's requirements

For a company just starting out with open source compliance, a good strategy is to raise its maturity level by fulfilling these OpenChain Specification requirements one by one.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 604px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/spec_hu_14b92d21e27f4a59.png" width="594" height="775">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Source: https://github.com/OpenChain-Project/Specification/blob/master/Official/en/2.1/openchainspec-2.1.pdf></center>

</p>
</figcaption>
</figure>


In December 2020, this OpenChain Specification was formally registered as the international standard[^ISO] for open source compliance.

[^ISO]: ISO/IEC 5230: https://www.iso.org/standard/81039.html

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 681px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/iso_hu_b3d947295c1afb95.png" width="671" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Source: https://www.iso.org/standard/81039.html></center>

</p>
</figcaption>
</figure>


The OpenChain Specification, which had been a de facto standard for the previous four years, was converted into the formal international standard ISO/IEC 5230:2020, the first international standard to define open source compliance and process management. As a result, interest in ISO/IEC 5230 compliance is growing among global IT companies, and more companies are expected to require their suppliers in the software supply chain to comply with ISO/IEC 5230.

## How to Get Certified for ISO/IEC 5230

If a company complies with all of the requirements in ISO/IEC 5230, it can be certified as having an open source program that conforms to ISO/IEC 5230. An open source program refers to the set of management systems, including policies, processes, and personnel, that a company puts in place to carry out open source compliance activities.

The image below lists the item numbers required by ISO/IEC 5230. A company that satisfies all of these items can be recognized as having built a transparent and trustworthy open source governance system across its software supply chain.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 682px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/spec3111_hu_ca82823cea2e5897.png" width="672" height="440">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">



</p>
</figcaption>
</figure>


The OpenChain project proposes three certification methods.
* Self Certification
* Independent Assessment
* Third-Party Certification

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/certify_hu_6ec67eff1d183638.png" width="900" height="596">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i> https://www.openchainproject.org/get-started/conformance </i>></center>

</p>
</figcaption>
</figure>


Let's look at each method.

### 1. Self Certification

Self certification is the method most recommended by the OpenChain project, and it has the advantage of being free of charge. The OpenChain Project provides an OpenChain self-certification website so that companies can check for themselves whether they comply with the OpenChain Specification[^question]. A company's open source manager can sign up on the OpenChain self-certification website and begin the online self-certification process. Self certification proceeds by answering Yes/No questions as shown below.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 846px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/question_hu_8cde8c4c95a4ad9f.png" width="836" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Source: https://certification.openchainproject.org/></center>

</p>
</figcaption>
</figure>


If a company has built a solid open source compliance system and can answer Yes to every question in OpenChain self-certification, it can submit these results on the website as a Conforming Submission. After a simple Q&A-style confirmation process by the Linux Foundation, the company can then declare ISO/IEC 5230 certification.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 877px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/sktannounce_hu_324168ab09a53f9c.png" width="867" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><Example: SK telecom's certification declaration - Source: https://www.openchainproject.org/featured/2021/09/08/sk-telecom></center>

</p>
</figcaption>
</figure>


Once this certification declaration is made, the company is recognized in the Global Software Supply Chain as having an open source program that conforms to ISO/IEC 5230.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 850px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/announcelogo_hu_baf613e8a8938a49.png" width="840" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Companies that have declared an ISO/IEC 5230 conforming program, source - https://www.openchainproject.org/  ></center>

</p>
</figcaption>
</figure>


The OpenChain project recommends the self-certification approach. For reference, most companies that have declared OpenChain conformance have also adopted self certification.

Furthermore, through the self-certification process, a company can determine what it lacks and what additional activities are needed. This guide explains how to comply with the ISO/IEC 5230 requirements, organized by key components such as organization, policy, and process.

If a company lacks the capability to fill these gaps on its own using the guide alone, it can consider the independent assessment method.

### 2. Independent Assessment

In independent assessment, an independent organization outside the company examines and evaluates the company's open source compliance status from a fair, external perspective. What distinguishes independent assessment is that it does not stop at producing an assessment report, but also provides consulting to help address the gaps that are identified. (Note, however, that it does not issue an official certificate.)

Through fair assessment and consulting from an independent organization, a company can raise its compliance level, and by repeating independent assessments, it can refine its policies and build out its processes.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/independent2_hu_ff934ab02968f472.png" width="900" height="409">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Independent Compliance Assessment, source - https://youtu.be/DEBd-g0Ab8E ></center>

</p>
</figcaption>
</figure>


Eventually, the company reaches a level at which it can obtain ISO/IEC 5230 certification, at which point it can proceed to self certification or third-party certification. In this way, independent assessment provides the evaluation and consulting needed to raise a company's open source compliance level, supporting the company as it works to build an ISO/IEC 5230 conforming program and obtain certification.

Companies that provide independent assessment include [AlektoMetis](https://alektometis.com/)[^AlektoMetis] and [Source Code Control](https://sourcecodecontrol.co/)[^SourceCodeControl].

[^AlektoMetis]: AlektoMetis - https://alektometis.com/,
[^SourceCodeControl]: Source Code Control - https://sourcecodecontrol.co/

In Korea, the [Conformance Group](https://openchain-project.github.io/OpenChain-KWG/subgroup/conformance/)[^conformancegroup], a subgroup of the OpenChain Korea Work Group, is a community where companies discuss and share methods for achieving ISO/IEC 5230 compliance among themselves. Any member of the OpenChain Korea Work Group can join and get help.

[^conformancegroup]: Conformance Group - https://openchain-project.github.io/OpenChain-KWG/subgroup/conformance/

### 3. Third-Party Certification

If a company wants to demonstrate a more reliable and transparent level of open source compliance to buyers in the software supply chain, it can obtain a certificate from a third-party certification body and use it for promotional purposes. It is also expected that some buyers who demand stronger assurance of open source compliance reliability may require their suppliers to obtain third-party certification.

As of October 2021, OpenChain's authorized third-party certification bodies are [ORCRO](https://orcro.co.uk/)[^ORCRO], [PWC](https://www.pwc.de/en/opensource)[^PWC], [TÜV SÜD](https://www.tuvsud.com/)[^TUVSUD], [Synopsys](https://www.synopsys.com/)[^synopsys], and [Bureau Veritas](https://group.bureauveritas.com/)[^BV].

[^ORCRO]: ORCRO- https://orcro.co.uk/
[^PWC]: PWC - https://www.pwc.de/en/opensource
[^TUVSUD]: TÜV SÜD - https://www.tuvsud.com
[^synopsys]: Synopsys - https://www.synopsys.com/
[^BV]: Bureau Veritas - https://group.bureauveritas.com/

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/3rdpartycertifiers_hu_7c533f93b38ab71e.png" width="900" height="320">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< Third-Party Certifiers, source - https://www.openchainproject.org/partners ></center>

</p>
</figcaption>
</figure>


These bodies provide assessments to confirm ISO/IEC 5230 conforming programs and issue certificates to companies that pass.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 910px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/pwc_hu_5bb61fd5d863abe9.png" width="900" height="331">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< PWC certification, source - https://youtu.be/HslvXCM-4pQ ></center>

</p>
</figcaption>
</figure>


As of October 2021, there still appear to be no buyers or institutions that mandatorily require third-party certification. However, some experts in the European automotive industry predict that it will not be long before ISO/IEC 5230 becomes mandatory for automotive software suppliers, much like [ASPICE](http://www.automotivespice.com/) (Automotive SPICE)[^aspice], the international standard process model for automotive software development.

[^aspice]: ASPICE: International standard process model for automotive software development - http://www.automotivespice.com

For more detail on the self-certification method, you can also refer to the following slides.

* [https://openchain-project.github.io/OpenChain-KWG/meeting/9th/OpenChain_Korea_20210311_howto.pptx](https://openchain-project.github.io/OpenChain-KWG/meeting/9th/OpenChain_Korea_20210311_howto.pptx)

## OpenChain Resources

The OpenChain project provides a variety of reference materials that companies need to build a compliance program, including policy document templates and training materials. These materials are designed to help organizations comply with the OpenChain Specification and support common open source compliance activities, and they are provided under a CC-0 license so that anyone can use them freely.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 843px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/resource_hu_bf8f6802d2e8f11f.png" width="833" height="557">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center>< OpenChain Curriculum, source - https://www.openchainproject.org/resources ></center>

</p>
</figcaption>
</figure>


Much of the content in this guide was also written based on materials published by OpenChain. If a company's open source manager needs policies, processes, or training materials, they should first check the OpenChain Resources. These materials are also translated into Korean and published. The [OpenChain Korea Work Group](https://openchain-project.github.io/OpenChain-KWG/)[^KWG] leads this translation effort. Anyone interested can [participate](https://openchain-project.github.io/OpenChain-KWG/resource/) in the Korean translation work[^translate].

[^KWG]: OpenChain Korea Work Group - https://openchain-project.github.io/OpenChain-KWG/

[^translate]: Korean translation work - https://openchain-project.github.io/OpenChain-KWG/resource/

## The ISO/IEC 5230 Trend

In early 2021, news emerged that a German automaker had begun requiring its parts suppliers to plan for ISO/IEC 5230 compliance, and a European open source professor said, "It is clear that buyers in the software supply chain will increasingly require suppliers to comply with ISO/IEC 5230 going forward," adding, "In the automotive industry, it will become like A-SPICE."

Reflecting this trend, in May 2021, Scania, part of the Volkswagen Group, included a requirement for ISO/IEC 5230 compliance in its own corporate standard (STD 4589) that suppliers must follow.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 323px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/scania_hu_2ffdfde30b765742.png" width="313" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>LinkedIn, May 2021</i></center>

</p>
</figcaption>
</figure>


Also, in July 2021, Bosch, an automotive and industrial technology company, declared that all of its group companies would have an ISO/IEC 5230 conforming program by the end of the year. Industry observers suggest it is only a matter of time before all automakers and companies in other industries begin requiring ISO/IEC 5230 within their software supply chains.

<figure class="card rounded p-2 td-post-card mb-4 mt-4" style="max-width: 323px">
<img class="card-img-top" src="/docs/governance_iso5230/1-whatisopenchain/bosch_hu_3bddac9870a960ef.png" width="313" height="600">
<figcaption class="card-body px-0 pt-2 pb-0">
<p class="card-text">


<center><i>LinkedIn, July 2021</i></center>

</p>
</figcaption>
</figure>
