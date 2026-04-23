from flask import Blueprint, render_template

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/")
def login_page():
    return render_template("login.html")

@auth_routes.route("/register")
def register_page():
    return render_template("register.html")