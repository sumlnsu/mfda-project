import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from PIL import Image

# ── Google Analytics 4 ──────────────────────────────────────────────────────
# 측정 ID를 발급받은 후 아래 값을 교체하세요. 예: "G-XXXXXXXXXX"
# 아직 발급 전이면 빈 문자열로 두면 GA 스크립트가 주입되지 않습니다.
_GA_MEASUREMENT_ID = ""  # TODO: 여기에 GA4 측정 ID 입력

def _inject_ga(measurement_id: str) -> None:
    """GA4 gtag.js를 Streamlit 앱에 주입합니다."""
    if not measurement_id:
        return
    components.html(
        f"""
        <script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{measurement_id}', {{
            'page_title': document.title,
            'page_location': window.parent.location.href
          }});
        </script>
        """,
        height=0,
    )

# 아이콘 이미지 로드 (없으면 기본 이모지 사용)
_icon_path = Path(__file__).parent / "assets" / "icon.png"
_page_icon = Image.open(_icon_path) if _icon_path.exists() else "👔"

st.set_page_config(
    page_title="MFDA - 남성 패션 데이터 분석 대시보드 플랫폼",
    page_icon=_page_icon,
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation(
    [
        st.Page("pages/home.py",      title="홈",              icon="🏠", url_path="home"),
        st.Page("pages/trend.py",     title="트렌드 분석",      icon="📈", url_path="trend"),
        st.Page("pages/community.py", title="커뮤니티 세그먼트", icon="👥", url_path="community"),
        st.Page("pages/keyword.py",   title="키워드 탐색기",    icon="🔍", url_path="keyword"),
    ]
)

# Sidebar branding
with st.sidebar:
    st.markdown(
        """
        <div style="padding:20px 8px 12px; border-bottom:1px solid #1E1E1E; margin-bottom:8px;">
            <div style="font-size:11px;letter-spacing:3px;text-transform:uppercase;
                        color:#C9A96E;font-weight:600;margin-bottom:4px;">MFDA</div>
            <div style="font-size:15px;font-weight:700;color:#F0F0F0;line-height:1.3;">
                남성 패션<br>데이터 분석
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="padding:12px 8px;font-size:11px;color:#444;line-height:1.7;">
            5개 커뮤니티 · 272,066건<br>
            남성 패션 커뮤니티 카페 게시글 분석
        </div>
        """,
        unsafe_allow_html=True,
    )

_inject_ga(_GA_MEASUREMENT_ID)
pg.run()
