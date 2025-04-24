import streamlit as st

st.set_page_config(page_title="Sthayee | Home", layout="wide")

# Inject CSS with background image and hero alignment
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: url('assets/images/background.png') no-repeat center center fixed;
        background-size: cover;
    }

    .glass {
        background: rgba(255, 255, 255, 0.88);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 3rem auto;
        width: 90%;
        max-width: 1100px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }

    .glass::before {
        content: "";
        background: url('assets/images/logo-faded.png') no-repeat center center;
        background-size: 280px;
        opacity: 0.08;
        position: absolute;
        top: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        height: 100%;
        z-index: 0;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #1a1a1a;
        z-index: 1;
        position: relative;
        margin-bottom: 10px;
    }

    .hero-tagline {
        font-size: 1.2rem;
        font-style: italic;
        text-align: center;
        max-width: 700px;
        margin: 0 auto;
        color: #444;
        z-index: 1;
        position: relative;
    }

    .section-title {
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 2.5rem;
        border-left: 5px solid #6a11cb;
        padding-left: 15px;
        color: #333;
    }

    .feature-card {
        border-radius: 16px;
        background-color: #ffffff;
        box-shadow: 0 8px 18px rgba(0,0,0,0.06);
        padding: 1.5rem;
        transition: 0.3s;
        text-align: center;
    }

    .feature-card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 24px rgba(0,0,0,0.1);
    }

    .feature-card img {
        border-radius: 12px;
        margin-bottom: 10px;
        height: 180px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# Start glass box
st.markdown('<div class="glass">', unsafe_allow_html=True)

# Hero text
st.markdown('<div class="hero-title">Welcome to Sthayee</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-tagline">A minimalist journey through the timeless soul of Indian classical music</div>', unsafe_allow_html=True)

# Hero image
st.image("assets/images/hero.png", use_container_width=True)

# Vision section
st.markdown('<div class="section-title">Our Vision</div>', unsafe_allow_html=True)
st.write("""
To create a modern, immersive experience that bridges the sacred essence of Indian classical music with modern digital design. Sthayee is not just a platform — it's a movement to preserve emotion, rhythm, and cultural elegance.
""")

# Feature cards
st.markdown('<div class="section-title">Explore the Experience</div>', unsafe_allow_html=True)
cols = st.columns(3)
with cols[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.image("assets/images/music_store.png", use_container_width=True)
    st.subheader("🎧 Music Player")
    st.caption("Handpicked classical tracks from heritage collections.")
    st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.image("assets/images/tabla.png", use_container_width=True)
    st.subheader("🎼 Instruments")
    st.caption("Discover and explore Indian instruments visually.")
    st.markdown('</div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.image("assets/images/blog2.png", use_container_width=True)
    st.subheader("🖼️ Gallery")
    st.caption("A visual diary of tradition, rhythm, and storytelling.")
    st.markdown('</div>', unsafe_allow_html=True)

# Close glass
st.markdown('</div>', unsafe_allow_html=True)
