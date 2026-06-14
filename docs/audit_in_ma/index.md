# 인수합병(M&A)에서의 오픈소스 감사

> 인수합병(M&A) 거래에서 오픈소스 감사를 위한 개요와 실무 가이드를 제공합니다.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="pageinfo pageinfo-primary">


이 문서는 Linux Foundation이 발행한 *Open Source Audits in Merger and Acquisition Transactions: The Basics You Must Know* (Ibrahim Haddad, Ph.D. 저, 2018)를 번역한 것입니다. 원저자는 이 번역을 검토하지 않았습니다. 원문은 [원문 PDF](https://www.ibrahimatlinux.com/wp-content/uploads/2022/01/OpenSourceAudits_MergerandAcquisition.pdf)에서 볼 수 있습니다.


</div>


소프트웨어가 모든 거래의 중심이 된 시대에, 인수합병(M&A)에서 오픈소스 실사(due diligence)는 표준 절차로 자리 잡았습니다. 이 책은 M&A 거래에서 오픈소스 감사(open source audit)가 어떻게 진행되는지, 인수 기업과 인수 대상 기업이 각각 무엇을 준비해야 하는지를 다룹니다.

---

Section pages:

- [Chapter 1. 들어가며](/docs/audit_in_ma/1-introduction/): M&A 거래에서 오픈소스 감사 프로세스의 개요를 소개합니다.
- [Chapter 2. 일반적인 오픈소스 사용 시나리오](/docs/audit_in_ma/2-usage-scenarios/): 오픈소스가 코드베이스에 들어오는 결합, 링크, 수정 방식을 정리합니다.
- [Chapter 3. 오픈소스 감사](/docs/audit_in_ma/3-audits/): 오픈소스 감사를 수행하는 이유와 발주 판단 기준, 그리고 감사 절차의 입력과 출력을 설명합니다.
- [Chapter 4. 감사 범위 산정](/docs/audit_in_ma/4-scope/): 감사 견적을 내기 위해 감사자가 파악해야 하는 코드 규모와 특성, 그리고 긴급도가 비용에 미치는 영향을 설명합니다.
- [Chapter 5. 감사 방법](/docs/audit_in_ma/5-audit-methods/): 전통적 감사, 블라인드 감사, 자체 수행(DIY) 감사 세 가지 감사 방법(audit methods)의 절차와 장단점을 설명합니다.
- [Chapter 6. 최종 보고서에 관한 참고사항](/docs/audit_in_ma/6-final-report/): 최종 보고서에는 잡음이 많이 섞여 있을 수 있으므로 실제 문제를 걸러낼 시간을 확보해야 하며, SPDX 형식 보고서는 요청해야 받을 수 있습니다.
- [Chapter 7. 보안과 버전 관리](/docs/audit_in_ma/7-security-version-control/): 오픈소스 프로젝트의 취약점은 수정 과정과 함께 공개되며, 보안과 버전 관리는 컴플라이언스 실사에 포함되지 않지만 스캔 서비스 제공자가 별도로 다룰 수 있습니다.
- [Chapter 8. 인수 전후 개선 조치](/docs/audit_in_ma/8-remediation/): 감사에서 드러난 컴플라이언스 문제를 해결하는 선택지와 각 선택지의 비용을 인수 대상 기업 가치 평가에 활용하는 방법을 다룹니다.
- [Chapter 9. 인수 대상 기업으로서 감사 준비](/docs/audit_in_ma/9-target-preparation/): 인수 대상 기업이 평소 컴플라이언스 활동을 통해 오픈소스 감사를 미리 준비하는 방법을 다룹니다.
- [Chapter 10. 인수 기업으로서 감사 준비](/docs/audit_in_ma/10-acquirer-preparation/): 인수 기업이 감사를 의뢰하기 전에 내려야 할 결정과 감사 결과 수령 후의 추가 의무사항을 다룹니다.
- [Chapter 11. 권장하는 컴플라이언스 관련 개발 관행](/docs/audit_in_ma/11-recommended-practices/): 컴플라이언스 문제를 줄이는 개발 관행과, 반드시 피해야 할 실수를 정리합니다.
- [Chapter 12. 맺음말](/docs/audit_in_ma/12-conclusion/): 오픈소스 실사를 매끄럽게 진행하기 위해 대상 기업과 인수 기업이 각각 준비해야 할 사항을 정리합니다.
