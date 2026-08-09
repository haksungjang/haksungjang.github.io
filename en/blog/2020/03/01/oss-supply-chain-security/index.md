# OSS Supply Chain Security

> A Publication of The Linux Foundation

---

LLMS index: [llms.txt](/llms.txt)

---

---

> Hello.
> 
> In February 2020, the Linux Foundation published an article about [security risks in the Open Source Software Supply Chain](https://www.linuxfoundation.org/publications/2020/02/open-source-software-supply-chain-security/), and this post summarizes that content.

---

## Introduction

Modern software development has become a far more complex process than it was in past decades. It is rare for an organization to develop all of its software in-house. Instead, most organizations make use of Open Source Software (OSS). They build products by incorporating a variety of OSS and developing only the connecting pieces in-house.

The "Software Supply Chain" is already highly complex. Whereas software used to be delivered to customers on physical media such as CDs, today's software (both OSS and proprietary software alike) is stored in "repositories" and distributed remotely on demand through a Project Dependency Manager (PDM) or Package Manager.

![](https://t1.daumcdn.net/thumb/R1280x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/UFqIj_ywPKiBf0csdt91M6rzRSU.png)

Most of the recent attention paid to security in the software supply chain has focused on the Developer, the first link in the chain, or the End User, the last link, but vulnerabilities exist at every level. Consider the following incidents.

### Xcode Repackaging for Malware Distribution in 2015

In 2015, a security firm warned Apple that 39 applications distributed through the App Store were infecting iPhones and iPads. The malicious applications downloaded to devices connected to a remote command-and-control server and uploaded sensitive user information. Further investigation revealed that the malicious code had been inserted into the applications through a "repackaged" version of Xcode, Apple's official development platform.

These apps were immediately removed, and Apple took additional measures to ensure that only legitimate developers could access the official version of Xcode, but the incident highlighted the risk that a software security vulnerability within the software supply chain can affect multiple applications.

> Apple scrambles after 40 malicious “XcodeGhost” apps haunt App Store, Dan Goodin, ArsTechnica \(Sep. 25, 2015\), [https://arstechnica.com/information-technology/2015/09/apple-scrambles-after-40-malicious-xcodeghost-apps-haunt-app-store/](https://arstechnica.com/information-technology/2015/09/apple-scrambles-after-40-malicious-xcodeghost-apps-haunt-app-store/) 


### The "left-pad" Dependency Incident of 2016

In 2016, following a naming-rights dispute over an unrelated OSS package, a well-known developer removed all of his OSS packages from npm, the software registry used to distribute Node.js code. The developer removed a total of 273 packages from npm, but the problem showed up in just one of them: "left-pad."

"left-pad," an incredibly simple package, right-aligns text to produce more readable text output. However, because a large number of important downstream packages depended on "left-pad," its sudden disappearance broke countless downstream packages. Another developer replaced the missing package with a functionally equivalent one, but downstream developers were still left with the task of updating their code to reference the new package.

This incident starkly highlighted the risk developers face when depending on upstream packages over which they have little control, and it exposed a broader "dependency" problem: because the package was embedded as an upstream dependency, even developers who had no intention of depending on "left-pad" were affected.

The "left-pad" incident occurred three years ago, but problems like this remain.

> Rage-quit: Coder unpublished 17 lines of JavaScript and “broke the Internet”, Sean Gallagher, ArsTechnica \(March 24, 2016\), [https://arstechnica.com/information-technology/2016/03/rage-quit-coder-unpublished-17-lines-of-javascript-and-broke-the-internet/](https://arstechnica.com/information-technology/2016/03/rage-quit-coder-unpublished-17-lines-of-javascript-and-broke-the-internet/) .

### Python Package \(PyPI\) Hijacking in 2017

In 2017, attackers created malicious libraries whose names were made to look "very similar" to those of built-in Python libraries. Unsuspecting developers downloaded these malicious libraries. The malicious packages contained the same code as the originals, but their installation scripts had been modified to include malicious code.

> Goodin, Dan. 2017-09-16. “Devs unknowingly use “malicious” modules snuck into official Python repository: Code packages available in PyPI contained modified installation scripts.” Ars Technica. [https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/) 

### Python Package Hijacking in 2018

In 2018, a cryptocurrency-stealing package called "Colourama" was discovered in the Python Software Repository. Its name was deliberately made to resemble "Colorama," a legitimate package that ranked among the 20 most-downloaded software packages in the Python repository, in order to cause confusion. Although the malicious package had been downloaded only 151 times by the time it was discovered, removing the infection from affected devices required considerable effort, which highlighted the security vulnerability of software repositories.

> Two new supply-chain attacks come to light in less than a week, Dan Goodin, ArsTechnica \(October, 23, 2018\), [https://arstechnica.com/information-technology/2018/10/two-new-supply-chain-attacks-come-to-light-in-less-than-a-week/](https://arstechnica.com/information-technology/2018/10/two-new-supply-chain-attacks-come-to-light-in-less-than-a-week/).


### Backdoor in the "event-stream" Library in 2018

In 2018, one of the most widely used JavaScript libraries had cryptocurrency-stealing code inserted into it as a backdoor. Notably, this insertion was far more sophisticated than similar incidents (by the time the backdoor was discovered, the library had recorded 2 million downloads).

First, the malicious actors behind the backdoor gained legitimate publishing rights to the event-stream package by offering to help the developer. Once they had obtained those rights, they used them to add a benign package, flatmap-stream, to the npm registry and added it as a dependency of event-stream itself. About a month later, the malicious actors added malicious code to flatmap-stream that targeted popular cryptocurrency wallet software (and was thereby added to event-stream as well).

This staged attack, together with the effort the attackers invested in gaining publishing rights to the event-stream package, shows not only that there are weaknesses in how new code and new developers are vetted, but also that malicious actors are willing to make that kind of effort. This suggests that similar attacks are likely to continue, and to increase in both frequency and sophistication.

> Widely used open source software contained bitcoin-stealing backdoor, Dan Goodin, ArsTechnica \(November 26, 2018\), [https://arstechnica.com/information-technology/2018/11/hacker-backdoors-widely-used-open-source-software-to-steal-bitcoin/](https://arstechnica.com/information-technology/2018/11/hacker-backdoors-widely-used-open-source-software-to-steal-bitcoin/)

### Account Takeover of a Popular RubyGems Package in July 2019

In July 2019, a developer updating a codebase noticed that one of its dependencies was missing a changelog.md file. The affected package, strong_password, had been updated from 0.0.6 to 0.0.7 with no explanation of the changes, and with a discrepancy between the code hosted on GitHub and the code hosted in the Ruby repository. Through further investigation, the developer discovered that the package had been updated to reach out to a remote URL and pull in additional code when it ran in a production environment. Once that happened, the new code created an opportunity for remote code execution within the infected environment.

The developer notified the package's original maintainer, who discovered that his Ruby repository account had been compromised. The malicious actor had taken over the maintainer's account, changed the package's ownership, and then published the backdoored code. Although it could not be confirmed, the original maintainer believed that the absence of two-factor or multi-factor authentication (2FA or MFA) was what allowed the malicious actor to access his developer account. Because a dependency such as strong_password is deployed in a wide variety of environments and is tied to a well-known developer with an established reputation for trustworthiness, taking over that developer's account is highly valuable. Attacks like this will only increase.

> strong\_password v0.0.7 rubygem hijacked, Tute Costa (July 3, 2019), [https://withatwist.dev/strong-password-rubygem-hijacked.html](https://withatwist.dev/strong-password-rubygem-hijacked.html)

### The Webmin Compromise of 2018-2019

Beginning in April 2018 and discovered in August 2019, an unknown malicious actor used a backdoor in the popular Webmin administration tool. The change was relatively small but could have significant impact. A malicious actor using the backdoor could send commands to an infected server through a specially crafted URL, allowing commands to be executed with root privileges.

According to the Webmin developers, the server containing the Webmin source code was compromised in April 2018 and malicious code was inserted into it. At the time, the attacker altered the relevant server logs to make it appear that the files had not been updated for some time, hiding the change from common detection mechanisms such as code comparison tools. The altered code went undetected, and additional malicious activity continued, until August 17, 2019, when it was discovered externally that the backdoor had been disclosed as part of a zero-day attack.

The Webmin maintainer removed the infection and took additional steps, but the incident became yet another example showing the vulnerability of such software and its continuing appeal to malicious actors.

> The year-long rash of supply chain attacks against open source is getting worse, Dan Goodin, Ars Technica (August 21, 2019) [https://arstechnica.com/information-technology/2019/08/the-year-long-rash-of-supply-chain-attacks-against-open-source-is-gettingworse/](https://arstechnica.com/information-technology/2019/08/the-year-long-rash-of-supply-chain-attacks-against-open-source-is-gettingworse/); Webmin page explaining exploit, Webmin, [http://www.webmin.com/exploit.html](http://www.webmin.com/exploit.html).

### Discovery of 11 Backdoored RubyGems Libraries in August 2019

In August 2019, an analysis by a developer investigating Ruby libraries uncovered 11 backdoored packages. In each case, the backdoor allowed malicious actors holding preselected credentials to remotely execute code on infected servers.

The infected packages also enabled cryptocurrency mining. It is not clear how each library became infected, but for at least one package, the code could be modified because the developer's account had been compromised. That account had been using a previously cracked password and was not protected by 2FA or MFA.

These incidents reveal weaknesses inherent in the current policies, processes, and procedures used by package managers and repositories. Making matters worse, because these elements of the supply chain are indispensable to modern software development, organizations are required to use them in nearly every case, and are therefore exposed to a high level of risk they cannot control.

Finally, there is one more element that stands apart from the software supply chain but is nonetheless indispensable: the "Vulnerability Database."

Given the distributed and overwhelmingly complex nature of modern software development, identifying, analyzing, remediating, and tracking vulnerabilities found in deployed software is critically important. However, the National Vulnerability Database (NVD), provided by the CVE (Common Vulnerabilities and Exposures) program and the most heavily relied-upon vulnerability tracking database in the world, continues to struggle under the growth, speed, and complexity of modern software development. These difficulties directly affect the developers and companies that depend on the CVE and NVD programs, and affect the security and stability of the software supply chain as a whole. This section examines the security and stability issues currently affecting the software supply chain and introduces areas and ways in which things can be changed to improve it overall.

## Examining the Software Supply Chain

### Developer Practices

In the diagram introduced earlier, the developer is shown as the first link in the software supply chain. That is true in a sense, but developers are actually present everywhere, at every stage. Developers choose the programming language, the repository, and the PDM. They choose the libraries, packages, and OSS that make up the finished product a company's customers will purchase. In other words, developers are the single most indispensable member of the software supply chain.

However, many developers do not follow security best practices when developing software. There are several reasons for this. One is that modern software development is an enormously complex process. This means that a "best practice" strategy for one person may turn out to be a critical weakness for another. Another reason is that security is often seen as something that gets in the way of the developer and user experience. As a result, many developers avoid or minimize the use of proper security practices.

Ignoring or being reluctant to adopt security practices in this way leads to a range of consequences, many of which were highlighted in the supply chain incidents described above. Many of these incidents could have been avoided if developers had used the following security practices.

* Using two-factor or multi-factor (2FA or MFA) authentication for developer accounts and other critical accounts involved in the design, construction, and maintenance of a given project
* Requiring that the project support change control tracking (including who made a change and when) throughout the development process
* Ensuring that the project has a unique version identifier for each release, so that downstream users can track new releases and build mechanisms to control and verify them
* Integrating testing into the project's development lifecycle to check not only for common bugs and unexpected behavior, but also for malicious changes made without the developer's knowledge
* Using tools or other mechanisms that ensure the project's dependencies are documented and communicated so downstream users can easily consume them
* Using tools that properly track, analyze, and manage dependencies
* Presenting cryptographic signing or other demonstrable evidence of the project's integrity
* Tracking and remediating vulnerabilities in both newly developed code and OSS dependencies incorporated into the project

Many developers fail to observe these practices. This may be due to a lack of the necessary resources, expertise, or support. What is clear, however, is that failing to follow these best practices carries serious consequences not only for developers but also for the end users of the software.

### Repository

In the past, much software development relied on code licensed from partners or vendors, but today most development incorporates large volumes of OSS retrieved freely and without restriction from the internet. Many developers depend on software repositories, known as "repositories," to build their software.

At its core, a software repository is a server that holds a set of software packages. These packages range from small utility libraries to full command line tools and development frameworks. Linux systems typically use an operating system repository to manage applications and their dependencies for a given Linux distribution. The developers of that distribution manage all packages within the repository's collection, keeping packages current based on upstream software package releases and, when necessary, fixing reported security and other bugs in those packages.

Beginning with Perl and continuing as interpreted programming languages grew, it became advantageous to provide users with an expanded repository of "helper" libraries. Because of the size of these repositories, they were generally excluded from the main packaging of individual Linux distributions. As these language-specific repositories grew, developers working in that language came to rely on the language repository's tooling to install required dependencies, not only during development but also whenever they needed to run the development software on a non-development system.

Today, a significant portion of software development depends on OSS, and because much of the most widely depended-upon OSS in the world is written in languages that rely on a language repository for their libraries, developers must pull portions of their software from these repositories. However, for a variety of historical and economic reasons, these language repositories lack even basic security or quality controls. For example:

* Few language repositories provide a mechanism to check that the code they store is what it purports to be, which increases consumer confusion and, in some cases, enables malicious activity.
* Few language repositories systematically check the stored code or deprecated packages for vulnerabilities.
* No language repository currently provides a mechanism for consumers to check whether one piece of stored code was derived from another, which limits their ability to determine whether a vulnerability or other problem carries over from a dependency.
* In most language repositories, weak or missing authentication and publisher verification mechanisms create uncertainty and risk regarding the origin of stored code.
* Some language repositories do not offer two-factor or multi-factor (2FA or MFA) authentication for developer accounts, and often neither require nor encourage it, signaling to others that developer accounts (and the packages they control) are weakly protected.
* Many language repositories offer code signing, but few provide or enable a robust mechanism for verifying the validity of those signatures.
* Some language repositories include an End User License Agreement (EULA) that restricts conscientious consumers from performing their own security and quality analysis of the stored code.
* Many language repositories do not verify that a generated package was produced from the expected, publicly available source that others could inspect, nor do they make it easy for other users to check this themselves.

Some language repositories have taken steps to address these concerns, but none has developed a mechanism that solves every problem. Moreover, some of the language repositories that have attempted to address these concerns have "commercialized" the repository itself, offering these capabilities only to customers who pay for a "premium" service. As a result, the security and quality controls that should be provided as a baseline remain out of reach for many everyday consumers.

### Project Dependency Manager \("Package Manager"\)

Managing large-scale software efficiently today requires tools that are both simple and powerful. Many such tools exist, but the most widely adopted of them is the "package manager." A package manager automates the process of installing, upgrading, configuring, and removing files such as software packages and libraries on a given system. In particular, package managers known as "project/application dependency managers" (PDM) are frequently used.

By using a PDM, users can collapse the many complex steps once required to find, install, and configure software into a single step. A PDM connects to a language repository, as described above, to search for and configure the software a user specifies, including any software it indirectly depends on. By simplifying software discovery and management in this way, PDMs have greatly reduced the level of expertise and resources required for modern software development.

However, a PDM is nothing more than a software discovery tool. It does not check the software it retrieves for the following, and it has no actionable way to fix them.

* Whether the software has known security or reliability issues
* Whether it contains unexpected or malicious behavior
* Whether it has a misleading package name ("typosquatting" and/or a name resembling that of a built-in library)

> Vaidya et al, “Security Issues in Language-based Software Ecosystems, March 6, 2019, [https://arxiv.org/abs/1903.02613](https://arxiv.org/abs/1903.02613)

Instead, as discussed above, these practices are generally expected to be carried out elsewhere in the software supply chain, but that is generally not the case. As a result, the efforts of PDM users and PDM maintainers to ensure some level of security and quality are undermined within the retrieved software itself. This is a problem in particular because, as can be seen from the increasing frequency of security incidents involving PDMs, the weaknesses inherent in current PDM procedures have become a popular vector for malicious actors.

### Vulnerability Database

As discussed above, modern software is composed of many software packages assembled together. These "building block" packages may be proprietary code, licensed code, or OSS, and a product may be composed of anywhere from dozens to thousands of these blocks. This provides significant benefits, but it also introduces risk. Today, developers and companies must manage not only the bugs and vulnerabilities in their own code, but also those in each of the software packages their product depends on.

Just as modern software development has outpaced in-house development strategies, the number, variety, and uniqueness of vulnerabilities and bugs found in modern software make it impossible to keep up through in-house vulnerability tracking alone. This was a reality the software community recognized early on, and it led to the creation of the CVE (Common Vulnerability and Exposure) program and the NVD (National Vulnerability Database) program, standardized U.S.-based programs for assigning, describing, and tracking vulnerabilities and bugs.

These two programs have existed for more than 20 years and have become the foundation for many modern cybersecurity tools, products, and practices.

> The NVD is considered so important that in 2018 it was exempted from the U.S. government shutdown. See “Closed Down: Government Shutdown Impacts Enterprise Security, December 31, 2018, [**https://duo.com/decipher/government-shutdown-impacts-enterprise-security** ](https://duo.com/decipher/government-shutdown-impacts-enterprise-security)

However, in recent years both programs have struggled as the astonishing growth of new technologies has driven a sharp increase in requests for additions to the NVD. These difficulties have given rise to a number of downstream problems, including the following.

* Vulnerabilities being missed or rejected, resulting in incomplete NVD coverage (Over 6,000 vulnerabilities went unassigned by MITRE’s CVE project in 2015, Steve Ragan, CSO Online (Sep. 22, 2016), [https://www.csoonline.com/article/3122460/over-6000-vulnerabilities-went-unassigned-by-mitres-cve-project-in-2015.html](https://www.csoonline.com/article/3122460/over-6000-vulnerabilities-went-unassigned-by-mitres-cve-project-in-2015.html).)
* Severe delays in assigning vulnerability identifiers, exposing unaware downstream parties to risk
* Insufficient descriptions of vulnerabilities, making remediation and management more difficult
* Vulnerability scores that are inflated or understated, leading to misallocated resources and, in some cases, "vulnerability fatigue"
* Abuse by developers who inflate their vulnerability counts to pad their resumes
* Difficulty rescinding a vulnerability once it is assigned and later found to be invalid, causing confusion and a lack of trust in the program as a whole
* Abuse by engineers at organizations who treat a CVE assignment as a way to bypass a difficult administrative process that would otherwise prevent a routine software upgrade
* Discomfort with the fact that the CVE program itself is administered by a U.S. federal agency
* An inability to handle persistent, complex vulnerabilities that require multiple packages to be fixed multiple times over an extended period

As a result, many stakeholders who rely on the CVE and NVD programs, including nearly every modern company, federal agency, and other organization, are not fully resolving their vulnerability exposure. Worse still, a lack of NVD coverage that produces few alerts can create a false sense of security, leading stakeholders to believe their products are safe and trustworthy when they are not.

### End User Practices

Given their position at the very end of the software supply chain, end users would seem to have the least control over security.

![](https://t1.daumcdn.net/thumb/R1280x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/FO95cqN6sfQpgXkxjSfHnZnJRog.png)

However, the picture changes if you think of the supply chain as a loop.

![](https://t1.daumcdn.net/thumb/R1280x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/uG9Vz6BGSxxkyT2FHCYrJATMwbM.png)

End users will typically use a technology vendor's solution, and in that case, they cannot make decisions about the choice of PDM or OSS packages. However, end users do control "acquisition requirements" (although many users do not make full use of this leverage).

The best practice here is for end users to add the following requirements to the contract when negotiating with a technology provider.

* A dependency list, Software BOM (bill of materials), or a similar component tracking mechanism is provided in a highly robust and transparent manner.
* Vulnerabilities within the product must be remediated within a specified period.
* All developer accounts involved in development must use 2FA or MFA.

In some cases, end users themselves carry out the same practices discussed under developer practices for the OSS packages within their own solutions. In addition to these practices and "acquisition requirement" practices, there are also practical steps end users can take on their own: checking the trustworthiness of software, downloading software only from trusted sources, and verifying that the software they received is the software they requested. They can also limit the permissions granted to software in order to reduce the impact of supply chain problems.

Even so, the following facts remain.

* There is no agreed-upon understanding of what it actually means for software to be "trustworthy," and no effective tools exist, making it difficult to determine whether a given piece of software can be trusted.
* Similarly, it is difficult to determine whether a download location, such as the repositories discussed above, can be trusted.
* Users often find it difficult to verify whether the software they requested is the package they trust, or whether it is malicious, fraudulent, or incorrect.
* Likewise, users are unable to confirm that the software they received is the software they wanted, for example by checking a digital signature. And some users run the code the moment they receive the software, without any check of its security, quality, or otherwise.

End users occupy both the best and worst position to influence the software supply chain. Companies that acquire technology from a vendor can use acquisition practices to encourage the vendor to apply security best practices, but they still face difficulty correcting, or even discovering, defects in the products they receive. For end users who wish to manage their own software themselves, they must recognize that doing so essentially requires them to become developers and to act accordingly. In either case, end users need to understand that as modern software development continues to change, their own behavior must change along with it.

## Conclusion

Modern software development relies on a "supply chain" that is distributed on a massive scale. This ever-increasing trend has reduced the average time to market for products and created substantial value, but it has also created risk and opportunities for abuse.

Software repositories, package managers, and vulnerability databases are all necessary components of the software supply chain, just as the developers and end users who make use of them are. However, unless the vulnerabilities currently inherent in these components are resolved, the companies and developers that depend on them will continue to face significant risk. This article was written to highlight known problems within the software supply chain and to spur action to address them. The Linux Foundation will convene a meeting of global technology leaders to design a comprehensive solution to these problems.
