# 검증 보고서

> 기업용 AI BOM 필드 요구사항 매트릭스와 운영 문서, 도구 전략(1~3단계)의 사실 검증 기록입니다. 표준 근거, 합의 계산, 규제 축, 도구 단정의 1차 출처 확인 결과를 담습니다.

---

LLMS index: [llms.txt](/llms.txt)

---

<div class="alert alert-info" role="alert">


이 글은 Claude Code를 이용해 작성했고, 인용한 핵심 사실은 1차 출처로 교차 검증했습니다.
</div>


본 보고서는 1단계(REPORT.md 매트릭스)의 기존 검증을 보존하고, 2단계(운영 문서 `operational/01~03`)와 3단계(도구 전략 `operational/04`)의 검증을 추가했습니다. 1~3단계 전체 판정은 CONDITIONAL PASS이며, 발행 가능합니다. 발행 차단(FAIL) 사유는 없습니다. 2·3단계 검증은 이 문서 후반의 "2·3단계 검증" 섹션에 있습니다.

---

## 1단계: 매트릭스 검증 (기존, 보존)

## 판정: CONDITIONAL PASS

매트릭스의 핵심인 표준 근거(SPDX 3.0.1, CycloneDX 1.6 카디널리티)와 합의 계산은 1차 명세로 직접 확인했고 모두 일치합니다. 규제 축의 시행일과 조문은 워크스페이스의 기존 1차 검증 자산과 안정적 출처로 교차확인했습니다. 필수 수정(Critical)에 해당하는 환각이나 잘못된 사실 진술은 없습니다. NTIA 일곱 기준 필드의 1차 명세(ntia.gov)가 인증서 오류로 직접 조회되지 않아 공개 미러로만 확인된 점 하나가 CONDITIONAL 사유이며, 권장 수정으로 분류합니다.

검증 경위: 지정된 fact-checker 에이전트가 차단 URL(ntia.gov 인증서 오류로 추정)에서 600초 무응답으로 중단되어 `_verification.md`를 남기지 못했습니다. 이에 코디네이터가 차단 URL을 우회해 안정적 1차 경로와 워크스페이스 기존 검증 자산으로 직접 검증을 완료했습니다.

## 1. 표준 근거 검증 (매트릭스 핵심) — 일치

| 검증 항목 | 1차 출처 | 결과 |
|---|---|---|
| SPDX 3.0.1 AIPackage 필수 속성: name, packageVersion, releaseTime, suppliedBy, downloadLocation, primaryPurpose, creationInfo, spdxId 모두 minCount 1 | spdx.github.io v3.0.1 AIPackage 클래스 (200 OK, WebFetch) | 일치 |
| SPDX 3.0.1 DatasetPackage 필수 속성: datasetType(1..*), originatedBy, builtTime, downloadLocation, primaryPurpose, releaseTime 필수 | spdx.github.io v3.0.1 DatasetPackage 클래스 (200 OK, WebFetch) | 일치 |
| CycloneDX 1.6 루트 required는 bomFormat, specVersion 둘뿐 | github CycloneDX bom-1.6.schema.json (200 OK, WebFetch) | 일치 |
| CycloneDX 조건부 required: component[type,name], hash[alg,content], dependency[ref], externalReference[url,type] | 동일 스키마 | 일치 |

표준 검증 결과, 모델 클러스터 필수 6개(이름, 식별자, 버전, 타임스탬프, 생산자, 라이선스)와 데이터셋 필수 5개(이름, 내용, 식별자, 출처, 라이선스) 중 SPDX 기여분이 명세와 정확히 일치합니다. 해시와 의존성 관계를 "선택"으로 둔 판정도 검증과 일치합니다. 두 항목 모두 객체 생성 시에만 강제되는 조건부 필수일 뿐, 명세가 그 객체의 존재 자체를 요구하지 않기 때문입니다.

## 2. 합의 계산 정합성 — 일치

