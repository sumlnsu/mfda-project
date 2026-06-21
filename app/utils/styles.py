MAIN_CSS = """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* header 전체를 숨기면 사이드바 토글 버튼도 함께 사라지므로
   헤더 배경만 투명하게 처리하고 내부 툴바 요소만 선택적으로 숨김 */
[data-testid="stHeader"] {
    background: transparent !important;
    border-bottom: none !important;
}
[data-testid="stToolbarActions"] { visibility: hidden; }
[data-testid="stDecoration"]     { display: none; }
[data-testid="stStatusWidget"]   { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0A0A0A;
    border-right: 1px solid #1E1E1E;
}
[data-testid="stSidebar"] .stMarkdown p {
    color: #888;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 24px;
    margin-bottom: 4px;
}

/* ── Main container ── */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* ── Hero section ── */
.mfta-hero {
    background: linear-gradient(135deg, #0D0D0D 0%, #161616 50%, #1A1410 100%);
    border: 1px solid #2A2A2A;
    border-radius: 16px;
    padding: 56px 48px;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}
.mfta-hero::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(201,169,110,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.mfta-hero-eyebrow {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #C9A96E;
    margin-bottom: 16px;
}
.mfta-hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.1;
    color: #F0F0F0;
    margin-bottom: 16px;
    letter-spacing: -1px;
}
.mfta-hero-title span { color: #C9A96E; }
.mfta-hero-subtitle {
    font-size: 16px;
    font-weight: 400;
    color: #888;
    line-height: 1.7;
    max-width: 560px;
}
.mfta-stat-grid {
    display: flex;
    gap: 40px;
    margin-top: 40px;
}
.mfta-stat { border-left: 2px solid #C9A96E; padding-left: 16px; }
.mfta-stat-value {
    font-size: 28px;
    font-weight: 700;
    color: #F0F0F0;
    line-height: 1;
}
.mfta-stat-label {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
    letter-spacing: 0.5px;
}

/* ── Dashboard cards (used as reference; rendered in components.html) ── */
.mfta-card {
    background: #111111;
    border: 1px solid #222222;
    border-radius: 12px;
    padding: 28px 24px;
    height: 100%;
}
.mfta-card-icon {
    font-size: 28px;
    margin-bottom: 16px;
    display: block;
}
.mfta-card-number {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #C9A96E;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.mfta-card-title {
    font-size: 20px;
    font-weight: 700;
    color: #F0F0F0;
    margin-bottom: 10px;
}
.mfta-card-desc {
    font-size: 13px;
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
    min-height: 88px;
}
.mfta-card-tag {
    display: inline-block;
    background: #1E1E1E;
    color: #888;
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 100px;
    margin-right: 6px;
    margin-bottom: 4px;
}

/* ── Section header ── */
.mfta-section-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #C9A96E;
    margin-bottom: 6px;
}
.mfta-section-title {
    font-size: 28px;
    font-weight: 700;
    color: #F0F0F0;
    margin-bottom: 6px;
}
.mfta-section-desc {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
    margin-bottom: 32px;
}

/* ── Divider ── */
.mfta-divider {
    border: none;
    border-top: 1px solid #1E1E1E;
    margin: 32px 0;
}

/* ── Keyword search box ── */
.mfta-search-panel {
    background: #111111;
    border: 1px solid #222222;
    border-radius: 12px;
    padding: 28px 28px 20px;
    margin-bottom: 32px;
}

/* ── Metric card ── */
.mfta-metric {
    background: #111111;
    border: 1px solid #1E1E1E;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
}
.mfta-metric-value {
    font-size: 32px;
    font-weight: 700;
    color: #C9A96E;
}
.mfta-metric-label {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
}

/* ── Community badge ── */
.comm-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 100px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* ── Chart container ── */
.mfta-chart-container {
    background: #111111;
    border: 1px solid #1E1E1E;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
}
.mfta-chart-title {
    font-size: 15px;
    font-weight: 600;
    color: #E0E0E0;
    margin-bottom: 4px;
}
.mfta-chart-sub {
    font-size: 12px;
    color: #555;
    margin-bottom: 16px;
}

/* ── Network legend ── */
.mfta-legend {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 8px;
}
.mfta-legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    color: #888;
}
.mfta-legend-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── Streamlit button overrides ── */
.stButton > button {
    background: #C9A96E;
    color: #0D0D0D;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 10px 28px;
    font-size: 14px;
    transition: background 0.2s;
    width: 100%;
}
.stButton > button:hover {
    background: #D4B97E;
    color: #0D0D0D;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] label {
    font-size: 12px;
    font-weight: 500;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ── Tableau embed container ── */
.tableau-container {
    background: #111;
    border: 1px solid #1E1E1E;
    border-radius: 12px;
    overflow: hidden;
}

/* ── Info box ── */
.mfta-info {
    background: #141410;
    border: 1px solid #2A2518;
    border-radius: 8px;
    padding: 14px 18px;
    color: #C9A96E;
    font-size: 13px;
}

/* ── Tag pill ── */
.mfta-type-brand { background: rgba(220,80,80,0.12);  color: #E05555; border: 1px solid rgba(220,80,80,0.25); }
.mfta-type-item  { background: rgba(80,200,120,0.12); color: #50C878; border: 1px solid rgba(80,200,120,0.25); }
.mfta-type-style { background: rgba(74,144,217,0.12); color: #4A90D9; border: 1px solid rgba(74,144,217,0.25); }
</style>
"""

PLOTLY_LAYOUT = dict(
    paper_bgcolor="#111111",
    plot_bgcolor="#111111",
    font=dict(family="Inter, sans-serif", color="#C0C0C0", size=12),
    margin=dict(l=16, r=16, t=40, b=16),
    title_font=dict(size=15, color="#E0E0E0", family="Inter, sans-serif"),
    xaxis=dict(
        gridcolor="#1E1E1E",
        zerolinecolor="#1E1E1E",
        tickfont=dict(color="#888", size=11),
        title_font=dict(color="#666", size=12),
    ),
    yaxis=dict(
        gridcolor="#1E1E1E",
        zerolinecolor="#1E1E1E",
        tickfont=dict(color="#888", size=11),
        title_font=dict(color="#666", size=12),
    ),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        bordercolor="#1E1E1E",
        font=dict(color="#888", size=11),
    ),
)
