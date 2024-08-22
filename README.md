# Personal Assistant Security System

## Overview

This project is a security system for a personal assistant, using Flask for the server implementation and a client for interacting with the server. The server handles user authentication, task management, and ensures data security through encryption and HMAC. The client provides an interface to communicate with the server, including login, fetching encrypted task data, and adding new tasks.

## Installation Requirements

To run this project, you need Python 3.7 or newer. Make sure to install the required libraries:

1. Install the dependencies using `pip`:

    ```bash
    pip install Flask cryptography requests
    ```

2. Generate the encryption key:

    Run `generate_key.py` to create the encryption key file:

    ```bash
    python generate_key.py
    ```

## Running the Project

### Running the Server

1. Start the server by running:

    ```bash
    python server.py
    ```

    The server will run on `https://127.0.0.1:5000` using a self-signed SSL certificate (the address will be shown in the command line).

### Running the Client

1. Start the client (in separate terminal) by running:

    ```bash
    python client.py
    ```

    The client will log in, fetch the encrypted task data, add a new task, and display the results.

## Note

- The server uses a self-signed SSL certificate, so the client uses the `verify=False` parameter to ignore certificate validation. In real-world scenarios, a valid certificate should be used.
- Ensure that the `secret.key` file is in the same directory as the scripts, or specify the correct path in the code.

---

For further information and assistance, please refer to the comments in the source code files.

### License
Free use, who needs this anyway
