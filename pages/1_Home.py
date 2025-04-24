import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sthayee | Home", layout="wide")

st.title("🎵 Welcome to Sthayee")
st.markdown("##### Blending Classical Music with a Modern Experience")

# Hero Image
st.image("assets/images/hero.png", use_column_width=True)

st.markdown("---")
st.header("🧠 About Sthayee")
st.write("""
**Sthayee** is a creative platform that integrates the richness of Indian classical music with modern technology. 
This app is built as a complete reimagining of the original web experience, bringing in interactivity, audio, visual storytelling, and cultural depth.
""")

# Highlight some of the areas covered
st.markdown("### 🌟 Key Sections")
cols = st.columns(3)
with cols[0]:
    st.image("assets/images/tabla.png", caption="Instrument Explorer", use_column_width=True)
with cols[1]:
    st.image("assets/images/blog2.png", caption="Portfolio & Gallery", use_column_width=True)
with cols[2]:
    st.image("assets/images/team-1.jpg", caption="Meet Our Team", use_column_width=True)

st.markdown("---")
st.success("Explore more using the sidebar on the left 👉")
