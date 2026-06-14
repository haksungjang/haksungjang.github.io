# 표준과 형식

> SBOM을 기계 판독 가능하게 표현하는 두 표준 형식 SPDX와 CycloneDX를 비교합니다.

---

LLMS index: [llms.txt](/llms.txt)

---

SBOM이 기계 판독성을 요구하는 이상 표준 형식이 필요합니다. 미국 NTIA 최소 요소가 명시한 세 형식
가운데 실무를 양분하는 것은 SPDX와 CycloneDX입니다. 세 번째인 SWID 태그는 주로 자산 관리에서
쓰이며, 식별자로서의 역할은 [식별자와 라이선스](./2-identifiers/)에서 다룹니다.

## SPDX

SPDX(System Package Data Exchange)는 리눅스 재단(Linux Foundation) 산하 프로젝트입니다. 버전 2.2.1이
2021년 8월 ISO/IEC 5962:2021로 국제 표준이 되었습니다. 현행 ISO 표준이 가리키는 것은 어디까지나
2.2.1 버전이라는 점을 유의해야 합니다.

리눅스 재단은 2024년 4월 16일 SPDX 3.0을 발표하며 용도별 프로파일(Profile) 구조를 도입했습니다.
핵심 모델 위에 보안(Security), 빌드(Build), 데이터셋(Dataset), 인공지능(AI) 프로파일을 얹는
방식입니다. AI 프로파일은 모델 학습과 특성화 정보를, 데이터셋 프로파일은 데이터의 출처와 라이선스를,
보안 프로파일은 취약점의 식별과 심각도, 악용 가능성, 완화 계획을 담습니다. 같은 해 12월에는 패치
릴리스 3.0.1이 나왔습니다. SPDX 3.x의 ISO 재표준화 진행 여부는 2026년 6월 기준 확인되지 않았습니다.

## CycloneDX

CycloneDX는 OWASP(Open Worldwide Application Security Project)에서 출발한 풀스택 BOM 표준입니다.
취약점 악용 가능성 교환(Vulnerability Exploitability eXchange, VEX)을 형식 안에서 네이티브로
지원하는 점이 특징입니다. 국제 표준화는 Ecma International의 기술위원회 TC54를 통해 이루어졌습니다.
v1.6이 2024년 6월 ECMA-424 1판으로 발행되며 암호 자재 명세서(Cryptographic Bill of Materials, CBOM)와
증명(CycloneDX Attestations)을 더했고, v1.7이 2025년 10월 발표돼 2025년 12월 ECMA-424 2판으로
표준화되었습니다. v1.7은 사후양자 암호 대비, 구조화된 인용, 특허 객체 지원을 추가했습니다.

CycloneDX는 한 형식으로 소프트웨어(SBOM), 하드웨어(HBOM), 서비스(SaaSBOM), 머신러닝 모델(ML-BOM)을
모두 표현할 수 있습니다.

## 두 형식 비교

| 구분 | SPDX | CycloneDX |
|---|---|---|
| 주관 | Linux Foundation | OWASP / Ecma TC54 |
| 국제표준 | ISO/IEC 5962:2021 (v2.2.1 기준) | ECMA-424 1판(v1.6, 2024-06), 2판(v1.7, 2025-12) |
| 최신 사양 | 3.0(2024-04), 3.0.1(2024-12) | 1.7(2025-10) |
| 확장 방식 | 용도별 프로파일(보안, 빌드, 데이터셋, AI) | 구성요소 타입과 부속 객체, VEX 네이티브 |
| 강점 | 라이선스 표현과 법적 컴플라이언스 이력 | 취약점·VEX 통합, 보안 운영 친화 |

**표 1.** SBOM 양대 표준 형식 비교 *(출처: ISO/IEC 5962:2021, Linux Foundation 2024, Ecma International ECMA-424. 수집일 2026-06-14)*

두 표준은 설계 철학이 다릅니다. SPDX는 프로파일 방식으로 적용 범위를 넓히고, CycloneDX는 구성요소
타입과 부속 객체로 표현합니다. 그러나 둘 다 구성요소의 식별, 라이선스, 의존 관계를 담는다는 점에서
같은 문제를 겨냥합니다. 어느 쪽을 택하든 두 형식 사이의 변환 도구가 있으므로, 거래 상대가 요구하는
형식과 자사 도구 체인이 잘 지원하는 형식을 기준으로 고르면 됩니다. 라이선스 컴플라이언스 중심이면
SPDX가, 취약점 운영 중심이면 CycloneDX가 익숙한 출발점입니다.

다음으로 형식 안에 무엇을 반드시 담아야 하는지를 정한 [최소 요소](./1-minimum-elements/)와,
구성요소를 일관되게 가리키는 [식별자와 라이선스](./2-identifiers/)를 살펴봅니다.

## 출처

ISO/IEC (2021). *ISO/IEC 5962:2021 — SPDX Specification V2.2.1*. The Linux Foundation (2024).
*SPDX 3.0 Release*. <https://www.linuxfoundation.org/press/spdx-3-revolutionizes-software-management-in-systems-with-enhanced-functionality-and-streamlined-use-cases>.
Ecma International. *ECMA-424 — CycloneDX Bill of Materials Specification*.
<https://ecma-international.org/publications-and-standards/standards/ecma-424/>. CycloneDX (2025).
*CycloneDX v1.7 Released*. <https://cyclonedx.org/news/cyclonedx-v1.7-released/>. (모두 접속: 2026-06-14)

---

Section pages:

- [SBOM의 최소 요소](/docs/sbom_guide/2-standards/1-minimum-elements/): NTIA 2021 최소 요소에서 CISA 2025 개정 초안까지, SBOM에 반드시 담아야 할 데이터 필드를 정리합니다.
- [식별자와 라이선스](/docs/sbom_guide/2-standards/2-identifiers/): 구성요소를 일관되게 가리키는 PURL·CPE·SWID 식별자와, SPDX 라이선스 식별자 표기 방법을 정리합니다.
