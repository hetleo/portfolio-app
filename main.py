import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=150)

with col2:
    st.title("Leon Bang-Hetlevik")
    content = """
Hei!

Jeg heter Leon, og dette mitt lille hjørne av internett. Denne siden bruker jeg 
til å teste forskjellige programmeringsprosjekt. 

Er du nysgjerrig? Ta en titt og bli med på eventyret!
"""
    st.info(content)

content2 = """
Resten av denne siden er viet til å vise frem mine prosjekt. 
Du kan trykke deg inn på de enkelte prosjektene for å lese mer og finne lenke til koden på Github.
"""
st.write(content2)