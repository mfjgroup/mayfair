import streamlit as st
import bcrypt
from datetime import datetime
import streamlit_authenticator as stauth

# Page setup
st.set_page_config(page_title='Revenue Management System', page_icon="✈", layout="wide")

# Hide sidebar
st.markdown("""
    <style>
        .stSidebar { display: none; }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOGIN CHECK ----------------

names = ['Mayfair Admin']
usernames = ['mayfairjets']
passwords = ['MFJ2025@rms']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    'rms_cookie', 'rms_app', cookie_expiry_days=1)

name, auth_status, username = authenticator.login('Login', 'main')

if auth_status:
    st.session_state.logged_in = True
    st.success(f"Welcome {name}")
    html_title = """
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
     <center><h1 class="title-test"> 🛩 Revenue Management System 📊 </h1></center>
     </div>
"""
    st.markdown(html_title, unsafe_allow_html=True)

    # Current time
    now = datetime.now()
    date_now = now.strftime("%d-%b-%y %H:%M:%S")
    st.markdown(f'<span style="color:#800080;font-weight:bold">Time is {date_now}</span>', unsafe_allow_html=True)
    # Navigation HTML
    html_content = """
<html>
<head>
<style>
ul {
    list-style-type: none;
    margin: 1;
    padding: 1;
    overflow: hidden;
    background-color: #FFF5EE;
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
  <li><a href="Homet" target="_self">Revenue & Inventory Report</a></li>
  <li><a href="PRL" target="_self">Flown & No-Show Data</a></li>
  <li><a href="Statistic" target="_self">Booking Statistics</a></li>
</ul>
</body>
</html>
"""
    st.markdown(html_content, unsafe_allow_html=True)

# Image
    image_path = "images/mayfairjets1.jpg"
    st.image(image_path, use_column_width=True)
elif auth_status is False:
    st.error('Username/password is incorrect')
elif auth_status is None:
    st.warning('Please enter your credentials')
    st.stop()






