---
title: "인도·한국 등 기타 관할권"
linkTitle: "인도·한국 등"
weight: 20
type: docs
categories: ["guide"]
tags: ["CERT-In", "한국", "규제"]
description: >
  인도 CERT-In과 한국을 비롯한 기타 관할권의 SBOM 권고 가이드라인을 정리합니다.
---

미국과 유럽연합 밖의 관할권은 대체로 권고 단계에 있습니다. 법적 강제나 제재는 없으나, 조달과 계약
관행에 영향을 주는 모범 사례로 기능합니다.

## 인도: CERT-In 기술 가이드라인

인도 침해사고대응팀(Indian Computer Emergency Response Team, CERT-In)은 *Technical Guidelines on
Software Bill of Materials (SBOM)*를 발행했습니다. 정부기관, 공공부문, 필수 서비스, 소프트웨어
생산·서비스 기업을 대상으로 한 자발적(voluntary) 가이드라인으로, SBOM의 가치와 모범 사례, 최소 요소,
취약점 추적 절차를 다룹니다. 법적 강제력은 없지만 정부 조달과 계약 관행에 영향을 줍니다.

CERT-In은 2025년 7월 이 가이드라인을 양자 BOM(QBOM), 암호 BOM(CBOM), AI BOM(AIBOM), 하드웨어
BOM(HBOM)까지 포괄하도록 확장했습니다. 자재 명세서 개념이 소프트웨어를 넘어 암호와 AI, 하드웨어로
번지는 흐름을 보여주는 사례입니다. AI BOM으로의 확장은 [5. 도구와 자동화](../../5-tools/)와 별도
가이드인 [AI SBOM 컴플라이언스 가이드](../../../ai-sbom_guide/)에서 더 다룹니다.

이 가이드의 초판이 바로 이 CERT-In 문서의 한국어 번역에서 출발했습니다. 현재 판은 그 골격을 미국과
유럽연합의 현행 1차 출처로 갱신하고 범용 실무 관점으로 넓힌 것입니다.

## 한국: SW 공급망 보안 가이드라인

한국은 과학기술정보통신부와 국가정보원, 한국인터넷진흥원(KISA) 등이 2024년 5월 SW 공급망 보안
가이드라인 1.0을 발표했습니다. SBOM 생성과 취약점 점검 절차, 미국 국립표준기술연구소(NIST)의 안전한
소프트웨어 개발 프레임워크(Secure Software Development Framework, SSDF) 활용을 권고하는 내용입니다.

다만 이는 행정 가이드라인 수준이며, EU 사이버 복원력법처럼 제조물 차원의 강제 보고 의무를 부과하는
법령은 현행 한국 법체계에 아직 없습니다. 그럼에도 EU와 미국에 소프트웨어를 수출하는 한국 기업은
해당 시장의 요건을 직접 충족해야 하므로, SBOM 역량 확보는 국내 규제와 무관하게 실질적 필요입니다.

## 실무 시사점

관할권마다 위상은 다르지만 요구하는 데이터의 골격은 수렴합니다. 한 번 잘 만든 SBOM 체계는 여러
관할권의 요건을 함께 충족할 수 있습니다. 수출 대상 시장 가운데 가장 엄격한 요건(현재로서는 EU CRA)을
기준으로 체계를 설계하면, 다른 관할권의 권고는 대체로 그 안에 포섭됩니다.

## 출처

Indian Computer Emergency Response Team (CERT-In). *Technical Guidelines on Software Bill of
Materials (SBOM)*, CIGU-2024-0002. <https://www.cert-in.org.in/>. 과학기술정보통신부·국가정보원·한국인터넷진흥원
(2024). *SW 공급망 보안 가이드라인 1.0*. <https://www.kisa.or.kr/>. (모두 접속: 2026-06-14)
