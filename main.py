import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns([1,3])

style = """
<style>
div[data-testid="st.Image"]{
  float: right;
}
</style>
"""

with col1:
    st.markdown(style, unsafe_allow_html=True)
    st.image("images/photo.png", width=150)

with col2:
    st.title("Leon Bang-Hetlevik")
    content = """
Hei!

Jeg er Leon, og dette mitt lille hjørne av internett. Denne siden bruker jeg 
til å teste forskjellige programmeringsprosjekt. 

Er du nysgjerrig? Ta en titt og bli med på eventyret!
"""
    st.info(content)

content2 = """
Resten av denne siden viser mine prosjekt. 
Du kan trykke på Source Code for å komme til koden på Github.
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
 
with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])