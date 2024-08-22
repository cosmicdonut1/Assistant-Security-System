import requests
from cryptography.fernet import Fernet
import hashlib
import hmac

# Server URL
server_url = 'https://127.0.0.1:5000'

# User credentials
username = 'master'
password = 'securepassword'

# Read the key from the file
with open('secret.key', 'rb') as key_file:
    encryption_key = key_file.read()

# Secret key for HMAC (same on client and server)
secret_key = b'SuperSecretKey'

def login():
    response = requests.post(f'{server_url}/login', json={'username': username, 'password': password}, verify=False)
    if response.status_code == 200:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False

def fetch_assistant_data():
    response = requests.get(f'{server_url}/assistant', headers={'Username': username, 'Password': password}, verify=False)
    if response.status_code == 200:
        data = response.json()
        encrypted_data = data['data']
        hmac_value = data['hmac']

        # Decrypt the data
        fernet = Fernet(encryption_key)
        decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()

        # Check data integrity
        computed_hmac = hmac.new(secret_key, decrypted_data.encode(), hashlib.sha256).hexdigest()
        if hmac_value == computed_hmac:
            print("Integrity check passed")
            print("Assistant data received: ", decrypted_data.split(","))
        else:
            print("Integrity check failed")
    else:
        print("Failed to fetch assistant data")

def add_task_to_assistant(task):
    response = requests.post(f'{server_url}/assistant/add', json={'task': task}, headers={'Username': username, 'Password': password}, verify=False)
    if response.status_code == 200:
        print("Task added successfully")
    else:
        print("Failed to add task")

if __name__ == '__main__':
    if login():
        fetch_assistant_data()
        add_task_to_assistant("Call the plumber")