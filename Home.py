import streamlit_authenticator as stauth

# TEMP: Generate hashed password
passwords = ['MFJ2025@rms123456']
hashed_passwords = stauth.Hasher(passwords).generate()

import streamlit as st
st.code(f"Hashed password: {hashed_passwords[0]}")
st.stop()  # Prevent the rest of the app from loading