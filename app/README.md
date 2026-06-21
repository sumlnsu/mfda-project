# Dashboard App

이 디렉터리는 MFDA Streamlit 대시보드 플랫폼입니다.

## Run

```bash
streamlit run app/app.py
```

## Pages

- `home.py`: 프로젝트 개요와 데이터 소스 요약
- `trend.py`: 연도 및 시즌별 키워드 트렌드 분석
- `community.py`: 커뮤니티별 키워드 분포와 세그먼트 비교
- `keyword.py`: 키워드별 공출현 네트워크, 시즌 추이, 커뮤니티 비중 탐색

## Data

`app/data/dashboard/`에는 대시보드 실행에 필요한 집계 데이터가 들어 있습니다.
