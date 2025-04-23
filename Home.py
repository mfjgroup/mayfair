import streamlit as st
import bcrypt
from datetime import datetime

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_image_path

st.set_page_config(page_title='Revenue Management System', page_icon="✈", layout="wide")
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
     <center><h1 class="title-test"> 🛩 Revenue Management System V2📊 </h1></center>
     </div>
     </html>
"""
st.markdown(html_title, unsafe_allow_html=True)
st.markdown("")
# Predefined correct username and password (hashed)
correct_username = "mayfairjets"
password = b"abcd1234"
salt = bcrypt.gensalt(rounds=15)
hashed_password = bcrypt.hashpw(password, salt)

# Function to show the login page
def login():
    # Display login form with input fields
    col1, col2, col3, col4, col5,col6 = st.columns(6)
    with col1:
        username_input = st.text_input("Username", "Enter User Name", key="placeholder")
        password_input = st.text_input("Password", type="password")
    
    tabs_font_css = """
    <style>
    div[class*="stTextInput"] label {
      font-size: 26px;
      color: #800080;
      width : 40 px;
    }
    div[class*="stNumberInput"] label {
      font-size: 26px;
      color: #800080;
      width : 40 px;
      border:1px solid #777;
    }
    </style>
    """
    
    st.write(tabs_font_css, unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # If already logged in, show the logout button and time
    if st.session_state.logged_in:
        logout_button = st.button("Logout")
        if logout_button:
            st.session_state.logged_in = False
            st.rerun()  # Reset and re-render the page

        st.markdown(
            """
            <style>
            .stSidebar {display: block;}  /* Hides the sidebar completely */
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Display current time for logged-in users
        now = datetime.now()
        date_now = now.strftime("%d-%b-%y %H:%M:%S")
        st.markdown('<span style="color:#800080;font-weight:bold">Time is ' + date_now + '</span>', unsafe_allow_html=True)
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
      <li class="w3-large"><a href="Homet"><i class="fa fa-homet"></i> Revenue & Inventory Report</a></li>
      <li class="w3-large"><a href="PRL"><i class="fa fa-homet"></i> Flown & No-Show Data</a></li>
      <li class="w3-large"><a href="Statistic"><i class="fa fa-homet"></i>Booking Statistics</a></li>
      </div>
    </ul>
  </body>
</html>
"""
 #<li class="w3-large"><a href="MyPivot">MyPivot</a></li>
# Render the HTML in Streamlit
        st.markdown(html_content, unsafe_allow_html=True)

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
        st.markdown(
    """
    <style>
    .stSidebar {display: block;}  /* Hides the sidebar completely */
    </style>
    """,
    unsafe_allow_html=True,
)
# Create a container to display the image
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image_path)
        st.markdown('</div>', unsafe_allow_html=True)

    # Login process
    else:
        if st.button("Login"):
            # Check if the entered username matches the correct username
            if username_input == correct_username:
                # Check if the entered password matches the stored hashed password
                if bcrypt.checkpw(password_input.encode('utf-8'), hashed_password):
                    # Set session state to indicate login success
                    st.session_state.logged_in = True
                    st.rerun()  # Re-render the page to reflect the logged-in state
                    

                else:
                    st.error("Password is incorrect")
            else:
                st.error("Username is incorrect")

login()