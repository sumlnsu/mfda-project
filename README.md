# MFDA Project

**Men's Fashion Data Analysis Dashboard Platform**

MFDA는 남성 패션 커뮤니티 게시글 데이터를 기반으로 브랜드, 아이템, 스타일 키워드의 변화와 커뮤니티별 차이를 분석하고, 그 결과를 Streamlit 대시보드와 브랜드 리포트로 확장한 데이터 분석 포트폴리오입니다.

## Project Scope

- 분석 대상: 5개 남성 패션 커뮤니티
- 분석 기간: 2022년 봄부터 2025년 여름
- 분석 규모: 게시글 272,066건 기준 대시보드 산출물
- 주요 분석 축: 브랜드, 아이템, 스타일 키워드
- 산출물: 분석 노트북, Tableau 기반 대시보드, Streamlit 키워드 탐색기, LMC 브랜드 트렌드 리포트

## Repository Structure

```text
mfda-project/
├── app/                 # Streamlit dashboard platform
│   ├── app.py
│   ├── pages/
│   ├── utils/
│   ├── data/
│   └── assets/
├── analysis/            # Analysis notebooks, processed data, plots
│   ├── notebooks/
│   ├── data/
│   └── plots/
├── reports/             # Portfolio report outputs
├── docs/                # Project explanation documents
├── requirements.txt
└── runtime.txt
```

## Dashboard

Streamlit 앱은 다음 화면으로 구성되어 있습니다.

- 홈: 프로젝트 개요, 데이터 소스, 핵심 지표 요약
- 트렌드 분석: 연도와 시즌별 브랜드, 아이템, 스타일 키워드 추이
- 커뮤니티 세그먼트: 커뮤니티별 키워드 분포와 유사도 비교
- 키워드 탐색기: 선택 키워드의 공출현 네트워크, 시즌별 언급량, 커뮤니티 비중 탐색

로컬 실행:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

Streamlit Cloud 배포 설정:

- Repository: `sumlnsu/mfda-project`
- Branch: `main`
- Main file path: `app/app.py`

## Analysis Assets

`analysis/`에는 기존 남성 패션 데이터 분석 프로젝트의 산출물이 들어 있습니다.

- `analysis/notebooks/`: 분석 및 대시보드 데이터 생성 노트북
- `analysis/data/`: 분석 과정에서 생성된 후보 키워드, 사전, 대시보드용 집계 데이터
- `analysis/plots/`: 분석 결과 시각화 이미지

## Report

`reports/lmc_trend_analysis_report.pdf`는 MFDA 분석 인사이트와 대시보드 플랫폼을 활용해 LMC 브랜드의 트렌드를 분석한 리포트 예시입니다.

이 리포트는 포트폴리오에서 다음 메시지를 전달하기 위한 산출물입니다.

- 대시보드가 단순 시각화 도구에 그치지 않고 브랜드별 분석 리포트로 확장 가능함
- 커뮤니티별 반응 차이와 시즌별 키워드 변화를 기반으로 브랜드 관점의 해석을 제공할 수 있음
- 패션 도메인 데이터 분석 결과를 의사결정 자료 형태로 정리할 수 있음

## Portfolio Positioning

이 프로젝트는 Data Analyst 지원용 포트폴리오에서 다음 역량을 보여주는 용도입니다.

- 비정형 커뮤니티 텍스트 데이터를 분석 가능한 키워드 단위로 정리
- 브랜드, 아이템, 스타일 축의 지표 설계
- 커뮤니티별 세그먼트 비교와 키워드 트렌드 해석
- Tableau와 Streamlit을 활용한 분석 결과 대시보드화
- 특정 브랜드 관점의 리포트 산출

## Notes

- 공개 레포에는 원본 수집 데이터가 아닌 분석 및 대시보드 산출물을 중심으로 포함했습니다.
- 대시보드 내 일부 시각화는 Tableau Public 임베드를 사용합니다.
- 기존 `mfta`와 `Mens-Fashion-Data-Analysis-Project`의 주요 산출물은 이 레포로 통합했습니다.
