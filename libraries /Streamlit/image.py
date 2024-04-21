import streamlit as st
from PIL import Image

# Set page title
st.title('Image Uploader App')

# Add an image uploader widget
uploaded_image = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

# Process the uploaded image
if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Optional: Perform image processing or analysis here
    # For example, you can apply filters, detect objects, or perform any other image-related tasks
