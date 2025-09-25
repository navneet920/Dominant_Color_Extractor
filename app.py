import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw

# Function to create color palette
def create_color_palette(dominant_colors, palette_size=(300, 50)):
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)
    swatch_width = palette_size[0] // len(dominant_colors)
    for i, color in enumerate(dominant_colors):
        draw.rectangle(
            [i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]],
            fill=tuple(map(int, color))
        )
    return palette

# Streamlit UI
st.title("🎨 Dominant Color Extractor")
st.write("Upload an image and extract its top dominant colors using KMeans clustering.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "jfif"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to array
    img_array = np.array(image)
    img_data = img_array.reshape((-1, 3))  # Flatten into RGB pixels

    # Sidebar controls
    st.sidebar.header("⚙️ Settings")
    n_clusters = st.sidebar.slider("Number of colors", 2, 10, 3)
    palette_width = st.sidebar.slider("Palette Width", 100, 600, 300)
    palette_height = st.sidebar.slider("Palette Height", 30, 150, 50)

    # Apply KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    kmeans.fit(img_data)
    top_colors = kmeans.cluster_centers_

    # Show palette
    st.subheader("Dominant Colors")
    palette_img = create_color_palette(top_colors, (palette_width, palette_height))
    st.image(palette_img, caption=f"Top {n_clusters} Colors", use_container_width=False)

    # Show hex values
    st.subheader("Hex Codes")
    hex_colors = ['#%02x%02x%02x' % tuple(map(int, color)) for color in top_colors]
    st.write(hex_colors)

    # Optionally show pie chart
    if st.checkbox("Show Pie Chart of Color Distribution"):
        labels, counts = np.unique(kmeans.labels_, return_counts=True)
        plt.pie(counts, labels=hex_colors, colors=hex_colors, autopct='%1.1f%%')
        st.pyplot(plt.gcf())
