# 2019 FOSS Legal Issue Top 10

> Top 10 FOSS legal developments in 2019

---

LLMS index: [llms.txt](/llms.txt)

---

---

> Hello.
> 
> Mark Radcliffe, an IP attorney at DLA Piper, recently contributed an article titled "[Top 10 FOSS legal developments in 2019](https://www-synopsys-com.cdn.ampproject.org/c/s/www.synopsys.com/blogs/software-security/top-10-open-source-legal-issues-2019/amp/)." Expecting it to be useful to those interested in Open Source Compliance, I have summarized it to the extent I understand it. \(Since I am not a lawyer, there may be shortcomings in the legal terminology or interpretation. I would appreciate it if you let me know of anything that needs correcting.\)

---

## 1. McHardy \(Linux system copyright troll, Germany\) adopts a new strategy

Patrick McHardy, an early contributor to the Linux kernel, has engaged in activity in Germany resembling that of a copyright troll seeking financial gain through litigation as a weapon. He has been active for seven and a half years and is reported to have approached more than 80 companies, but since many companies settled rather than going to trial and German court proceedings are kept confidential, it is difficult to estimate exact figures. In the [Geniatech case](https://www.jolts.world/index.php/jolts/article/view/128), which McHardy filed in 2017, the appellate court judge in 2018 responded skeptically to McHardy's copyright claims alleging GPLv2 violations, and McHardy ultimately withdrew the suit.

Since then, McHardy has not been generating further lawsuits, but he continues to make claims of GPLv2 compliance violations. Whereas he previously extracted financial gain by first signing a light contractual penalty and then, after discovering additional violations, enforcing a heavier penalty, since early 2019 he has shifted to a new strategy of demanding compensation for the time he spent finding violations (demanding excessive engineering costs).

## 2. Richard Stallman resigns from GNU, MIT, and the Free Software Foundation

Richard Stallman [resigned](https://www.fsf.org/news/richard-m-stallman-resigns) as President and board member of the Free Software Foundation. The Free Software (and Open Source) movement owes a great deal to Richard Stallman's vision and sustained effort. However, over the past several years he has stirred controversy by voicing various opinions on matters outside the FOSS movement. His statements this year about a victim in the Jeffrey Epstein case led to pressure for him to resign from the Free Software Foundation.

He also resigned from MIT, and the maintainers of the GNU operating system removed him. While acknowledging his contributions, they [stated](https://guix.gnu.org/blog/2019/joint-statement-on-the-gnu-project/) the following: "However, it must be recognized that over the years Stallman's conduct has undermined the interests of [all computer users](https://www.gnu.org/gnu/manifesto.html#benefit), a core value of the GNU project. GNU cannot properly carry out its mission when a leader's conduct diverges from the values we aim to reach."

It is not yet clear who will take up the leadership role in the Free Software movement going forward.

\(Related domestic article: [http://www.zdnet.co.kr/view/?no=2019091817351](http://www.zdnet.co.kr/view/?no=20190918173513)\)

## 3. The trade war reaches OSS

In May 2019, the US Bureau of Industry and Security (BIS) [placed](https://www.federalregister.gov/documents/2019/05/21/2019-10616/addition-of-entities-to-the-entity-list) Huawei Technologies Co., Ltd. and 68 non-US affiliates on the Entity List. In August 2019, BIS added 46 more non-US Huawei affiliates to the Entity List. Companies cannot export, re-export, or transfer items subject to the Export Administration Regulations (EAR) to Huawei, except in four areas for which BIS issued a temporary license (narrowed to three in August 2019).

Google immediately [cut off](https://www.theverge.com/2019/5/19/18631558/google-huawei-android-suspension) access to Google Services such as the Google Play Store as well as the Android OS (though some updates continued to be provided under the BIS exception). Huawei had to fall back on using the Android Open Source Project. BIS extended the Temporary General License several times. Huawei [announced](https://www.engadget.com/2019/08/09/huawei-harmony-os-hongmeng-android/) that it is developing a version that could replace Android and may ship it with its next phone. This suspension of Huawei's access to Google's Android OS appears likely to be permanent, raising the possibility that Android will split into two ecosystems, one US-based and one China-based.

## 4. Ethical restrictions in OSS licenses

There have been repeated attempts to condition OSS use on ethical grounds. This year saw several examples of "Ethical Licenses." In one case, developer Seth Vargo [deleted](https://www.wired.com/story/developer-deletes-code-protest-ice/) his open source library project Chef Sugar, making it unavailable to users. He deleted Chef Sugar because it was used as part of a contract with U.S. Immigration and Customs Enforcement (ICE), which he criticized for detaining parents and children separately after illegal entry.

Chef, the provider of Chef Sugar, initially tried to resolve the issue by asserting that it owned the copyright to the Chef Sugar project. Chef's CEO said Chef would continue to provide services to ICE, but four days later the CEO [announced](https://www.businessinsider.com/chef-ice-contract-expires-next-year-2019-9) that Chef would not renew its license with ICE and would donate the proceeds of the ICE contract to charities dealing with family separation (families separated because of ICE).

Activist Coraline Ada Ehmke created the [Hippocratic License](https://firstdonoharm.dev/). She says this license "adds ethics to Open Source projects." The Hippocratic License adds the following clause to the MIT License:

"The software may not be used by anyone for systems or activities that actively and knowingly endanger, harm, or otherwise threaten the physical, mental, economic, or general well-being of other individuals or groups, in violation of the [United Nations Universal Declaration of Human Rights](https://www.un.org/en/universal-declaration-human-rights/)."

OSI promptly [stated](https://perens.com/2019/09/23/sorry-ms-ehmke-the-hippocratic-license-cant-work/) that the Hippocratic License is not an "open source" license. Unfortunately, this additional clause makes the license very difficult to interpret.

## 5. FOSS strategies of blockchain projects

Many [blockchain](https://www.synopsys.com/glossary/what-is-blockchain.html) projects have been released under FOSS licenses. The blockchain community has made complex and unusual choices regarding infrastructure technology. Algorand, a new blockchain project, released its SDK, example applications, and helper library under the MIT License in 2019. However, the Algorand node software was licensed under [AGPLv3](https://github.com/algorand/go-algorand/blob/master/COPYING_FAQ). Many companies' legal or Compliance departments restrict the use of software under AGPLv3 because ensuring compliance is difficult. This may make it harder for companies to adopt the Algorand project.

## 6. The Oracle v. Google war

The Court of Appeals for the Federal Circuit (CAFC) [issued](http://www.cafc.uscourts.gov/sites/default/files/opinions-orders/17-1118.Opinion.3-26-2018.1.PDF) its second decision in Oracle v. Google, ruling that Google's unauthorized use of 37 packages of Oracle's Java Application Programming Interface (API) in the Android operating system infringed Oracle's copyright. In 2014, the CAFC reversed the district court's first-instance ruling and held that the API was copyrightable, remanding the case to the district court to determine whether the use qualified as Fair Use. In 2016, the district court ruled in Google's favor on the ground that Google's use of the API constituted Fair Use, and Oracle appealed. In March 2019, the CAFC once again reversed the district court's ruling, holding that Google's use of the API did not, as a matter of law, constitute Fair Use. The Supreme Court granted certiorari (arguments scheduled to begin in March 2020). This case will be a critically important precedent in determining the scope of copyright protection for computer software.

\(Related domestic article: [https://byline.network/2020/02/11-94/](https://byline.network/2020/02/11-94/)\)

## 7. The German Hellwig/VMware case concludes

In March 2015, Christoph Hellwig, a core Linux kernel developer, [sued VMware](https://www.theregister.co.uk/2015/03/05/vmware_sued_for_gpl_violation_by_linux_kernel_developer/) in the Hamburg Regional Court in Germany. Hellwig claimed that VMware violated the terms of GPLv2 by (1) combining Linux with VMware's proprietary code, called "vmkernel," in a manner that created a derivative work, while (2) failing to provide the complete corresponding source code for vmkernel as required under GPLv2. Vmkernel, the "kernel" of the VMware ESXi operating system, manages the hardware and software resources of the physical server.

VMware responded that vmkernel is not a derivative work of Linux but merely communicates with Linux through the VMK API. VMware also [stated](http://vmware.com/company/news/vmware-update-to-mr-hellwigs-legal-proceedings.html) that the drivers that operate with vmkernel need not be Linux drivers, and that "a compatibility alternative called 'vmklinux' (interoperating with any Linux driver) via a loadable kernel module is loaded by vmkernel and interfaces with vmkernel through the VMK API." Because the complaint and court filings are kept confidential under German court rules, the facts underlying the dispute cannot be confirmed.

The Hamburg court dismissed Hellwig's suit on the ground that Hellwig failed to establish which components of the Linux system he had developed and whether VMware had used those components. The Hamburg Higher Regional Court dismissed the appeal of the first-instance ruling, and Hellwig decided not to appeal that decision further. Neither court addressed the substantive issues raised in the complaint; both ruled based on insufficient evidence regarding the right of ownership or copyright-protectability of certain components taken from Linux.

In response to these rulings, VMware [stated](https://www.vmware.com/company/news/updates/march-2019-hellwig-legal-proceedings.html), "VMware has been actively working for several years, independent of the litigation, to remove vmklinux from vSphere and hopes to accomplish this in a future major release."

## 8. OSS business models and licensing

Many commercial FOSS companies have expressed concern that traditional OSS licenses allow Cloud Service Providers to use their programs without paying the FOSS company. In June 2019, CockroachDB [adopted the BSL (Business Source License)](https://www.cockroachlabs.com/blog/oss-relicensing-cockroachdb/), first developed for MariaDB by Bruce Perens, one of the founders of the Open Source movement. CockroachDB's CEO said the following: "Today we are adopting a very permissive license, the BSL (Business Source License). Users of CockroachDB can scale CockroachDB across multiple nodes. They can use CockroachDB or embed it in an application (whether distributing the application to customers or running it as a service). They can also run it internally as a service. **The one and only restriction is that CockroachDB cannot be offered as a commercial service without purchasing a license.**"

In November, Sentry also [adopted the BSL](https://blog.sentry.io/2019/11/06/relicensing-sentry/). There were also several developments regarding new licenses adopted in 2018. In 2018, Redis Labs changed the license of its Redis modules from AGPL to Apache v2.0 with Commons Clause added (these Redis modules are add-ons on top of Redis core). Commons Clause was introduced as an addition to the Apache Software License version 2 to restrict use of the product by Cloud Service Providers. The introduction of this mixed license was highly controversial, and Redis abandoned the Commons Clause, [adopting the Redis Source Available License](https://redislabs.com/blog/redis-labs-modules-license-changes/) for RediSearch, RedisGraph, RedisJSON, Redis-ML, and RedisBloom. Other companies adopted similar licenses.

## 9. Conflicts over RAND patent licensing between FOSS-governed and standards-body-governed projects

As FOSS has become widely adopted as a development methodology, standard setting organizations (SSOs) have worked to incorporate FOSS approaches into their processes. However, the methodologies of FOSS projects and SSOs differ considerably. FOSS projects operate with much more diverse responsibilities and in a more decentralized manner. One particular source of friction is the typical SSO approach of granting members patent rights on a royalty-bearing basis (under Fair, Reasonable, And Non-Discriminatory / FRAND terms). This friction is reflected in articles addressing patent licensing disputes under open source licenses ([here](http://www.stlr.org/download/volumes/volume20/kappos.pdf) and [here](http://stlr.org/2019/03/04/oss-and-frand-complementary-models-for-innovation-and-development/)).

David Kappos, the former Director of the US Patent and Trademark Office, [stated](http://stlr.org/2018/10/15/the-truth-about-oss-frand-by-all-indications-compatible-models-in-standards-settings/) the following: "Instead, we have found substantial support for the opposite conclusion — that OSD-compliant licenses should not be assumed to grant patent licenses absent an explicit patent grant clause. That is, OSS licensors can choose licenses that grant patent licenses, or choose licenses that do not, such as MIT and Berkeley. This preserves the ability of OSS and standard-essential patents (SEP) to work together to advance innovation."

Van Lindberg, on the other hand, [responded](http://stlr.org/2019/03/04/oss-and-frand-complementary-models-for-innovation-and-development/) as follows: "This is why open source and FRAND are complementary but not compatible: open source and FRAND innovate relying on different intellectual property policies. These two development models can learn from each other and compete with each other, but they are fundamentally grounded in different underlying principles."

"It's understandable why SSOs want to incorporate OSS. Open source is cheap, interoperable, and innovative. SSOs have the ability to change to secure interoperability with OSS. All they need to do, as many organizations have already done, is adopt a Royalty-free IPR (intellectual property rights) policy. But an SSO that wants to impose FRAND royalties ultimately has the same choice that commercial companies have when dealing with open source: either respect the licenses and rules that must be followed when using OSS, or invest the time to create a commercial version."

The difference in how royalties are paid on patents is creating tension between the FOSS and SSO communities. And some in the SSO community have argued that they should be able to define what "open source" is. This issue does not appear likely to be resolved anytime soon.

## 10. Open source licensing expands into data and cryptography issues

Data has been called the "new oil." The concept of open source has been applied to data licensing (see the Linux Foundation's [Community Data License Agreement](https://cdla.io/) from 2017). This year, however, it was applied to data and cybersecurity. For example, the [Cryptographic Autonomy License](https://github.com/holochain/cryptographic-autonomy-license) (CAL) was developed by Van Lindberg, an open source lawyer well known from his work with Holochain. Holochain [explained](https://medium.com/holochain/understanding-the-cryptographic-autonomy-license-172ac920966d) this license as follows: "For distributed apps, the cryptographic key occupies a strange middle ground between code and user data. Code is functional and provides the process that routes and transforms user data as input or output for a computing system. User data is generally more like passive content that can be processed and stored by code. A cryptographic key is both user data and functional. In Holochain, cryptographic keys mediate proof of ownership of data: where data is stored, who controls the data, who verifies the security and encryption of communication and storage, and the operation of the chain structure for progressive hashing and signing that establishes the order and integrity of data."

The CAL [provides](https://github.com/holochain/cryptographic-autonomy-license/blob/master/README.md) the following obligation with respect to user data: "Throughout any period in which You exercise any of the permissions granted to You under this License, You must also provide to any Recipient to whom you provide services via the Work, a no-charge copy, provided in a commonly used electronic form, of the Recipient's User Data in your possession, to the extent that such User Data is available to You for use in conjunction with the Work."

The license also allows a delay in providing source code when addressing a security flaw, which is a new and welcome approach: "You may delay providing the Source Code corresponding to a particular modification of the Work for up to ninety (90) days (the 'Embargo Period') if: a) the modification is intended to address a newly-identified vulnerability or a security flaw in the Work, b) disclosure of the vulnerability or security flaw before the end of the Embargo Period would put the data, identity, or autonomy of one or more Recipients of the Work at significant risk, c) You are participating in a coordinated disclosure of the vulnerability or security flaw with one or more additional Licensees, and d) Access to the Source Code pertaining to the modification is provided to all Recipients at the end of the Embargo Period."

The Linux Foundation has continued to work on open data issues through the JDF (Joint Development Foundation). Working with AWS, Genesys, and Salesforce, the JDF developed the Cloud Information Model, an open source data model that standardizes data interoperability across cloud applications.
