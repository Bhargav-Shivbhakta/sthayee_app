import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sthayee | Portfolio", layout="wide")
st.title("🖼️ Portfolio & Blog Highlights")

st.write("A glimpse into our creative work and project showcases:")

# Blog Section
st.subheader("📝 Blog Visuals")
blog_images = [
    "blog1png.png", "blog2.png", "blog3.png",
    "blog4png.png", "blog5.png", "blog6.png"
]

cols = st.columns(3)
for i, img in enumerate(blog_images):
    with cols[i % 3]:
        st.image(f"assets/images/{img}", caption=f"Blog {i+1}", use_column_width=True)

st.markdown("---")

# Portfolio Section
st.subheader("🎨 Portfolio Showcase")
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
        st.image(f"assets/images/{img}", caption=f"Portfolio {i+1}", use_column_width=True)
