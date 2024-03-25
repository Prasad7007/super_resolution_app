# Super Resolution Web App

This is a web application built with Flask and Streamlit for performing super-resolution on images. Super-resolution is the process of enhancing the resolution of an image to produce a higher-resolution version while preserving details and reducing noise.

## Overview

The Super Resolution Web App consists of two main components:
- **Backend**: Built with Flask, the backend server handles image uploads, performs super-resolution processing using a deep learning model, and serves the super-resolved images.
- **Frontend**: Built with Streamlit, the frontend provides a user-friendly interface for uploading images, initiating super-resolution processing, and displaying the results.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the backend server by navigating to the `backend` directory and executing `python app.py`.
4. Run the frontend interface by navigating to the `frontend` directory and executing `streamlit run frontend.py`.

## Usage

1. Open the Streamlit web interface in your browser.
2. Upload an image using the file uploader in the sidebar.
3. Click the "Super Resolution" button to initiate the super-resolution process.
4. Once the processing is complete, the super-resolved image will be displayed along with a download link.

## Project Structure

1. **backend/**: This directory contains the backend code responsible for image super-resolution.
   - **app.py**: This file contains the Flask backend code.
   - **models/**: This folder stores pre-trained model files used for super-resolution.
     - **RRDB_ESRGAN_x4.pth**: Pre-trained model for ESRGAN.
     - **RRDB_PSNR_x4.pth**: Pre-trained model for PSNR.
   - **uploads/**: Folder for storing uploaded images.
   - **results/**: Folder for storing super-resolved images.
   - **RRDBNet_arch.py**: Definition of the RRDBNet architecture used in the models.

2. **frontend/**: This directory contains the frontend interface for the web application.
   - **frontend.py**: Streamlit frontend code.
   - **index.html**: HTML template for Streamlit frontend.

3. **models/**: This directory holds pre-trained model files.
   - **RRDB_ESRGAN_x4.pth**: Pre-trained model for ESRGAN.
   - **RRDB_PSNR_x4.pth**: Pre-trained model for PSNR.

4. **requirements.txt**: This file lists all the Python dependencies required to run the project.

5. **.gitignore**: Git ignore file to specify which files and directories to ignore when pushing to a Git repository.
   
## Dependencies

- Flask
- Streamlit
- opencv-python-headless
- numpy
- torch>=1.8.0

## Credits

- The super-resolution model architecture (`RRDBNet`) is based on the [ESRGAN](https://arxiv.org/abs/1809.00219) model.
- This project utilizes the [Streamlit](https://streamlit.io/) library for building the user interface.

## License

This project is licensed under the [MIT License](LICENSE).
