#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)
auth = HTTPBasicAuth()


users = {
    "user": {
        "username": "user1",
        "password": generate_password_hash("user1"),
        "role": "user"
    },
    "admin": {
        "username": "admin1",
        "password": generate_password_hash("admin1"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted for user {current_user}"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_info = users.get(current_user)

    if user_info['role'] != 'admin':
        return jsonify({"msg": "Forbidden"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
