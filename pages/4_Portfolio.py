import streamlit as st

st.set_page_config(page_title="Sthayee | Portfolio", layout="wide")
st.title("🖼️ Portfolio & Blog Showcase")

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
    .gallery-img {
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .gallery-img:hover {
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# Section 1: Blog Images
st.markdown('<div class="section-title">📝 Blog Visuals</div>', unsafe_allow_html=True)
blog_images = [
    "blog1png.png", "blog2.png", "blog3.png",
    "blog4png.png", "blog5.png", "blog6.png"
]

cols = st.columns(3)
for i, img in enumerate(blog_images):
    with cols[i % 3]:
        st.image(f"assets/images/{img}", caption=f"Blog {i+1}", use_container_width=True, output_format="auto")

# Section 2: Portfolio Grid
st.markdown('<div class="section-title">🎨 Project Portfolio</div>', unsafe_allow_html=True)
portfolio_images = [
    f"portfolio/portfolio-{i}.jpg" for i in range(1, 10)
] + [
    "portfolio/portfolio-details-1.jpg",
    "portfolio/portfolio-details-2.jpg",
    "portfolio/portfolio-details-3.jpg"
]

cols = st.columns(3)
for i, img in enumerate(portfolio_images):
    with cols[i % 3]:
        st.image(f"assets/images/{img}", caption=f"Project {i+1}", use_container_width=True, output_format="auto")
