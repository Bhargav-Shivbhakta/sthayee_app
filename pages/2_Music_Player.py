import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Sthayee | Music", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
    .music-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        text-align: center;
        margin-top: 40px;
    }
    .music-card h3 {
        color: #6a11cb;
        margin-bottom: 10px;
    }
    .music-card img {
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        max-height: 250px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎧 Sthayee Music Player")

# Check file
audio_path = "assets/audio/ilahi.mp3"
image_path = "assets/images/music_store.png"

if os.path.exists(audio_path):
    st.markdown('<div class="music-card">', unsafe_allow_html=True)

    st.image(image_path, use_container_width=True)  # 🔁 FIXED HERE

    st.markdown("<h3>Now Playing: Ilahi</h3>", unsafe_allow_html=True)

    audio_bytes = open(audio_path, 'rb').read()
    st.audio(audio_bytes, format="audio/mp3")

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.error("Audio file not found. Please check the path or filename.")
