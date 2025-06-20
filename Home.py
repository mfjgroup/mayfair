from streamlit_authenticator.utilities.hasher import Hasher
pw = ["MFJ2025@rms123456"]
hashed = Hasher.hash_list(pw)
print(hashed[0])