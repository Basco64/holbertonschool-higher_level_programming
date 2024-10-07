#!/usr/bin/python3

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "Ok"


@app.route("/data")
def data():
    return jsonify(users)


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username or not name or not age or not city:
        return jsonify({"error": "Missing information"}), 400

    users[username] = {
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()