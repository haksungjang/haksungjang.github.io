# 영문 번역 지침

이 사이트는 한국어가 기본 언어이고 영어판을 함께 제공한다. 번역 작업자(사람 또는 에이전트)는
이 문서 하나만 읽고 작업할 수 있어야 한다.

## 출력 위치와 파일명

한국어 원본과 **같은 폴더**에 파일명 접미사 `.en`을 붙여 만든다. 폴더를 새로 만들지 않는다.

```
content/en/research/2026-cisa-sbom-minimum-elements/_index.md      ← 한국어 원본
content/en/research/2026-cisa-sbom-minimum-elements/_index.en.md   ← 영어판
content/en/blog/20240906_spdx_30/index.md                          ← 한국어 원본
content/en/blog/20240906_spdx_30/index.en.md                       ← 영어판
```

최상위 폴더 이름이 `content/en`인 것은 과거 템플릿의 잔재이며 언어와 무관하다. 이 폴더 안의
접미사 없는 파일이 한국어, `.en.md`가 영어다. 폴더 이름을 바꾸거나 파일을 옮기지 않는다.

이미지 등 페이지 리소스는 두 언어가 같은 폴더의 것을 공유한다. **이미지 파일을 복사하지 않는다.**

## 프론트매터

번역하는 키와 그대로 두는 키가 정해져 있다.

| 처리 | 키 |
|---|---|
| 번역한다 | `title`, `linkTitle`, `description`, `tags`, `subtitle`, 그 밖의 사람이 읽는 문구 |
| 영문 표기로 바꾼다 | `author: 장학성` → `author: Haksung Jang` |
| 원본 그대로 둔다 | `date`, `weight`, `type`, `categories`, `resources`, `draft`, `aliases`, `menu`, `ai_generated`, `ai_generator`, `verified_at`, `verification_verdict`, `hide_feedback` |

`categories`는 분류 키로 쓰이므로 번역하지 않는다. `tags`는 화면에 노출되는 이름표이므로 번역하되,
고유명사와 표준 이름은 원문 그대로 둔다(`SBOM`, `CISA`, `SPDX`, `CycloneDX`, `OpenChain`, `BomLens`).

`source_pdf`처럼 원래 영문 자료를 가리키는 값은 영어 서지 형식으로 자연스럽게 옮긴다.

`description`이 여러 줄(`>-`)이면 그 형식을 유지한다.

## 본문 규칙

**shortcode는 구조를 그대로 두고 내부 문구만 번역한다.**

```
{{% alert color="info" %}}      ← 태그와 파라미터 유지
번역 대상 문구                    ← 여기만 번역
{{% /alert %}}

{{< imgproc 이미지이름 Fit "900x600" >}}   ← 이미지 이름과 크기 유지
번역 대상 캡션                              ← 여기만 번역
{{< /imgproc >}}

{{% pageinfo %}} ... {{% /pageinfo %}}     ← 같은 방식
```

**이미지 참조는 경로와 파일명을 그대로 둔다.** `![설명](./elements-structure.png)`에서 대괄호 안
대체 텍스트만 번역한다. 경로를 바꾸면 공유 리소스 참조가 깨진다.

**`{{< relref "..." >}}`의 인자는 그대로 둔다.** 링크 표시 문구만 번역한다. 참조 대상의 영어판이
아직 없으면 빌드에 경고가 남지만 정상이며, 해당 문서가 번역되면 자동으로 해소된다.

**코드 블록 안에서 실행에 관여하는 것은 번역하지 않는다.** 명령어, 파일 경로, 키 이름, 식별자,
실제 설정 값을 그대로 둔다.

다만 코드 블록 안이라도 사람이 읽으라고 쓴 한국어는 번역한다. 두 가지가 여기 해당한다.

- 한국어 주석
- 예시의 자리표시자 문구. 예를 들어 JSON 예시의 `"name": "공급사 정식 명칭"`은
  `"name": "Supplier legal name"`으로 옮긴다. 키 `"name"`은 그대로 두고 값만 바꾼다.

판단 기준은 그 문구를 한국어로 남겨 두었을 때 영어권 독자가 뜻을 알 수 있는지다. 알 수 없으면 번역한다.

**mermaid 다이어그램은 라벨 문구만 번역하고 문법과 노드 아이디는 건드리지 않는다.**

**표는 열 개수와 구분선을 그대로 유지한다.** 셀 안의 백틱 코드 값은 번역하지 않는다.

**URL은 바꾸지 않는다.** 한국어 페이지를 가리키는 내부 절대 링크도 그대로 둔다. 대상의 영어판이
없을 때 404보다 한국어 페이지로 연결되는 편이 낫다.

