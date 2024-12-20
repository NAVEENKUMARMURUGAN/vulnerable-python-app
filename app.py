# app.py
from flask import Flask, request, render_template_string
import sqlite3
import pickle
import os
import jwt
import hashlib

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded secrets
SECRET_KEY = "super_secret_key_123"
DB_PASSWORD = "database_password_123"
API_KEY = "sk_live_12345"

# VULNERABILITY 2: Weak password hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABILITY 3: SQL Injection
@app.route('/users')
def get_users():
    name = request.args.get('name')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Direct string formatting - SQL Injection vulnerability
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return str(cursor.fetchall())

# VULNERABILITY 4: Command Injection
@app.route('/ping')
def ping():
    hostname = request.args.get('hostname')
    # Unsafe command execution
    return os.system(f"ping -c 1 {hostname}")

# VULNERABILITY 5: Server-Side Template Injection
@app.route('/greet')
def greet():
    name = request.args.get('name')
    # Unsafe template rendering
    template = f'''
    <h1>Hello {name}!</h1>
    '''
    return render_template_string(template)

# VULNERABILITY 6: Unsafe Deserialization
@app.route('/load_data', methods=['POST'])
def load_data():
    data = request.get_data()
    # Unsafe pickle deserialization
    return str(pickle.loads(data))

# VULNERABILITY 7: Path Traversal
@app.route('/download')
def download_file():
    filename = request.args.get('filename')
    # Path traversal vulnerability
    with open(f"files/{filename}", 'r') as f:
        return f.read()

# VULNERABILITY 8: Weak JWT Implementation
@app.route('/login')
def login():
    username = request.args.get('username')
    # Weak algorithm and no expiration
    token = jwt.encode({'user': username}, SECRET_KEY, algorithm='HS256')
    return token

# requirements.txt contains vulnerable versions:
# flask==0.12.2
# pyjwt==1.5.0
# requests==2.18.0
# sqlalchemy==1.1.0

if __name__ == '__main__':
    app.run(debug=True)  # VULNERABILITY 9: Debug mode in production