import streamlit as st
import streamlit.components.v1 as components
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.styles import MAIN_CSS

st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="mfta-hero">
        <div class="mfta-hero-eyebrow">Men's Fashion Data Analysis</div>
        <div class="mfta-hero-title">
            남성 패션 커뮤니티<br><span>데이터 분석 인사이트</span>
        </div>
        <div class="mfta-hero-subtitle">
            5개 남성 패션 커뮤니티의 실제 게시글 데이터를 분석해
            남성 패션의 브랜드·아이템·스타일 데이터를 시각화합니다.
        </div>
        <div class="mfta-stat-grid">
            <div class="mfta-stat">
                <div class="mfta-stat-value">272,066</div>
                <div class="mfta-stat-label">총 게시글 수</div>
            </div>
            <div class="mfta-stat">
                <div class="mfta-stat-value">5</div>
                <div class="mfta-stat-label">분석 커뮤니티</div>
            </div>
            <div class="mfta-stat">
                <div class="mfta-stat-value">454</div>
                <div class="mfta-stat-label">추적 키워드</div>
            </div>
            <div class="mfta-stat">
                <div class="mfta-stat-value">2022.03–2025.08</div>
                <div class="mfta-stat-label">분석 기간</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Dashboard Cards ────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="mfta-section-label">대시보드</div>
    <div class="mfta-section-title">분석 도구 선택</div>
    <div class="mfta-section-desc">
        세 가지 대시보드를 통해 남성 패션 데이터를 다각도로 탐색하세요.
    </div>
    """,
    unsafe_allow_html=True,
)

components.html(
    """
    <!DOCTYPE html>
    <html>
    <head>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
            rel="stylesheet">
      <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
          background: #0D0D0D;
          font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
          padding: 4px 0 12px;
          overflow: hidden;
        }
        .card-grid {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr;
          gap: 24px;
        }
        /* ── Link wrapper: 링크 기본 스타일 완전 제거 ── */
        a.card-link {
          display: block;
          text-decoration: none;
          color: inherit;
          outline: none;
        }
        /* ── Card ── */
        .card {
          background: #111111;
          border: 1px solid #222222;
          border-radius: 12px;
          padding: 28px 24px;
          cursor: pointer;
          transition: border-color 0.25s ease, background 0.25s ease,
                      transform 0.25s ease;
          user-select: none;
          height: 100%;
        }
        .card:hover {
          border-color: #C9A96E;
          background: #141410;
          transform: translateY(-4px);
        }
        .card-icon {
          font-size: 28px; margin-bottom: 16px; display: block;
        }
        .card-number {
          font-size: 11px; font-weight: 600; letter-spacing: 3px;
          text-transform: uppercase; color: #C9A96E; margin-bottom: 8px;
        }
        .card-title {
          font-size: 20px; font-weight: 700; color: #F0F0F0; margin-bottom: 10px;
        }
        .card-desc {
          font-size: 13px; color: #666; line-height: 1.6;
          margin-bottom: 20px; min-height: 88px;
        }
        .card-tag {
          display: inline-block;
          background: #1E1E1E; color: #888;
          font-size: 11px; padding: 4px 10px;
          border-radius: 100px; margin-right: 6px; margin-bottom: 4px;
        }
      </style>
    </head>
    <body>
      <div class="card-grid" id="grid">

        <div class="card" onclick="nav('/trend')">
          <span class="card-icon">📈</span>
          <div class="card-number">Dashboard 01</div>
          <div class="card-title">트렌드 분석</div>
          <div class="card-desc">
            연도·시즌별 브랜드와 아이템, 스타일의 언급량 추이를 추적합니다.
            어떤 키워드가 부상하고 있는지 한눈에 파악하세요.
          </div>
          <span class="card-tag">시즌 트렌드</span>
          <span class="card-tag">연도별 추이</span>
          <span class="card-tag">Tableau</span>
        </div>

        <div class="card" onclick="nav('/community')">
          <span class="card-icon">👥</span>
          <div class="card-number">Dashboard 02</div>
          <div class="card-title">커뮤니티 세그먼트</div>
          <div class="card-desc">
            5개 커뮤니티 간 패션 취향 차이를 분석합니다.
            각 커뮤니티의 고유한 스타일 정체성을 발견하세요.
          </div>
          <span class="card-tag">커뮤니티 비교</span>
          <span class="card-tag">Jaccard 유사도</span>
          <span class="card-tag">Tableau</span>
        </div>

        <div class="card" onclick="nav('/keyword')">
          <span class="card-icon">🔍</span>
          <div class="card-number">Dashboard 03</div>
          <div class="card-title">키워드 탐색기</div>
          <div class="card-desc">
            특정 키워드의 공출현 네트워크와 시즌·커뮤니티별 분포를
            인터랙티브하게 탐색할 수 있습니다.
          </div>
          <span class="card-tag">공출현 네트워크</span>
          <span class="card-tag">시즌 추이</span>
          <span class="card-tag">커뮤니티 비중</span>
        </div>

      </div>

      <script>
        function nav(path) {
          try {
            // 사이드바의 네비게이션 링크를 찾아 클릭 (Streamlit WebSocket 라우팅 사용)
            const parentDoc = window.parent.document;
            const links = parentDoc.querySelectorAll('a[href]');
            for (const a of links) {
              const href = a.getAttribute('href');
              if (href === path || href === path + '/' || href.endsWith(path)) {
                a.click();
                return;
              }
            }
          } catch(e) {}
          // 사이드바 링크를 못 찾으면 직접 이동
          try { window.parent.location.href = path; } catch(e) {}
        }

        // iframe 높이를 콘텐츠 높이에 맞게 동적으로 조절
        function fitHeight() {
          const h = document.getElementById('grid').offsetHeight + 20;
          try {
            if (window.frameElement) window.frameElement.style.height = h + 'px';
          } catch(e) {}
        }
        window.addEventListener('load', fitHeight);
        window.addEventListener('resize', fitHeight);
        new ResizeObserver(fitHeight).observe(document.getElementById('grid'));
      </script>
    </body>
    </html>
    """,
    height=320,
    scrolling=False,
)

# ── Community Info ─────────────────────────────────────────────────────────────
st.markdown('<hr class="mfta-divider">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="mfta-section-label">데이터 소스</div>
    <div class="mfta-section-title">분석 대상 커뮤니티</div>
    """,
    unsafe_allow_html=True,
)

