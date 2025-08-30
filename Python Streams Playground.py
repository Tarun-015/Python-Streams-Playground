import streamlit as st
import pandas as pd
from PIL import Image
import gzip
import io


st.set_page_config(page_title="Python Streams Playground", page_icon="📘", layout="wide")


st.sidebar.title("📂 Choose Stream Type")
option = st.sidebar.radio(
    "Select a demo:",
    ["🏷 Text Stream", "🖼 Image Stream", "📦 Compressed Stream", "📊 Large CSV Stream"]
)

st.sidebar.info("Upload a file based on the stream type you selected.")


st.title("📘 Python Streams Playground")
st.markdown(
    """
    <style>
    .big-font {font-size:20px !important;}
    </style>
    """,
    unsafe_allow_html=True
)
st.write("Explore different types of **Streams in Python** interactively!")


if option == "🏷 Text Stream":
    st.header("📄 Text Stream Demo")
    uploaded = st.file_uploader("Upload a text/CSV file", type=["txt", "csv"])
    if uploaded:
        st.success("File uploaded successfully!")
        st.write("Streaming file (first 10 lines):")
        for i, line in enumerate(uploaded):
            if i >= 10: break
            st.text(line.decode("utf-8").strip())

elif option == "🖼 Image Stream":
    st.header("🖼 Image Stream Demo")
    uploaded = st.file_uploader("Upload an Image", type=["jpg", "png"])
    if uploaded:
        st.success("Image uploaded successfully!")
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image", use_container_width=True)

elif option == "📦 Compressed Stream":
    st.header("📦 Compressed File Stream Demo")
    uploaded = st.file_uploader("Upload a .gz file", type=["gz"])
    if uploaded:
        st.success("Compressed file uploaded successfully!")
        with gzip.open(uploaded, "rt", encoding="utf-8") as f:
            st.write("First 5 lines from compressed file:")
            for i, line in enumerate(f):
                if i >= 5: break
                st.code(line.strip(), language="text")

elif option == "📊 Large CSV Stream":
    st.header("📊 Large CSV Stream Demo")
    uploaded = st.file_uploader("Upload a Large CSV", type=["csv"])
    if uploaded:
        st.success("Large CSV uploaded successfully!")
        st.info("Showing first chunk of 1000 rows...")
        for chunk in pd.read_csv(uploaded, chunksize=1000):
            st.write("Chunk shape:", chunk.shape)
            st.dataframe(chunk.head())
            break


st.sidebar.markdown("---")
st.sidebar.write("Made with Streamlit for learning **Streams in Python**")
st.sidebar.write("Made by :: Tarun Chaudhary")
