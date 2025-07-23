import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from PIL import Image # This is for image Display 
import google.generativeai as genai

# Configure the Key and Initiate the Model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model=genai.GenerativeModel('gemini-1.5-flash')

# Create the front end of the Page
st.header('⛶IMAGE TO TEXT APPLICATION 📈',divider=True)
st.subheader('╰┈➤ Enter the Prompt',divider=True)
prompt=st.text_input(label='Enter Details',max_chars=10000)
uploaded_image=st.file_uploader('Upload the Image',type=['jpg','jpeg','png'])
submit=st.button(label='Build Campaign')

# Image Display
image=''
if uploaded_image is not None:
    image=Image.open(uploaded_image)
    st.image(image,use_container_width=True)

def get_llm_response(prompt, image):
    if prompt != "":
        response = model.generate_content([prompt , image])
    else:
        response = model.generate_content([prompt])
    return response.text

# Run the function
submit = st.button("Submit")
if submit:
    response = get_llm_response(prompt,image)
    st.subheader(":orange[Response:]")
    st.markdown(response)
