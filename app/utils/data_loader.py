import streamlit as st
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data" / "dashboard"

COMMUNITY_LABELS = {
    "ZZ": "Z9DY (짱구대디랑)",
    "KK": "KKST (깡스타일리스트)",
    "FS": "FIT THE SIZE (핏더사이즈)",
    "HA": "HAO (How About OOTD)",
    "GO": "GOCD (Go Out Casually Dressed)",
}

COMMUNITY_COLORS = {
    "FIT THE SIZE": "#C9A96E",
    "GOCD":         "#4A90D9",
    "HAO":          "#7B68EE",
    "KKST":         "#50C878",
    "Z9DY":         "#FF6B6B",
}

TYPE_LABELS = {
    "BRAND": "브랜드",
    "ITEM":  "아이템",
    "STYLE": "스타일",
}

TYPE_COLORS = {
    "BRAND": "#E05555",
    "ITEM":  "#50C878",
    "STYLE": "#4A90D9",
}

SEASON_ORDER = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
SEASON_KO    = {"Spring": "봄", "Summer": "여름", "Fall": "가을", "Winter": "겨울"}


@st.cache_data
def load_cooccur():
    item_item   = pd.read_parquet(DATA_DIR / "cooccur_item_item.parquet")
    style_style = pd.read_parquet(DATA_DIR / "cooccur_style_style.parquet")
    item_style  = pd.read_parquet(DATA_DIR / "cooccur_item_style.parquet")
    return item_item, style_style, item_style


@st.cache_data
def load_keyword_season():
    df = pd.read_parquet(DATA_DIR / "keyword_season_count.parquet")
    df["_sort"] = df["YEAR"] * 10 + df["SEASON"].map(SEASON_ORDER)
    df = df.sort_values("_sort").drop(columns=["_sort"])
    df["SEASON_KO"] = df["SEASON"].map(SEASON_KO)
    df["SEASON_YEAR_KO"] = df["YEAR"].astype(str) + " " + df["SEASON_KO"]
    return df


@st.cache_data
def load_keyword_comm():
    return pd.read_parquet(DATA_DIR / "keyword_comm_share.parquet")


_EXCLUDE_TOKENS = {"acc", "bottom", "outer", "핏이"}

@st.cache_data
def get_all_tokens():
    df = load_keyword_season()
    return {
        t: sorted(
            tok for tok in df[df["TOKEN_TYPE"] == t]["token"].unique().tolist()
            if tok not in _EXCLUDE_TOKENS
        )
        for t in ["BRAND", "ITEM", "STYLE"]
    }


def get_cooccurrence(keyword: str, token_type: str, top_n: int = 25):
    """Return DataFrame of co-occurring keywords with columns: neighbor, neighbor_type, count."""
    item_item, style_style, item_style = load_cooccur()
    parts = []

    if token_type == "ITEM":
        a = item_item[item_item["item_a"] == keyword][["item_b", "count"]].rename(columns={"item_b": "neighbor"})
        b = item_item[item_item["item_b"] == keyword][["item_a", "count"]].rename(columns={"item_a": "neighbor"})
        combined = pd.concat([a, b]).groupby("neighbor", as_index=False)["count"].sum()
        combined["neighbor_type"] = "ITEM"
        parts.append(combined)

        s = item_style[item_style["item"] == keyword][["style", "count"]].rename(columns={"style": "neighbor"})
        s["neighbor_type"] = "STYLE"
        parts.append(s)

    elif token_type == "STYLE":
        a = style_style[style_style["style_a"] == keyword][["style_b", "count"]].rename(columns={"style_b": "neighbor"})
        b = style_style[style_style["style_b"] == keyword][["style_a", "count"]].rename(columns={"style_a": "neighbor"})
        combined = pd.concat([a, b]).groupby("neighbor", as_index=False)["count"].sum()
        combined["neighbor_type"] = "STYLE"
        parts.append(combined)

        i = item_style[item_style["style"] == keyword][["item", "count"]].rename(columns={"item": "neighbor"})
        i["neighbor_type"] = "ITEM"
        parts.append(i)

    if not parts:
        return pd.DataFrame(columns=["neighbor", "neighbor_type", "count"])

    result = pd.concat(parts).sort_values("count", ascending=False).head(top_n).reset_index(drop=True)
    return result
