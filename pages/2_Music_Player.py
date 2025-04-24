import streamlit as st
from PIL import Image
import os

st.title("🎧 Sthayee Music Player")

# Path to audio file
audio_file = "assets/audio/ilahi.mp3"

# Show album cover or a themed image
st.image("assets/images/music_store.png", width=400)

st.markdown("### Now Playing: Ilahi - Yeh Jawaani Hai Deewani")

# Check and play audio file
if os.path.exists(audio_file):
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')
else:
    st.error("Audio file not found. Please check the file path.")
