import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# Configure API Key (from environment variable)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get intelligence from model
def get_image_text(prompt, image):
    response = model.generate_content(
        [prompt, image],  # Pass PIL image directly
        stream=False,
    )
    return response.text.strip()

# Streamlit UI
st.header(" Image to Text Application", divider=True)

# User inputs
prompt = st.text_input("Enter the prompt")
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Process on submit
if prompt and uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Submit"):
                result = get_image_text(prompt, image)
                st.markdown("###  Output:")
                st.success(result)
