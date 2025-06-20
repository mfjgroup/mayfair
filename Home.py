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
# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
# ---------- HARDCODED USER + HASHED PASSWORD ----------

# ---------- LOGIN FORM ----------
if not st.session_state.logged_in:
    st.title("🛩 Revenue Management System Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "mayfairjets" and password=="MFJ2025@rms123456":
            st.session_state.logged_in = True
            st.success("✅ Login successful.")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password.")
    st.stop()  # stop app if not logged in

# ---------- LOGOUT ----------
if st.button("🔓 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# ---------- MAIN CONTENT ----------
st.success("✅ You are logged in.")

now = datetime.now()
st.markdown(f"<b style='color:#800080'>Time is {now.strftime('%d-%b-%y %H:%M:%S')}</b>", unsafe_allow_html=True)
# Header
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

# Navigation
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