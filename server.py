from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import hashlib
import hmac

app = Flask(__name__)

# Read the key from the file
with open('secret.key', 'rb') as key_file:
    encryption_key = key_file.read()

fernet = Fernet(encryption_key)

# Secret key for HMAC
secret_key = b'SuperSecretKey'

# Single user
user = {
    "username": "master",
    "password": "securepassword"
}

# Data store for the personal assistant
data_store = {
    "tasks": ["Pick up dry cleaning", "Buy groceries", "Schedule dentist appointment"]
}

def authenticate(username, password):
    return username == user['username'] and password == user['password']

def encrypt_data(data):
    return fernet.encrypt(data.encode())

def decrypt_data(data):
    return fernet.decrypt(data).decode()

def compute_hmac(data):
    return hmac.new(secret_key, data.encode(), hashlib.sha256).hexdigest()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if authenticate(username, password):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/assistant', methods=['GET'])
def get_assistant_data():
    username = request.headers.get('Username')
    password = request.headers.get('Password')

    if not authenticate(username, password):
        return jsonify({"message": "Unauthorized"}), 401

    # Prepare data for transmission
    data = ",".join(data_store["tasks"])
    encrypted_data = encrypt_data(data)
    hmac_value = compute_hmac(data)

    return jsonify({
        "data": encrypted_data.decode(),
        "hmac": hmac_value
    })

@app.route('/assistant/add', methods=['POST'])
def add_task():
    username = request.headers.get('Username')
    password = request.headers.get('Password')

    if not authenticate(username, password):
        return jsonify({"message": "Unauthorized"}), 401

    task = request.json.get('task')
    if task:
        data_store["tasks"].append(task)
        return jsonify({"message": "Task added successfully"})
    else:
        return jsonify({"message": "Invalid task data"}), 400

if __name__ == '__main__':
    app.run(ssl_context='adhoc')