import streamlit as st
import streamlit.components.v1 as components
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.styles import MAIN_CSS

st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="mfta-section-label">Dashboard 01</div>
    <div class="mfta-section-title">트렌드 분석</div>
    <div class="mfta-section-desc">
        연도·시즌별 브랜드와 아이템, 스타일 키워드의 언급량 추이를 탐색합니다.
        필터를 조정해 부상 중인 트렌드와 사라지는 키워드를 파악하세요.
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Guide ─────────────────────────────────────────────────────────────────────
with st.expander("대시보드 설명", expanded=False):
    st.markdown(
        """
        - **연도 필터**: 2022~2025년 구간을 선택해 추이를 비교합니다.
        - **키워드 유형**: 시각화에 사용된 색상 기준은 아래와 같습니다.
          - 🔴 **브랜드 (BRAND)** — 기업·브랜드명 키워드
          - 🟢 **아이템 (ITEM)** — 의류·패션 아이템 키워드
          - 🔵 **스타일 (STYLE)** — 스타일·무드·소재 키워드
        - 차트나 범례를 클릭해 특정 키워드를 하이라이트할 수 있습니다.
        """,
        unsafe_allow_html=False,
    )

# ── Tableau Embed ─────────────────────────────────────────────────────────────
TABLEAU_URL = (
    "https://public.tableau.com/views/_17746789847900/sheet4"
    "?:language=ko-KR&:display_count=n&:showVizHome=no&:embed=true"
)

st.markdown('<div class="tableau-container">', unsafe_allow_html=True)
components.iframe(TABLEAU_URL, height=900, scrolling=True)
st.markdown("</div>", unsafe_allow_html=True)

# ── Footer note ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="margin-top:16px; padding:12px 16px; background:#0A0A0A;
                border:1px solid #1A1A1A; border-radius:8px;
                font-size:12px; color:#444; line-height:1.6;">
        데이터 출처: 5개 남성 패션 커뮤니티 (Z9DY · KKST · FIT THE SIZE · HAO · GOCD)<br>
        분석 기간: 2022년 봄 ~ 2025년 여름 · 총 272,066건 게시글
    </div>
    """,
    unsafe_allow_html=True,
)
