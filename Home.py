import streamlit as st
import streamlit_authenticator as stauth

names = ["Alice", "Bob"]
usernames = ["alice", "bob"]
passwords = ["password123", "secure456"]

hashed_passwords = stauth.Hasher(passwords).hash_passwords()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "some_cookie_name",
    "some_signature_key",
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.success(f"Welcome {name}!")
elif authentication_status is False:
    st.error("Username/password is incorrect")
else:
    st.info("Please enter your username and password")