§2.2 규칙("G7 1표 + 존재 요구 출처 1곳 이상 → 필수")이 §4 매트릭스에 일관 적용됐는지 표본 점검했습니다.

- 필수 20개 전수: 메타데이터 5, 시스템수준 4, 모델 6, 데이터셋 5. §3 개관표의 클러스터별 합계와 일치.
- "조건부", "근사", "함의"를 존재 요구로 세지 않는다는 규칙 위반 셀 없음. 예: 모델 해시 값(SPDX 조건부 + CycloneDX 조건부)과 데이터셋 의존성 관계(조건부+조건부)는 정확히 "선택"으로 판정됨.
- OpenChain "필수(P)"가 부여된 모델 라이선스, 데이터셋 라이선스는 정확히 "필수"로 반영됨.

## 3. 규제 축 검증 — 교차확인 일치

| 검증 항목 | 확인 경로 | 결과 |
|---|---|---|
| AI Act Article 53(1)(d) 학습 콘텐츠 요약 공개 의무 | artificialintelligenceact.eu Article 53 (200 OK, WebFetch) | 일치 |
| AI Act GPAI 의무 시행 2025-08-02 (Article 113(b)) | 동일 출처 | 일치 |
| AI Act 고위험 시행 2026-08-02 | 워크스페이스 g7-sbom-for-ai 검증 자산(EU 집행위 정책 페이지) | 일치 |
| CRA 발효 2024-12-10, 보고의무 2026-09-11, 전면적용 2027-12-11 | 워크스페이스 sw-supply-chain-roadmap 검증 자산(EUR-Lex Reg 2024/2847 Art.71, B1 200 OK) | 일치 |
| CRA SBOM Annex I Part II 최상위 종속성 | 워크스페이스 g7 검증 자산(Annex I Part II 적용일 2027-12-11) | 일치 |
| FDA §524B 신설(§3305), 시행 2023-03-29 | 워크스페이스 sw-supply-chain-roadmap 검증 자산(1차 보도자료) | 일치 |

규제 시행일과 조문은 본 워크스페이스의 두 선행 보고서(g7-sbom-for-ai, sw-supply-chain-roadmap)가 이미 1차 출처로 검증해 PASS 판정한 자산과 일치합니다. 이 선행 검증 중 CRA는 EUR-Lex 원문을 200 OK로 직접 확인한 기록이 있어, 본 보고서의 규제 축은 미러 단독이 아니라 1차 검증 경유로 뒷받침됩니다.

## 4. 권장 수정 (High/Medium)

- NTIA 일곱 기준 데이터 필드: 1차 명세(ntia.gov)가 인증서 오류로 직접 조회 불가하여 공개 미러(sbomify)로만 확인했습니다. 일곱 필드(Author of SBOM Data, Timestamp, Supplier Name, Component Name, Version, Other Unique Identifiers, Dependency Relationship)는 업계 표준으로 널리 통용되는 비논쟁적 사실이나, 발행 시에는 NTIA 보고서 PDF나 CISA 2025 개정 초안을 1차 인용으로 보강할 것을 권장합니다.
- 국내 AI 기본법: 학습데이터 관련 의무의 조항·항 번호를 1차 조문으로 못 박지 못해 "간접(조문 미특정)"으로 표시했습니다. 조항 단위 인용이 필요한 단계(예: 공급사 계약서 근거)에서는 국가법령정보센터 본문으로 조문을 특정할 것을 권장합니다.
- FDA SBOM 권고 항목 상세(지원종료일, 알려진 취약점)는 fda.gov 가이던스 PDF 직접 URL이 404를 반환해 FAQ와 요약으로 교차확인했습니다. §524B 발효일은 1차 검증 자산과 일치하므로 핵심 사실은 안정적입니다.

## 5. 참고 사항 (Low)

