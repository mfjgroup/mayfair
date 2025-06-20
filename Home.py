from streamlit_authenticator.utilities.hasher import Hasher

# Create a Hasher instance with a list of passwords
hasher = Hasher(["MFJ2025@rms123456"])

# Call hash_list on the instance
hashed_passwords = hasher.hash_list()

# Print the hashed password (you'll use this in your app)
print(hashed_passwords[0])