**앵커가 한국어인 내부 링크는 대상 영어판의 헤딩에 맞춰 고친다.** Hugo는 헤딩 문구에서 앵커를
만들기 때문에, 대상 문서가 영어로 번역되면 앵커도 영어로 바뀐다.

```
원본:   [단계별 구축 로드맵 보기](../../#단계별-구축-로드맵)
영어판: [View the full implementation roadmap](../../#phased-implementation-roadmap)
```

대상 문서의 영어판(`.en.md`)을 열어 실제 헤딩 문구를 확인하고, 그것을 소문자로 바꾸고 공백을
하이픈으로 바꾼 값을 앵커로 쓴다. 대상 영어판이 아직 없으면 한국어 앵커를 그대로 두고 넘어간다.
번역이 다 끝난 뒤 일괄 점검한다.

**각주 표기(`[A2]`, `[C3]` 등)와 참고문헌 번호를 그대로 유지한다.**

## 문체

한국어 원문은 존댓말(-습니다)이지만 영어는 기술 문서의 중립 평서문으로 쓴다. 원문의 문단 구성과
소제목 구조를 그대로 따르고, 문단을 합치거나 나누지 않는다. 내용을 요약하거나 생략하지 않으며,
원문에 없는 설명을 더하지 않는다.

날짜는 영어 표기로 옮긴다. `2026년 7월 29일` → `July 29, 2026`.

그림과 표 캡션의 라벨을 옮긴다. `**그림 1.**` → `**Figure 1.**`, `**표 1.**` → `**Table 1.**`.

원문이 인용한 영문 문서의 표현은 가능하면 원래 영어 표현을 되살린다. 확인할 수 없으면 일관된
역어를 쓰고 임의로 바꾸지 않는다.

## 용어집

표준·조직·제품의 정식 명칭은 원문 그대로 쓴다. 줄여 쓰지 않는다.

| 한국어 | 영어 |
|---|---|
| 자재 명세서 | Bill of Materials |
| 소프트웨어 자재 명세서 | Software Bill of Materials (SBOM) |
| 최소 요소 | minimum elements |
| 데이터 필드 | data fields |
| 운영 원칙 | operational practices |
| 전이 의존성 | transitive dependencies |
| 커버리지 | Coverage |
| 깊이 | Depth |
| 컴포넌트 생산자 | Component Producer |
| 공급자 이름 | Supplier Name |
| 미상 | unknown |
| 보류 | withheld |
| 기계 처리 가능 | machine-readable |
| 사람 검토 | human review |
| 충족 / 미달 | met / not met |
| 적합성 판정 | conformance assessment |
| 오픈소스 프로그램 오피스 | Open Source Program Office (OSPO) |
| 소프트웨어 공급망 | software supply chain |
| 취약점 관리 | vulnerability management |
| 라이선스 컴플라이언스 | license compliance |
| 오픈소스 컴플라이언스 | open source compliance |
| 빌드 파이프라인 | build pipeline |
| 서명 인프라 | signing infrastructure |
| 유럽연합 사이버 복원력법 | EU Cyber Resilience Act |
| 제조자 | manufacturer |
| 조달 | procurement |
| 국가정보원 산하 국가사이버안보센터 | National Cyber Security Center under the National Intelligence Service |
| 한국인터넷진흥원 | Korea Internet & Security Agency |
| 미국 사이버보안·인프라보안국 | Cybersecurity and Infrastructure Security Agency (CISA) |
| 미국 통신정보관리청 | National Telecommunications and Information Administration (NTIA) |
| 일본 경제산업성 | Ministry of Economy, Trade and Industry |
| SK텔레콤 | SK telecom |

한국어 원문이 `한국어명(English Name, ABBR)` 형식으로 처음 등장할 때 병기한 것은 영어판에서
`English Name (ABBR)` 한 번만 쓰고 이후로는 약어를 쓴다.

## 기준 사례

`content/en/research/2026-cisa-sbom-minimum-elements/_index.en.md`가 이 지침을 적용한 표본이다.
판단이 서지 않을 때 원본 `_index.md`와 나란히 놓고 비교한다.

## 금지 사항

- 파일을 옮기거나 이름을 바꾸지 않는다.
- 한국어 원본을 수정하지 않는다.
- 이미지를 복사하거나 새로 만들지 않는다.
- 원문에 없는 절, 요약, 맺음말을 추가하지 않는다.
- 번역하지 못한 부분을 건너뛰고 넘어가지 않는다. 문서는 처음부터 끝까지 빠짐없이 옮긴다.
