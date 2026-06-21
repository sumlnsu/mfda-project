import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.styles import MAIN_CSS, PLOTLY_LAYOUT
from utils.data_loader import (
    get_all_tokens,
    get_cooccurrence,
    load_keyword_season,
    load_keyword_comm,
    TYPE_LABELS,
    TYPE_COLORS,
    COMMUNITY_COLORS,
    SEASON_KO as SEASON_KO_MAP,
)

st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="mfta-section-label">Dashboard 03</div>
    <div class="mfta-section-title">키워드 탐색기</div>
    <div class="mfta-section-desc">
        브랜드·아이템·스타일 키워드를 선택하면 공출현 네트워크,
        시즌별 언급량 추이, 커뮤니티별 비중을 인터랙티브하게 탐색할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Search Panel ───────────────────────────────────────────────────────────────
all_tokens = get_all_tokens()

st.markdown('<div class="mfta-search-panel">', unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1], gap="medium")

with c1:
    type_choice = st.selectbox(
        "키워드 유형",
        options=["ITEM", "STYLE", "BRAND"],
        format_func=lambda x: f"{TYPE_LABELS[x]}  ({x})",
        key="type_select",
    )

with c2:
    token_list = all_tokens[type_choice]
    keyword_choice = st.selectbox(
        "키워드 선택",
        options=token_list,
        key="keyword_select",
    )

with c3:
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    search_clicked = st.button("분석하기", key="btn_search")

st.markdown("</div>", unsafe_allow_html=True)

# ── Helper: build PyVis network ───────────────────────────────────────────────
def build_pyvis_html(keyword: str, token_type: str) -> str | None:
    from pyvis.network import Network

    cooc_df = get_cooccurrence(keyword, token_type, top_n=25)
    if cooc_df.empty:
        return None

    net = Network(height="520px", width="100%", bgcolor="#111111", font_color="#CCCCCC")
    net.set_options("""
    {
      "nodes": {
        "borderWidth": 0,
        "shadow": { "enabled": true, "size": 10 }
      },
      "edges": {
        "smooth": { "type": "continuous" },
        "shadow": false
      },
      "physics": {
        "solver": "forceAtlas2Based",
        "forceAtlas2Based": {
          "gravitationalConstant": -80,
          "centralGravity": 0.005,
          "springLength": 160,
          "springConstant": 0.06,
          "damping": 0.4
        },
        "stabilization": { "iterations": 200, "updateInterval": 25 }
      },
      "interaction": {
        "hover": true,
        "tooltipDelay": 150
      }
    }
    """)

    # Center node
    net.add_node(
        keyword,
        label=keyword,
        color={"background": "#C9A96E", "border": "#F0C070", "highlight": {"background": "#F0C070"}},
        size=32,
        font={"size": 16, "color": "#FFFFFF", "bold": True},
        title=f"<b>{keyword}</b><br>선택된 키워드",
        shape="dot",
        fixed=False,
    )

    max_count = cooc_df["count"].max()
    for _, row in cooc_df.iterrows():
        neighbor = row["neighbor"]
        count    = int(row["count"])
        ntype    = row["neighbor_type"]

        color = "#50C878" if ntype == "ITEM" else "#4A90D9"
        size  = 10 + 20 * (count / max_count)

        net.add_node(
            neighbor,
            label=neighbor,
            color={"background": color, "border": color,
                   "highlight": {"background": "#FFFFFF", "border": color}},
            size=size,
            font={"size": 11, "color": "#DDDDDD"},
            title=f"<b>{neighbor}</b><br>유형: {TYPE_LABELS.get(ntype, ntype)}<br>공출현: {count:,}회",
            shape="dot",
        )
        edge_width = 1 + 6 * (count / max_count)
        net.add_edge(
            keyword, neighbor,
            width=edge_width,
            color={"color": "rgba(180,180,180,0.25)", "highlight": "rgba(201,169,110,0.8)"},
            title=f"공출현 {count:,}회",
        )

    return net.generate_html()


# ── Helper: plotly layout merge ───────────────────────────────────────────────
def apply_layout(fig, title="", height=360):
    layout = {**PLOTLY_LAYOUT, "title": title, "height": height}
    fig.update_layout(**layout)
    return fig


# ── Main Output (runs immediately, updates on search click) ───────────────────
if "last_keyword" not in st.session_state:
    st.session_state.last_keyword = None
    st.session_state.last_type    = None

if search_clicked:
    st.session_state.last_keyword = keyword_choice
    st.session_state.last_type    = type_choice

active_keyword = st.session_state.last_keyword or keyword_choice
active_type    = st.session_state.last_type    or type_choice

