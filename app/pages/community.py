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
    <div class="mfta-section-label">Dashboard 02</div>
    <div class="mfta-section-title">커뮤니티 세그먼트</div>
    <div class="mfta-section-desc">
        5개 커뮤니티가 어떤 키워드를 즐겨 쓰고, 서로 얼마나 비슷한 취향을 가지는지 비교합니다.
        커뮤니티별 키워드 점유율과 상호 유사도를 통해 각 커뮤니티의 패션 정체성을 발견하세요.
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Community Overview ────────────────────────────────────────────────────────
cols = st.columns(5, gap="small")
communities = [
    ("Z9DY",         "짱구대디랑",     "#FF6B6B"),
    ("KKST",         "깡스타일리스트",   "#50C878"),
    ("FIT THE SIZE", "핏더사이즈",      "#C9A96E"),
    ("HAO",          "How About OOTD", "#7B68EE"),
    ("GOCD",         "Go Out Casually Dressed", "#4A90D9"),
]
for col, (abbr, name, color) in zip(cols, communities):
    col.markdown(
        f"""
        <div style="background:#111;border:1px solid #1E1E1E;border-top:3px solid {color};
                    border-radius:8px;padding:14px 12px;text-align:center;">
            <div style="font-size:13px;font-weight:700;color:#F0F0F0;">{abbr}</div>
            <div style="font-size:10px;color:#555;margin-top:4px;">{name}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="mfta-divider">', unsafe_allow_html=True)

# ── Guide ─────────────────────────────────────────────────────────────────────
with st.expander("대시보드 설명", expanded=False):
    st.markdown(
        """
        - **키워드 점유율**: 각 커뮤니티에서 특정 키워드가 차지하는 비중을 비교합니다.
        - **Jaccard 유사도**: 두 커뮤니티가 공통으로 자주 언급하는 키워드의 비율입니다.
        - **밀도 분석**: 커뮤니티 내 키워드 사용의 집중도를 나타냅니다.
        - 커뮤니티 이름을 클릭해 해당 커뮤니티에 집중된 뷰로 전환할 수 있습니다.
        """,
    )

# ── Tableau Embed ─────────────────────────────────────────────────────────────
TABLEAU_URL = (
    "https://public.tableau.com/views/_17746918072630/sheet4"
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
