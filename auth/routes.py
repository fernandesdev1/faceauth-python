from flask import Blueprint, render_template, request, jsonify
from auth.services import register_user, login_user

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/")
def login_page():
    return render_template("login.html")


@auth_routes.route("/register")
def register_page():
    return render_template("register.html")


@auth_routes.route("/register_face", methods=["POST"])
def register_face():
    data = request.json

    success, message = register_user(
        data["username"],
        data["password"],
        data["image"]
    )

    return jsonify({"success": success, "message": message})


@auth_routes.route("/login_face", methods=["POST"])
def login_face():
    data = request.json

    success, message = login_user(
        data["username"],
        data["password"],
        data["image"]
    )

    return jsonify({"success": success, "message": message})