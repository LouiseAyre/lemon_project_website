import streamlit as st
import requests
import base64

# url='http://localhost:8000/predict' #this is a local api
url ="https://lemonprojectapi-tjtjmdtcna-de.a.run.app/predict"

lemon_background = "https://storage.googleapis.com/wagon-data-852-chin/lemon_background.png"
lemon_bg = "https://storage.googleapis.com/wagon-data-852-chin/lemon_bg.png"

page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://storage.googleapis.com/wagon-data-852-chin/lemon_background.png");
    background-size: cover;
    }
    </style>
    '''

st.write(page_bg_img, unsafe_allow_html=True)

# set_png_as_page_bg('lemon_background.png')
# st.markdown(set_png_as_page_bg('lemon_background.png'), unsafe_allow_html=True)

def lemon_health(new_image):
    files = {"file": (new_image.name, new_image, "multipart/form-data")}
    response = requests.post(url,files=files).json()
    health_rating = response['health']

    if type(health_rating) == str:
        health = "No lemon found, please try again"
    if health_rating > 0.9:
        health = "Unhealthy"
    else:
        health = "Healthy"
    return health

st.markdown("**Lemon Health Assessment**")

direction = st.radio('Select an option',('Upload jpg','Take a picture'))


if direction == 'Upload jpg':
    new_image = st.file_uploader("Upload jpg", type=".jpg", accept_multiple_files=False)
else:
    direction == 'Take a picture'
    new_image = st.camera_input("Take a picture")


if new_image is not None:
    st.write("Image uploaded")
    st.image(new_image, width=300)
    health_rating = lemon_health(new_image)
    st.write("Lemon health:", health_rating)
else:
    st.write("Please upload image")
