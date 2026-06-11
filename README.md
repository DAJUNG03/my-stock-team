# my-stock-team

종목명을 넣으면 애널리스트 에이전트들이 협업해 리서치를 만들고, 검증을 거쳐
PPTX 리포트로 내보내는 Claude Code 플러그인입니다. **무료 공개 데이터 기반 학습용**이며
투자 권유가 아닙니다.

## 구성

| 종류 | 이름 | 역할 |
|---|---|---|
| 에이전트 | `fundamental-analyst` | DART 공시·재무 분석 (3개년 추세, 부문별 분해, 밸류에이션) |
| 에이전트 | `market-technical-analyst` | FinanceDataReader 주가·추세·수급 분석 |
| 에이전트 | `news-sentiment-analyst` | 웹서치 뉴스·이슈·시장 심리 분석 |
| 에이전트 | `risk-manager` | 세 분석 종합 → 핵심 리스크 3개 + 모니터링 포인트 (pykrx) |
| 에이전트 | `verification-analyst` | 리포트 품질 검증 (직접 수정 없이 통과/보류 판정) |
| 스킬 | `report-pptx` | reports/{종목명}.md → KB 옐로우 톤 7장 PPTX |
| 커맨드 | `/my-stock-team:research <종목명>` | 풀 파이프라인 (병렬 분석 → 리스크 → 리드 종합 → 검증 → 리포트) |
| 커맨드 | `/my-stock-team:verify <종목명>` | 완성 리포트 검증만 단독 실행 |

## 설치

```
# 1) 마켓플레이스 등록 (이 폴더 경로 또는 git 저장소 URL)
/plugin marketplace add <이 폴더 경로>

# 2) 플러그인 설치
/plugin install my-stock-team@my-stock-team-marketplace
```

## 사전 준비 (프로젝트 폴더에서)

1. **Python 패키지**:
   ```
   pip install python-pptx matplotlib finance-datareader pykrx pandas python-dotenv
   ```
2. **DART API 키**: 프로젝트 루트에 `.env` 파일을 만들고 본인 키를 넣습니다.
   ```
   DART_KEY=<https://opendart.fss.or.kr 에서 발급받은 본인 키>
   ```
   ⚠️ `.env`는 절대 커밋하지 마세요 (`.gitignore`에 추가). 이 플러그인에는 키가 포함되어 있지 않습니다.
3. **폴더 규칙**: 중간 산출물은 `outputs/research/`, 리포트는 `reports/`에 생성됩니다 (자동 생성).

## 사용 예

```
/my-stock-team:research 삼성전자
/my-stock-team:verify 삼성전자
/report-pptx 삼성전자
```

## 가드레일

모든 산출물에 적용: 수치마다 출처·기준일 표기, 확인 불가/[미확인] 명시, 매수·매도·목표가 등
투자 행동 단정 금지(판단 근거 정리까지만), 리포트 머리·꼬리에 학습용 고지와 출처 목록.
