import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sthayee | Instruments", layout="wide")
st.title("🎻 Explore Classical Instruments")

st.write("Here are some iconic instruments that shape Indian classical music:")

# Instrument List (Image filename, Display name)
instruments = [
    ("tabla.png", "Tabla"),
    ("tanpura_1.png", "Tanpura"),
    ("veena.png", "Veena"),
    ("taal_library.png", "Taal"),
    ("raga_library.png", "Raga Visualization"),
]

cols = st.columns(3)
for index, (img_file, label) in enumerate(instruments):
    with cols[index % 3]:
        st.image(f"assets/images/{img_file}", caption=label, use_column_width=True)
