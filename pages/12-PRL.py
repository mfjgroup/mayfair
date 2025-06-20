import streamlit as st
import streamlit.components.v1 as components
import  pandas as pd
import os
from datetime import datetime
import numpy as np
import bcrypt 

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_image_path

st.set_page_config(page_title='PRL', page_icon="✈", layout="wide",initial_sidebar_state="collapsed")
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Access denied. Please log in from the Home page.")
    st.stop() 
#hide_sidebar = False
st.hide_sidebar=True
#st.sidebar.image("images/logo.jpg",caption="")
html_title = """
    <html>
    <style>
        .title-test{ color:#FFFFFF; font-weight:bold; padding:5px; border-radius:6px }
        .container {
            text-align: center;
            background-color: #800080;
            color: white;
            padding: 5px;
            border-radius: 20px;
        }
    </style>
     <div class="container">
     <center><h1 class="title-test"> 🛩 FLown and No-Show Data 👥 </h1></center>
     </div>
     </html>
"""
st.markdown(html_title, unsafe_allow_html=True)
# Sample username and password setup
st.markdown("")
now=datetime.now()
date_now=now.strftime("%d-%b-%y %H:%M:%S")

#
st.markdown('<span style="color:#800080;font-weight:bold">Time is '+ date_now +  '</span>', unsafe_allow_html=True)
    #st.success(f"File saved at {file_path}")
    #st.write(f"File Name: {uploaded_file.name}")
    #<li><a href="Home" class="active">Home</a></li>
st.markdown("")

html_content = """
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"> 
   <head>
    <style>
      ul {
        list-style-type: none;
        margin:1;
        padding: 1;
        overflow: hidden;
        background-color: #FFF5EE;
        #display: flex;
      }
      li {
        float: left;
      }
      li a {
        display: block;
        color: white;
        text-align: center;
        
        padding: 10px 12px;
        text-decoration: none;
      }
      li a:hover:not(.active) {
        background-color: #d59fe2;
         color: #000000;
      }
      .active {
       
        background-color: #d59fe2;
        color: #000000;
      }
    </style>
  </head>
    <body>
    <ul>
      <div class="w3-container w3-center w3-animate-top">
      <li class="w3-large"><a href="PRL_CONT" target="_self">Passenger Reconcillation List</a></li> 
      <li class="w3-large"><a href="flown_no_show" target="_self">Flown and No-Show Summary</a></li>   
      </div>
    </ul>
  </body>
</html>
"""
 #<li class="w3-large"><a href="MyPivot">MyPivot</a></li>
# Render the HTML in Streamlit
st.markdown(html_content, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        div[data-testid="collapsedControl"] {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

image_path = get_image_path("mayfairjets1.jpg")

# Custom CSS to set the background and make the image take half the height
st.markdown(
    """
    <html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <style>
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background-size: cover;
        height: 400px%;
        width: 100%;
    }
    </style>
    </html>
    """,
    unsafe_allow_html=True
)

# Create a container to display the image
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image(image_path)
st.markdown('</div>', unsafe_allow_html=True)
########################################################



