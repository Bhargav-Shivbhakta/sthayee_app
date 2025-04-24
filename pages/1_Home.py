import streamlit as st

st.set_page_config(page_title="Sthayee | Home", layout="wide")

# Custom CSS for styling everything
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Josefin Sans', sans-serif;
    }

    .hero-container {
        padding: 80px 40px;
        background: linear-gradient(120deg, #6a11cb, #2575fc);
        color: white;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 50px;
    }

    .hero-container h1 {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .hero-container p {
        font-size: 1.3rem;
        font-weight: 300;
        opacity: 0.95;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 600;
        margin-top: 50px;
        margin-bottom: 20px;
        border-left: 5px solid #6a11cb;
        padding-left: 15px;
        color: #222;
    }

    .card {
        background: #ffffff;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        padding: 20px;
        text-align: center;
        transition: transform 0.2s ease;
    }

    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 25px rgba(0,0,0,0.2);
    }

    .card img {
        border-radius: 12px;
        margin-bottom: 10px;
        height: 180px;
        object-fit: cover;
    }

    .cta-box {
        margin-top: 60px;
        padding: 40px;
        background-color: #f4f7ff;
        text-align: center;
        border-radius: 12px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    }

    .cta-box h3 {
        font-size: 2rem;
        color: #6a11cb;
        margin-bottom: 10px;
    }

    .cta-box p {
        font-size: 1.2rem;
    }

    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.markdown("<h1>🎵 Welcome to Sthayee</h1>", unsafe_allow_html=True)
st.markdown("<p>Where the timeless beauty of Indian classical music meets the magic of modern technology.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Mission & Vision Section
st.markdown('<div class="section-title">Our Vision & Mission</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("🎯 Vision")
    st.write("""
    To bridge the gap between tradition and technology by providing a unique digital experience for classical music lovers, students, and artists.
    """)
with col2:
    st.subheader("🚀 Mission")
    st.write("""
    To preserve and promote the heritage of Indian classical instruments, ragas, and rhythms through modern interfaces, interactivity, and immersion.
    """)

# Features Section
st.markdown('<div class="section-title">Explore the Features</div>', unsafe_allow_html=True)

feature_cols = st.columns(3)
with feature_cols[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("assets/images/music_store.png", caption=None, use_container_width=True)
    st.subheader("🎧 Music Player")
    st.write("Play, explore, and experience hand-picked classical tunes.")
    st.markdown("</div>", unsafe_allow_html=True)

with feature_cols[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("assets/images/tabla.png", caption=None, use_container_width=True)
    st.subheader("🎼 Instruments")
    st.write("Discover traditional instruments with visuals and stories.")
    st.markdown("</div>", unsafe_allow_html=True)

with feature_cols[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("assets/images/blog2.png", caption=None, use_container_width=True)
    st.subheader("🖼️ Portfolio")
    st.write("Browse through our visual and creative galleries.")
    st.markdown("</div>", unsafe_allow_html=True)

# Call to Action
st.markdown('<div class="cta-box">', unsafe_allow_html=True)
st.markdown("<h3>🔎 Ready to Dive Deeper?</h3>", unsafe_allow_html=True)
st.markdown("<p>Use the sidebar to navigate and explore all the rich sections Sthayee has to offer.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
