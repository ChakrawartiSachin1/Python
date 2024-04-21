import streamlit as st
from PIL import Image
import pytesseract

# Set page title
st.set_page_config(page_title='OCR App')

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Function to perform OCR
def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

# Main code
def main():
    # Title
    st.title('Image Text Extraction')

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # If image is uploaded
    if uploaded_file is not None:
        # Open uploaded image
        image = Image.open(uploaded_file)

        # Display uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform OCR
        text = perform_ocr(image)

        # Display extracted text
        if text:
            st.subheader('Extracted Text:')
            st.write(text)
        else:
            st.warning('No text detected.')

if __name__ == "__main__":
    main()
