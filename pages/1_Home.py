import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sthayee | Home", layout="wide")

# 🔹 Inject Custom CSS
st.markdown("""
    <style>
    .hero {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
        padding: 60px 0;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .hero img {
        max-height: 250px;
        margin-top: 20px;
    }
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 40px;
        border-left: 5px solid #6a11cb;
        padding-left: 15px;
    }
    .feature-img {
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
    }
    .feature-img:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 🔹 Hero Section
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown("<h1>🎵 Welcome to Sthayee</h1>", unsafe_allow_html=True)
st.markdown("<p>An immersive blend of Indian Classical Music & Modern Tech</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Hero Image
st.image("assets/images/hero.png", use_container_width=True)

# 🔹 About Section
st.markdown('<div class="section-title">About Sthayee</div>', unsafe_allow_html=True)
st.write("""
**Sthayee** is a platform that preserves the heritage of Indian Classical Music 
while embracing digital interactivity. What started as a simple static website has now transformed 
into a full-featured app experience with audio, visuals, and musical learning tools.
""")

# 🔹 Feature Previews
st.markdown('<div class="section-title">Explore the App</div>', unsafe_allow_html=True)

cols = st.columns(3)
with cols[0]:
    st.image("assets/images/music_store.png", caption="🎧 Music Player", use_container_width=True)
with cols[1]:
    st.image("assets/images/tabla.png", caption="🎼 Instruments", use_container_width=True)
with cols[2]:
    st.image("assets/images/blog2.png", caption="🖼️ Gallery", use_container_width=True)

st.success("Navigate using the sidebar to explore each feature!")
