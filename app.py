import streamlit as st
import requests

st.markdown("Lemon Health Assessment")

new_image = st.file_uploader("Upload a jpg file", type=".jpg", accept_multiple_files=False)
if new_image is not None:
    st.write("uploaded jpg file...")
    st.image(new_image)

    url='http://localhost:8000/predict' #this is a local api

    files = {"file": (new_image.name, new_image, "multipart/form-data")}
    # response = {'health':0.5}
    response = requests.post(url,files=files).json()
    print("response", type(response), response.keys(), response['health'])
    health_rating = response['health']

    if health_rating <0.3:
        health = "Fairly healthy"
    elif health_rating >=0.3 and health_rating <= 0.6:
        health = "Not very healthy"
    else:
        health= "Unhealthy!"

    st.write("health of lemon:", health)

else:
    st.write("please upload image")
