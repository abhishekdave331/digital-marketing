import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
import io

# Configure API Key (make sure it's set in environment or manually add here)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Replace with your key if needed

# Initialize Gemini multimodal model
model = genai.GenerativeModel("gemini-1.5-flash")


st.header("Image to Text Application", divider=True)
prompt = st.text_input("Enter the prompt")
st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

image = ""

if uploaded_image is not None:
  image = Image.open(uploaded_image)
  st.image(image)
