# my-stock-team

종목명을 말하면 애널리스트 에이전트 5인이 협업해 리서치 리포트(md/PPTX)까지 만들어 주는
Claude Code 플러그인입니다. (무료 공개 데이터 기반 **학습용**이며 투자 권유가 아닙니다.)

## 설치

Claude Code에서 아래 두 줄을 입력하면 끝입니다.

```
/plugin marketplace add DAJUNG03/my-stock-team
/plugin install my-stock-team@my-stock-team
```

## 사전 준비

1. **DART API 키 (필수, 각자 발급)** — 이 플러그인에는 키가 들어 있지 않습니다.
   [opendart.fss.or.kr](https://opendart.fss.or.kr)에서 본인 키를 무료로 발급받은 뒤,
   분석을 실행할 프로젝트 폴더 루트에 `.env` 파일을 만들어 넣어 주세요.

   ```
   DART_KEY=발급받은_본인_키
   ```

   ⚠️ `.env`는 절대 커밋하지 마세요 (`.gitignore`에 추가).

2. **Python 패키지**

   ```
   pip install python-pptx matplotlib finance-datareader pykrx pandas python-dotenv
   ```

## 사용법

설치 후 Claude Code에 자연어로 요청하면 됩니다.

```
삼성전자 분석해줘
```

→ 펀더멘털·기술·뉴스 분석이 병렬로 돌고, 리스크 종합과 검증 게이트를 거쳐
`reports/삼성전자.md` 리포트가 만들어집니다.

명시적으로 커맨드를 쓸 수도 있습니다.

```
/my-stock-team:research 삼성전자     # 풀 파이프라인 실행
/my-stock-team:verify 삼성전자       # 완성된 리포트 검증만 실행
/report-pptx 삼성전자                # md 리포트 → PPTX 변환
```

## 무엇이 들어 있나

| 종류 | 이름 | 역할 |
|---|---|---|
| 에이전트 | `fundamental-analyst` | DART 공시·재무 분석 (3개년 추세, 부문별 분해, 밸류에이션) |
| 에이전트 | `market-technical-analyst` | 주가·추세·수급 분석 (FinanceDataReader) |
| 에이전트 | `news-sentiment-analyst` | 뉴스·이슈·시장 심리 분석 (웹서치) |
| 에이전트 | `risk-manager` | 세 분석 종합 → 핵심 리스크 3개 + 모니터링 포인트 (pykrx) |
| 에이전트 | `verification-analyst` | 리포트 품질 검증 — 직접 수정 없이 통과/보류 판정 |
| 스킬 | `report-pptx` | `reports/{종목명}.md` → KB 옐로우 톤 7장 PPTX |
| 커맨드 | `/my-stock-team:research` | 풀 파이프라인 (병렬 분석 → 리스크 → 종합 → 검증 → 리포트) |
| 커맨드 | `/my-stock-team:verify` | 리포트 검증 단독 실행 |

산출물은 중간 데이터 `outputs/research/`, 최종 리포트 `reports/`에 생성됩니다 (자동 생성).

## 가드레일

모든 산출물에 항상 적용됩니다: 수치마다 출처·기준일 표기, 확인 불가한 데이터는
"확인 불가"/"[미확인]"으로 명시, 매수·매도·목표가 등 투자 행동 단정 금지(판단 근거
정리까지만), 리포트 머리·꼬리에 학습용 고지와 출처 목록 포함.
