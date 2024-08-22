# generate_key.py
from cryptography.fernet import Fernet

# Generate a key and write it to a file
encryption_key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(encryption_key)

print(f"Generated key: {encryption_key.decode()}")