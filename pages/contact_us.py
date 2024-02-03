import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("contact us")

with st.form("key=email form"):
    user_email = st.text_input("your email address")
    option = st.selectbox(
        "what topic do you want to discuss?",
        df["topic"])

    raw_message = st.text_area("Text")
    message = f"""\
Subject : New email delivered {user_email}
from:{user_email}
topic {option}
{raw_message}"""

    button = st.form_submit_button("submit")
    print(button)

    if button:
        send_email(message)
        st.info("your email was sent succesfully")
