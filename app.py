import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Sthayee App", layout="wide")

# Sidebar Navigation
st.sidebar.title("🎵 Sthayee Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Music Player", "Instruments", "Portfolio", "Music Store"])


# Page Logic
if selection == "Home":
    st.title("🎶 Welcome to Sthayee")
    st.write("An interactive app built from our classical music-themed website.")
    
    image = Image.open("assets/images/hero.png")
    st.image(image, use_column_width=True)
    
    st.markdown("---")
    st.subheader("About Us")
    st.write("""
    **Sthayee** is a platform that blends classical Indian music with modern digital experiences.
    This app replicates and extends the web project with a fully interactive experience.
    """)
elif selection == "Music Player":
    exec(open("pages/2_Music_Player.py").read())
elif selection == "Instruments":
    exec(open("pages/3_Instruments.py").read())
elif selection == "Portfolio":
    exec(open("pages/4_Portfolio.py").read())