# ── Type badge ────────────────────────────────────────────────────────────────
badge_class = f"mfta-type-{active_type.lower()}"
st.markdown(
    f"""
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:28px;">
        <div style="font-size:26px;font-weight:700;color:#F0F0F0;">{active_keyword}</div>
        <span class="comm-badge {badge_class}" style="font-size:12px;padding:4px 14px;">
            {TYPE_LABELS[active_type]}
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Load data ─────────────────────────────────────────────────────────────────
season_df = load_keyword_season()
comm_df   = load_keyword_comm()

kw_season = season_df[
    (season_df["token"] == active_keyword) & (season_df["TOKEN_TYPE"] == active_type)
].copy()
kw_comm = comm_df[
    (comm_df["token"] == active_keyword) & (comm_df["TOKEN_TYPE"] == active_type)
].copy()

# ── Metrics row ───────────────────────────────────────────────────────────────
total_mentions = int(kw_season["count"].sum())
peak_row       = kw_season.loc[kw_season["count"].idxmax()] if not kw_season.empty else None
top_community  = kw_comm.loc[kw_comm["share"].idxmax(), "COMMUNITY"] if not kw_comm.empty else "—"

m1, m2, m3, m4 = st.columns(4, gap="small")
for col, val, label in [
    (m1, f"{total_mentions:,}", "총 언급량"),
    (m2, f"{peak_row['SEASON_YEAR_KO']}" if peak_row is not None else "—", "최다 언급 시즌"),
    (m3, f"{peak_row['count']:,}" if peak_row is not None else "—", "최다 시즌 언급수"),
    (m4, top_community, "최다 커뮤니티"),
]:
    col.markdown(
        f"""
        <div class="mfta-metric">
            <div class="mfta-metric-value">{val}</div>
            <div class="mfta-metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# Section A: Network + Top Co-occurring (ITEM & STYLE only)
# ═════════════════════════════════════════════════════════════════════════════
if active_type in ("ITEM", "STYLE"):
    cooc_df = get_cooccurrence(active_keyword, active_type, top_n=25)

    net_col, bar_col = st.columns([3, 2], gap="large")

    # ── A1: Network ───────────────────────────────────────────────────────────
    with net_col:
        st.markdown(
            """
            <div class="mfta-chart-container">
                <div class="mfta-chart-title">공출현 네트워크</div>
                <div class="mfta-chart-sub">함께 언급된 키워드들의 연결 구조</div>
            """,
            unsafe_allow_html=True,
        )
        if cooc_df.empty:
            st.markdown(
                '<div class="mfta-info">해당 키워드의 공출현 데이터가 없습니다.</div>',
                unsafe_allow_html=True,
            )
        else:
            html_str = build_pyvis_html(active_keyword, active_type)
            if html_str:
                components.html(html_str, height=540, scrolling=False)
            # Legend
            st.markdown(
                """
                <div class="mfta-legend">
                    <div class="mfta-legend-item">
                        <div class="mfta-legend-dot" style="background:#C9A96E;"></div>
                        선택 키워드
                    </div>
                    <div class="mfta-legend-item">
                        <div class="mfta-legend-dot" style="background:#50C878;"></div>
                        아이템
                    </div>
                    <div class="mfta-legend-item">
                        <div class="mfta-legend-dot" style="background:#4A90D9;"></div>
                        스타일
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    # ── A2: Top Co-occurring Bar Chart ────────────────────────────────────────
    with bar_col:
        st.markdown(
            """
            <div class="mfta-chart-container">
                <div class="mfta-chart-title">함께 언급된 Top 키워드</div>
                <div class="mfta-chart-sub">공출현 빈도 기준 상위 15개</div>
            """,
            unsafe_allow_html=True,
        )
        if cooc_df.empty:
            st.markdown(
                '<div class="mfta-info">공출현 데이터가 없습니다.</div>',
                unsafe_allow_html=True,
            )
        else:
            top15 = cooc_df.head(15).sort_values("count")
            bar_colors = [
                TYPE_COLORS.get(t, "#888") for t in top15["neighbor_type"]
            ]
            fig_bar = go.Figure(
                go.Bar(
                    x=top15["count"],
                    y=top15["neighbor"],
                    orientation="h",
                    marker=dict(color=bar_colors, opacity=0.85),
                    text=top15["count"].apply(lambda v: f"{v:,}"),
                    textposition="outside",
                    textfont=dict(size=10, color="#888"),
                    hovertemplate="<b>%{y}</b><br>공출현: %{x:,}회<extra></extra>",
                )
            )
            apply_layout(fig_bar, height=520)
            fig_bar.update_layout(
                xaxis_title="공출현 횟수",
                yaxis=dict(tickfont=dict(size=11), automargin=True),
                margin=dict(l=8, r=60, t=20, b=40),
                bargap=0.25,
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # BRAND — no cooccurrence data
    st.markdown(
        """
        <div class="mfta-info" style="margin-bottom:24px;">
            브랜드 키워드는 공출현 네트워크 데이터가 제공되지 않습니다.
            아래 시즌 추이와 커뮤니티 비중 차트를 참고하세요.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="mfta-divider">', unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# Section B: Season Trend + Community Share
# ═════════════════════════════════════════════════════════════════════════════
trend_col, comm_col = st.columns([3, 2], gap="large")

# ── B1: Season Trend Line Chart ───────────────────────────────────────────────
with trend_col:
    st.markdown(
        """
        <div class="mfta-chart-container">
            <div class="mfta-chart-title">시즌별 언급량 추이</div>
            <div class="mfta-chart-sub">봄·여름·가을·겨울 시즌 단위 언급 빈도</div>
        """,
        unsafe_allow_html=True,
    )
    if kw_season.empty:
        st.markdown(
            '<div class="mfta-info">해당 키워드의 시즌 데이터가 없습니다.</div>',
            unsafe_allow_html=True,
        )
    else:
        season_marker_colors = {
            "Spring": "#98FB98",
            "Summer": "#FFD700",
            "Fall":   "#DEB887",
            "Winter": "#87CEEB",
        }
        fig_trend = go.Figure()

        # Main line
        fig_trend.add_trace(
            go.Scatter(
                x=kw_season["SEASON_YEAR_KO"],
                y=kw_season["count"],
                mode="lines+markers",
                name=active_keyword,
                line=dict(color="#C9A96E", width=2.5),
                marker=dict(
                    size=9,
                    color=[season_marker_colors.get(s, "#C9A96E") for s in kw_season["SEASON"]],
                    line=dict(color="#C9A96E", width=1.5),
                ),
                fill="tozeroy",
                fillcolor="rgba(201,169,110,0.08)",
                hovertemplate=(
                    "<b>%{x}</b><br>언급량: %{y:,}회<extra></extra>"
                ),
            )
        )
        apply_layout(fig_trend, height=380)
        fig_trend.update_layout(
            xaxis=dict(
                tickangle=-35,
                tickfont=dict(size=10),
                gridcolor="#1A1A1A",
            ),
            yaxis_title="언급량",
            showlegend=False,
            margin=dict(l=16, r=16, t=20, b=60),
        )

        # Season color legend as annotation
        season_legend_html = " &nbsp;".join(
            f'<span style="color:{c};font-size:11px;">● {label}</span>'
            for (label, c) in [("봄","#98FB98"),("여름","#FFD700"),("가을","#DEB887"),("겨울","#87CEEB")]
        )
        st.plotly_chart(fig_trend, use_container_width=True)
        st.markdown(
            f'<div style="text-align:center;margin-top:-8px;">{season_legend_html}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
# ── B2: Community Share Bar Chart ─────────────────────────────────────────────
with comm_col:
    st.markdown(
        """
        <div class="mfta-chart-container">
            <div class="mfta-chart-title">커뮤니티별 언급 비중</div>
            <div class="mfta-chart-sub">전체 게시글 대비 해당 커뮤니티 내 비중</div>
        """,
        unsafe_allow_html=True,
    )
    if kw_comm.empty:
        st.markdown(
            '<div class="mfta-info">해당 키워드의 커뮤니티 데이터가 없습니다.</div>',
            unsafe_allow_html=True,
        )
    else:
        kw_comm_sorted = kw_comm.sort_values("share", ascending=True)
        comm_colors = [
            COMMUNITY_COLORS.get(c, "#888") for c in kw_comm_sorted["COMMUNITY"]
        ]
        fig_comm = go.Figure(
            go.Bar(
                x=kw_comm_sorted["share"] * 100,
                y=kw_comm_sorted["COMMUNITY"],
                orientation="h",
                marker=dict(color=comm_colors, opacity=0.85),
                text=[f"{v*100:.1f}%" for v in kw_comm_sorted["share"]],
                textposition="outside",
                textfont=dict(size=11, color="#888"),
                hovertemplate=(
                    "<b>%{y}</b><br>언급 비중: %{x:.2f}%<extra></extra>"
                ),
            )
        )
        apply_layout(fig_comm, height=380)
        fig_comm.update_layout(
            xaxis_title="언급 비중 (%)",
            xaxis=dict(ticksuffix="%", gridcolor="#1A1A1A"),
            yaxis=dict(automargin=True),
            margin=dict(l=8, r=70, t=20, b=40),
            bargap=0.3,
            showlegend=False,
        )
        st.plotly_chart(fig_comm, use_container_width=True)

        # Raw counts table toggle
        with st.expander("원본 수치 보기"):
            display_df = kw_comm_sorted[["COMMUNITY", "count", "total", "share"]].copy()
            display_df["share"] = (display_df["share"] * 100).round(2).astype(str) + "%"
            display_df.columns = ["커뮤니티", "언급수", "전체 게시글", "비중"]
            st.dataframe(display_df, hide_index=True, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
