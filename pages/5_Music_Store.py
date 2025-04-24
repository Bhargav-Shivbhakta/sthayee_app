import streamlit as st

st.set_page_config(page_title="Sthayee | Music Store", layout="wide")
st.title("🛍️ Digital Music Store")

# Inject CSS for image card style
st.markdown("""
    <style>
    .store-img {
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .store-img:hover {
        transform: scale(1.03);
    }
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        margin: 30px 0 15px;
        border-left: 5px solid #6a11cb;
        padding-left: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Instrument Visual Showcase</div>', unsafe_allow_html=True)

store_images = [
    "store1.png", "store2.png", "store3.png", "store4.png",
    "store5.png", "store6.png", "storeimg.png", "sthayee.png", "sthayee1.png"
]

cols = st.columns(3)
for i, img in enumerate(store_images):
    with cols[i % 3]:
        st.image(f"assets/images/{img}", caption=f"Store {i+1}", use_container_width=True, output_format="auto")
