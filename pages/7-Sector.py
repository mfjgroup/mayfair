import pandas as pd
import streamlit as st
import plotly.express as px
#from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os
import numpy as np

# Set up Streamlit page configuration
st.set_page_config(page_title='Revenue Management System', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Access denied. Please log in from the Home page.")
    st.stop() 
#####################
# Custom HTML Title

html_title = """
    <style>
        .title-test{ color:#FFFFFF; font-weight:bold; padding:5px; border-radius:6px }
        .container {
            text-align: center;
            background-color: #800080;
            color: white;
            padding: 3px;
            border-radius: 20px;
        }
    </style>
     <div class="container"
     <center><h1 class="title-test"> 🛩 Sector Summary</h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)
st.markdown("")
UPLOAD_FOLDER = "uploads/"

# Get the list of files in the upload folder
uploaded_files = os.listdir(UPLOAD_FOLDER)

if uploaded_files:
    #st.write("Available files in the upload folder:")
    for file in uploaded_files:
        #st.write("")
      #selected_file = st.selectbox("Select a file from the folder", file)
      selected_file=uploaded_files[0]
    # Load the file using pandas
    file_path = os.path.join(UPLOAD_FOLDER, selected_file)
    
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name='Booking_Data')  # Specify the sheet index or name
    except Exception as e:
        st.error(f"Error reading the file: {e}")
    
        