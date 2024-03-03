import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns([1,3])

with col1:
    st.image("images/photo.png", width=150)

with col2:
    st.title("Leon Bang-Hetlevik")
    content = """
Hei!

Jeg er Leon, og dette mitt lille hjørne av internett. Her vil jeg 
legge ut forskjellige programmeringsprosjekt.

Er du nysgjerrig? Ta en titt og bli med på eventyret!
"""
    st.info(content)

content2 = """
Resten av denne siden viser mine prosjekt. 
Du kan trykke på Source Code for å komme til koden på Github.
"""
st.write(content2)

st.divider()

col3, empty_col, col4 = st.columns([1.5, 0.3,1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.image("images/" + row["image"], width=150)
        st.header(row["title"])
        st.write(row["description"])
        st.write("[Source code on Github](https://github.com/hetleo)")
        st.divider()
 
with col4:
    for index, row in df[11:].iterrows():
        st.image("images/" + row["image"], width=150)
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Source code on Github]({row['url']})")
        st.divider()