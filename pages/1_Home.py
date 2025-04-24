import streamlit as st

st.set_page_config(page_title="Sthayee | Home", layout="wide")

# Inject elegant CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;600&family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'EB Garamond', serif;
        background-color: #fdfdfd;
        color: #1e1e1e;
    }

    .hero {
        padding: 80px 60px 40px;
        text-align: center;
    }

    .hero h1 {
        font-size: 3.5rem;
        font-weight: 600;
        margin-bottom: 0.3em;
    }

    .hero p {
        font-size: 1.2rem;
        font-style: italic;
        opacity: 0.8;
        max-width: 800px;
        margin: 0 auto;
    }

    .section {
        padding: 30px 60px;
        margin-top: 40px;
    }

    .feature-title {
        font-size: 1.7rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .feature-text {
        font-size: 1.05rem;
        opacity: 0.9;
    }

    .subtle-box {
        background-color: #f7f8fa;
        padding: 30px;
        border-radius: 12px;
        margin-top: 30px;
    }

    .image-rounded {
        border-radius: 12px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown("<h1>Welcome to Sthayee</h1>", unsafe_allow_html=True)
st.markdown("""
<p>
A timeless journey through the echoes of Indian classical music, reimagined through elegant digital storytelling.
</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.image("assets/images/hero.png", use_container_width=True)

# Intro Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="feature-title">Our Vision</div>', unsafe_allow_html=True)
st.markdown("""
<div class="feature-text">
To preserve and promote the essence of Indian classical music through an immersive, minimalist digital experience that feels timeless and powerful.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Features Section
st.markdown('<div class="section subtle-box">', unsafe_allow_html=True)
st.markdown('<div class="feature-title">Explore the Experience</div>', unsafe_allow_html=True)

cols = st.columns(3)
with cols[0]:
    st.image("assets/images/music_store.png", use_container_width=True)
    st.markdown("**🎧 Music Player**")
    st.caption("Listen to handpicked tracks from classical archives.")

with cols[1]:
    st.image("assets/images/tabla.png", use_container_width=True)
    st.markdown("**🎼 Instruments**")
    st.caption("Discover the soul of Indian rhythm through visuals.")

with cols[2]:
    st.image("assets/images/blog2.png", use_container_width=True)
    st.markdown("**🖼️ Gallery**")
    st.caption("Explore the rich visuals and stories of tradition.")
st.markdown('</div>', unsafe_allow_html=True)

# Final CTA
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Begin your musical journey ➤</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; opacity: 0.7;'>Use the sidebar to navigate and experience Sthayee.</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