communities = [
    ("Z9DY",         "짱구대디랑",         "#FF6B6B", "트렌드에 민감한 10대 후반~20대 초중반 중심 대형 패션 커뮤니티"),
    ("KKST",         "깡스타일리스트",       "#50C878", "한국 패션 유튜버 중 가장 많은 구독자를 보유한 남친룩 스타일링 중심 커뮤니티"),
    ("FIT THE SIZE", "핏더사이즈",          "#C9A96E", "친근한 동네 형 느낌의 유쾌한 소통과 2030 라이프스타일 패션을 다루는 커뮤니티"),
    ("HAO",          "How About OOTD",     "#7B68EE", "실제 사람들의 착장(OOTD) 기반, 고감도 스타일링을 이야기하는 커뮤니티"),
    ("GOCD",         "Go Out Casually Dressed", "#4A90D9", "주로 30대 이상 남성들이 선호하는 깔끔하고 캐주얼한 스타일 중심 커뮤니티"),
]

cols = st.columns(5, gap="small")
for col, (abbr, name, color, desc) in zip(cols, communities):
    col.markdown(
        f"""
        <div style="background:#111;border:1px solid #1E1E1E;border-radius:10px;
                    padding:18px 14px;height:100%;">
            <div style="width:36px;height:4px;background:{color};
                        border-radius:2px;margin-bottom:12px;"></div>
            <div style="font-size:13px;font-weight:700;color:#F0F0F0;
                        margin-bottom:4px;">{abbr}</div>
            <div style="font-size:11px;color:#C9A96E;margin-bottom:8px;">{name}</div>
            <div style="font-size:11px;color:#555;line-height:1.5;">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
