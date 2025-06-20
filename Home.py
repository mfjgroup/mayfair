import streamlit as st

# Dummy credentials dictionary
users = {
    "alice": "password123",
    "bob": "secure456"
}

def login(username, password):
    return users.get(username) == password

def main():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success(f"Welcome, {username}!")
            # Secure content goes here
            st.write("This is your dashboard.")
        else:
            st.error("Invalid username or password.")

if __name__ == "__main__":
    main()