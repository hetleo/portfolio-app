import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Leon Bang-Hetlevik")
    content = """
Hei!

Jeg heter Leon, og jeg er en bibliotekar med lidenskap for teknologi. 
Jeg er en problemløser, en veileder og en nysgjerrig sjel som leter etter nye måter å bruke teknologi til å forbedre folks liv.
Når jeg ikke er omgitt av bøker, liker jeg å utforske nye teknologier og leke meg med Python.

På denne nettsiden kan du finne ut mer om mine prosjekter.

Er du nysgjerrig? Ta en titt og bli med på eventyret!
"""
    st.info(content)