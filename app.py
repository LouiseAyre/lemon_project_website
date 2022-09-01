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

    if health_rating > 0.9:
        health = "Unhealthy"
    else:
        health = "Healthy"
    return health

st.markdown("**Lemon Health Assessment**")

direction = st.radio('Select an option',('upload jpg','take a picture'))


if direction == 'upload jpg':
    new_image = st.file_uploader("Upload jpg", type=".jpg", accept_multiple_files=False)
else:
    direction == 'take a picture'
    new_image = st.camera_input("Take a picture")


if new_image is not None:
    st.write("image uploaded")
    st.image(new_image, width=300)
    health_rating = lemon_health(new_image)
    st.write("health of lemon:", health_rating)
else:
    st.write("please upload image")