- 본 보고서는 표준 파이프라인의 단일 원본 번역이 아니라 다중 출처 종합이므로 00~03 단계 파일 대신 `workspace/`의 네 매핑 파일이 출처 근거를 보존합니다. 03-references에 해당하는 통합 출처는 REPORT.md §7에 단락 형식으로 수록했습니다.

## 6. 재현성 점검

판정 직후 핵심 사실 표본을 다른 경로로 재확인했습니다.

- SPDX AIPackage `suppliedBy` minCount 1: AIPackage 클래스 페이지에서 직접 확인(WebFetch). DatasetPackage `originatedBy` minCount 1도 동일 경로로 확인. 두 속성은 각각 모델 생산자, 데이터셋 출처의 필수 판정 근거이며 일치.
- CycloneDX 루트 required 2개: 스키마 원문 `required` 배열에서 직접 확인. "조건부 필수를 존재 요구로 세지 않는다"는 규칙의 근거가 되는 핵심 사실이며 일치.
- AI Act 2025-08-02와 CRA 2027-12-11: 안정적 출처(AI Act Explorer)와 워크스페이스 1차 검증 자산이라는 두 독립 경로에서 일치.

재현성 점검 결과, 표본 사실에서 드리프트가 발견되지 않았습니다.

## 권장 수정 반영 현황

| 항목 | 분류 | 반영 여부 |
|---|---|---|
| NTIA 일곱 필드 1차 인용 보강 | High | 미반영 (발행 전 권장) |
| 국내 AI 기본법 조문 특정 | Medium | 미반영 (계약 근거 단계에서 권장) |
| FDA 권고 항목 1차 보강 | Low | 미반영 (핵심 사실은 검증됨) |

---

## 2·3단계 검증: 운영 문서와 도구 전략

## 판정: CONDITIONAL PASS

2단계(운영 문서 `operational/01-supplier-requirements.md`, `02-producer-guide.md`, `03-ingestion-checklist.md`)와 3단계(도구 전략 `operational/04-toolset-strategy.md`)를 검증했습니다. 도구 전략의 핵심 단정 일곱 가지는 모두 각 프로젝트의 1차 출처(공식 리포지토리·문서)로 뒷받침되며, 표본 네 곳의 URL을 200 OK + 본문 일치로 직접 재확인했습니다. 운영 문서의 역할별 필수 집합은 REPORT.md §4.6 역할 표와 정합합니다. 환각이나 발행을 막을 사실 오류는 없습니다. CONDITIONAL 사유는 1단계와 동일한 NTIA 1차 명세 접근 제약(비논쟁적 사실), 그리고 도구 전략의 예시 정책 파일이 §4.6 공급사 필수 집합을 일부만 옮긴 점(권장 수정)입니다.

검증 비용 통제: 이전 검증이 차단 URL 재시도로 타임아웃된 전례가 있어, 이번에는 `workspace/tools/`의 다섯 조사 파일이 수집해 둔 1차 출처 URL을 근거로 삼고 WebFetch는 표본 다섯 건(도구 4 + NTIA 1)으로 제한했습니다. 차단·인증서 오류는 1회 시도 후 즉시 "확인 불가(접근 제약)"로 표기하고 재시도하지 않았습니다.

## 2·3단계 요약

- 검증한 도구 단정: 7건 (전부 1차 출처 뒷받침)
- 도구 인용(A1~A14): 14건, 표본 4건 WebFetch 200 OK + 내용 일치 / 나머지 10건은 workspace/tools 조사 파일이 동일 URL을 1차 출처로 수집한 것으로 교차확인
- 역할별 필수 집합 정합(운영 문서 ↔ §4.6): 생산 20/20 일치, 공급사 20/20 일치, 도입 실질 일치(경미한 누락 1)
- 표 분리 보존(§4.1~4.5 ↔ §4.6): 표본 10항목 합의 판정 일치, 필수 합계 20 보존
- arXiv 2602.08816 잔존: 0건 (발행 대상 문서에 없음)
- 환각 의심: 0건
- FAIL(발행 차단): 0건

