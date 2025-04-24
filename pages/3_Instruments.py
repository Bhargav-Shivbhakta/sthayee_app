import streamlit as st

st.set_page_config(page_title="Sthayee | Instruments", layout="wide")
st.title("🎻 Explore Classical Instruments")

# Inject custom CSS
st.markdown("""
    <style>
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        margin: 30px 0 15px;
        border-left: 5px solid #6a11cb;
        padding-left: 15px;
    }
    .instrument-img {
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .instrument-img:hover {
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Featured Instruments</div>', unsafe_allow_html=True)

# Instruments: (Image filename, Display name)
instruments = [
    ("tabla.png", "Tabla"),
    ("tanpura_1.png", "Tanpura"),
    ("veena.png", "Veena"),
    ("taal_library.png", "Taal"),
    ("raga_library.png", "Raga Visualizer")
]

cols = st.columns(3)
for i, (img, name) in enumerate(instruments):
    with cols[i % 3]:
        st.image(f"assets/images/{img}", caption=name, use_container_width=True, output_format="auto")
