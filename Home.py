import streamlit as st

# Dummy credentials
users = {
    "alice": "password123",
    "bob": "secure456"
}

def login(username, password):
    return users.get(username) == password

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

def main():
    st.title("Login Demo with Session Persistence")

    if not st.session_state.logged_in:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f"Welcome, {username}!")
            else:
                st.error("Invalid credentials.")
    else:
        st.success(f"Already logged in as {st.session_state.username}")
        if st.button("Logout"):
            logout()
        st.write("Your secure content goes here.")

if __name__ == "__main__":
    main()