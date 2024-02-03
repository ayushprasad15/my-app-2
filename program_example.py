import streamlit as st
import webbrowser
import pandas


st.set_page_config(layout="wide")

content = """The Best Company """
st.title(content)

content1 = """It's important to note that the "best" company for one person may not be the best for another,
as individual preferences and priorities vary. Additionally, what may be considered the best company at one point in
time may change due to evolving circumstances """
st.write(content1)

st.write("<h1>Our Team</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("csv_files.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("img/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("img/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("img/" + row["image"])
