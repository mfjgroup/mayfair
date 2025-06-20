import streamlit as st
import streamlit_authenticator as stauth

# User credentials
names = ["Alice", "Bob"]
usernames = ["alice", "bob"]
passwords = ["password123", "secure456"]

# Hashed passwords for security
hashed_passwords = stauth.Hasher(passwords).generate()

# Create the authenticator object with cookie params
authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "some_cookie_name",  # cookie name (unique per app)
    "some_signature_key",  # secret key for signing cookies (make this secret!)
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.write(f"Welcome *{name}*")
    st.write("You are logged in")
elif authentication_status is False:
    st.error("Username/password is incorrect")
else:
    st.info("Please enter your username and password")