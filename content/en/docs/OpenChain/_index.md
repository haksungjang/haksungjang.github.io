---
title: "OpenChain을 활용한 기업 오픈소스 컴플라이언스 가이드"
linkTitle: "OpenChain 해설서"
weight: 20
description: >
  OpenChain 규격은 오픈소스 컴플라이언스를 위한 유일한 국제 표준(ISO)이다. 이를 활용하여 기업이 오픈소스 컴플라이언스 수준을 높이기 위한 방법을 설명한다. 
---

{{% pageinfo %}}
정보통신산업진흥원(NIPA)이 주관하고 오픈업에서 연구를 수행하여 기업이 오픈소스 컴플라이언스의 국제 표준인 OpenChain 규격을 준수하기 위해 필요한 사항들을 설명하는 해설서를 가이드 형태로 제작하였습니다. : [기업 공개SW 거버넌스 OpenChain 2.0 해설](https://www.oss.kr/oss_guide/show/7050bff0-d06b-43f0-99a6-9975afcd486f)

여기서는 이 해설서의 개정본 원고를 작성하고 있습니다.
{{% /pageinfo %}}

##  1장. OpenChain이란?

오늘날 소프트웨어는 갈수록 그 규모와 복잡도가 커지고 있다. 하나의 소프트웨어를 개발하기 위해서는 자체 개발한 소프트웨어뿐 아니라 오픈소스, 타사 소프트웨어<sub>3rd party software</sub>, 벤더의 SDK 등 소프트웨어 공급망에 걸친 다양한 소프트웨어가 사용될 수 있다.

이러한 복잡한 소프트웨어 공급망의 여러 조직 중 한 곳이라도 오픈소스 라이선스 의무를 준수하지 않거나 올바른 오픈소스 사용 정보를 제공하지 않으면 최종 소프트웨어를 배포하는 기업은 오픈소스 라이선스 의무 준수에 실패할 수밖에 없다. 이로 인해 소송을 제기당해 제품 판매가 중단되는 상황이 발생할 수도 있다.

{{< imgproc supplychain Fit "900x600" >}}
<center>[OpenChain Open Source Software License Compliance General Public Guide]</center>
{{< /imgproc >}}

2009년 12월, Busybox라는 오픈소스 관련된 소송이 있었다. Busybox는 임베디드 시스템에 광범위하게 사용되고 있는 GPL-2.0 라이선스가 적용된 오픈소스인데, 국내 회사 두 곳을 포함하여 14개 회사가 소송 대상이 되었다. 이 사례에서 주목할만한 점은 이 중에는 제품을 직접 개발하지 않고 배포만 한 회사도 소송을 당하였다는 점이다.

이와 같은 복잡한 소프트웨어 공급망 환경에서는 어느 한 기업이 아무리 훌륭한 프로세스를 갖추고 있다고 해도 자체적으로 완벽한 오픈소스 컴플라이언스를 달성하는 건 매우 어렵다. 결국 한 기업이 오픈소스 컴플라이언스를 제대로 이행하기 위해서는 소프트웨어 공급망의 모든 구성원이 라이선스 의무를 준수하고 올바른 오픈소스 정보를 제공해야 한다. 공급망 전체에 걸쳐 이런 신뢰가 구축되어야 한다.

Linux Foundation의 [OpenChain](https://www.openchainproject.org/) 프로젝트는 기업이 오픈소스 컴플라이언스를 위해 준수해야 할 핵심 사항을 간결하고 일관성 있게 정의하고, 이를 모두가 준수한다면 소프트웨어 공급망 전체에 걸쳐 오픈소스 라이선스 측면의 신뢰를 구축할 수 있다는 믿음으로 설립되었다. 

{{< imgproc openchainlogo Fit "600x450" >}}
<center>[OpenChain Project Logo]</center>
{{< /imgproc >}}

2016년 유럽에서의 한 오픈소스 콘퍼런스에서 퀄컴의 오픈소스 변호사인 데이브 머<sub>Dave Marr</sub>는 바로 이 점을 강조하였다. 한 기업의 오픈소스 컴플라이언스 수준을 높이기 위해서는 소프트웨어 공급망 내 모든 구성원의 오픈소스 컴플라이언스 수준을 높여야 한다. 아울러 이를 위해서는 오픈소스를 충분히 이해하고, 정책 및 프로세스를 이미 구축하고 있는 선진 기업이 자신의 자산과 노하우를 공개하여 누구나 이를 참고할 수 있게 하면 어떻겠냐는 의견을 제시하였다. 콘퍼런스 참석자들은 “오픈소스 컴플라이언스는 기업의 이익을 차별화할 수 있는 분야가 아니다. 기업은 적은 리소스를 투입하면서도 적정한 수준의 리스크 관리를 원한다. 그렇기 때문에 기업이 가진 자산을 서로 공유하면 할수록 적은 리소스로 모두 함께 컴플라이언스를 달성 할 수 있게 된다”는 아이디어에 공감하였다. 그렇게 OpenChain 프로젝트(당시에는 Work Group)는 시작되었고, 퀄컴, 지멘스, 윈드리버, ARM, 어도비 등 다수 글로벌 기업들이 참여하였다.

OpenChain 프로젝트는 기업들이 오픈소스 컴플라이언스를 더욱 쉽게 달성 할 수 있도록 크게 다음 세 가지를 제공한다. 

1. OpenChain 규격[^specification]
2. OpenChain 적합성 인증[^question]
3. 문서 자료[^resource]

[^specification]: OpenChain 규격 - https://www.openchainproject.org/contribute-to-the-standard
[^question]: OpenChain 자체 인증 웹사이트 - https://certification.openchainproject.org/
[^resource]: OpenChain 문서 자료 - https://www.openchainproject.org/resources


기업이 어떻게 이들을 활용할 수 있을지 하나씩 알아보자. 

### 1. OpenChain 규격

OpenChain 규격은 오픈소스 컴플라이언스를 위한 핵심 요구사항을 정의한 10페이지 분량의 문서이다. 2016년 OpenChain 규격 버전 1.0이 발표되었다. OpenChain 규격은 기업의 규모나 업종과 관계없이 모든 기업에 적합하도록 설계되었다. 

2019년 4월에는 버전 2.0의 규격이 배포됐으며, 기업이 오픈소스 컴플라이언스 달성을 위해 꼭 수행해야 할 여섯 가지 핵심 요구사항과 이를 입증하기 위해 필요한 자료 목록을 정의하고 있다.

1. 프로그램 설립
2. 관련 업무 정의 및 지원
3. 오픈소스 콘텐츠 검토 및 승인
4. 컴플라이언스 산출물 생성 및 전달
5. 오픈소스 커뮤니티 참여에 대한 이해
6. 규격 요구사항 준수

오픈소스 컴플라이언스를 처음 시작하는 기업이라면 이러한 OpenChain 규격의 요구사항을 하나씩 충족해가면서 수준을 향상시키는 것이 좋은 전략이다.

{{< imgproc spec Fit "1200x900" >}}
<center>< 출처 : https://github.com/OpenChain-Project/Specification/blob/master/Official/en/2.1/openchainspec-2.1.pdf></center>
{{< /imgproc >}}

2020년 12월 OpenChain 규격은 오픈소스 컴플라이언스에 대한 국제 표준[^ISO]으로 정식 등록되었다. 

[^ISO]: ISO/IEC 5230 : https://www.iso.org/standard/81039.html


{{< imgproc iso Fit "900x600" >}}
<center>< 출처 : https://www.iso.org/standard/81039.html></center>
{{< /imgproc >}}


지난 4년간 사실상의 표준이었던 OpenChain 규격이 ISO/IEC 5230:2020이라는 정식 국체 표준으로 전환되었고, 이는 오픈소스 컴플라이언스 및 프로세스 관리를 정의한 최초의 국제 표준이다. 이로써 글로벌 IT기업의 ISO/IEC 5230 준수에 관한 관심이 높아지고 있고, 소프트웨어 공급망에서 공급자들에게 ISO/IEC 5230 준수를 요구하는 기업이 늘어날 것으로 예상된다. 

OpenChain 규격 내 각 요구사항의 준수 방법은 ["2장. OpenChain 규격 준수 방법"](#2장-openchain-규격-준수-방법)에서 상세히 다룬다. 

### 2. OpenChain 적합성 인증

OpenChain 규격에서의 요구 사항을 모두 준수한다면 OpenChain 적합한 오픈소스 프로그램을 보유했음을 인증받을 수 있다. 오픈소스 프로그램이란 정책, 프로세스, 인원 등 기업이 오픈소스 컴플라이언스 활동을 수행하기 위한 일련의 관리 체계를 의미한다. 이 장에서는 인증 방법과 적합성 선언에 관해 설명한다. 

OpenChain 프로젝트에서 제안하는 인증 방법은 세 가지 이다. 
* 자체 인증
* 독립 평가
* 타사 인증

각각의 방법을 알아보자. 

#### 자체 인증

자체 인증은 OpenChain 프로젝트에서 제일 권장하는 방법이며, 비용이 발생하지 않는다는 장점이 있다. OpenChain은 기업이 OpenChain 규격을 준수하는지 자체적으로 확인할 수 있도록 OpenChain 자체 인증 웹사이트를 제공한다[^question]. 기업의 오픈소스 담당자는 OpenChain 자체 인증 웹사이트에 가입해 온라인 자체 인증을 시작할 수 있다. 자체 인증은 아래와 같이 Yes/No 질문에 답변하는 방식으로 진행된다.


{{< imgproc question Fit "900x600" >}}
<center>< 출처 : https://certification.openchainproject.org/></center>
{{< /imgproc >}}


오픈소스 컴플라이언스 체계를 잘 구축하여 OpenChain 자체 인증 질문지의 모든 항목을 Yes로 대답할 수 있다면 이 결과를 웹사이트상에 제출할 수 있다<sub>Conforming Submission</sub>. 그러면 Linux Foundation의 간단한 문답식의 확인 절차를 거친 후 OpenChain 적합성 선언을 할 수 있게 된다. 

{{< imgproc announce Fit "900x600" >}}
<center><예: LG전자 적합성 선언 - 출처: https://www.openchainproject.org/featured/2021/02/08/lg-openchain-iso-5230></center>
{{< /imgproc >}}

그렇게 OpenChain 적합성 선언을 하게 되면, OpenChain에 적합한 오픈소스 프로그램을 가진 기업으로 인정됨과 동시에, OpenChain 프로젝트의 웹사이트에 기업의 로고를 등록할 수 있게 된다.

{{< imgproc organization Fit "900x600" >}}
<center>< ISO/IEC 5230 적합 프로그램 보유 선언 기업, 출처 - https://www.openchainproject.org/  ></center>
{{< /imgproc >}}

OpenChain 적합 프로그램을 보유한 기업에는 OpenChain 로고를 사용할 수 있는 자격이 주어진다. 

{{< imgproc certilogo Fit "900x600" >}}
<center>< OpenChain Logo, 출처 - https://www.openchainproject.org/ ></center>
{{< /imgproc >}}

이렇게 OpenChain 적합 프로그램을 갖췄다고 인정받은 기업은 소프트웨어 공급망 내에서 오픈소스 컴플라이언스를 충실하게 수행하고 있음을 나타낼 수 있다. OpenChain 프로젝트는 자체 인증 방식을 권장한다. 참고로, OpenChain 적합성을 선언한 대부분의 기업도 자체 인증 방식을 채택하였다. 

기업은 자체 인증을 통해 부족한 부분이 무엇인지, 추가로 필요한 활동이 무엇인지 판단할 수 있다. 미흡한 부분을 보완하기 위해서는 2장에서 설명하는 OpenChain 규격 준수 방법을 참고할 수 있다. 자체적으로 보완할 수 있는 역량이 부족한 기업인 경우 독립 평가 방법을 고려할 수 있다. 

#### 독립 평가

독립 평가는 기업 외부의 독립 기관이 공정한 관점에서 기업의 오픈소스 컴플라이언스 상태를 점검하고 평가한다. 어떤 인증서를 발급해주지는 않는다는 점이 자체 인증, 타사 인증과는 다른 점이다. 독립 평가의 특징은 평가 보고서를 생성하는 것에 그치지 않고 도출된 미비점을 보완하기 위한 컨설팅을 제공한다. 

기업은 독립 기관으로부터의 공정한 평가와 컨설팅을 받아 컴플라이언스 수준을 높이고, 다시 독립 평가를 수행하는 반복적인 과정을 통해 정책을 세분화하고 프로세스를 구축할 수 있다. 


{{< imgproc independent2 Fit "900x1200" >}}
<center>< Independent Compliance Assessment, 출처 - https://youtu.be/DEBd-g0Ab8E ></center>
{{< /imgproc >}}

결국 기업은 OpenChain 인증을 받을 수 있는 수준에 도달하게 된다. 그때 자체 인증, 혹은 타사 인증을 획득하는 절차에 돌입할 수 있다. OpenChain의 독립 평가는 이렇게 기업의 오픈소스 컴플라이언스 수준을 높이기 위한 평가와 컨설팅을 제공하여서 기업이 OpenChain 적합 프로그램을 보유하고 인증을 획득할 수 있게 지원한다. 

독립 평가를 제공하는 업체는 [AlektoMetis](https://alektometis.com/)[^AlektoMetis], [Source Code Control](https://sourcecodecontrol.co/)[^SourceCodeControl] 등이 있다. 

[^AlektoMetis]: AlektoMetis - https://alektometis.com/, 
[^SourceCodeControl]: Source Code Control - https://sourcecodecontrol.co/

국내에서는 이와 유사한 프로그램을 NIPA의 [오픈업](https://www.oss.kr/open_up_intro)[^openup]에서 국내 기업 대상으로 [공개소프트웨어 활용지원 프로그램](https://www.oss.kr/news/show/49e410fb-604d-4d35-ba25-8286b5f2c50d)[^program]을 통해 무료로 제공한다. 

[^openup]: 오픈업 - https://www.oss.kr/open_up_intro
[^program]: 공개소프트웨어 활용 지원 프로그램 - https://www.oss.kr/news/show/49e410fb-604d-4d35-ba25-8286b5f2c50d

{{< imgproc openup2 Fit "900x600" >}}
<center>< OpenUp 주요 업무, 출처 - https://www.oss.kr/open_up_task ></center>
{{< /imgproc >}}


#### 타사 인증

소프트웨어 공급망에서 구매자에게 보다 신뢰성 있고 투명한 오픈소스 컴플라이언스 수준을 나타내고자 한다면 타사 인증 기관으로부터 인증서를 발급받고 이를 홍보에 활용할 수 있다. 또한, 오픈소스 컴플라이언스의 보다 견고한 신뢰성을 요구하는 일부 구매자는 공급자<sub>Supplier</sub>에게 타사 인증을 의무화 할 수도 있을 것으로 예상된다. 

2021년 4월 기준, OpenChain의 공인 타사 인증 기관은 [ORCRO](https://orcro.co.uk/)[^ORCRO], [PWC](https://www.pwc.de/en/opensource)[^PWC], [TÜV SÜD](https://www.tuvsud.com/)[^TUVSUD]이다.

[^ORCRO]: ORCRO- https://orcro.co.uk/
[^PWC]: PWC - https://www.pwc.de/en/opensource
[^TUVSUD]: TÜV SÜD - https://www.tuvsud.com

{{< imgproc 3rdparty Fit "900x600" >}}
<center>< Third-Party Certifiers, 출처 - https://www.openchainproject.org/partners ></center>
{{< /imgproc >}}

이들은 ISO/IEC 5230 적합 프로그램 확인을 위한 평가를 제공하고 통과한 기업에 인증서를 발급한다. 

{{< imgproc pwc Fit "900x600" >}}
<center>< PWC certification, 출처 - https://youtu.be/HslvXCM-4pQ ></center>
{{< /imgproc >}}


2021년 4월 현재, 아직은 타사 인증을 의무적으로 요구하는 구매자나 기관은 없어 보인다. 하지만 유럽의 자동차 업계에서는 ISO/IEC 5230이 [ASPICE](http://www.automotivespice.com/)<sub>Automotive SPICE</sub>[^aspice] 자동차 소프트웨어 개발을 위한 국제 표준 프로세스 모델)와 같이 자동차 소프트웨어 공급자에게 의무화될 날이 머지않을 것이라고 예견하는 전문가도 있다. 

[^aspice]: ASPICE : 자동차 소프트웨어 개발을 위한 국제 표준 프로세스 모델 - http://www.automotivespice.com

### 3. 문서 자료

OpenChain 프로젝트에서는 기업이 컴플라이언스 프로그램을 구축하는 데 필요한 정책 문서 템플릿, 교육 자료 등 다양한 문서 자료를 제공한다. 이 자료는 OpenChain 규격을 준수하고 일반적인 오픈소스 컴플라이언스 활동을 지원하기 위해 고안됐으며, 누구나 자유롭게 사용할 수 있도록 CC-0 라이선스로 제공된다.

{{< imgproc resource Fit "900x600" >}}
<center>< OpenChain Curriculum, 출처 - https://www.openchainproject.org/resources ></center>
{{< /imgproc >}}

이 가이드의 많은 내용도 OpenChain에서 공개한 자료를 기반으로 작성하였다. 각 기업의 오픈소스 담당자는 정책, 프로세스, 교육자료가 필요하다면 OpenChain Resources를 먼저 찾아보기 바란다. 또한 이 자료는 한국어로도 번역되어 공개되고 있다. [OpenChain Korea Work Group](https://openchain-project.github.io/OpenChain-KWG/)[^KWG]에서 이러한 번역 작업을 주도하고 있다. 한국어 번역은 관심 있는 누구나 [참여](https://openchain-project.github.io/OpenChain-KWG/resource/)할 수 있다[^translate].

[^KWG]: OpenChain Korea Work Group - https://openchain-project.github.io/OpenChain-KWG/

[^translate]: 한국어 번역 작업 - https://openchain-project.github.io/OpenChain-KWG/resource/

2장에서는 OpenChain 규격의 각 요구사항을 어떻게 준수해야 할지에 대해 세부적으로 설명한다. 

## 2장. OpenChain 규격 준수 방법

OpenChain 규격은 오픈소스 컴플라이언스를 위한 핵심 요구 사항을 정의한다. OpenChain 규격을 모두 준수하여 OpenChain 적합 프로그램을 갖췄다고 선언한 기업은 소프트웨어 솔루션을 배포하는 공급망 내에서 신뢰를 나타낼 수 있게 된다.

이 장에서는 기업이 OpenChain 규격 버전 2.1을 준수하기 위해 충족해야 하는 여섯 가지 주요 요구사항과 각각의 준수 방법을 세부적으로 설명한다. 참고로 OpenChain 규격의 2.1 버전은 [ISO/IEC 5230](https://www.iso.org/standard/81039.html)[^iso]에 등록된 버전이다. 

[^iso]: ISO/IEC 5230 - https://www.iso.org/standard/81039.html

### 1. 프로그램 설립<sub>Program foundation</sub>

오픈소스를 이용하여 소프트웨어를 개발하고 배포하는 기업이라면 오픈소스를 관리하기 위한 정책과 프로세스를 만들고, 이를 위한 인력과 자원을 적절하게 할당해야 한다. 앞 장에서도 한번 언급했지만, 오픈소스 프로그램이란 정책, 프로세스, 인원 등 기업이 오픈소스 컴플라이언스 활동을 수행하기 위한 일련의 관리 체계를 의미하며, OpenChain 규격의 첫 번째 요구사항은 바로 이 오픈소스 프로그램을 설립하라는 것이다. 

#### 1-1. 정책

그 첫 번째 요구사항으로 문서화된 오픈소스 정책이 있어야 한다. OpenChain 규격 버전 2.1의 3.1.1항에서는 다음과 같이 정책에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.1.1 Policy

3.1.1 정책

배포용 소프트웨어의 오픈소스 라이선스 컴플라이언스를 관리하는 문서화된 오픈소스 정책이 있어야 한다. 이 정책은 조직 내부에 전파되어야 한다.

입증 자료

* 3.1.1.1 문서화된 오픈소스 정책
* 3.1.1.2 프로그램 참여자가 오픈소스 정책의 존재를 알 수 있게 하는 문서화된 절차 (교육, 내부 위키, 혹은 기타 실질적인 전달 방법 등)

---

A written open source policy shall exist that governs open source license compliance of the supplied software. The policy shall be internally communicated.

Verification Material(s):  

* 3.1.1.1 A documented open source policy.
* 3.1.1.2 A documented procedure that makes program participants aware of the existence of the open source policy (e.g., via training, internal wiki, or other practical communication method).

{{% /alert %}}

기업이 이 요구사항을 어떻게 준수해야 할지, [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문별로 방법과 절차를 알아보자. 

| 1.a  | 배포용 소프트웨어의 배포를 위한 오픈소스 라이선스 컴플라이언스를 관리하는 문서화된 정책이 있습니까? |
|---|:---|
|  | Do you have a documented policy that governs open source license compliance of the Supplied Software distribution? |


기업은 이 질문에 YES로 답하려면 어떤 준비를 해야 할까? 먼저 오픈소스 정책을 수립하고 문서화해야 한다. 오픈소스 정책은 다음을 포함한다. 
* 기업이 오픈소스를 사용하여 소프트웨어 제품과 서비스를 만들어서 배포하기 위한 정책
* 외부 오픈소스 커뮤니티에 기여하기 위한 정책
* 기업의 소프트웨어를 오픈소스로 공개하기 위한 정책

이 안내서에서는 참고를 위해 OpenChain 규격의 요구사항을 충족하는 샘플 오픈소스 정책 문서를 “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)”에서 제공한다. 기업은 이 샘플 정책을 기반으로 기업의 비즈니스 전략과 환경에 맞게 수정하여 사용할 수 있다. 

| 1.b  | 오픈소스 정책의 존재를 모든 프로그램 참여자에게 알리는 문서화된 절차가 있습니까? (예: 교육, 내부 위키 혹은 기타 실질적인 전달 방법) |
|---|:---|
|  | Do you have a documented procedure that communicates the existence of the open source policy to all Software Staff? (e.g., via training, internal wiki, or other practical communication method) |


기업은 모든 프로그램 참여자가 조직 내에 오픈소스 정책이 있다는 것을 인식하고 필요한 활동을 할 수 있도록 교육, 내부 위키 등 실질적인 수단을 제공해야 한다. 여기서 프로그램 참여자란 기업이 소프트웨어를 개발하고 배포, 기여하는 데 관여하는 모든 직원을 의미하며, 소프트웨어 개발자, 배포 엔지니어, 품질 엔지니어 등을 포함한다.

많은 기업은 오픈소스 정책 문서를 사내 위키 사이트를 통해 공개하여 직원 누구나 필요한 사항을 확인할 수 있게 한다. 또한, 신규 채용 인원의 입사 연수 시 오픈소스 정책에 대한 교육을 의무화하고, 프로그램 참여자를 대상으로 매년 혹은 2년에 한 번씩 주기적인 교육을 제공함으로 모든 프로그램 참여자가 오픈소스 정책의 존재를 인식하게 한다. 즉, 기업은 이러한 방법들을 다음의 예와 같이 작성하여 오픈소스 정책 문서 포함해야 한다. 

~~~
1. 교육 및 평가

모든 소프트웨어 배포 참여자는 매년 [Learning Portal]에서 제공하는 오픈소스 의무
교육을 수강해야 한다. 
이를 통해 오픈소스 정책, 관련 교육 정책 및 조회 방법을 숙지한다. 교육 이력은 
[Learning Portal]에 보존한다. 
~~~


#### 1-2. 역량

이 장은 프로그램 참여자가 갖추어야 할 역량에 대한 요구사항을 정의한다. OpenChain 규격 2.1의 3.1.2항에서는 다음과 같이 역량에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}


3.1.2 역량

조직은 다음 사항을 수행해야 한다: 
* 프로그램의 성과와 효율에 영향을 미치는 역할이 무엇인지, 그 역할에 해당하는 책임은 무엇인지 확인한다. 
* 각 역할을 수행할 프로그램 참여자가 갖춰야 할 필요 역량을 결정한다. 
* 프로그램 참여자가 적절한 교육, 훈련 및/또는 경험을 바탕으로 자격을 갖춘 자임을 확인한다.
* 해당되는 경우, 필요한 역량을 확보하기 위해 조치한다.
* 역량 보유를 증명하기 위한 정보를 문서화하여 유지한다. 

입증 자료:

* 3.1.2.1 프로그램의 여러 참여자에 대한 역할과 각 역할의 책임을 나열한 문서 
* 3.1.2.2 각 역할을 위해 필요한 역량을 기술한 문서
* 3.1.2.3 각 프로그램 참여자의 역량을 평가한 문서화된 증거

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

기업이 이 요구사항을 어떻게 준수해야 할지, [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문별로 방법과 절차를 알아보자. 

| 1.c  | 프로그램의 성능과 효과에 영향을 미치는 역할과 그에 상응하는 책임을 확인했습니까? |
|---|:---|
|  | Have you identified the roles and the corresponding responsibilities that affect the performance and effectiveness of the Program? |


오픈소스 프로그램이 효율적이고 성과를 내기 위해서 필요한 역할이 무엇인지와 그 역할이 담당해야 할 책임을 정의해야 한다. 오픈소스 프로그램에 필요한 일반적인 역할은 다음과 같다. 
* 오픈소스 프로그램 매니저
* 법무 담당
* 인프라 담당
* 보안 담당
* 개발 문화 담당
* 품질 담당
* 소프트웨어 개발부서
* OSPO[^OSPO]
* OSRB[^OSRB]

[^OSPO]: OSPO - Open Source Program Office
[^OSRB]: OSRB - Open Source Review Board

위의 모든 역할을 처음부터 구성해야 하는 것은 아니다. 처음 시작하는 기업이라면 오픈소스 프로그램 매니저 역할을 하는 인원 한 명으로 시작할 수도 있다. 

각 역할에 대한 일반적인 책임을 명시한 문서를  “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [4. 역할, 책임 및 역량](#4-역할-책임-및-역량sub3121sub)”에서 제공한다.

| 1.d  | 각 역할에 필요한 역량을 확인하고 문서화했습니까? |
|---|:---|
|  | Have you identified and documented the competencies required for each role? |



각 역할과 그에 대한 책임을 정의하였으면, 그 역할을 수행할 인원이 갖춰야 할 필요 역량이 무엇인지 정의해야 한다. 이 부분도 마찬가지로 “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [4. 역할, 책임 및 역량](#4-역할-책임-및-역량sub3121sub)”에 포함하였으니 참고하기 바란다. 

| 1.e  | 각 프로그램 참여자의 역량을 평가한 증거를 문서화했습니까? |
|---|:---|
|  | Have you documented evidence of assessed competence for each Program participant? |

기업은 각 역할에 대한 담당자를 지정하고, 지정된 담당자가 교육, 훈련 및 경험을 바탕으로 맡은 역할을 수행할 수 있는 자격을 갖추었음을 확인해야 한다. 필요할 경우, 프로그램 참여자가 충분한 역량을 갖출 수 있도록 교육도 제공해야 한다. 그리고 기업은 각 참여자가 역량을 갖추고 있는지 평가하고 결과를 보관해야 한다. 
1. 기업은 각 참여자가 필요한 역량을 보유할 수 있도록 교육을 제공한다. 
2. 교육 내용을 기반으로 평가를 수행한다. 
3. 평가 결과는 기업의 교육 시스템 혹은 HR 부서에서 보관한다. 

프로그램 참여자가 수백 명 이상이어서 교육 제공이 쉽지 않을 경우, 기업의 온라인 교육과 평가 시스템을 이용하는 것도 좋은 방법이다. 

이와 같은 내용은 기업의 오픈소스 정책에 다음과 같이 포함할 수 있다. 

~~~

4. 역할, 책임 및 역량
이 정책의 효과를 보장하기 위해 다음과 같이 역할과 책임 및 각 역할의 담당자가 갖추어야 
할 역량을 정의한다. 
각 역할의 담당 조직/담당자와 필요 역량 수준은 "Appendix 1. 담당자 현황"에서 정의한다. 

5. 교육 및 평가
4장에서 정의한 각 역할을 담당하는 모든 구성원은 [Learning Portal]에서 제공하는 
오픈소스 교육을 수강해야 한다. 
교육 이력과 평가 결과는 [Learning Portal]에서 최소 3년간 보존한다. 
~~~

#### 1-3. 인식 

다음으로 OpenChain 규격은 다음과 같이 프로그램 참여자가 기업의 오픈소스 정책과 영향 등에 대해 인식할 수 있어야 함을 요구한다.


{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.1.3 인식

조직은 프로그램 참여자가 다음 사항을 인식하도록 보장해야 한다:

* 오픈소스 정책
* 오픈소스 관련 목표
* 효과적인 프로그램이 되기 위한 참여자의 기여 방법
* 프로그램 요구사항을 준수하지 않을 경우 미치는 영향

입증 자료: 

3.1.3.1 다음 사항에 대한 프로그램 참여자의 인식을 평가하였음을 나타내는 문서화된 증거 : 프로그램의 목표, 프로그램 내에서의 참여자 기여 방법 및 프로그램을 준수하지 않을 경우 미치는 영향

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

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문은 다음과 같다. 

| 1.f<br>  | 다음 주제에 대한 프로그램 참여자의 인식을 문서화 한 증거가 있습니까?<br> i. 오픈소스 정책 및 이를 찾을 수 있는 위치 <br>ii. 오픈소스 관련 목표  <br>iii. 효과적인 프로그램이 되기 위한 참여자의 기여 방법  <br>iv. 프로그램 요구사항을 준수하지 않을 경우 미치는 영향  |
|---|:---|
|  | Do you have evidence documenting the awareness of your personnel of the following topics?  <br>i - The open source policy and where to find it;  <br>ii - The relevant open source objectives;  <br>iii - The contributions expected to ensure the effectiveness of the Program;  <br>iv - The implications of failing to follow the Program requirements. |

기업은 프로그램 참여자가 기업의 오픈소스 정책, 오픈소스 관련 목표, 효과적인 오픈소스 프로그램이 되기 위한 참여자의 기여 방법, 그리고 프로그램 요구사항을 준수하지 않을 경우 미치는 영향에 대해 인식하게 해야 한다. 이를 위해 기업은 교육을 제공하고, 프로그램 참여자에게 올바르게 인식하였는지 확인하기 위해 평가를 수행한다. 평가 결과는 문서화하여 보관한다.

이를 위한 아래의 예와 같은 내용을 기업의 오픈소스 정책에 포함할 수 있다.

~~~
1. 목적
  (1) 정책의 목적
    이 정책은 회사에서 소프트웨어 개발, 서비스, 배포에 관여하는 전체 조직이 올바르게 
    오픈소스를 활용하기 위해 다음과 같은 원칙을 제공한다. 

    1) 오픈소스 라이선스를 고려한 컴플라이언스 수행 원칙
    2) 외부 오픈소스 프로젝트로의 기여 원칙
    3) 사내 프로젝트를 오픈소스로 공개하기 위한 원칙
   
   이러한 원칙은 회사의 모든 구성원이 오픈소스의 가치를 이해하고, 오픈소스를 올바르게 
   사용하며, 오픈소스 커뮤니티에 기여하기 위한 방법을 제공한다.

  (2) 미준수 시 영향
   이 정책을 준수하지 않는다면 다음과 같은 상황이 발생할 수 있다.  
   * 외부로부터 오픈소스 라이선스 준수 요구를 받게 된다.
   * 회사가 개발한 소스 코드를 원하지 않게 공개해야 한다.
   * 오픈소스 저작권자로부터 법적 소송을 제기당하게 된다.
   * 저작권 침해 및 계약 위반으로 벌금을 부과 당하거나, 제품 판매 중지 명령을 받게 된다.
   * 회사 평판이 손실된다. 
   * 공급업체와의 계약 위반이 되어 손해배상 청구를 당하게 된다.
  이러한 이유로 회사는 오픈소스 정책의 위반을 심각하게 간주하며, 이를 위반하는
  구성원이나 조직은 징계 절차에 처할 수 있다.

  (3) 구성원의 공헌 방법
    모든 구성원은 이 정책의 근거와 내용을 이해하고 필요한 활동을 충실히 수행함으로써 
    정책의 효과 및 회사의 컴플라이언스 수준 향상에 공헌할 수 있다.

~~~

또, 프로그램 참여자가 오픈소스 정책을 인식하게 하기 위한 교육과 평가 방침도 수립해야 한다. 이에 대한 예시를 “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [5. 교육 및 평가](#5-교육-및-평가)”에서 제공한다.

#### 1-4. 프로그램 적용 범위

오픈소스 프로그램을 기업 내 어느 조직 혹은 어느 제품에 적용할지를 결정해야 하며 이를 위한 절차가 필요하다. OpenChain 규격 2.1의 3.1.4항에서는 다음과 같이 프로그램의 적용 범위에 대한 요구사항과 입증 자료를 정의한다. 


{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.1.4 프로그램 적용 범위

프로그램은 다양한 범위별로 적용하여 관리할 수 있다. 예를 들어, 한 프로그램을 단일 제품군에만 적용할 수도 있고, 전체 부서 또는 전체 조직에 적용하여 관리할 수 있다. 따라서 각 프로그램에서는 적용 범위를 정확히 명시해야 한다.

입증 자료:

* 3.1.4.1 프로그램의 적용 범위와 한계를 명확하게 정의한 문서화된 진술

---

3.1.4 Program scope  

Different programs may be governed by different levels of scope. For example, a program could govern a single product line, an entire department or an entire organization. The scope designation needs to be declared for each program.

Verification material(s):
* 3.1.4.1 A written statement that clearly defines the scope and limits of the program.

{{% /alert %}}

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문은 다음과 같다. 


| No | 자체 인증 질문 |
|---|:---|
| 1.h | 프로그램의 적용 범위와 한계를 명확하게 정의한 문서화된 진술이 있습니까? |
| 1.h | Do you have a written statement clearly defining the scope and limits of the Program? |

하나의 오픈소스 프로그램을 반드시 기업 전체에 적용해야 하는 것은 아니다. 기업 내 각 조직과 제품의 특성에 따라 적용 범위를 달리 지정할 수 있다. 조직별로, 제품별로 다른 오픈소스 프로그램을 적용할 수 있다. 마찬가지로, 소프트웨어를 전혀 배포하지 않는 조직이라면 오픈소스 프로그램의 적용 범위에서 제외할 수 있다. 기업은 조직과 제품의 특성을 고려하여 오픈소스 프로그램의 적용 범위와 한계를 명확히 정의하고, 이를 오픈소스 정책에 명시할 수 있다.

| No | 자체 인증 질문 |
|---|:---|
| 1.g | 프로그램의 적용 범위를 결정하는 프로세스가 있습니까? |
| 1.g | Do you have a process for determining the scope of your Program? |

또한, 기업의 조직과 제품 및 서비스가 비즈니스 환경에 맞추어 변화함에 따라 프로그램의 적용 범위를 결정하거나 수정해야 하는 상황이 발생할 수 있다. 가업은 이에 대응하기 위한 프로세스를 다음의 예와 같이 준비해야 한다.

1. 오픈소스 프로그램 매니저는 새로운 프로젝트를 시작할 때 해당 프로젝트가 프로그램 적용 범위 내에 포함되는지 여부를 판단한다. 
2. 포함된다고 판단되는 경우, 해당 프로젝트를 프로그램 적용 범위에 포함 시키기 위한 제안을 OSRB[^OSRB]에 제출한다.
3. OSRB에서 수락할 경우, 이에 맞게 프로그램의 적용 범위를 수정한다. 
4. 이외 오픈소스 프로그램 매니저는 프로그램 적용 범위에 대한 검토가 필요하다고 판단되는 경우, 동일한 프로세스에 따라 프로그램 적용 범위에 대한 검토를 시작할 수 있다.

이를 위하여 다음의 예와 같은 내용을 오픈소스 정책에 포함한다. 

~~~
2. 적용 범위
이 정책은 다음 세 부분에 적용한다.

1) 회사가 외부로 제공하거나 배포하는 모든 제품에 적용한다. 
   단, 오픈소스를 내부 사용 목적으로만 사용하는 것은 이 정책의 범위에 포함되지 않는다.
2) 구성원이 외부 오픈소스 프로젝트로의 기여 시에 적용한다.
3) 내부 코드를 오픈소스로 공개할 때 적용한다.

적용 범위는 회사의 비즈니스 환경에 맞추어 변경할 수 있으며, 이를 위한 절차는 다음과 같다. 

1) 오픈소스 프로그램 매니저는 신규사업, 조직개편 등 회사의 비즈니스 환경이 변화에 따라 
   정책의 적용 범위 변경이 필요하다고 판단할 경우, 이를 위한 제안을 OSRB에 제출한다. 
2) OSRB에서는 적절한 수준의 적용 범위 변경을 승인한다. 
3) OSRB는 오픈소스 정책을 수정하여 정책의 적용 범위를 변경한다. 

~~~

이 가이드에서는 프로그램 범위 지정에 대한 예시를 “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [2. 적용 범위](#2-적용-범위sub3141sub)”에서 제공한다.


#### 1-5. 라이선스 의무

오픈소스를 사용하면 각 라이선스가 부과하는 의무를 준수해야 한다. OpenChain 규격 2.1의 3.1.5항에서는 다음과 같이 각 오픈소스 라이선스가 부과하는 의무를 알아내기 위한 검토 프로세스를 요구한다. 


{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.1.5 라이선스 의무

각 라이선스에 의해 부과된 의무, 제한 및 권리를 알아내기 위해 식별된 라이선스를 검토하는 프로세스가 있어야 한다.

입증 자료

* 3.1.5.1 각 식별된 라이선스에 의해 부여된 의무, 제한 및 권리를 검토하고 기록하기 위한 문서화된 절차

---

3.1.5 License obligations

A process shall exist for reviewing the identified licenses to determine the obligations, restrictions and rights granted by each license.

Verification material(s):

* 3.1.5.1 A documented procedure to review and document the obligations, restrictions and rights granted by each identified license.

{{% /alert %}}

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문은 다음과 같다. 

| 1.i | 오픈소스 라이선스 의무, 제한 및 권리를 검토하는 프로세스가 있습니까? |
|---|:---|
|  | Do you have a process for reviewing open source license obligations, restrictions and rights? |

오픈소스의 사용 가능 여부를 판단하기 위해서는 먼저 사용하려는 오픈소스의 라이선스가 무엇인지 식별하고, 라이선스가 요구하는 의무사항을 확인해야 한다. 오픈소스를 사용하였는지, 라이선스는 무엇인지, 각 라이선스가 부여하는 의무는 무엇인지 검토하고 기록해야 한다. 이를 위한 절차의 예는 다음과 같다. 

1. 오픈소스 프로그램 매니저는 오픈소스 정책에서 정의한 기준에 따라 라이선스를 예비 평가한다. 
2. 의문이 있는 경우, 오픈소스 프로그램 매니저는 외부 법률 전문가에게 자문을 요청한다. 
3. 모든 내외부의 결정 결과 및 관련 근거는 보관한다. 

기업의 오픈소스 프로그램 매니저는 주요 오픈소스 라이선스가 부여하는 의무, 제한 및 권리를 쉽게 이해할 수 있도록 오픈소스 라이선스 의무 요약 자료를 작성하고 오픈소스 정책에 포함해서 누구나 열람할 수 있게 하라. 한국저작권위원회에서 제공하는 [라이선스 가이드](https://www.olis.or.kr/license/licenseGuide.do)[^copyrightguide]을 참고할 수 있다. SK텔레콤의 오픈소스 가이드 내 [라이선스별 의무사항](https://sktelecom.github.io/guide/use/obligation/)[^sktobligation] 문서도 좋은 사례이다.

[^copyrightguide]: 한국저작권위원회 라이선스 가이드 - https://www.olis.or.kr/license/licenseGuide.do
[^sktobligation]: SK텔레콤의 오픈소스 가이드 내 라이선스별 의무사항 - https://sktelecom.github.io/guide/use/obligation/

여기서 요구하는 "각 식별된 라이선스에 의해 부가된 의무, 제한 및 권리를 검토하고 기록하기 위한 문서화된 절차“는 "[부록 2. 샘플 오픈소스 컴플라이언스 프로세스](#부록-2-샘플-오픈소스-컴플라이언스-프로세스)”의 [1. 오픈소스 식별 단계](#1-오픈소스-식별subidentification-of-open-sourcesub)에 해당한다.

### 2. 관련 업무 정의 및 지원<sub>Relevant tasks defined and supported</sub>

오픈소스 프로그램이 효과적으로 운용되기 위해서는 충분한 리소스와 인력 할당이 필요하다. 여기에서는 이를 위한 요구사항을 정의한다. 

#### 2-1. 접근성

먼저 OpenChain 규격 2.1의 3.2.1항에서는 외부의 문의에 얼마나 효과적으로 대응하는 프로세스를 유지하였는지에 대한 요구사항과 입증 자료를 정의한다. 

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.2.1 외부 문의 대응 (Access)

외부의 오픈소스 문의에 효과적으로 대응하기 위한 프로세스를 유지해야 한다. 제 3자가 오픈소스 컴플라이언스에 대해 문의 할 수 있는 방법을 공개해야 한다.

입증 자료:

* 3.2.1.1 제 3자가 오픈소스 라이선스 컴플라이언스에 대해 문의 할 수 있는 공개된 방법 (담당자 이메일 주소, 또는 Linux Foundation의 Open Compliance Directory 활용 등)
* 3.2.1.2 제 3자의 오픈소스 라이선스 컴플라이언스 문의에 대응하기 위한 내부의 문서화된 절차

---

3.2.1 Access

Maintain a process to effectively respond to external open source inquiries. Publicly identify a means by which a third party can make an open source compliance inquiry.

Verification material(s):

* 3.2.1.1 Publicly visible method that allows any third party to make an open source license compliance inquiry (e.g., via a published contact email address, or the Linux Foundation's Open Compliance Directory).
* 3.2.1.2 An internal documented procedure for responding to third party open source license compliance inquiries.


{{% /alert %}}


이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 2.a  | 외부 오픈소스 컴플라이언스 문의를 받을 담당자(오픈소스 연락담당자)를 지정했습니까? |
|---|:---|
|  | Have you assigned individual(s) responsible for receiving external open source compliance inquiries ("Open Source Liaison")? |

오픈소스를 사용하여 개발한 제품 혹은 서비스에 대해 고객 및 오픈소스 저작권자가 기업에 오픈소스 관련 문의, 요청 및 클레임을 제기하는 경우가 있다. 외부 문의 및 요청의 주된 내용은 다음과 같다.

* 특정 제품 및 서비스에 오픈소스가 사용되었는지 문의
* 서면 약정(Written Offer)에 언급된 GPL, LGPL 라이선스 하의 소스 코드 제공 요청
* 오픈소스 고지문에 명시되지 않았지만, 제품에서 발견된 오픈소스에 대한 해명 및 소스 코드 공개 요청
* GPL, LGPL 등의 의무로 공개된 소스 코드에 누락된 파일 및 빌드 방법 제공 요청
* 저작권 표시 요청

기업은 이러한 외부 문의를 처리할 담당자를 지정해야 한다. 일반적으로 오픈소스 프로그램 매니저가 담당한다. 

| 2.b  | 오픈소스 연락 담당자 정보가 외부에 공개되어 있습니까(예: 이메일 주소 또는 Linux Foundation의 Open Compliance Directory 활용)? |
|---|:---|
|  | Is the Open Source Liaison function publicly identified (e.g. via an email address and/or the Linux Foundation's Open Compliance Directory)? |

외부의 오픈소스 개발자가 특정 기업의 오픈소스 컴플라이언스 관련 이슈를 논의하기 위해 기업 담당자에게 연락하고 싶어도 연락 방법을 찾지 못하다가 결국 바로 법적 클레임을 제기하는 경우가 있다. 이를 방지하기 위해 기업은 제 3자가 기업에 오픈소스 관련하여 문의 및 요청을 할 수 있는 연락 방법을 항시 공개적으로 밝혀야 한다. 

외부에서 기업에 오픈소스 관련된 문의를 할 수 있는 연락 방법은 (1) 기업 오픈소스 프로그램 매니저의 이메일 주소를 공개하거나, (2) Linux Foundation의 [Open Compliance Directory](https://compliance.linuxfoundation.org/references/open-compliance-directory/)[^directory]를 이용하는 것이다. 기업 오픈소스 프로그램 사무소의 대표 이메일 주소는 제품 및 서비스와 동봉하는 오픈소스 고지문에 포함하여 공개하는 것도 한 방법이다. 

[^directory]: Open Compliance Directory - https://compliance.linuxfoundation.org/references/open-compliance-directory/

Linux Foundation은 기업이 오픈소스 담당자의 연락처를 공개할 수 있도록 Open Compliance Directory라는 공간을 마련하였다.

{{< imgproc directory Fit "900x600" >}}
<center>< 이미지 출처- https://compliance.linuxfoundation.org/references/open-compliance-directory/></center>
{{< /imgproc >}}

기업의 오픈소스 담당자는 "Add an Organization"을 이용하여 기업의 연락처를 등록한다. 외부 개발자는 "Request a Contact"에서 오픈소스 컴플라이언스 관련 문의 및 요청을 할 수 있다. 이를 통해 오픈소스 개발자들은 원하는 기업의 컨택 포인트 정보를 쉽게 확인할 수 있고, 법적 클레임까지 제기하기 이전에 기업의 오픈소스 담당자와 오픈소스 컴플라이언스 이슈를 논의하여 문제를 해결할 수 있다. Open Compliance Directory에 기업 정보 및 연락 방법을 등록하는 것이 소송 리스크를 줄일 수 있는 방법의 하나다.

다음 자체 인증 질문을 살펴보자.

| 2.c  | 오픈소스 컴플라이언스 문의를 받고 대응하기 위한 책임을 할당하는 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure that assigns responsibility for receiving and responding to open source compliance inquiries? |

기업이 외부 클레임에 의해 법적 소송까지 당하지 않기 위해서는 외부 문의 및 요청에 가능한 빠르고 정확하게 대응하는 것이 중요하다. 이를 위해 기업은 외부 오픈소스 문의를 빠르고 효과적으로 대응 할 수 있는 프로세스를 갖추고 있어야 한다. 

위의 내용은 다음의 예시 문장을 오픈소스 정책에 반영할 수 있다.  

~~~

1. 외부 문의 대응
(1) 외부 문의 대응책임
외부로부터 오픈소스 컴플라이언스에 대한 문의 및 요청에 대한 대응은 오픈소스 프로그램 
매니저가 담당한다. 

오픈소스 프로그램 매니저는 [회사] 내의 적절한 인원에게 문의에 대한 전체 또는 일부의 
처리를 할당할 수 있다. 필요할 경우 법률 담당에게 문의하여 처리한다.
외부로부터 오픈소스 컴플라이언스에 대한 문의를 받은 사람은 누구나 이를 오픈소스 
프로그램 매니저에게 알려서 신속한 대응이 될 수 있게 한다. 

(2) 연락처 공개
오픈소스 프로그램 매니저는 외부에서 오픈소스 관련한 문의 및 요청을 할 수 있도록 
담당자의 연락처를 공개적으로 제공한다.

* 오픈소스 고지문에 연락받을 수 있는 이메일 주소 정보를 제공한다. 
* Linux Foundation의 Open Compliance Directory에 연락처를 등록한다.

(3) 외부 문의 대응 절차
외부로부터의 오픈소스 컴플라이언스 문의에 신속하고 정확하게 대응한다면 소송까지 
진행되는 위험을 크게 줄일 수 있다. 이를 위해 회사는 외부의 오픈소스 컴플라이언스 
문의에 대응하기 위해 오픈소스 컴플라이언스 프로세스에서 정의한 외부 문의 대응 절차를 
준수한다. 

~~~

또한 이 가이드에서는 오픈소스 컴플라이언스 문의에 대응하기 위한 일반적인 절차에 대한 예시를 “[부록 2. 샘플 오픈소스 컴플라이언스 프로세스](#부록-2-샘플-오픈소스-컴플라이언스-프로세스)의 [2. 외부 문의 대응 프로세스](#2-외부-문의-대응-프로세스)”에서 제공한다.


#### 2-2. 효과적인 리소스 제공

OpenChain 규격 2.1의 3.2.2항에서는 다음과 같이 효과적인 오픈소스 프로그램의 운영을 위한 리소스 제공에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.2.2 효과적인 리소스 제공

프로그램이 효과적일 수 있도록 다음과 같이 업무를 정의하고 리소스를 제공해야 한다:

* 프로그램을 성공적으로 수행할 수 있도록 각 업무에 대한 책임을 할당한다. 
* 프로그램의 업무를 위한 충분한 리소스를 제공한다.
  * 업무 수행 시간을 할당한다.
  * 예산을 적절하게 지원한다.
* 정책 및 지원 업무를 검토하고 개선하는 프로세스가 존재한다.
* 오픈소스 라이선스 컴플라이언스와 관련된 전문 법률 자문을 이용 할 수 있게 한다.
* 오픈소스 라이선스 컴플라이언스 문제를 해결하기 위한 프로세스가 존재한다.

입증 자료:
* 3.2.2.1 프로그램 내 각 역할을 담당하는 인원, 그룹 또는 직무의 이름을 기재한 문서
* 3.2.2.2 프로그램 내 각 역할을 담당하는 인원이 적합하게 배치되고, 예산이 적절하게 지원되어야 한다.
* 3.2.2.3 오픈소스 라이선스 컴플라이언스 문제 해결을 위해 내부 또는 외부의 전문 법률 자문을 이용하는 방법
* 3.2.2.4 오픈소스 컴플라이언스에 대한 내부 책임을 할당하는 문서화된 절차
* 3.2.2.5 미준수 사례를 검토하고 이를 수정하기 위한 문서화된 절차

---
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

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 각각의 질문과 충족 방안을 살펴보자. 

| 2.d | 프로그램 내 각 역할을 담당하는 인원, 그룹 또는 직무의 이름을 기재한 문서가 있습니까?  |
|---|:---|
| | Have you documented the persons, group or function supporting the Program role(s) identified? |

기업은 각 프로그램 참여자의 역할 및 그에 따른 책임을 나열하고, 각 역할을 담당하는 담당자 혹은 담당 조직을 지정해야 한다. 그리고 이를 문서화하고 오픈소스 정책 문서에 포함해서 누구나 열람할 수 있게 해야 한다. 다음의 예시를 참고하라. 

~~~
4. 역할, 책임 및 역량
이 정책의 효과를 보장하기 위해 다음과 같이 역할과 책임 및 각 역할의 담당자가 갖추어야 
할 역량을 정의한다. 

각 역할의 담당 조직/담당자와 필요 역량 수준은 [Appendix 1. 담당자 현황]에서 
정의한다. 오픈소스 프로그램 매니저는 회사의 비즈니스 상황에 맞추어 주기적으로 명단을 
업데이트한다. 
~~~

다음 자체 인증 질문을 살펴보자. 

| 2.e | 프로그램 내 각 역할을 담당하는 인원이 적합하게 배치되고, 예산이 적절하게 지원되었습니까? |
|---|:---|
|  | Have the identified Program roles been properly staffed and has adequate funding provided? |

기업은 오픈소스 프로그램이 원활하게 기능을 수행할 수 있도록 충분한 리소스를 제공해야 한다. 프로그램 내 각 역할을 담당하는 인원을 적합하게 배치하고, 충분한 예산과 업무 시간을 보장해야 한다. 그렇지 않을 경우, 이를 보완할 수 있는 절차가 마련되어야 한다. 다음의 예시 문장을 오픈소스 정책 문서에 추가할 수 있다. 

~~~
4. 역할, 책임 및 역량

각 역할에 대한 담당 조직의 장은 조직 내 담당자를 지정하고, 담당자가 역할을 충실하게 
수행할 수 있는 적절한 사간과 예산을 할당한다. 각 역할의 담당자는 자신이 역할을 
수행하면서 적절한 지원이 되지 않는다면 오픈소스 프로그램 매니저에게 문제를 제기해야 
한다. 오픈소스 프로그램 매니저는 해당 조직장과 문제 해결을 논의한다. 적절하게 
해결되지 않는다면, 오픈소스 프로그램 매니저는 OSRB에 문제 해결을 요청할 수 있다. 
OSRB는 상위 조직의 장에게 문제를 공유하고 해결을 요청한다. 

~~~


| 2.f | 오픈소스 컴플라이언스와 관련된 문제 해결을 위해 내부 또는 외부의 법률 전문 자문을 이용하는 방법이 있습니까? |
|---|:---|
|  | Is legal expertise pertaining to internal and external open source compliance identified? |

기업은 프로그램 참여자가 이슈 해결을 위해 법률적인 검토가 필요할 경우, 이에 대해 법률 자문을 요청할 수 있는 방법을 제공해야 한다. 회사 내의 법무팀을 통해 우선 제공하고, 이슈가 첨예한 경우, 오픈소스 전문 변호사를 보유한 외부 법무 법인을 이용할 수 있다. 이를 위한 오픈소스 정책의 예시는 다음과 같다. 

~~~

4. 역할, 책임 및 역량

(2) 오픈소스 프로그램 매니저
* 오픈소스 프로그램 매니저는 구성원이 오픈소스 관련 법률 자문을 받을 수 있는 방법을 
  제공한다. 
* 오픈소스 프로그램 매니저는 외부 법무 법인을 참여시켜야 하는지 여부를 결정한다. 
  외부 법률 고문의 효과와 적절성은 오픈소스 프로그램 매니저가 매년 평가하고 검토한다.

~~~

참고로, OpenChain 프로젝트에서는 파트너 프로그램을 통해 오픈소스 관련 자문을 제공하는 글로벌 법무법인 리스트를 제공한다.

{{< imgproc partners Fit "900x600" >}}
<center>< https://www.openchainproject.org/partners ></center>
{{< /imgproc >}}

OpenChain 파트너로 등록된 법무법인은 OpenChain 프로젝트에서 요구하는 요건을 충족한 곳들이며, 대한민국에서는 유일하게 법무법인 태평양이 등록되어 있다.


| 2.g | 오픈소스 컴플라이언스에 대한 내부 책임을 할당하는 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure assigning internal responsibilities for Open Source compliance? |

오픈소스 컴플라이언스를 위한 내부 책임을 할당하는 절차가 있어야 한다. 이는 오픈소스 프로그램 매니저의 역할이다. 오픈소스 프로그램 매니저는 이슈를 파악하고 각 역할의 담당자에게 적절히 이슈를 할당해야 한다. 이를 위해 기업은 오픈소스 정책 문서에 이러한 내용을 아래와 같이 기술할 수 있다.

~~~

4. 역할, 책임 및 역량

(2) 오픈소스 프로그램 매니저

오픈소스 프로그램 매니저는 회사의 오픈소스 프로그램에 대한 총괄 책임을 담당한다. 
오픈소스를 사용한 제품과 서비스의 오픈소스 컴플라이언스를 보장하기 위해 다음 사항에 대한 
책임이 있다.

* 오픈소스 컴플라이언스를 위해 필요한 역할을 정의하고, 각 역할을 책임질 담당 조직 및 
  담당자를 지정한다. 필요 시 OSRB와 협의한다.

~~~


| 2.h | 미준수 사례를 검토하고 이를 수정하기 위한 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure for handling review and remediation of non-compliant cases? |

컴플라이언스 미준수 문제가 제기된 경우, 기업은 이를 신속히 검토하고 대응하기 위한 절차를 문서화해야 한다. 다음의 예시를 참고하여 오픈소스 정책에 포함할 수 있다. 

~~~
1. 오픈소스 사용

(5) 컴플라이언스 이슈 수정 절차
컴플라이언스 이슈가 제기될 경우, 오픈소스 프로그램 매니저는 다음의 절차를 수행하여 
신속히 대응한다. 

1. 문의 접수를 확인하고 적절한 해결 시간을 명시한다.
2. 이슈 내용이 실제 문제를 지적하고 있는지를 확인한다. (아닐 경우, 이슈 제기자에게 
   문제가 아님을 알린다.)
3. 실제 문제인 경우, 우선순위를 정하고 적절한 대응 방안을 결정한다.
4. 대응을 수행하고, 필요할 경우, 오픈소스 컴플라이언스 프로세스를 적절하게 보완한다.
5. 위의 내용은 Jira Tracker를 이용하여 보존한다.
~~~

### 3. 오픈소스 콘텐츠 검토 및 승인<sub>Open	source	content	review	and	approval</sub>


#### 3.1 BOM (Bill of Materials)

OpenChain 규격 버전 2.1의 3.3.1항에서는 다음과 같이 BOM(Bill of Materials)에 대한 요구사항과 입증 자료를 정의하고 있다.


{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.3.1 BOM

배포용 소프트웨어를 구성하는 오픈소스 컴포넌트(및 식별된 라이선스)에 대한 BOM(Bill of Materials)을 생성하고 관리하는 프로세스가 있어야 한다.

입증 자료:

* 3.3.1.1 배포용 소프트웨어를 구성하는 오픈소스 컴포넌트에 대한 정보를 식별, 추적, 검토, 승인 및 보관하는 문서화된 절차 
* 3.3.1.2 문서화된 절차가 적절히 준수되었음을 보여주는 배포용 소프트웨어에 대한 오픈소스 컴포넌트 기록

---

3.3.1 Bill of Materials

A process shall exist for creating and managing a bill of materials that includes each open source component (and its identified licenses) from which the supplied software is comprised.

Verification Material(s):

* 3.1.1.1  A documented procedure for identifying, tracking, reviewing, approving, and archiving information about the collection of open source components from which the supplied software is comprised.
* 3.3.1.2 Open source component records for the supplied software that demonstrates the documented procedure was properly followed.

{{% /alert %}}

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 3.a  | 배포용 소프트웨어를 구성하는 오픈소스 컴포넌트에 대한 정보를 식별, 추적, 검토, 승인 및 보관하는 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure for identifying, tracking and archiving information about the collection of open source components from which a Supplied Software release is comprised? |

오픈소스 컴플라이언스 활동의 가장 기본은 배포용 소프트웨어에 포함된 오픈소스 현황을 파악하는 것이다. 배포용 소프트웨어에 포함된 오픈소스와 그 라이선스를 식별하여 그 정보를 담고 있는 BOM(Bill of Materials)을 작성하고 관리하는 프로세스를 구축해야 한다. 배포용 소프트웨어의 버전마다 어떤 오픈소스가 포함되어 있는지 알고 있어야 소프트웨어를 배포할 때 각 오픈소스의 라이선스가 요구하는 의무 사항을 준수할 수 있기 때문이다.

모든 오픈소스는 배포용 소프트웨어에 통합하기 전에 검토 및 승인되어야 한다. 오픈소스의 기능, 품질뿐만 아니라 출처, 라이선스 요건을 충족할 수 있는지 사전 검토가 되어야 한다. 이를 위해 검토 요청 → 리뷰 → 승인 과정이 필요하다. [부록 2. 샘플 오픈소스 컴플라이언스 프로세스](#부록-2-샘플-오픈소스-컴플라이언스-프로세스)에서는 기업의 오픈소스 컴플라이언스를 위한 프로세스 모든 과정에 관해 설명하고 있다. [1. 오픈소스 식별](#1-오픈소스-식별subidentification-of-open-sourcesub)부터 [6. 등록](#6-등록subregistrationsub)까지의 과정을 통해 BOM을 작성하고 관리하게 된다.

또 이와 같은 오픈소스 컴플라이언스 프로세스의 모든 과정과 결과는 문서화가 되어야 한다. 이메일을 사용하는 것보다는 Jira, Bugzilla 등의 이슈 트래킹 시스템을 이용하는 것이 이러한 과정을 효율적으로 문서화 할 수 있다.

| 3.b  | 문서화된 절차가 적절히 준수되었음을 보여주는 배포용 소프트웨어에 대한 오픈소스 컴포넌트 기록이 있습니까? |
|---|:---|
|  | Do you have open source component records for each Supplied Software release which demonstrates the documented procedure was properly followed? |

배포용 소프트웨어에 포함된 오픈소스 목록은 문서화하여 보관해야 한다. Eclipse 재단에서 후원하는 오픈소스 프로젝트인 [SW360](https://projects.eclipse.org/proposals/sw360)[^sw360]은 배포용 소프트웨어별로 포함하고 있는 오픈소스 목록을 트래킹할 수 있는 기능을 제공한다. SW360 사용 방법은 [부록 3. 오픈소스 도구](#부록-3-오픈소스-도구)을 참고할 수 있다.

[^sw360]: SW360 - https://projects.eclipse.org/proposals/sw360

이 가이드에서는 BOM 사용 정책에 대한 예시를 “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)"의 [6. 오픈소스 사용](#6-오픈소스-사용)에서 제공한다.


#### 3.2 라이선스 컴플라이언스

OpenChain 규격 버전 2.1의 3.3.2항에서는 다음과 같이 라이선스 컴플라이언스에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.3.2 라이선스 컴플라이언스

프로그램은 배포용 소프트웨어에 대해 프로그램 참여자가 접할 수 있는 일반적인 오픈소스 라이선스의 사용 사례를 관리할 수 있어야 한다. 여기에는 다음과 같은 사용 사례가 포함될 수 있다(아래 목록이 모든 사례를 다루는 것은 아니며, 또한 이 사례를 모두 다뤄야만 하는 것은 아님). :

- 바이너리 형태로 배포
- 소스 형태로 배포
- 추가 라이선스 의무를 유발하는 다른 오픈소스와 통합
- 수정된 오픈소스 포함
- 배포용 소프트웨어 내의 다른 컴포넌트와 서로 호환되지 않는 라이선스 하의 오픈소스 또는 다른 소프트웨어를 포함
- 저작자 표시 요구사항을 갖는 오픈소스 포함

입증 자료:

* 3.3.2.1 배포용 소프트웨어 내의 오픈소스 컴포넌트에 대해 일반적인 오픈소스 라이선스 사용 사례를 처리하기 위한 문서화된 절차

---
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

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 3.c  | 각 배포용 소프트웨어 릴리스 내의 오픈소스 컴포넌트에 대해 적어도 다음과 같은 일반적인 오픈소스 라이선스 사용 사례를 처리하는 절차를 구현했습니까? <br><br> i - 바이너리 형태로 배포; <br>ii - 소스 형태로 배포; <br>iii - Copyleft 의무를 발생시킬 수 있는 다른 오픈 소스와 통합; <br>iv - 수정된 오픈소스 포함;<br>v - 배포용 소프트웨어 내의 다른 컴포넌트와 서로 호환되지 않는 라이선스 하의 오픈소스 또는 다른 소프트웨어를 포함;<br>vi - 저작자 표시 요구사항을 갖는 오픈소스 포함 |
|---|:---|
|  | Have you implemented a procedure that handles at least the following common open source license use cases for the open source components of each supplied Supplied Software release?<br><br>i - distributed in binary form;<br>ii - distributed in source form;<br>iii - integrated with other open source such that it may trigger copyleft obligations;<br>iv - contains modified open source;<br>v - contains open source or other software under an incompatible license interacting with other components within the Supplied Software;<br>vi - contains open source with attribution requirements.|

오픈소스 라이선스를 제대로 준수하기 위해서는 오픈소스 라이선스별로 요구하는 사항에 대해 정확히 알고 있어야 한다. 하지만 개별 소프트웨어 개발자가 이를 일일이 파악하는 것은 어려우므로 오픈소스 책임자는 자주 사용되는 오픈소스 라이선스에 대해 일반적인 사용 사례별 요구사항/주의사항을 정리하여 회사 내부에 공유하는 것이 좋다. 오픈소스 라이선스에 대한 일반적인 가이드와 라이선스 의무 요약 자료는 NIPA에서 제공하는 [공개소프트웨어 라이선스 가이드](https://www.oss.kr/oss_license)[^nipa-license]를 참고할 수 있다. 또한, 소프트웨어의 사용 사례별 라이선스 의무를 분석한 SK텔레콤의 오픈소스 라이선스 가이드[^gpl]도 좋은 사례가 된다. 

[^nipa-license]: NIPA 공개소프트웨어 라이선스 가이드 - https://www.oss.kr/oss_license

[^gpl]: SK텔레콤 오픈소스 라이선스 가이드 - https://sktelecom.github.io/guide/use/obligation/gpl-2.0/

[부록 2. 샘플 오픈소스 컴플라이언스 프로세스](#부록-2-샘플-오픈소스-컴플라이언스-프로세스)의 오픈소스 컴플라이언스 프로세스의 오픈소스 식별, 검사, 문제해결, 리뷰, 승인 단계를 통해 배포용 소프트웨어의 오픈소스 컴포넌트에 대해 일반적인 오픈소스 라이선스 사용 사례를 처리할 수 있다.

식별 및 검사 단계에서는 소스 코드 스캔 도구를 사용할 수 있다. 소스 코드 스캔 도구는 무료로 사용할 수 있는 오픈소스 기반 도구부터 상용 도구까지 다양하게 있는데, 각 도구는 특장점 들이 있지만 어떤 하나도 모든 문제를 해결할 수 있는 완벽한 기능을 제공하지 않는다. 따라서 기업은 제품의 특성과 요구사항에 맞는 적합한 도구를 선택해야 한다. 많은 기업이 이러한 자동화된 소스 코드 스캔 도구와 수동 검토를 병행하여 이용한다. Linux Foundation의 FOSSology[^fossology] 프로젝트는 오픈소스로 공개된 소스 코드 스캔 도구로서 기업들이 손쉽게 무료로 사용할 수 있다. 사용 방법은 [부록 3. 오픈소스 도구](#부록-3-오픈소스-도구)를 참고한다. 

[^fossology]: FOSSology - http://fossology.org/

### 4. 컴플라이언스 산출물 생성 및 제공<sub>Compliance	artifact	creation	and	delivery</sub>

#### 4.1 컴플라이어스 산출물

OpenChain 규격 버전 2.1의 3.4.1항에서는 다음과 같이 컴플라이언스 산출물에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.4.1 컴플라이언스 산출물

 배포용 소프트웨어에 대한 컴플라이언스 산출물을 생성하는 프로세스가 있어야 한다. 

입증 자료:

* 3.4.1.1 식별된 라이선스가 요구하는 컴플라이언스 산출물을 준비하고, 이를 배포용 소프트웨어와 함께 제공하기 위한 프로세스를 설명하는 문서화된 절차
* 3.4.1.2 배포용 소프트웨어의 컴플라이언스 산출물 사본을 보관하기 위한 문서화된 절차 
  - 산출물 사본은 배포용 소프트웨어의 마지막 배포 이후 합리적인 기간 동안 혹은 식별된 라이선스에서 요구하는 기간 동안 보관해야 한다(둘 중 더 긴 기간을 따름). 
  - 이러한 절차가 올바르게 수행되었음을 입증하는 기록이 존재해야 한다.

---

3.4.1 Compliance artifacts

A process shall exist for creating the set of compliance artifacts for the supplied software.

Verification Materials(s):

* 3.4.1.1 A documented procedure that describes the process under which the compliance artifacts are prepared and distributed with the supplied software as required by the identified licenses.
* 3.4.1.2 A documented procedure for archiving copies of the compliance artifacts of the supplied software - where the archive is planned to exist for a reasonable period of time (determined by domain, legal jurisdiction and/or customer contracts) since the last offer of the supplied software; or as required by the identified licenses (whichever is longer). Records exist that demonstrate the procedure has been properly followed.

{{% /alert %}}

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 4.a  | 식별된 라이선스가 요구하는 컴플라이언스 산출물을 준비하고, 이를 배포용 소프트웨어와 함께 제공하기 위한 프로세스를 설명하는 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure that describes a process that ensures the Compliance Artifacts are distributed with Supplied Software as required by the Identified Licenses? |

앞 장에서 오픈소스 컴플라이언스 활동의 가장 기본은 배포용 소프트웨어에 포함된 오픈소스 현황을 파악하는 것이라고 하였다. 이는 바로 오픈소스 컴플라이언스의 핵심인 오픈소스 라이선스 요구사항을 올바르게 충족하기 위해서이다. 즉, 배포용 소프트웨어에 포함된 오픈소스에 대한 컴플라이언스 산출물 세트를 생성하는 프로세스가 구축되어야 한다.

컴플라이언스 산출물은 크게 두 가지로 구분된다.

1. 오픈소스 고지문 : 오픈소스 라이선스 전문과 저작권 정보 제공을 위한 문서
2. 공개할 소스 코드 패키지 : GPL, LGPL 등 소스 코드 공개를 요구하는 오픈소스 라이선스 의무 이행을 위해 공개할 소스 코드를 취합한 패키지

이 가이드에서는 컴플라이언스 산출물 생성을 위한 정책에 대한 예시를 “[부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [6. 오픈소스 사용](#6-오픈소스-사용)”에서 제공한다.

컴플라이언스 산출물은 배포용 소프트웨어를 배포할 때 함께 제공해야 한다. “[부록 2. 샘플 오픈소스 컴플라이언스 프로세스](#부록-2-샘플-오픈소스-컴플라이언스-프로세스)”의 고지, 배포 전 확인, 배포 단계를 통해 컴플라이언스 산출물을 생성하여 배포한다.

| 4.b  | 배포용 소프트웨어의 컴플라이언스 산출물 사본을 보관합니까? |
|---|:---|
|  | Do you archive copies of the Compliance Artifacts of the Supplied Software? |

| 4.c  | 컴플라이언스 결과물 사본은 적어도 배포용 소프트웨어가 제공되는 중이거나 식별된 라이선스가 요구하는 기간 중 더 긴 시간 동안 보관됩니까? |
|---|:---|
|  | Are the copies of the Compliance Artifacts archived for at least as long as the Supplied Software is offered or as required by the Identified Licenses (whichever is longer)? |

배포용 소프트웨어를 배포 시, 공개할 소스 코드 패키지를 동봉하는 것이 곤란할 경우, 최소 3년간 소스 코드를 제공하겠다는 서면 약정서(Written Offer)를 제공하는 것으로 대신할 수 있다. 일반적으로 서면 약정서는 제품의 사용자 매뉴얼을 통해 제공하며, 예시는 다음과 같다.

> The software included in this product contains copyrighted software that is licensed under the GPL. A copy of that license is included in this document on page X. You may obtain the complete Corresponding Source code from us for a period of three years after our last shipment of this product, which will be no earlier than 2011-08- 01, by sending a money order or check for $5 to:
>
> GPL Compliance Division  
> Our Company  
> Any Town, US 99999  
>   
> Please write“source for product Y” in the memo line of your payment.  
> You may also find a copy of the source at http://www.example.com/sources/Y/.  
> This offer is valid to anyone in receipt of this information.

_<center>< 출처 : SPLC Guide to GPL Compliance ></center>_

따라서, 컴플라이언스 산출물은 3년 이상 보관해야 하며 이를 위한 프로세스가 구축되어야 한다. 일부 기업은 자체적인 웹사이트(예: http://opensource.lge.com/) 구축하여 외부 고객들이 배포용 소프트웨어에 대한 오픈소스 고지문과 공개할 소스 코드 패키지를 언제든지 다운받을 수 있도록 편의를 제공한다.


### 5. 오픈소스 커뮤니티 참여에 대한 이해<sub>Understanding	open	source	community	engagements</sub>

#### 5.1 기여 

OpenChain 규격 버전 2.1의 3.5.1항에서는 다음과 같이 컴플라이언스 산출물에 대한 요구사항과 입증 자료를 정의하고 있다.


{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.5.1 기여

조직이 외부 오픈소스 프로젝트로의 기여를 허용하려고 한다면,
- 외부 오픈소스 프로젝트로의 기여를 관리하는 문서화된 정책이 있어야 한다. 
- 이 정책이 내부에 전파되어야 한다.
- 정책을 시행하는 프로세스가 있어야 한다. 

입증 자료:

조직이 외부 오픈소스 프로젝트로의 기여를 허용하는 경우, 다음 사항이 있어야 한다.:
- 3.5.1.1 문서화된 오픈소스 기여 정책
- 3.5.1.2 오픈소스 기여를 관리하는 문서화된 절차
- 3.5.1.3 모든 프로그램 참여자가 오픈소스 기여 정책의 존재를 인식하도록 하는 문서화된 절차 (예: 교육, 내부 위키, 또는 기타 실질적인 전달 방법 등)

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

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 5.a  | 조직을 대신하여 오픈소스 프로젝트에 기여하는 것을 관리하는 정책이 있습니까? |
|---|:---|
|  | Do you have a policy that governs contributions to open source projects on behalf of the organization? |


글로벌 소프트웨어 기업들은 제품을 만들고 서비스를 하는 데 오픈소스를 사용하는 것뿐만 아니라 오픈소스 프로젝트에 기여하며 창출할 수 있는 전략적 가치도 중요하게 여긴다. 그러나 오픈소스 프로젝트 생태계와 커뮤니티 운영방식에 대한 충분한 이해와 전략 없이 접근한다면 예기치 않게 회사의 명성이 손상되고 법적 위험이 발생할 수 있다. 따라서 기업은 오픈소스 프로젝트로의 참여 및 기여를 위한 전략과 정책을 만드는 것이 중요하다.

이러한 오픈소스 기여에 대한 정책은 [부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [7. 오픈소스 기여](#7-오픈소스-기여)를 참고할 수 있다.

| 5.b  | 오픈소스 기여를 관리하는 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure that governs Open Source contributions? |

외부 오픈소스 프로젝트에 기여를 허용하는 정책을 갖고 있다면, 사내 개발자들이 어떤 절차로 외부 프로젝트에 기여할 수 있을지 관리하는 문서화된 절차가 있어야 한다. SK텔레콤에서 공개한 [오픈소스 기여 절차](https://sktelecom.github.io/guide/contribute/process/)[^skt-contribution]는 좋은 예이다. 

[^skt-contribution]: SK텔레콤 오픈소스 기여 절차 - https://sktelecom.github.io/guide/contribute/process/

| 5.c  | 모든 프로그램 참여자가 오픈소스 기여 정책의 존재를 인식하도록 하는 문서화된 절차가 있습니까? |
|---|:---|
|  | Do you have a documented procedure that makes all Software Staff aware of the existence of the Open Source contribution policy? |

오픈소스 기여 정책을 만들었다 해도 사내 구성원이 이에 대한 존재를 알지 못한다면 무용지물이 되어버린다. 모든 사내 개발자가 오픈소스 기여 정책의 존재를 알 수 있게 하는 절차가 필요하다. 3.1.1.2에서의 오픈소스 정책 전파 활동과 병행하여 오픈소스 기여 정책을 전파하라. 


### 6. 규격 요구사항 준수<sub>Adherence	to	the	specification	requirements</sub>

#### 6.1 적합성<sub>Conformance</sub>

OpenChain 규격 버전 2.1의 3.6.1항에서는 다음과 같이 적합성에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.6.1 적합성

프로그램이 OpenChain에 적합하다고 간주하기 위해서는 조직은 프로그램이 이 규격에서 제시한 모든 요구사항을 충족하는지 확인해야 한다.

입증 자료:

* 3.6.1.1 3.1.4조에서 명시한 프로그램이 이 규격의 모든 요구사항을 충족함을 확인하는 문서

----------------

3.6.1 Conformance

In order for a program to be deemed OpenChain conformant, the organization shall affirm that the program satisfies the requirements presented in this document.

Verification Materials(s):

* 3.6.1.1 A document affirming the program specified in §3.1.4 satisfies all the requirements of this document.

{{% /alert %}}

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 6.a  | 프로그램이 이 규격의 모든 요구사항을 충족함을 확인하는 문서가 있습니까? |
|---|:---|
|  | Do you have documentation confirming that your Program meets all the requirements of this specification? |

OpenChain 규격 2.1의 모든 요구사항을 충족하는 기업은 이를 Linux Foundation에 알리고, 확인 과정을 거친 후, ISO/IEC 5230 적합성 인증을 취득하고, 이를 선언할 수 있다. 어느 하나의 요구사항이라도 충족하지 못한다면 ISO/IEC 5230에 적합하다고 할 수 없다.  

OpenChain 규격의 모든 요구사항을 충족한다면, [부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [10. OpenChain](#10-openchain)에서와 같이 OpenChain에 적합하다고 정책 문서상에 명시할 수 있다.

#### 6.2 지속 기간

OpenChain 규격 버전 2.1의 3.6.2항에서는 다음과 같이 지속 기간에 대한 요구사항과 입증 자료를 정의하고 있다.

{{% alert title="OpenChain 규격 버전 2.1, " color="success" %}}

3.6.2 지속 기간

이 규격의 버전 2.1에 적합한 OpenChain 프로그램은 적합성 인증을 획득한 날로부터 18개월 동안 지속되어야 한다. 적합성 인증 등록 절차는 OpenChain 프로젝트의 웹사이트에서 확인할 수 있다.

입증 자료:

* 3.6.2.1 프로그램이 적합성 인증을 획득한 후 지난 18개월 동안 이 규격 버전(v2.1)의 모든 요구사항을 충족하고 있음을 확인하는 문서

---

3.6.2 Duration

A program that is OpenChain conformant with this version of the specification shall last 18 months from the date conformance validation was obtained. The conformance validation registration procedure can be found on the OpenChain project’s website.

Verification Materials(s):

* 3.6.2.1 A document affirming the program meets all the requirements of this document, within the past 18 months of obtaining conformance validation.

{{% /alert %}}

이와 관련하여 [OpenChain 자체 인증](https://certification.openchainproject.org/)[^question]에서 요구하는 질문과 그에 대한 대응책은 다음과 같다.  

| 6.b  | 지난 18개월 이내에 프로그램 적합성을 검토했음을 확인하는 문서가 있습니까? |
|---|:---|
|  | Do you have documentation confirming that your Program conformance was reviewed within the last 18 months? |

기업은 OpenChain에 적합하다고 선언한 이후에도 계속해서 준수하는 활동을 유지하는 것이 중요하다. OpenChain 규격 버전 2.1의 3.6.2.1조에서는 OpenChain을 적합성을 선언한 이후에도 최소 18개월 이상은 변함없이 OpenChain 규격 버전 2.1의 모든 요구사항을 준수하고 있어야 함을 요구한다.

기업은 OpenChain 적합성을 선언한 이후 적어도 18개월 이상 계속해서 준수하는 상태를 유지하여야 하며, 그렇게 하고 있다면, [부록 1. 샘플 오픈소스 정책](#부록-1-샘플-오픈소스-정책)의 [10. OpenChain](#10-openchain)에서와 같이 OpenChain을 18개월 이상 계속하여 충족하고 있음을 문서상에 명시할 수 있다. 

또한, SK텔레콤과 같이 웹사이트를 이용하여 이를 외부에 알리는 것도 좋은 방법이다.

{{< imgproc iso5230-skt Resize "700x" >}}
<center><i>https://sktelecom.github.io/compliance/iso5230/ </i></center>
{{< /imgproc >}}

## 부록 1. 샘플 오픈소스 정책

### 1. 목적

#### (1) 정책의 목적<sub>(3.1.3.1)</sub>

이 정책은 OOO 주식회사(이하 "회사"라 함)에서 소프트웨어 개발, 서비스, 배포에 관여하는 전체 조직이 올바르게 오픈소스 소프트웨어(이하 "오픈소스"라 함)를 활용하기 위해 다음과 같은 원칙을 제공한다. 

1. 오픈소스 라이선스를 고려한 컴플라이언스 수행 원칙
2. 외부 오픈소스 프로젝트로의 기여 원칙
3. 사내 프로젝트를 오픈소스로 공개하기 위한 원칙

이러한 원칙은 회사의 모든 구성원이 오픈소스의 가치를 이해하고, 오픈소스를 올바르게 사용하며, 오픈소스 커뮤니티에 기여하기 위한 방법을 제공한다.

회사의 모든 구성원은 사내 위키의 다음 링크에서 오픈소스 정책을 확인할 수 있다. : [internal_link]<sub>(3.1.1.1)</sub>

#### (2) 미준수 시 영향
이 정책을 준수하지 않는다면 다음과 같은 상황이 발생할 수 있다.  

- 외부로부터 오픈소스 라이선스 준수 요구를 받게 된다.
- 회사가 개발한 소스 코드를 원하지 않게 공개해야 한다.
- 오픈소스 저작권자로부터 법적 소송을 제기당하게 된다.
- 저작권 침해 및 계약 위반으로 벌금을 부과 당하거나, 제품 판매 중지 명령을 받게 된다.
- 회사 평판이 손실된다. 
- 공급업체와의 계약 위반이 되어 손해배상 청구를 당하게 된다.

이러한 이유로 회사는 오픈소스 정책의 위반을 심각하게 간주하며, 이를 위반하는 구성원이나 조직은 징계 절차에 처할 수 있다.

#### (3) 구성원의 공헌 방법

회사의 모든 구성원은 이 정책의 근거와 내용을 이해하고 필요한 활동을 충실히 수행함으로써 정책의 효과 및 회사의 컴플라이언스 수준 향상에 공헌할 수 있다.

### 2. 적용 범위<sub>(3.1.4.1)</sub>
이 정책은 다음 세 부분에 적용한다.

1. [회사가 외부로 제공하거나 배포하는 모든 제품]에 적용한다. 단, 오픈소스를 내부 사용 목적으로만 사용하는 것은 이 정책의 범위에 포함되지 않는다.
2. 구성원이 외부 오픈소스 프로젝트로의 기여 시에 적용한다.
3. 내부 코드를 오픈소스로 공개할 때 적용한다.

적용 범위는 회사의 비즈니스 환경에 맞추어 변경할 수 있으며, 이를 위한 절차는 다음과 같다. 

1. 오픈소스 프로그램 매니저는 신규사업, 조직개편 등 회사의 비즈니스 환경이 변화에 따라 정책의 적용 범위 변경이 필요하다고 판단할 경우, 이를 위한 제안을 OSRB에 제출한다. 
2. OSRB에서는 적절한 수준의 적용 범위 변경을 승인한다. 
3. OSRB는 오픈소스 정책을 수정하여 정책의 적용 범위를 변경한다. 


### 3. 용어
* BOM (Bill of Materials) 
* 소프트웨어 배포 참여자 : 회사가 소프트웨어를 개발하고 배포, 기여하는 데 관여하는 모든 직원을 의미하며, 소프트웨어 개발자, 배포 엔지니어, 품질 엔지니어 등을 포함한다. 
* ...

### 4. 역할, 책임 및 역량<sub>(3.1.2.1)</sub>
  정책의 효과를 보장하기 위해 다음과 같이 역할과 책임 및 각 역할의 담당자가 갖추어야 할 역량을 정의한다. 

 각 역할의 담당 조직/담당자와 필요 역량 수준은 [Appendix 1. 담당자 현황]에서 정의한다.<sub>(3.1.2.2)</sub>
 
* 오픈소스 프로그램 매니저는 회사의 비즈니스 상황에 맞추어 주기적으로 명단을 업데이트한다.<sub>(3.2.2.1)</sub>
* 각 역할에 대한 담당 조직의 장은 조직 내 담당자를 지정하고, 담당자가 역할을 충실하게 수행할 수 있는 적절한 사간과 예산을 할당한다.<sub>(3.2.2.2)</sub>
  * 각 역할의 담당자는 자신이 역할을 수행하면서 적절한 지원이 되지 않는다면 오픈소스 프로그램 매니저에게 문제를 제기해야 한다.
  * 오픈소스 프로그램 매니저는 해당 조직장과 문제 해결을 논의한다. 적절하게 해결되지 않는다면, 오픈소스 프로그램 매니저는 OSRB에 문제 해결을 요청할 수 있다.
  * OSRB는 상위 조직의 장에게 문제를 공유하고 해결을 요청한다. 

#### (1) OSRB
OSRB<sub>Open Source Review Board</sub>는 회사의 오픈소스 컴플라이언스 위해 오픈소스 프로그램 매니저와 법무팀, 특허팀, 개발팀, 인프라팀 등 관련 조직의 책임자로 구성된 협의체이다. 

* 오픈소스 컴플라이언스를 위한 정책과 프로세스를 만들고, 이를 수행하기 위한 회사 내의 역할과 책임을 정의한다. 
* 회사 내 오픈소스 컴플라이언스 이슈 발생 시, 해결 방안을 논의하고, 대응책을 마련한다.
* 필요 시, 임원진에 이슈를 보고하여 리스크 완화 방안에 대한 피드백을 받는다. 

#### (2) 오픈소스 프로그램 매니저
오픈소스 프로그램 매니저는 회사의 오픈소스 프로그램에 대한 총괄 책임을 담당한다. 오픈소스를 사용한 제품과 서비스의 오픈소스 컴플라이언스를 보장하기 위해 다음 사항에 대한 책임이 있다.<sub>(3.2.2.4)</sub>

- 오픈소스 컴플라이언스를 위해 필요한 역할을 정의하고, 각 역할을 책임질 담당 조직 및 담당자를 지정한다. 필요 시 OSRB와 협의한다. 
- 오픈소스 컴플라이언스 교육을 주관하고 평가한다.
- OSRB의 의장을 맡아서 활동을 지휘한다.
- 외부로부터의 오픈소스 사용 및 컴플라이언스 관련 문의 및 요청에 대응한다.
- 오픈소스 사용 요청을 검토하고 승인한다. 
- 오픈소스 BOM 기록을 유지한다.
- 구성원에게 오픈소스 관련 법률 자문 받는 방법을 제공한다.<sub>(3.2.2.3)</sub>
- 오픈소스 고지 및 소스 코드 공개를 위한 저장소를 유지한다.

#### (3) OSPO
OSPO<sub>Open Source Program Office</sub>는 회사 안팎으로 오픈소스 활동의 성장을 위해 지원, 육성하는 역할을 한다. 

- 오픈소스 정책을 수립, 개선 및 전파한다. 
- 외부 오픈소스 프로젝트로의 코드 기여를 위한 가이드를 제공한다.
- 사내 프로젝트를 오픈소스로 공개하기 위한 가이드를 제공한다. 
- 오픈소스 포털을 개발 및 운영한다. 
- 오픈소스 도구를 개발 및 선택한다. 
- 오픈소스 프로젝트 이벤트를 후원한다.
- 오픈소스 커뮤니티와의 관계를 관리한다.

#### (4) 법무 담당
법무 담당은 오픈소스 라이선스와 의무를 해석하는 등 오픈소스 활용 과정에서 발생할 수 있는 법적 위험과 완화 방안에 대한 자문을 제공한다. 

- 호환되지 않는 오픈소스 라이선스로 인한 충돌을 포함하여 라이선스 및 지식재산권 문제에 대해 자문을 제공한다.
- 외부 오픈소스 프로젝트로의 기여 시 오픈소스 라이선스, CLA<sub>Contributor License Agreement</sub> 등 필요한 법적 사항을 검토한다. 

#### (5) IT 인프라 담당
IT 인프라 담당은 오픈소스 분석 도구를 운영하고 자동화하여 모든 배포용 소프트웨어에 대해 라이선스 분석이 원활히 수행되도록 시스템을 구축한다. 

- 오픈소스 라이선스 분석 도구를 운영한다. 
- DevOps 환경과 통합하여 라이선스 분석을 자동화한다. 
- 모든 배포용 소프트웨어를 대상으로 라이선스 분석이 수행되도록 시스템과 프로세스를 구축한다. 
- 모든 배포용 소프트웨어에 대한 오픈소스 BOM을 확보하고 유지한다. 

#### (6) 보안 담당
보안 담당은 오픈소스 보안취약점 분석 도구를 운영하여 모든 배포용 소프트웨어에 대해 보안취약점 분석이 원활히 수행되도록 시스템을 구축한다. 

- 오픈소스 보안취약점 분석 도구를 운영한다. 
- DevSecOps 환경과 통합하여 오픈소스 보안취약점 분석을 자동화한다. 
- 모든 배포용 소프트웨어를 대상으로 오픈소스 보안취약점 분석이 수행되도록 시스템과 프로세스를 구축한다. 

#### (7) 개발 문화 담당
개발 문화 담당은 사내 개발자들이 오픈소스를 적극적으로 활용하고 사내외 커뮤니티에 참여하여 선진 개발 문화를 습득할 수 있도록 지원한다. 

- 오픈소스 커뮤니티로의 참여를 장려한다. 
- 활발한 외부 오픈소스 프로젝트 활동을 사내 성과로 인정할 수 있는 문화를 조성한다. 
- 오픈소스 개발자들에게 매력 있는 회사로 인식될 수 있는 개발 문화를 만들어간다. 

#### (8) 품질 담당
QA 등 품질을 담당하는 조직은 소프트웨어 배포 시 오픈소스 라이선스 의무를 적절히 수행하였는지 확인한다. 

- 개발 프로세스 단계에 맞추어 오픈소스 컴플라이언스 활동이 수행되었는지 확인한다. 
- 오픈소스 라이선스가 요구하는 대로 산출물을 생성하였는지 확인한다. 
- 소프트웨어 배포 시 오픈소스 고지문과 공개할 소스 코드를 함께 제공하는지 확인한다. 
- 이슈가 있으면 소프트웨어 개발/배포 조직에 통보하여 즉시 이슈를 수정하도록 안내한다. 


### 5. 교육 및 평가
모든 소프트웨어 배포 참여자는 매년 [Learning Portal]에서 제공하는 오픈소스 의무 교육을 수강해야 한다. 이를 통해 오픈소스 정책, 관련 교육 정책 및 조회 방법을 숙지한다. 교육 이력은 [Learning Portal]에 보존한다.<sub>(3.1.1.2)<sub>

4장에서 정의한 각 역할을 담당하는 모든 구성원은 [Learning Portal]에서 제공하는 오픈소스 교육 고급 과정을 수강해야 한다. 교육 이력과 평가 결과는 [Learning Portal]에 최소 3년간 보존한다.<sub>(3.1.2.3)</sub>

### 6. 오픈소스 사용

오픈소스를 사용하여 제품 및 서비스를 개발하고 배포하려면 각 오픈소스 라이선스가 요구하는 의무 사항을 준수해야 한다. 이를 위한 활동을 오픈소스 컴플라이언스라고 한다. 

올바른 오픈소스 컴플라이언스 활동을 위해 소프트웨어 개발/배포 조직은 다음 사항을 준수해야 한다.<sub>(3.3.1.1)</sub>

* 오픈소스 컴플라이언스 프로세스의 모든 과정은 Jira Tracker에 기록하여 보존한다. 

#### (1) 오픈소스 식별 및 라이선스 의무 사항 검토

오픈소스를 제품 / 서비스 개발에 도입 시, 먼저 오픈소스 라이선스가 무엇인지 식별하고, 라이선스가 요구하는 의무 사항을 검토하고 확인한다. 

회사의 [오픈소스 라이선스 가이드]에는 주요 오픈소스 라이선스 목록이 포함되어 있으며, 라이선스마다 다음의 배포 형태별 요구하는 의무사항을 구분하여 설명한다.<sub>(3.3.2.1)</sub>

- 바이너리 형태
- 소스 형태
- 강한/약한 Copyleft
- SasS 기반 제공
- 수정 여부
- 저작자 표시 요구 오픈소스 포함 등. 

소프트웨어 개발/배포 조직은 오픈소스 라이선스 의무 검토 시 이 가이드를 참고할 수 있다. 이 가이드에서 언급하지 않는 오픈소스 라이선스의 검토가 필요할 경우, 오픈소스 프로그램 매니저에게 문의한다. 

#### (2) 오픈소스 라이선스 고려 설계

오픈소스의 결합 관계를 파악하여 자사의 코드가 오픈소스 라이선스의 영향을 받지 않도록 소프트웨어 아키텍처를 설계한다.

회사의 [오픈소스 라이선스 가이드]에서는 오픈소스 라이선스별 소스 코드 공개 범위 및 자사 코드의 공개를 방지하기 위한 설계 방법을 설명한다.

#### (3) 오픈소스 컴플라이언스 산출물 생성
오픈소스 컴플라이언스 활동의 가장 기본은 배포용 소프트웨어에 포함된 오픈소스 현황을 파악하는 것이다. 이는 바로 오픈소스 컴플라이언스의 핵심인 오픈소스 라이선스 요구사항을 올바르게 충족하기 위해서이다. 즉, 배포용 소프트웨어에 포함된 오픈소스에 대한 컴플라이언스 산출물 세트를 생성해야 한다.<sub>(3.4.1.1)</sub>

오픈소스 컴플라이언스 산출물은 크게 두 가지로 구분된다.

1. 오픈소스 고지문 : 오픈소스 라이선스 전문과 저작권 정보 제공을 위한 문서
2. 공개할 소스 코드 패키지 : GPL, LGPL 등 소스 코드 공개를 요구하는 오픈소스 라이선스 의무 이행을 위해 공개할 소스 코드를 취합한 패키지

이러한 컴플라이언스 산출물을 취합, 배포, 보관하기 위해 다음 사항을 준수한다.<sub>(3.4.1.2)</sub>

- 오픈소스 고지문이나 공개할 소스 코드 패키지는 각 라이선스가 요구하는 조건대로 취합한다. 예를 들어, 라이선스가 라이선스 전체 텍스트의 동봉을 요구하는데, 링크만을 제공해서는 안 된다. 
- 취합한 산출물은 별도의 저장소에 보관한다. 
- 공개할 소스 코드를 서면 약정서로 제공할 경우, 취합한 산출물의 저장소를 외부에서 접근할 수 있도록 다운로드 링크를 공개한다. 
  
회사의 오픈소스 컴플라이언스 프로세스를 통해 오픈소스 고지문을 발급하고, 공개할 소스 코드 패키지를 취합할 수 있다. 

#### (4) 오픈소스 BOM (Bill of Materials) 생성
배포용 소프트웨어에 포함된 오픈소스 현황(BOM : Bill of Materials)을 생성하고 관리해야 한다.<sub>(3.3.1.2)</sub>

회사의 오픈소스 컴플라이언스 프로세스를 통해 오픈소스 도구를 활용하여 오픈소스 BOM을 생성하고 보존할 수 있다. 

#### (5) 컴플라이언스 이슈 수정 절차

컴플라이언스 이슈가 제기될 경우, 오픈소스 프로그램 매니저는 다음의 절차를 수행하여 신속히 대응한다.<sub>(3.2.2.5)</sub>

1. 문의 접수를 확인하고 적절한 해결 시간을 명시한다.
2. 이슈 내용이 실제 문제를 지적하고 있는지를 확인한다. (아닐 경우, 이슈 제기자에게 문제가 아님을 알린다.)
3. 실제 문제인 경우, 우선순위를 정하고 적절한 대응 방안을 결정한다. 
4. 대응을 수행하고, 필요할 경우, 오픈소스 컴플라이언스 프로세스를 적절하게 보완한다.
5. 위의 내용은 Jira Tracker를 이용하여 보존한다.

### 7. 오픈소스 기여
회사는 오픈소스에서의 비즈니스 가치 창출을 위해 외부 오픈소스 프로젝트로의 참여와 기여를 권장한다. 그러나 이 과정에서 의도하지 않은 회사의 지식 재산 노출 혹은 제 3자의 권리 침해에 주의해야 한다. 이를 위해 회사의 구성원이 외부 오픈소스 프로젝트로의 기여를 위해서는 다음 사항을 준수해야 한다.<sub>(3.5.1.1)</sub>

#### (1) 리뷰 요청 및 승인

오픈소스 기여는 저작권 관점에서 저작자가 저작물을 수정/사용/배포할 수 있는 권한을 오픈소스 프로젝트에 부여하는 것이다. 때에 따라서는 오픈소스 프로젝트에 여러분의 저작권을 양도해야 하기도 한다. 그런데 일반적으로 고용 기간에 만든 저작물의 저작권은 고용주가 소유한다. 즉, 회사 구성원이 만든 저작물은 회사가 소유한다. 구성원이 임의로 저작물을 오픈소스에 기여하는 행위는 불필요한 저작권 침해 이슈를 유발할 수 있다. 

따라서, 기여하고자 하는 오픈소스 프로젝트가 있다면 오픈소스 기여 프로세스에 따라 최초 기여하기 전에 리뷰 요청 및 승인 절차를 준수한다.

단, 다음과 같이 단순한 내용일 경우, 저작권 침해 리스크가 크지 않기 때문에 리뷰 절차 없이 구성원의 판단에 따라 기여할 수 있다. 

- 10 라인 이하의 작은 코드 조각
- Stack Overflow에서의 문의 / 답변
- GitHub에서의 관리 활동 : Issue 생성, Pull Request Review / Approve 등

#### (2) 기여할 권리가 있는 코드만 기여
기여할 권리가 있는 코드만 기여해야 한다. 즉, 직접 작성한 코드를 기여한다. 제 3자의 코드를 임의로 기여해서는 안 된다. 

#### (3) 지식 재산 노출 주의
민감한 정보, 특허 등 회사의 지식재산 노출이 우려되는 코드, 문서는 기여하지 않는다. 

* 기여하려는 코드에 회사의 특허가 포함되어 있다면, 이 특허를 오픈소스 라이선스로 프로젝트에 기여해도 되는지 확인해야 한다. 모호한 부분이 있다면 OSPO에 문의한다. 

#### (4) CLA 서명 주의
어떤 오픈소스 프로젝트는 모든 기여자에게 CLA<sub>Contributor License Agreement</sub>에 서명할 것을 요구한다. 이는 프로젝트가 여러 기여자의 저작물을 관리하면서 발생할 수 있는 저작권 분쟁을 줄이기 위해 기여자들에게 동의를 구하는 약정서이다. 보통 대회사가 주도하는 프로젝트에서 CLA에 서명할 것을 요구한다.

CLA는 프로젝트마다 다르지만 주로 다음 사항을 동의한다는 내용을 담고 있다.

- 나(또는 소속 회사)는 내가 기여하려고 하는 기여물을 프로젝트에 기여할 권리가 있다. (즉, 이 기여물의 저작자이다.)
- 나(또는 소속 회사)는 나의 기여물을 프로젝트가 수정, 배포, 관리할 수 있는 권한을 프로젝트에 부여한다.
- 나(또는 소속 회사)는 부여한 권한을 철회하지 않는다.
- 나(또는 소속 회사)는 프로젝트가 향후 필요에 따라 라이선스를 변경할 수 있는 권한을 프로젝트에 부여한다.

또한, 드문 경우지만, 어떤 CLA는 다음과 같은 조건에 대해서도 동의를 요구한다.

- 나(또는 소속 회사)는 나의 기여물을 기여함과 동시에 나의 저작권을 프로젝트 또는 프로젝트 관리 조직으로 양도한다.

회사는 자사의 지식재산 보호를 위해 저작권 양도를 요구하는 오픈소스 프로젝트로의 기여는 허용하지 않는다. 이러한 판단을 위해 회사의 구성원은 기여하려는 오픈소스 프로젝트에서 CLA 서명을 요구할 경우, 서명하기 전에 반드시 OSPO에 리뷰를 요청한다.

#### (5) 저작권 표시

구성원이 재직 기간에 생성한 저작물의 지식재산은 기본적으로 회사가 소유한다. 따라서, 구성원은 외부 오픈소스 프로젝트에 코드를 기여할 때 회사의 저작권을 표기해야 한다.

하나 이상의 파일을 기여할 때, 다음과 같이 파일 상단에 저작권과 라이선스를 표기한다. 

~~~
Copyright (c) {$year} {$Company}
SPDX-License-Identifier: {$SPDX_license_name}
~~~
여기서 $SPDX_license_name은 해당 오픈소스 프로젝트의 라이선스 정책에 따라 작성한다.

단, 버그 수정 등의 목적으로 기존 코드를 수정하는 정도라면 해당 코드 수정에 대해 저작권을 표기할 필요는 없다. 

#### (6) 회사 이메일 사용
오픈소스 프로젝트에 기여 시 개인 이메일을 사용하지 말고, 회사 이메일을 사용한다. 이를 통해 (1) 구성원은 회사를 대표하여 커뮤니티와 커뮤니케이션한다는 책임감을 갖게 되고, (2) 회사가 오픈소스 커뮤니티에 기여 활동을 활발히 하는 회사로 인지도를 개선할 수 있다.

### 8. 오픈소스 공개

회사는 오픈소스 커뮤니티와의 협업의 가치를 존중하고, 이를 내부 소프트웨어를 오픈소스 프로젝트로의 공개를 장려한다. 하지만, 회사의 지식재산 보호와 의도치 않은 저작권 침해를 방지하기 위해 준수해야 할 몇 가지 규칙이 있다. 

#### (1) 승인
오픈소스 공개는 저작권 관점에서 저작자가 저작물을 누구나 수정/사용/배포할 수 있는 권한을 오픈소스 라이선스를 통해 부여하는 것이다. 일반적으로 고용 기간에 만든 저작물의 저작권은 고용주가 소유한다. 즉, 회사 구성원이 만든 저작물은 회사가 소유한다. 구성원이 임의로 저작물을 오픈소스로 공개하는 행위는 불필요한 저작권 침해 이슈를 유발할 수 있다. 

따라서, 소프트웨어를 오픈소스로 공개하고자 한다면 회사 오픈소스 공개 정책에 따라 리뷰 요청 및 승인 절차를 따른다. 

공개하는 과정에서 어느 것이라도 무언가 바람직하지 않아 보이는 상황이 있다면 주저하지 말고 OSPO에 문의한다.

#### (2) 공개할 권리가 있는 코드만 공개

오픈소스 프로젝트에서 발생할 수 있는 최악의 상황 중 하나는 법적으로 문제가 있는 코드가 프로젝트에 포함되는 것이다. 회사가 배포할 권리가 없는 코드이거나, 다른 회사의 특허와 같은 IP를 침해하는 코드가 법적인 문제를 유발할 수 있다. 따라서, 공개할 코드를 준비하면서 모든 코드의 출처를 확인하고 문제 소지가 있는 코드는 삭제한다.‌ 

#### (3) 지식 재산 노출에 주의
민감한 정보, 특허 등 기업의 지식재산 노출이 우려되는 코드, 문서는 공개하지 않는다.

공개하려는 코드에 회사의 특허가 포함되어 있다면, 이 특허를 오픈소스 라이선스로 공개해도 되는지 확인한다. 모호한 부분이 있다면 OSPO에 문의한다.

#### (4) 유용한 코드 공개
성공적인 프로젝트가 되기 위해서는 다른 사람들에게도 유용해야 한다. 만약, 유사한 프로젝트가 이미 존재한다면, 새로운 프로젝트를 만드는 것보다 기존의 프로젝트에 참여한다. 

공개하려는 오픈소스가 (1) 오픈소스 커뮤니티에 차별화된 가치를 제공하고, (2) 커뮤니티가 해결되지 못했던 문제를 해결하며, (3) 우리의 기술력을 공개함으로 긍정적인 관심을 끌 수 있는 프로젝트가 되기를 기대할 수 있어야 한다. 
* 실제 제품이나 서비스에 사용하지 못한 코드라면 오픈소스로도 공개하지 않는다.
* 오픈소스 커뮤니티에서 이미 해결한 문제를 다루는 코드는 공개하지 않는다. 이런 경우라면, 기존의 오픈소스 프로젝트에 기여한다.

#### (5) 리소스 확보
개발자를 포함해서 프로젝트에 투입해야 할 리소스를 확보한다.‌

* 초기에는 일반적인 사내 프로젝트와 비슷한 수준의 개발자가 필요하다.
* 외부의 기여를 신속하게 리뷰 할 수 있는 개발자가 필요하다.
* 법무팀, 마케팅팀의 역할도 필요하다.
* 프로젝트를 유지, 관리하는데 요구되는 인프라에 대한 예산을 확보한다. 여기에는 Github와 같은 프로젝트 호스팅을 위한 도구가 포함된다.

충분한 리소스가 지원되는 환경을 조성할 수 없다면, 오픈소스로 공개하지 않는다.

#### (6) 회사 이메일 사용
오픈소스 공개 활동 시 개인 이메일을 사용하지 말고, 회사 이메일을 사용한다. 이를 통해 (1) 구성원은 회사를 대표하여 커뮤니티와 커뮤니케이션한다는 책임감을 갖게 되고, (2) 회사가 오픈소스 커뮤니티에 공개 활동을 활발히 하는 기업으로 인지도를 개선할 수 있다.

### 9. 외부 문의 대응

#### (1) 외부 문의 대응책임
외부로부터 오픈소스 컴플라이언스에 대한 문의 및 요청에 대한 대응은 오픈소스 프로그램 매니저가 담당한다.<sub>(3.2.1.2)</sub>

* 오픈소스 프로그램 매니저는 회사 내의 적절한 인원에게 문의에 대한 전체 또는 일부의 처리를 할당할 수 있다. 필요할 경우 법률 담당에게 문의하여 처리한다.
* 외부로부터 오픈소스 컴플라이언스에 대한 문의를 받은 사람은 누구나 이를 오픈소스 프로그램 매니저에게 알려서 신속한 대응이 될 수 있게 한다. 

#### (2) 연락처 공개
오픈소스 프로그램 매니저는 외부에서 오픈소스 관련한 문의 및 요청을 할 수 있도록 담당자의 연락처를 공개적으로 제공한다.<sub>(3.2.1.1)</sub>

* 오픈소스 고지문에 연락받을 수 있는 이메일 주소 정보를 제공한다. 
* Linux Foundation의 Open Compliance Directory에 연락처를 등록한다.

#### (3) 외부 문의 대응 절차
외부로부터의 오픈소스 컴플라이언스 문의에 신속하고 정확하게 대응한다면 소송까지 진행되는 위험을 크게 줄일 수 있다. 이를 위해 회사는 외부의 오픈소스 컴플라이언스 문의에 대응하기 위해 회사의 오픈소스 컴플라이언스 프로세스에서 정의한 외부 문의 대응 절차를 준수한다.<sub>(3.2.1.2)</sub> 

### 10. OpenChain
회사는 소프트웨어 공급망에서의 오픈소스 컴플라이언스 수준 향상을 위해 Linux Foundation의 OpenChain 프로젝트의 정신을 지지하며 적극적으로 참여한다. 

- 회사는 이 오픈소스 정책을 적용하여 2021년 10월 1일부로 ISO/IEC 5230:2020을 준수함을 보장한다.<sub>(3.6.1.1)</sub>
- 회사는 적합성 인증을 획득한 후 18개월 이상 OpenChain 규격 버전 2.1, ISO/IED 5230:2020의 모든 요구사항을 충족함을 보장한다.<sub>(3.6.2.1)</sub>
- 회사는 최소 18개월 간격으로 적합성을 검토하고 필요에 따라 정책을 변경 및 갱신한다. 


### Appendix 1. 담당자 현황

| No | 역할 | 책임 | 필요 역량 | 담당 조직 | 담당자 | 
|---|:---|:---|:---|:---|:---|
| 1 | 오픈소스 프로그램 매니저 | 회사의 오픈소스 프로그램에 대한 총괄 책임을 담당한다. | 1. 소프트웨어 개발 프로세스 이해<br>2. 저작권, 특허 등 오픈소스 라이선스와 관련한 지식재산 이해<br>3. 오픈소스 컴플라이언스에 대한 전문 지식<br>4. 오픈소스 개발 경험<br>5. 커뮤니케이션 스킬  | CTO | OOO |
| 2 | 법무 담당 | 오픈소스 라이선스와 의무를 해석한다. 이러한 의무를 실제 이행하는 등 오픈소스 활용을 위해 발생할 수 있는 법적 위험의 완화를 위한 자문을 제공한다. | 1. 오픈소스 생태계에 대한 기본 지식<br>2. 소프트웨어 저작권에 대한 전문 지식<br>3. 오픈소스 라이선스에 대한 전문 지식 | 법무팀 | OOO | 
| 3 | 인프라 담당 | 오픈소스 분석 도구를 운영하고 자동화하여 모든 배포용 소프트웨어에 대해 라이선스 분석이 원활히 수행되도록 시스템을 구축한다. | 1. 오픈소스 컴플라이언스 프로세스에 기본 지식<br>2. 오픈소스 라이선스 분석 도구에 대한 이해<br>3. IT 인프라에 대한 전문 지식 | IT 인프라팀 | OOO | 
| 4 | 보안 담당 | 오픈소스 보안취약점 분석 도구를 운영하여 모든 배포용 소프트웨어에 대해 보안취약점 분석이 원활히 수행되도록 시스템을 구축한다. | 1. 오픈소스 컴플라이언스 프로세스에 기본 지식<br>2. 오픈소스 라이선스 분석 도구에 대한 이해<br>3. 보안에 대한 전문 지식 | 보안팀 | OOO | 
| 5 | 개발 문화 담당 | 사내 개발자들이 오픈소스를 적극적으로 활용하고 사내외 커뮤니티에 참여하여 선진 개발 문화를 습득할 수 있도록 지원한다.  | 1. 소프트웨어 개발 프로세스 이해<br>2. 오픈소스 컴플라이언스에 대한 기본 지식<br>3. 오픈소스 정책에 대한 이해 | DR | OOO | 
| 6 | 개발팀 | 소프트웨어 개발/배포 조직은 올바른 오픈소스 활용을 위해 오픈소스 정책 및 프로세스를 준수한다.  | 1. 소프트웨어 개발 프로세스 이해<br>2. 오픈소스 컴플라이언스에 대한 기본 지식<br>3. 오픈소스 정책에 대한 이해<br>4. 오픈소스 라이선스에 대한 기본 지식 | 개발팀 | 전원 | 




## 부록 2. 샘플 오픈소스 컴플라이언스 프로세스

OOO 주식회사(이하 "회사"라 함)는 소프트웨어를 포함하는 제품과 서비스를 개발하면서 오픈소스 소프트웨어(이하 "오픈소스"라 함)를 적극적으로 활용한다. 회사는 소프트웨어를 배포하면서 오픈소스 라이선스가 부과하는 의무사항을 준수하기 위한 활동을 수행해야 하며 이를 오픈소스 컴플라이언스라고 한다. 

### 1. 소프트웨어 제품 개발/배포를 위한 프로세스

오픈소스 컴플라이언스 프로세스는 회사가 소프트웨어 제품 및 서비스를 개발하고 배포하기 위한 각 개발 단계에 맞게 오픈소스 라이선스 의무 준수를 위해 수행해야 할 절차를 정의한다. 소프트웨어 제품 개발/배포에 관여하는 모든 구성원은 다음의 오픈소스 컴플라이언스 프로세스 10단계를 준수한다.

{{< imgproc general-osc-process Fit "1200x1200" >}}
{{< /imgproc >}}

#### 1. 오픈소스 식별<sub>Identification of Open Source</sub>
개발 부서는 소프트웨어 설계 단계에서 다음 사항을 준수한다.

- 소프트웨어를 설계하면서 예측 가능한 오픈소스 사용 현황을 파악하고 라이선스를 확인한다.
- 오픈소스 라이선스별 의무 사항을 확인한다. 라이선스별 의무 사항은 회사의 오픈소스 라이선스 가이드에서 확인할 수 있다. 
- 각 오픈소스 라이선스의 소스 코드 공개 범위를 고려하여 소프트웨어를 설계한다. 

오픈소스 프로그램 매니저는 주요 오픈소스 라이선스 의무, 제한, 권리에 대한 가이드를 작성하고 공개하여 전사의 개발 부서에서 참고하게 한다. 

개발 부서는 회사 규칙에 맞게 소스 코드에 저작권 및 라이선스를 표기한다. 회사의 소스 코드 내 저작권 및 라이선스 표기 규칙은 다음 페이지에서 확인할 수 있다. : (insert_link)

개발 부서는 새로운 오픈소스 도입 검토 시, 먼저 라이선스를 식별한다. 회사의 오픈소스 라이선스 가이드에 따라 라이선스 의무, 제한 및 권리를 확인한다. 회사의 오픈소스 라이선스 가이드에서 설명하지 않는 라이선스일 경우, 오픈소스 프로그램 매니저에게 도입 가능 여부 및 주의 사항을 문의한다. Jira Ticket을 생성하여 문의한다. 

오픈소스 프로그램 매니저는 오픈소스 라이선스 의무를 분석하여 소프트웨어 개발 조직에 안내한다.

- 의문이 있는 경우, 법무 담당에 자문을 요청하여 명확한 가이드를 제공한다. 
- 새롭게 분석한 라이선스 정보는 전사 라이선스 가이드에 반영한다. 

#### 2. 소스 코드 검사<sub>Auditing Source Code</sub>

개발 부서는 인프라 담당의 안내에 따라 소스 코드를 제공하여 오픈소스 점검을 요청한다. 

인프라 담당은 오픈소스 분석 도구를 사용하여 오픈소스 점검을 하고, 오픈소스 BOM을 생성한다. 

오픈소스 프로그램 매니저는 오픈소스 라이선스 의무 준수 가능 여부, 오픈소스 라이선스 충돌 여부를 검토하고, 이슈가 있으면, 개발 부서에 해결을 요청한다. 이슈 사항은 Jira Ticket으로 생성하여 개발 부서에 할당한다. 

#### 3. 문제 해결<sub>Resolving Issues</sub>

개발 부서는 소스 코드 검사 단계에서 발견된 모든 문제를 해결한다. 이슈가 된 오픈소스를 제거하거나, 다른 라이선스 하의 오픈소스로 교체하는 등 조치를 한다. 

개발 부서는 발견된 모든 이슈를 해결하면 Jira Ticket 이슈를 Resolve하고, 재검토를 요청한다. 

#### 4. 검토<sub>Reviews</sub>

오픈소스 프로그램 매니저는 모든 이슈가 적절하게 보완되었는지를 검토한다. 필요할 경우, 오픈소스 분석 도구를 사용하여 소스 코드 검사를 재수행한다. 

#### 5. 승인<sub>Approval</sub>

오픈소스 프로그램 매니저는 오픈소스 컴플라이언스 절차가 적절하게 수행되었는지를 최종 승인 혹은 거절한다. 거절 시에는 이유에 대한 설명과 수정 방법을 개발 부서에 제안한다. 

#### 6. 등록<sub>Registration</sub>

오픈소스 프로그램 매니저는 소프트웨어의 버전별 오픈소스 사용 목록을 추적하기 위한 BOM을 확정한다.

인프라 담당은 확정된 BOM을 시스템에 등록한다. BOM에는 배포용 소프트웨어에 포함된 오픈소스 목록과 다음과 같은 정보를 포함한다. 

- 배포용 소프트웨어의 제품(혹은 서비스) 이름과 버전
- 오픈소스 목록
  - 오픈소스 이름 / 버전
  - 오픈소스 라이선스


#### 7. 고지<sub>Notices</sub>

오픈소스 프로그램 매니저는 고지 의무를 준수하기 위한 오픈소스 고지문을 생성한다. 오픈소스 고지문에는 다음 사항을 포함한다. 

- 오픈소스 관련 문의할 수 있는 오픈소스 연락처
- 오픈소스별 고지 내용
  - 저작권 
  - 오픈소스 라이선스 이름
  - 오픈소스 라이선스 사본
  - (해당하는 경우) 소스 코드 사본을 얻을 수 있는 서면 약정 (Written Offer)

오픈소스 프로그램 매니저는 오픈소스 고지문을 생성하여 개발 부서에 전달한다. 이때 소스 코드 공개가 필요할 경우 개발 부서에 공개할 소스 코드 취합 방법을 안내한다. 

개발 부서는 오픈소스 고지문을 제품 배포 시 동봉한다. 화면이 있는 제품일 경우, 사용자가 메뉴를 통해 확인할 수 있도록 조치한다.  (예: 앱 > 메뉴 > 설정 > 저작권 정보 > 오픈소스 라이선스)

개발 부서는 GPL, LGPL 등 소스 코드 공개를 요구하는 라이선스 하의 오픈소스를 사용하였을 경우, 이에 대한 소스 코드 공개 범위를 확인하여 공개할 소스 코드를 취합한다. 

- GPL, LGPL 등의 라이선스 의무 준수를 위해 취합한 소스 코드는 제품에 탑재된 바이너리를 구성하는 소스 코드와 일치해야 한다. 즉, 취합한 소스 코드를 빌드하면 제품에 탑재된 바이너리와 동일해야 한다. 

#### 8. 배포 전 확인<sub>Pre-Distribution Verifications</sub>

개발 부서는 오픈소스 컴플라이언스 활동이 적절히 수행되었음을 입증하는 다음의 산출물을 제출한다. 

1. 제품에 포함한 최종 오픈소스 고지문
2. 제품에 오픈소스 고지문이 포함되었음을 확인하는 자료 (예: 오픈소스 고지문을 보여주는 화면 캡처 이미지)
3. (해당할 경우) 공개할 소스 코드 (하나의 파일로 압축하여 제출)

오픈소스 프로그램 매니저는 개발 부서가 제출한 자료를 검토하여 이상 여부를 확인한다. 

#### 9. 배포<sub>Distribution</sub>

오픈소스 프로그램 매니저는 개발 부서가 제출한 컴플라이언스 산출물을 인프라 담당에 제출한다.

인프라 담당은 컴플라이언스 산출물을 회사의 오픈소스 배포 사이트에 등록한다. 

#### 10. 최종 확인 (Final Verifications)

오픈소스 프로그램 매니저는 컴플라이언스 산출물이 이상 없이 회사의 오픈소스 포털에 등록이 되었는지, 외부에서 이상 없이 다운로드가 되는지 등 종합적인 확인을 한다. 

### 2. 외부 문의 대응 프로세스
외부로부터의 오픈소스 컴플라이언스 문의에 신속하고 정확하게 대응한다면 소송까지 진행되는 위험을 크게 줄일 수 있다. 이를 위해 기업은 외부의 오픈소스 컴플라이언스 문의에 대응하기 위해 다음과 같은 프로세스를 준수한다.

{{< imgproc general-inquiry-process Fit "1200x900" >}}
{{< /imgproc >}}

#### 1. 접수 알림<sub>Acknowledge</sub>
오픈소스 프로그램 매니저는 문의를 받은 즉시 요청자에게 문의가 접수되었음을 알린다. 이때 조치 예정일을 함께 알린다. 요청자의 의도가 무엇인지 정확히 파악하는 것이 중요하기 때문에 문의가 불명확한 경우 추가 설명을 요청한다.

대응이 필요한 문의 및 요청의 주요 내용은 아래와 같다. 

- 특정 제품 및 서비스에 오픈소스가 사용되었는지 문의
- 서면 약정(Written Offer)에 언급된 GPL, LGPL 라이선스 하의 소스 코드 제공 요청
- 오픈소스 고지문에 명시되지 않았지만, 제품에서 발견된 오픈소스에 대한 해명 및 소스 코드 공개 요청
- GPL, LGPL 등의 의무로 공개된 소스 코드에 누락된 파일 및 빌드 방법 제공 요청
- 저작권 표시 요청

오픈소스 프로그램 매니저는 접수한 요청에 대한 Jira Issue를 생성하여 대응 상황을 모두 자세히 기록한다.

#### 2. 조사 알림<sub>Inform</sub>

오픈소스 프로그램 매니저는 요청자에게 오픈소스 컴플라이언스를 충실히 수행하고 있음과 요청자의 문의를 조사하고 있음을 알린다. 내부 조사 진행 상황이 업데이트될 때마다 알리는 것이 좋다.

#### 3. 내부 조사<sub>Investigate</sub>

오픈소스 프로그램 매니저는 요청 사항에 대한 내부 조사를 진행한다. 문제가 된 제품의 버전에 대하여 컴플라이언스 프로세스가 적절하게 수행되었는지 BOM 및 문서화된 검토 이력을 통해 확인한다. 필요 시 법무 담당에 자문을 요청한다. 

특정 개발 부서에서 확인이 필요한 사항일 경우 오픈소스 프로그램 매니저는 개발 부서에 조사를 요청한다. 조사를 요청받은 개발 부서는 컴플라이언스 산출물에 문제가 있는지 즉시 확인하고 결과를 오픈소스 프로그램 매니저에게 보고한다. 

#### 4. 요청자에게 보고<sub>Report</sub>

요픈소스 컴플라이언스 담당은 조치 예정일 내에 내부 조사를 마치고, 요청자에게 결과를 알린다.

- 요청자의 문의가 오해로 인한 잘못된 지적이었다면 추가 조치 없이 요청자에게 이를 알리고 처리를 종료한다.
- 문제가 맞는다면 요청자에게 해당 오픈소스 라이선스의 의무를 이행하기 위한 정확한 방법과 시기를 알린다.

#### 5. 문제 보완 / 알림<sub>Rectify</sub>

내부조사에서 실제 컴플라이언스 문제가 발견되면 해당 개발 부서는 컴플라이언스 문제를 해결하는 데 필요한 모든 절차를 수행한다.

#### 6. 문제 해결 알림<sub>Report</sub>

문제를 해결한 후에는 즉시 요청자에게 알리고 문제가 해결되었음을 확인할 수 있는 최선의 방법을 제공한다.

#### 7. 프로세스 개선<sub>Improve</sub>

컴플라이언스 문제가 있었던 경우, OSRB 미팅을 통해 사례를 검토하고, 문제가 발생한 경위를 파악하여, 문제가 재발하지 않을 수 있도록 프로세스를 개선한다.

## 부록 3. 오픈소스 도구

오픈소스 컴플라이언스 활동을 위해서는 정책, 프로세스나 교육자료뿐만 아니라 소스 코드 스캔, Dependency 분석, 오픈소스 BOM 관리 등을 위한 다양한 도구와 시스템도 요구된다. 그 때문에 다수의 기업이 이러한 도구와 시스템을 도입하고 활용하는 데 많은 리소스를 투입하고 있다. 특히 오픈소스 컴플라이언스를 처음 시작하는 기업은 프로세스뿐 아니라 비용 측면에서도 어려움을 겪고 있다.

이런 어려움을 해결하는 데, 2019년 6월, OpenChain 프로젝트에 참여하고 있는 지멘스, 보쉬, 도시바, 후지쓰, 히타치 등의 오픈소스 컴플라이언스 도구 전문가들을 주축으로 [Open Source Tooling Group](https://github.com/Open-Source-Compliance/Sharing-creates-value)[^toolinggroup]이 시작되었다.

[^toolinggroup]: Open Source Tooling Group - https://github.com/Open-Source-Compliance/Sharing-creates-value


Open Source Tooling Group은 여러 기업의 오픈소스 전문가들이 이슈를 함께 해결하고 결과물을 공유해 오픈소스 컴플라이언스 비용을 절감하고 양질의 컴플라이언스 결과물을 만들어 내기 위해 구성되었다.

구체적으로는 FOSSology, SW360, ORT, Software Heritage, ClearlyDefined, SPDX 등의 기존 오픈소스 프로젝트를 활용하여 통합(turn-key) 오픈소스 툴 체인을 만들고, 모든 기업이 이를 자유롭게 사용할 수 있도록 하는 것을 목표로 삼고 있다. 

여기서는 FOSSology와 SW360에 대해 소개 및 간단한 사용 방법에 관해 알아본다.

### 1. FOSSology

오픈소스 컴플라이언스를 위해 소프트웨어 내에 포함된 오픈소스와 라이선스 정보를 검출하기 위해 소스 코드 스캔 도구를 사용할 수 있다. 

{{< imgproc fossology1 Fit "900x600" >}}
<center>< https://www.fossology.org/ ></center>
{{< /imgproc >}}

Linux Foundation의 FOSSology 프로젝트는 이러한 스캔 도구를 개발하고 오픈소스로 공개해 누구나 자유롭게 사용할 수 있게 한 도구이다.

#### 주요 특징

FOSSology는 웹기반의 프로그램으로 사용자는 웹사이트에 로그인하여 개별 파일 혹은 소프트웨어 패키지를 업로드할 수 있다. FOSSology는 업로드된 파일 내에 라이선스 텍스트와 Copyright 정보를 검출한다. 개발자는 사용하고자 하는 오픈소스의 라이선스가 무엇인지, Copyright은 어떻게 되는지에 대한 정보를 확인하고자 할 때 FOSSology를 이용하는 것이 좋다. FOSSology는 개발자가 업로드한 오픈소스 패키지 내의 모든 파일을 스캔하여 각 파일 내 라이선스 관련 텍스트와 Copyright 정보를 자동으로 검출하고, 이를 리포트로 생성한다. FOSSology 주요 특징에 대한 자세한 내용은 다음 페이지를 참고할 수 있다. : [https://www.fossology.org/features/](https://www.fossology.org/features/)

#### 설치

기업 내에서 FOSSology를 사용하기 위해서는 사내에 FOSSology 서버를 구축해야 한다. 이를 위해 리눅스 기반의 서버 시스템에 FOSSology를 설치해야 한다. FOSSology는 다음 세 가지 방법으로 설치할 수 있다.

1. Docker 사용
2. Vagrant와 VirtualBox 사용 
3. Source build하여 설치

여기서는 가장 간편한 방법인 Docker를 사용하는 방법에 관해 설명한다.

FOSSology는 컨테이너화된 Docker 이미지를 Docker Hub를 통해 공개하고 있다. : [https://hub.docker.com/r/fossology/fossology](https://hub.docker.com/r/fossology/fossology)

Pre-built 된 Docker 이미지는 다음 명령어를 사용하여 실행할 수 있다.

```text
$ docker run -p 8081:80 fossology/fossology
```

Docker 이미지는 다음 URL과 계정 정보로 사용할 수 있다. : http://\[IP\_OF\_DOCKER\_HOST\]:8081/repo

* Username : fossy
* Passwd : fossy

설치와 관련한 자세한 내용은 다음 페이지를 참고하라. : [https://github.com/fossology/fossology/blob/master/README.md](https://github.com/fossology/fossology/blob/master/README.md)

#### 테스트 서버

FOSSology를 설치할 수 있는 시스템 구축이 곤란한 상황이라면, FOSSology Project에서 제공하는 테스트 서버를 이용할 수 있다. FOSSology 프로젝트에서는 테스트를 위한 환경을 제공한다. (테스트 서버는 예고없이 중단될 수 있다.) 

사용자는 다음 계정으로 FOSSology 테스트 서버에 접속하여 FOSSology 기능을 시험해볼 수 있다.

{{< alert  >}}
테스트 서버 URL: [https://fossology.osuosl.org/](https://fossology.osuosl.org/)

* Username: fossy
* Password: fossy
{{< /alert  >}}

![](../fossology2.png)

#### Basic Workflow

FOSSology의 기본 사용 절차는 다음과 같다. 

* 사용하고자 하는 오픈소스의 라이선스와 Copyright 정보를 확인하기 위해 오픈소스의 소스 코드를 하나의 파일로 압축하여 FOSSology에 업로드한다. 
* 이를 위해 메뉴 &gt; Upload &gt; From File을 선택한다. 

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/Oywr9jqM09g1SfxfZ-2HERmYA_8)

* 업로드할 파일을 선택하고 Upload 버튼을 클릭한다. 
* 업로드가 완료되면 Job Agent에 의해 자동으로 분석을 수행한다. 
* 메뉴 &gt; Jobs &gt; My Recent Jobs에서 분석 중인 Status를 확인할 수 있다. 

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/9IKts-8lH7YK_Dat124-hEw_q4I)

* 분석이 완료되면 메뉴 &gt; Browse에서 분석 결과를 확인할 수 있다.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/C62vBvaVNeBLAqrRrx-XKoeuMhg)

* 개별 파일을 선택하면 FOSSology가 검출한 라이선스 관련 텍스트가 무엇인지 확인할 수 있다.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/9idwgtBqNj7YAl7Wg0i98QJ5b4w)

* 메뉴 &gt; Browser &gt; 파일 혹은 디렉터리를 선택 &gt;  Copyright/Email/Url/Author에서는 FOSSology가 검출한 Copyright/Email/Url/Author 정보를 보여다.

![](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/NrjeCqal75rJ1bwGLPPmjhBEn4Q)

사용자는 FOSSology는 이렇게 분석한 결과가 유효한지 여부에 관해 확인 후 잘못 검출된 항목에 대해서는 분석 결과에서 제외하는 작업을 할 수 있다. FOSSology는 이를 Clearing 과정이라고 설명하며, 자세한 사항은 다음 페이지를 참고할 수 있다. : [https://www.fossology.org/get-started/basic-workflow/](https://www.fossology.org/get-started/basic-workflow/)

위와 같은 방법으로 사용하고자 하는 오픈소스의 라이선스는 무엇인지, Copyright 정보는 어떻게 되는지를 간단히 확인할 수 있다.


### 2. SW360

오픈소스를 포함하는 제품을 개발하고 배포하는 기업이라면 각 제품과 릴리스 버전마다 사용한 오픈소스의 버전, 라이선스 등의 정보를 수집하고 추적해야 한다. 이를 통해 기업은 올바른 오픈소스 컴플라이언스 활동을 수행할 수 있다.

특히, [NVD](https://nvd.nist.gov/vuln)[^nvd]<sub>National Vulnerability Database</sub>에서 특정 오픈소스 버전에 보안 취약점이 보고 되었을 때, 해당 버전을 사용하고 있는 제품이 무엇인지 추적을 할 수 없다면, 그 기업은 어느 제품에 보안 패치를 적용해야 할지 알 수 없는 상황에 처하게 되고, 그 기업의 제품들은 보안취약점에 그대로 노출이 될 수밖에 없다.

[^nvd]: NVD : NATIONAL VULNERABILITY DATABASE - https://nvd.nist.gov/vuln

이렇듯, 오픈소스 정보를 추적하는 활동은 꼭 필요하다. 기업들은 이를 위해 자체 시스템을 구축하거나, 상용 서비스를 구매하여 사용하기도 한다. SW360은 Eclipse 재단에서 후원하는 오픈소스로서 소프트웨어 BOM에 대한 정보를 수집 및 추적하기 위한 웹 애플리케이션 및 저장소를 제공한다.

{{< imgproc sw3601 Fit "900x600" >}}
<center>< https://www.eclipse.org/sw360/ ></center>
{{< /imgproc >}}

#### 주요 특징

SW360은 웹 기반의 UI를 제공하며 주요 기능은 다음과 같다.

* 제품에 사용된 컴포넌트 추적
* 보안 취약점 평가
* 라이선스 의무 관리
* 고지문 등 법적 문서 생성

![https://www.eclipse.org/sw360/](https://lh3.googleusercontent.com/MPrOy70nOVSCRiorql9Momzi18lG66Liqttyutjwc9LAhVUwqmVf8xyeEkg085Pm1OYxwPRzyh68Th93ZlKA3fjG5_PnsBQijwUGkRa7o72h8Jco_7BcIwfoR7FGu8hsZA8n5ASq)

#### 설치

SW360은 다음과 같이 구성된다. 

* Frontend : Liferay-(Tomcat-)based portal application
* Backend : Tomcat-based thrift service
* Database : CouchDB

Project 구조와 설치를 위해 요구되는 소프트웨어 등 자세한 내용은 README의 Required software 부분에서 확인할 수 있다. : [https://github.com/eclipse/sw360/blob/master/README.md](https://github.com/eclipse/sw360/blob/master/README.md)

SW360은 다음 세 가지의 설치 방법을 제공한다. 사용자는 이 중 하나를 선택하여 설치할 수 있다. 

1. Vagrant 기반 설치 : Vagrant는 가상화 인스턴스를 관리하는 도구로서 sw360vagrant에서는 SW360을 한 번에 Deploy 하기 위한 환경을 제공한다. : [https://github.com/sw360/sw360vagrant](https://github.com/sw360/sw360vagrant)
2. SW360의 구성요소를 개별적으로 설치할 수 있다. : [https://github.com/eclipse/sw360](https://github.com/eclipse/sw360)
3. Docker를 통해 Deploy 할 수 있다. : [https://github.com/sw360/sw360chores](https://github.com/sw360/sw360chores)

여기서는 CentOS 7.6 시스템에 Vagrant 기반으로 설치하여 Deploy하는 방법을 소개한다. 자세한 사항은 README를 참고한다. : [https://github.com/sw360/sw360vagrant/blob/master/README.md](https://github.com/sw360/sw360vagrant/blob/master/README.md) 

##### 1) 사전 설치

vagrant box에 SW360을 설치하기 위해서는 openjdk, VirtualBox 및 Vagrant를 설치해야 다. 먼저 openjdk 1.8.0을 설치한다.

```text
$ yum install java-1.8.0-openjdk
$ java -version
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-b12)”
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

VirtualBox를 설치한다.

```text
$ sudo wget https://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo -P /etc/yum.repos.d
$ sudo yum install VirtualBox-5.2
```

CentOS 7에서 VirtualBox 설치 시, “kernel module is not loaded’ 에러가 발생할 경우, kernel-devel을 설치하여 해결한 후 VirtualBox를 재설치한다. 

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

Vagrant와 vagrant-aws plugin을 설치한다.

```text
$ sudo yum install https://releases.hashicorp.com/vagrant/2.2.6/vagrant_2.2.6_x86_64.rpm 
# vagrant-aws plugin 설치
$ vagrant plugin install vagrant-aws
```

그리고, sw360vagrant 코드를 Clone 한다. 

```text
$ git clone https://github.com/sw360/sw360vagrant.git
```

##### 2) Dependency 다운로드

Vagrant box를 빌드하는 시간을 줄이기 위해 Dependency Package들을 미리 다운로드 받는다. 

```text
$ cd sw360vagrant
$ ./download-packages.sh
```

그러면 다음의 package들이 ./shared/package 폴더 안에 다운로드 된다.

* Liferay 7.2.1 CE GA2 with Tomcat (9.0.17)
* Postgresql-42.2.9 ODBC client for Java as \*.jar file
* SW 360에서 필요한 11개의 \*.jar 파일
* Thrift 0.11
* A box images from the Ubuntu 16.04 LTS (xenial-server-cloudimg-amd64-vagrant.box)

##### 3) Base box 생성

이제 다음 명령어로 Base box를 생성한다.

```text
$ cd generate-box
$ ./generate_box.sh
```

이 작업은 수십 분 소요될 수 있다. 

##### 4) Box 실행

다음 명령어로 Box를 실행한다. 

```text
# If you have built a vagrant box from this directory earlier, you will have to destroy it first via
$ vagrant destroy
$ cd ../sw360-single
$ vagrant up
```

Box를 실행하면 liferay, postgresql 및 couchdb가 구성된다. 이상 없이 실행이 될 경우, [https://localhost:8443/](https://localhost:8443/) 로 Liferay 화면에 접근할 수 있다.

![](https://lh6.googleusercontent.com/leof_ntxQlxjDeD91E7ZfwWY0ftUlD0D_L58AkeNJb_bEFFzKvuL28yzb4iIA6-bAuSfQydo-gVBlnn5EVGGBKcPh0-6Y7p2Qbar74qpB4uwa_nibrV535NJwEIpWXZPFeNUSRd-)

##### 5) SW360 Layout Deploy

마지막 단계는 Liferay에서 SW360의 Layout을 Deploy하는 것이다. 이 작업은 아직 자동화가 되지 않아 관리자가 수동으로 수행해야 다. [https://localhost:8443/](https://localhost:8443/)에 접근하여 다음 계정으로 로그인한다. 

* id : [setup@sw360.org](mailto:setup@sw360.org)
* pw : sw360fossy

이후에는 다음 사이트의 안내에 따라 Layout deploy를 수행한다. [https://github.com/eclipse/sw360/wiki/Deploy-Liferay7](https://github.com/eclipse/sw360/wiki/Deploy-Liferay7)

Deploy가 완료되면 다음과 같은 화면을 볼 수 있다. 

![](https://lh5.googleusercontent.com/INu1-WWi1-SA9P61IMNlgZhugTXbiwbSKUOu2eWq_d5sIIp8NfqxQntwId41ZDmTG6_5Ope8GdU1J2S0adaJDolM09dtfkwIbOE2gTDC4MZXMxhX9kN28E4Yj8a3deBUHBL7yCqj)

#### Basic Workflow

##### 1) License 등록

SW360을 처음 설치하면 먼저 자주 사용하는 오픈소스 라이선스 들을 등록해야 한다. 라이선스 다음과 같은 정보를 포함한다. 

* Full Name
* Short Name
* License Type
* GPL-2.0 Compatibility (예: yes, no)
* License Text

메뉴 &gt; Licenses &gt; Add License를 선택하면 다음과 같이 Create License 화면으로 진입한다. 

![](https://lh6.googleusercontent.com/8bn6z_39PK5WrjP7mzhHrTwfM5PU19QT3TiQnAatOYywVwcGLJGFMmMgMkzh4CKAPM0SOOy7VDoboaj9OKpD1QEZv6KWOeWxZfqGA_2geYrYOBm2kOVzrNOmGPVK-8hzJvBZ-klT)

이와 같이 라이선스를 하나씩 수동으로 등록하는 일은 상당히 수고스러울 수 있는데, 다행히 SW360은 SPDX License List를 한 번에 Import 하는 기능을 제공한다. 메뉴 &gt; Admin &lt; Import SPDX Information을 클릭한다.  

![](https://lh5.googleusercontent.com/d8ZK-dD34z1yKZn-szPNrN7iT4zg1EQnKnAv4QcPslSR0-laETy37ArojuweqSsxpWuvGXtdF5FabiWk57So-bD_iiEx7eVIR6tWDsYO2SkaCdlKr6ELDN9y_NdkqWFbQgRF2lXN)

그러면, 곧 SPDX License List가 자동으로 등록됩니다. 메뉴 &gt; Licenses에서 338개의 License가 등록된 것을 확인할 수 있다. 

![](https://lh6.googleusercontent.com/Ucjuo09uJKhEhACZ90y98PszgSiCGtlDotH8mbTXJ2ePnF3TquzNX2yWzOCENTKNk1UjMJhyFgHxTCH6lxvZJg1l07M0hCc-v-14loAJ0efUU9V9hqS9mUabAT9QNysYL8E2tgIf)

##### 2) Component 및 Release 등록

SW360에서 Component는 하나의 소프트웨어 단위이다. 여기에는 다양한 형태의 소프트웨어가 해당할 수 있으며, 그 예는 다음과 같다. 

* 오픈소스 소프트웨어
* 라이브러리
* 3rd party 소프트웨어

Component는 다음과 같은 정보를 포함한다.  

* Component Name
* Main Licenses
* Categories (예: Library, Cloud, Mobile, ...)
* Component Type (예: OSS, Internal, InnerSource, Service, Freeware)
* Default Vendor
* Homepage URL

Release는 Component에서 하나의 Version을 가리키는 단위이다. 따라서 하나의 Component는 여러 개의 Release를 가질 수 있다. Release는 하나의 Component 하위에 생성되어 관리된다. 

Release는 다음과 같은 정보들을 포함한다. 

* Component Name
* Version
* License
* Download URL
* CPE ID (예: cpe:2.3:a:apache:maven:3.0.4)

예를 들어, zlib-1.2.8을 등록해야 한다면, 먼저 Component에 zlib을 먼저 등록한 후, Release에 zlib 1.2.8을 등록한다. Menu &gt; Components &gt; Add Component를 선택하면 Create Component 화면으로 진입하여 zlib에 대한 정보를 등록할 수 있다. 

![](https://lh6.googleusercontent.com/0a3ecmmFzumTZTaoWCOZPKkQIZLJwbPoAaduCTfwQMH_N67DPaMpTkerA4LOynwkl_nLkNT-pRh-rKzj4XHtBjoTkVMW9g06Rywryk3wbAj-Y3ONDg16VcGepMEm7m7Y8M3iDWyH)

Component를 생성하면, Components &gt; Releases &gt; Add Release에서 zlib-1.2.8 version에 대한 정보를 등록할 수 있다. 

![](https://lh4.googleusercontent.com/ynUEB5-rGVYDirFghLx2v3tUt-uh-WL3YTN0siaGZWBrWQKYnIiV3B04mvdv3nZUW7t_U2Gl8msV_es1X181uq95YAp1bnqa0e3QLshhd1zhqk6z8ubPeEfo74cKdwho95_NyI1J)

하나의 zlib이라는 Component에 1.2.8과 1.2.11 version을 각각의 Release로 등록하였을 때, Release Overview 화면에서 다음과 같이 2개의 Release가 존재하는 것을 볼 수 있다. 

![](https://lh3.googleusercontent.com/GxgMJQbNjRBNxMTMBvqEXNFNElXGXoCnaksCMs46ydREIrqrj7dFxMK0YkvjviHYMCiHY07xlR-Xixpa_C5nMFLzih0dXZAtv-6yKg4RdADJxr5qmDwhAEopVOaVNqzVWc3gMpLq)

SW360은 다수의 Component 정보를 Import 시키기 위한 기능을 제공한다. 메뉴 &gt; Admin &gt; Import / Export에 CSV template에 등록을 원하는 Component 정보를 입력 후 Import 할 수 있다. 

![](https://lh5.googleusercontent.com/VInFwWAV-1lG1E7zFQPvn1GIlYPPY5ToGbSa49Brg7XuB-AwyCEHA9han0EUij1KX3c8aN2UZ1mKkN-5Y4BNv8LOV3O5YoypLQ7EF43QFPAU9L18XT57Ec5eoneswtGtt3rMSPoQ)

단, 이 기능은 2020년 2월 기준 아직 안정적으로 동작하지 않을 수 있다.  

##### 3) Project 생성

Project는 하나의 제품을 가리킨다. 사업 유형에 따라 제품일수도 있고, 서비스 혹은 소프트웨어 일수도 있다. Project에는 제품에 사용된 Component/Release를 등록하여 관리한다. 

Project 생성 시에는 다음과 같은 정보를 등록한다. 

* Project Name
* Version
* Project type (예: Product, Customer Project, Service, Internal Project, InnerSource)

메뉴 &gt; Projects &gt; Add Project를 통해 Project를 생성할 수 있다. 

![](https://lh6.googleusercontent.com/6gNtLci53U6zaU6Th5SHousuZ4VUijzuYjiJJlB0R6JwiHG4ggjb0RcnRYDkZCBhE2dMP2gGbT4qmB2FE5O8EW8hTfv1lgM4_XN0vzQUkttfTbX2cF0aNftHYuUy9EXczT2LzLO5)

Project를 생성하고 나면, 포함하는 Release나 하위 Project를 등록한다. 메뉴 &gt; Projects에서 해당 Project를 선택하면 “Linked Releases and Projects”에서 Linked Projects와 Linked Releases를 등록할 수 있다. 

![](https://lh4.googleusercontent.com/ZjD7r7EzxfdQ4bhw4ODsChydb6Vgqj1m4Ad0cWlYtyYXO40MCbPpTHHcy-wJmbHeA_FxTa66Mpza6-9ohu0e93b7BaGb7Zc9soTA3mGCHGnyGURukRUnJS_duI7T8IL2aTgMFzjB)

다음은 SuperCalc라는 Project에 OpenSSL 1.0.1과 zlib 1.2.8을 Linked Releases로 등록한 이후의 화면이다. 

![](https://lh3.googleusercontent.com/tZCshPwxtukNLvfL-f-LfNOH-4ATof0bIGxpghVKXQ9QMBgoc_t0ROJMYafS9V4PuRaOOEW9zp25yk0gFA_kcaoRN83UKwUaFhaXxSWg7xPWvsYoJ_-pZkROkey1mYVTqGxKsCRu)

##### 4) 보안 취약점 관리

SW360은 등록된 Release에 대해 보안 취약점이 있는지 자동으로 확인할 수 있다. 이를 위해 SW360은 CVE 정보를 주기적으로 수집하도록 스케쥴링하는 기능을 제공한다. 메뉴 &gt; Admin &gt; Schedule 에서 CVE SEARCH 정보를 24시간마다 수집하도록 스케쥴링을 설정할 수 있다. 

![](https://lh5.googleusercontent.com/V2AJbexZqJJqwFYD1kFpjdZ7zVM9PCd-I_6MSBu3djO2Gi6gQxxQpKoqqsETxDaSkpDXOKFOp9h0Fps1xYHEphesVX9ECwBwnSX5cWdziXoohh-CMmqRh_wVkwUD8dZE9w1raJRk)

이렇게 스케쥴링을 설정하면 SW360은 정해진 시간에 CVE Search 사이트([https://cve.circl.lu/](https://cve.circl.lu/))에서 CVE 정보를 수집한다. 수집한 CVE 정보는 메뉴 &gt; Vulnerabilities에서 확인할 수 있다. 

![](https://lh3.googleusercontent.com/dpIMyX7qCMdnibNihuL6RBSKg2fEckbOBPWJEtw08mY4quhv6Hh3BlgFIeydPOS6N8rF6ZSs4hpZgBGcXbcJI9saFDyfv4i-TCvxV5z-4LD9ZXpKah0jQU45j3iibxFpYoa7Hj9u)

이렇게 Vulnerabilities 정보가 수집된 이후에는 생성한 Project에 보안 취약점이 있는지 조회할 수 있다. 위에서 생성한 SuperCalc Project에서는 85개의 보안 취약점이 보고된 것을 확인할 수 있다. 

![](https://lh5.googleusercontent.com/lGeLbWHIBk6y2OSOXskcp4A2c5od0eTH6n7U5YG0p4cwTrrX02b6TpeRqJ7VXg5aUE7qDP2X2f8o4Rj1JsPHhZ-CUdLiy80O532Cgw-h_P9r-jHdL61QaXhFOPxIjTlX1cg9XPk5)

이와 같은 방법으로 기업에서 개발/배포하는 소프트웨어를 SW360에 등록하여 관리한다면, 오픈소스 컴플라이언스뿐만 아니라 보안 취약점에 대해서도 리스크를 최소화할 수 있는 형태로 관리가 가능하다. 

또한 SW360은 위와 같은 Web Interface 뿐만 아니라 대부분의 기능을 REST API로 제공하여서 FOSSology 등의 다른 도구와의 연동이 가능하다. : [https://github.com/eclipse/sw360/wiki/Dev-REST-API](https://github.com/eclipse/sw360/wiki/Dev-REST-API)

즉, 소스 코드 스캐닝 도구의 분석 결과를 SW360에 Import 시키는 등의 방법으로 DevOps에 Integration 시켜서 Project, Release 등록을 자동화시켜서 관리한다면 효율성이 크게 증가할 것이다. 


