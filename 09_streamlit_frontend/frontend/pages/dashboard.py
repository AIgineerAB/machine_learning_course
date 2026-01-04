import streamlit as st
import httpx
import pandas as pd


data = httpx.get("http://127.0.0.1:8000/books").json()
df = pd.DataFrame(data)


st.markdown("# Books dashboard")

st.markdown("Some statistics and metrics about our books")

st.markdown("## KPIs")

st.markdown("Here we use st.columns to divide into columns and place an st.metric in each column")

cols = st.columns(4)

with cols[0]:
    st.metric("total books", len(df))
with cols[1]:
    st.metric("old books", len(df.query("year < 1860")))
with cols[2]:
    st.metric("newer books", len(df.query("year > 1860")))
with cols[3]:
    st.metric("unique authors", len(df["author"].unique()))


st.markdown(
    "older books refer to books before 1860 and newer ones refer to those after 1860"
)

st.markdown("## Year distribution")

st.markdown("There are several ways to plot using streamlit. Here is an example using matplotlib and st.pyplot")

ax = df["year"].plot(
    kind="hist",
    xlabel="year",
    ylabel="count",
    title="Year distribution for all available books",
)
fig = ax.get_figure()

st.pyplot(fig)


st.markdown("## All available books")
st.dataframe(data)