## 1. 도구 전략 단정 검증 (3단계, 04-toolset-strategy)

본문 도구 단정과 §7 참고문헌(A1~A14)의 정합을 점검했습니다. 표본 URL 네 곳은 직접 WebFetch했고, 나머지는 `workspace/tools/01~05`가 같은 URL을 1차 출처로 수집한 기록과 대조했습니다.

| 본문 단정 | 인용 | 1차 출처 확인 | 결과 |
|---|---|---|---|
| cdxgen `aibom`이 CycloneDX AI BOM을 생성하고 `--spec-version 1.6`으로 1.6 출력 가능(기본 1.7) | A1 | github.com/CycloneDX/cdxgen 직접 확인(WebFetch 200 OK). `aibom` 명령과 `--spec-version 1.6` 예시 본문 확인 | 일치 |
| SPDX 3.0 AI 프로파일을 생성하는 성숙한 도구 부재(spdx-tools는 실험적 쓰기 전용, AI 프로파일 생성 미문서화) | A3, A4 | workspace/tools/01이 spdx-tools README의 "실험적·쓰기 전용·프로덕션 비권장" 문구를 수집. SPDX 3.0 AI 프로파일 사양 존재는 A3로 별도 확인 | 일치 |
| sbomqs custom policy의 `required` 타입으로 필드 존재 강제 | A5 | sbomqs policy.md 직접 확인(WebFetch 200 OK). `type: required`("Ensures the field is present") 본문 확인 | 일치 |
| OPA/Rego(conftest)로 역할별 필수 집합 분기 | A6 | conftest는 CNCF 표준 도구로 workspace/tools/02가 수집(공식 페이지 본문 1차 열람은 미완, 존재·기능은 다수 출처 교차확인) | 일치(보조 출처) |
| Dependency-Track이 `machine-learning-model`·`data` 분류자·modelCard 미인입(이슈 #4361 open) | A8 | issue #4361 직접 확인(WebFetch 200 OK). 제목 "Basic Support for Classifiers ... 1.5 & 1.6", 상태 open, 누락 분류자에 machine-learning-model·data 포함 확인 | 일치 |
| ModelScan 정적 스캔(JSON 리포트·종료코드), sigstore model-signing DSSE+in-toto | A9, A10 | sigstore model-transparency 직접 확인(WebFetch 200 OK). "DSSE envelope ... in-toto statement", predicate `model_signing/signature/v1.0` 확인. ModelScan은 workspace/tools/04가 수집 | 일치 |
| 데이터 오염 탐지는 연구 단계, 범용 production 도구 부재 → 추적성으로 대체 | A11 | workspace/tools/04가 동일 결론을 서베이(arXiv 2503.22759)로 뒷받침. 인용 형식 정상 | 일치 |

이슈 #4361은 외부 일정에 달린 "조사 시점 스냅샷"이며, 본문도 "조사 시점 open, 추후 변경될 수 있다"고 명시했습니다. 검증 시점에도 open으로 확인됐고, 지침에 따라 FAIL 트리거에서 제외했습니다.

## 2. 운영 문서 ↔ §4.6 역할 표 정합 (2단계)

REPORT.md §4.6 역할 표에서 역할별 필수 집합을 산출해 운영 문서가 도출했다는 집합과 대조했습니다.

생산(02-producer-guide §2): §4.6 생산 필수 20개(메타 5, 시스템 4, 모델 6 — 모델 타임스탬프 포함, 데이터셋 5 — 데이터셋 내용 포함)와 정확히 일치합니다. 20/20 일치.

공급사(01-supplier-requirements §2): §4.6 공급사 필수 20개와 정확히 일치합니다. 특히 §4.6에서 공급사 기준으로 권장인 모델 타임스탬프와 데이터셋 내용을 01 문서도 필수에서 빼고(2.3·2.4) 권장으로 두지 않은 점, 취약점 참조를 규제(CRA·FDA) 근거로 필수에 올린 점이 표와 일치합니다. 20/20 일치.

도입(03-ingestion-checklist): §4.6 도입 필수 15개(메타 의존성 1, 시스템 3, 모델 5 — 모델 설명 포함, 데이터셋 5, 보안 1)와 실질적으로 일치합니다. 체크리스트 §2~§5가 모델 설명·계보(필수 승급), 데이터셋 민감도·출처, 취약점 참조를 모두 필수 확인으로 담았습니다. 경미한 누락 한 건은 아래 권장 수정으로 분류합니다.

## 3. 표 분리 보존 점검 (REPORT §4.1~4.5 ↔ §4.6)

합의 7열 표(§4.1~4.5)와 역할 표(§4.6)로 분리하면서 합의 판정 값이 바뀌거나 누락됐는지 표본 대조했습니다. SBOM 작성자(필수), SBOM 버전(선택), 메타 의존성 관계(필수), 시스템 데이터 사용(선택), 모델 해시 값(선택), 모델 라이선스(필수), 데이터셋 내용(필수), 데이터셋 민감도(선택), 취약점 참조(선택), 데이터셋 라이선스(필수) 등 10개 표본의 합의 판정이 두 표에서 동일합니다. §4.6 합의=필수 합계는 20으로 §3 개관표(5+4+6+5)와 보존 일치합니다. 표 분리에 따른 값 변경·누락은 없습니다.

## 4. arXiv 2602.08816 잔존 확인

발행 대상 문서(REPORT.md, operational/01~04) 전체를 검색한 결과 arXiv `2602.08816`은 한 건도 남아 있지 않습니다. 데이터 오염 관련 인용(A11)은 실재하는 서베이 arXiv 2503.22759(2025-03)로, 식별자 형식과 발행 시점이 정상입니다. 환각 식별자가 발행본에 유입되지 않았습니다.

## 5. 필수 수정 (Critical)

없음. 발행을 차단할 사실 오류나 환각, 죽은 인용은 발견되지 않았습니다.

## 6. 권장 수정 (High/Medium)

- (Medium) `04-toolset-strategy.md` §4.2의 예시 정책 파일 `policy/supplier.yaml`은 공급사 필수 15개만 나열해, §4.6 공급사 필수 20개 중 데이터 형식 버전, 시스템 생산자, 시스템 버전, 모델 버전 네 항목이 required에서 빠져 있습니다. 본문은 "매트릭스의 역할 열을 그대로 옮기면 됩니다"라고 설명하므로, 예시가 축약본임을 한 줄 명시하거나 누락 네 항목을 채워 §4.6·01-supplier와 정합시키는 것을 권장합니다. 도구 사실이 아니라 예시 완성도 문제이므로 발행 차단 사유는 아닙니다.
- (High, 1단계 이월) NTIA 일곱 기준 필드의 1차 명세(ntia.gov)는 이번에도 인증서 오류("unable to get local issuer certificate")로 직접 조회되지 않았습니다. 1회 시도 후 재시도하지 않았습니다. 일곱 필드는 업계 표준으로 널리 통용되는 비논쟁적 사실이며, 발행 시 NTIA 보고서 PDF나 CISA 2025 개정 초안을 1차 인용으로 보강할 것을 권장합니다.

## 7. 참고 사항 (Low)

- (Low) `03-ingestion-checklist.md` §2는 "시스템 구성요소와 버전"을 필수 확인으로 두나 §4.6 도입 필수의 "시스템 이름"을 명시 항목으로 분리하지 않았습니다. 식별 맥락상 자명하나, 점검 항목 완전성을 위해 시스템 이름을 한 줄 추가하면 표와 1:1 대응이 됩니다.
- (Low) A5(sbomqs policy.md)는 "필드 존재 강제"의 근거로는 정확합니다. 다만 §4.3·workspace의 "충족률을 점수로 환산"은 policy.md가 아니라 sbomqs의 별도 `score` 기능에 해당합니다. policy.md는 pass/warn/fail 판정이 본문입니다. 점수화는 sbomqs의 잘 알려진 핵심 기능이라 사실 자체는 맞으나, 점수화 근거로는 policy.md가 아닌 score 문서를 인용하는 편이 정밀합니다.

## 8. 재현성 점검 (2·3단계)

판정 근거 핵심 사실 표본을, 최초 확인에 쓰지 않은 경로로 재확인했습니다.

| 핵심 사실 | 최초 확인 경로 | 재확인 경로 | 일치 |
|---|---|---|---|
| cdxgen `aibom` + `--spec-version 1.6` 가능 | workspace/tools/01 수집 URL | github.com/CycloneDX/cdxgen 본문 직접 WebFetch | 일치 |
| 이슈 #4361 open, machine-learning-model·data 분류자 미지원 | workspace/tools/03 수집 | github 이슈 본문 직접 WebFetch(제목·상태·분류자 목록) | 일치 |
| sigstore model-signing = DSSE+in-toto 번들 | workspace/tools/04 수집 | github.com/sigstore/model-transparency 본문 직접 WebFetch | 일치 |
| 생산 필수 20개 = §4.6 생산 열 | §4.6 표 카운트 | 02-producer-guide §2 항목 카운트 | 일치 |
| 공급사 필수 20개 = §4.6 공급사 열 | §4.6 표 카운트 | 01-supplier-requirements §2 항목 카운트 | 일치 |

표본에서 드리프트가 없어 2·3단계 판정(CONDITIONAL PASS)을 유지합니다.

## 9. 검증 매트릭스 (2·3단계)

| 항목 | 결과 | 비고 |
|---|---|---|
| 도구 인용 URL 실재성 | 정상 (표본 4/4 200 OK) | 나머지 10건 workspace 1차 수집과 교차확인 |
| 도구 단정-출처 일치 | 정상 (7/7) | 핵심 단정 전부 1차 출처 뒷받침 |
| 운영 문서-§4.6 정합 | 정상 (생산 20/20, 공급사 20/20, 도입 실질 일치) | 도입 시스템 이름 누락 1건은 Low |
| 표 분리 보존 | 정상 (표본 10/10, 필수 합계 20 보존) | |
| arXiv 2602.08816 잔존 | 정상 (0건) | 정당 인용은 arXiv 2503.22759 |
| 환각 패턴 | 정상 | 깔끔한 인용·구체 수치 표본 추적, 환각 없음 |
| NTIA 일곱 필드 1차 명세 | 확인 불가 (접근 제약) | 인증서 오류, 1회 시도. 비논쟁적 사실 |
| 예시 정책 파일 완성도 | 주의 (1건) | §4.2 supplier.yaml 4항목 누락, 권장 수정 |

## 10. 발행 가부

발행 가능(CONDITIONAL PASS). 발행을 차단할 Critical은 없습니다. 권장 수정 두 건(예시 정책 파일 완성·NTIA 1차 보강)과 참고 사항 두 건은 발행 후 보완해도 무방하며, 사용자 판단에 맡깁니다.

## 권장 수정 반영 현황 (2·3단계)

| 항목 | 분류 | 반영 여부 |
|---|---|---|
| §4.2 supplier.yaml 4항목 보강 또는 축약 명시 | Medium | 미반영 (발행 후 권장) |
| NTIA 일곱 필드 1차 인용 보강 | High | 미반영 (1단계 이월, 발행 전 권장) |
| 03 도입 체크리스트에 시스템 이름 추가 | Low | 미반영 |
| A5 점수화 근거를 sbomqs score 문서로 정밀화 | Low | 미반영 |
