import requests
import streamlit as st
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

#output = query("image.jpg")

st.file_uploader("uplode an image file",type="jpg")