import streamlit as st
import streamlit_authenticator as stauth
from datetime import datetime

# Configured credentials
users = {
    "mayfairjets": {
        "name": "Mayfair Admin",
        "password": "MFJ2025@rms123456"
    }
}

# Create authenticator
authenticator = stauth.Authenticate(
    credentials={"usernames": {
        username: {"name": data["name"], "password": stauth.Hasher([data["password"]]).generate()[0]}
        for username, data in users.items()
    }},
    cookie_name="rms_login",  # This sets a persistent browser cookie
    key="auth"
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"✅ Welcome {name}")
    now = datetime.now()
    st.markdown(f"<b style='color:#800080'>Time is {now.strftime('%d-%b-%y %H:%M:%S')}</b>", unsafe_allow_html=True)

elif authentication_status is False:
    st.error("❌ Incorrect username or password.")
elif authentication_status is None:
    st.warning("Please enter your credentials.")