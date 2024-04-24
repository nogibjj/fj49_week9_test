import streamlit as st
import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.content


def main():
    st.title("Image Captioning App")
    st.write("Enter a description and let the model generate a caption for it.")

    description = st.text_input("Enter a description:")
    if st.button("Generate Caption"):
        if description:
            image_bytes = query({"inputs": description})
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Caption", use_column_width=True)
        else:
            st.warning("Please enter a description.")


if __name__ == "__main__":
    main()
