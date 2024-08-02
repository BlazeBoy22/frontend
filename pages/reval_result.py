import streamlit as st
import pandas as pd
import requests

# Apply CSS styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
       
            # background-image: linear-gradient(38deg, rgba(35, 28, 118, 0.7) 37%, rgba(200, 80, 192, 0.5) 26%, rgba(41, 86, 162, 0.6) 20%);
        
    }
    .stFileUploader {
        background-color: black;
        color: white;
    }
    .eczjsme18 .eczjsme11 {
            background-color: #03864d;
            color: black;
        }
    .eczjsme15 {
            color: black;
            font-size: 1.3rem;
        }
        .eczjsme18 .eczjsme11 {
            font-family: "Lucida Console", "Courier New", monospace;
            background: rgba(238,174,202,0.7);/* Green with transparency */
            background-image: linear-gradient(38deg, rgba(35, 28, 118, 0.7) 37%, rgba(200, 80, 192, 0.5) 26%, rgba(41, 86, 162, 0.6) 20%);
        }
    .stDataFrame {
        color: black;
        background-color: white;
    }
    .stButton > button {
           background: cyan;
           width:2rem;
            color: black;
            width: fit-content;
            font-size: 3rem; /* Adjust font size as needed */
            font-weight: 800;

            
    }
    .ef3psqc12{
    font-size:1.5rem;
    }

    .stTitle {
        font-size: 4rem;
        font-weight: 700;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True
)

def reval():
    st.markdown('<h1 class="stTitle">File Upload and Marks Visualization</h1>', unsafe_allow_html=True)

    # Initialize session state for button activation
    if 'file_uploaded' not in st.session_state:
        st.session_state.file_uploaded = False

    uploaded_file = st.file_uploader("Choose a file")

    # Check if a file is uploaded
    if uploaded_file:
        # Load the file into a DataFrame and display it
        df = pd.read_csv(uploaded_file)
        st.write(df)  # Display the DataFrame with default styling

        # Set the session state to indicate a file has been uploaded
        st.session_state.file_uploaded = True

    # Add the button for backend call
    if uploaded_file:
        if st.button('Upload to Backend'):
            # Convert the uploaded file to bytes
            file_bytes = uploaded_file.getvalue()

            # Upload the file to the backend
            upload_file_to_backend(uploaded_file.name, file_bytes)

    # Add download buttons in the same line
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button('Download'):
            download_file_from_backend()

    with col2:
        if st.button('Download Reval File'):
            download_excel_from_backend()
            
    with col3:
        if st.button('Download CGPA List'):
            download_cgpa_from_backend()

def upload_file_to_backend(filename, file_bytes):
    url = "http://localhost:5000/upload"
    files = {'file': (filename, file_bytes)}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        st.success('File successfully uploaded to backend')
    else:
        st.error('Failed to upload file to backend')
        st.error(f'Status code: {response.status_code}')
        st.error(f'Response: {response.text}')

def download_file_from_backend():
    url = "http://localhost:5000/download"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        # Create a temporary file to store the downloaded content
        with open("downloaded_file.xlsx", "wb") as f:
            f.write(response.content)
        
        # Use Streamlit's file download functionality
        with open("downloaded_file.xlsx", "rb") as f:
            st.download_button(
                label="Download Updated File",
                data=f,
                file_name="student_marks.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error('Failed to download file from backend')
        st.error(f'Status code: {response.status_code}')
        st.error(f'Response: {response.text}')

def download_excel_from_backend():
    url = "http://localhost:5000/download_excel"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        # Create a temporary file to store the downloaded content
        with open("downloaded_excel.xlsx", "wb") as f:
            f.write(response.content)
        
        # Use Streamlit's file download functionality
        with open("downloaded_excel.xlsx", "rb") as f:
            st.download_button(
                label="Download Reval File",
                data=f,
                file_name="student_reval.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error('Failed to download Excel file from backend')
        st.error(f'Status code: {response.status_code}')
        st.error(f'Response: {response.text}')

def download_cgpa_from_backend():
    url = "http://localhost:5000/download_cgpa"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        # Create a temporary file to store the downloaded content
        with open("downloaded_cgpa.xlsx", "wb") as f:
            f.write(response.content)
        
        # Use Streamlit's file download functionality
        with open("downloaded_cgpa.xlsx", "rb") as f:
            st.download_button(
                label="Download to List",
                data=f,
                file_name="toppers.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error('Failed to download CGPA file from backend')
        st.error(f'Status code: {response.status_code}')
        st.error(f'Response: {response.text}')

reval()
