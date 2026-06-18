import streamlit as st
import pandas as pd


# -----------------
# PAGE CONFIG
# -----------------

st.set_page_config(
    page_title="குறள் தேடல் (Kural Quest)",
    page_icon="📖",
    layout="centered"
)


# -----------------
# LOAD DATA
# -----------------

@st.cache_data
def load_data():

    df = pd.read_csv("raw_kh.csv")

    df["Kural Number"] = (
        df["Kural Number"].astype(int)
    )

    return df


try:
    df = load_data()

except:
    st.error("raw_kh.csv not found")
    st.stop()


# -----------------
# HEADER
# -----------------

left_header, right_header = st.columns([4, 1])

with left_header:

    st.title("📖 Kural Quest")

    st.caption(
        "Explore the wisdom of Thirukkural"
    )

with right_header:

    st.image(
        "images/logo.png",
        width=140
    )

st.divider()


# -----------------
# SEARCH
# -----------------

left, right = st.columns([3, 1])

with left:

    kural_num = st.number_input(
        "Kural Number",
        min_value=1,
        max_value=1330,
        value=1
    )


with right:

    st.write("")


search = st.button(
    "🔍 Search",
    use_container_width=True
)


# -----------------
# RESULTS
# -----------------

if search:

    row = df[
        df["Kural Number"] == kural_num
    ]

    if row.empty:

        st.warning(
            "Kural not found"
        )

    else:

        r = row.iloc[0]

        c1, c2 = st.columns(2)

        with c1:

            st.text_input(
                "Section Name",
                str(r["Section Name"]),
                disabled=True
            )

        with c2:

            st.text_input(
                "Chapter Number",
                str(r["Chapter Number"]),
                disabled=True
            )

        st.text_input(
            "Chapter Name",
            str(r["Chapter Name"]),
            disabled=True
        )

        st.subheader("📜 Kural")

        st.text_area(
            "",
            str(r["Kural"]),
            height=120
        )

        st.subheader(
            "🌍 Translation"
        )

        st.text_area(
            "",
            str(r["Translation"]),
            height=150
        )

        st.subheader(
            "💡 Explanation"
        )

        st.text_area(
            "",
            str(r["Explanation"]),
            height=220
        )


st.divider()

st.caption(
    "Created by Gopikrishna"
)
