import streamlit as st
import pandas
from send_email import send_email


df = pandas.read_csv("/Users/leon/prosjekt/portfolio-app/topics.csv")
topics = df["Topics"].tolist()
topics.insert(0, "Velg et tema...")

st.header("Kontakt meg")

with st.form(key="kontakt_skjema"):
    user_email = st.text_input("Din epost-adresse")
    topic = st.selectbox("Hva gjelder henvendelsen?", topics)
    raw_message = st.text_area("Din melding her")
    message = f"""\
Subject: Ny epost - {topic}

Fra: {user_email}

{raw_message}
"""
    button = st.form_submit_button("Send melding")
    if button:
        send_email(message)
        st.info("E-posten er sendt!")
    