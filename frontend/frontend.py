import streamlit as st
import requests

# Streamlit UI
def main():
    st.set_page_config(page_title="Super Resolution Image App", page_icon=":camera:", layout="wide")

    col1, col2 = st.columns(2)

    with col1:
        st.title('PIXEL : Super Resolution Image Web App')
        st.write('Upload a low resolution image and let our AI model enhance it for you.')

    with col2:
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        col1, col2 = st.columns(2)

        with col1:
            st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True, output_format='PNG')

        with col2:
            # Display the super-resolved image
            if st.button('Super Resolution'):
                st.write("Check the sidebar for the Super Resolved Image.")
                # Send the image to the backend for processing
                response = requests.post('http://localhost:5000/upload', files={'file': uploaded_file})
                if response.status_code == 200:
                    # Display the super-resolved image
                    st.sidebar.title('Converted to Super Resolution Image')
                   
                    st.sidebar.markdown("")
                    st.sidebar.image(f'http://localhost:5000/results/{response.text}', caption='', use_column_width=True)

                    # Provide download link for the super-resolved image
                    download_link = f'<a href="http://localhost:5000/results/{response.text}" download>Click here to download the Enhanced Image</a>'
                    st.sidebar.markdown(download_link, unsafe_allow_html=True)
                    
                else:
                    st.sidebar.markdown("Failed to enhance image. Please try again.")
                    

if __name__ == "__main__":
    main()
