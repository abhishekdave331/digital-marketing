import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
import io

# Configure API Key (set in environment or replace directly)
genai.configure(api_key=AIzaSyCVrrwxoQ5O6TMMCQL_kbfMW9Cpw9LoXcw)  # Or replace with your actual key
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get intelligence from model
def get_image_text(prompt, image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    response = model.generate_content(
        [prompt, image_bytes],
        stream=False,
    )
    return response.text.strip()

# Streamlit UI
st.header("Image to Text Application", divider=True)

# User inputs
prompt = st.text_input("Enter the prompt")
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Process on submit
if prompt and uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Submit"):
        with st.spinner("Generating response..."):
            result = get_image_text(prompt, image)
        st.markdown("### 📝 Output:")
        st.success(result)
