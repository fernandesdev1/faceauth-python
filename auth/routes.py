from flask import Blueprint, render_template, request, jsonify, session, redirect
from database import connect
from auth.services import register_user, login_user, login_face_only

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/")
def login_page():
    return render_template("login.html")


@auth_routes.route("/register")
def register_page():
    return render_template("register.html")

@auth_routes.route("/verify")
def verify_page():
    return render_template("verify.html")

@auth_routes.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")

@auth_routes.route("/verify_face", methods=["POST"])
def verify_face():
    if "temp_user" not in session:
        return {"success": False, "message": "Sessão inválida"}

    username = session["temp_user"]
    data = request.json

    success, message = login_face_only(username, data["image"])

    if success:
        session.pop("temp_user")
        session["user"] = username
        return {"success": True}

    return {"success": False, "message": message}

@auth_routes.route("/register_face", methods=["POST"])
def register_face():
    data = request.json

    success, message = register_user(
        data["username"],
        data["password"],
        data["image"]
    )

    return jsonify({"success": success, "message": message})

@auth_routes.route("/register_user", methods=["POST"])
def register_user_route():
    data = request.json

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (data["username"], data["password"])
        )
        conn.commit()
        return {"success": True, "message": "Conta criada!"}
    except:
        return {"success": False, "message": "Usuário já existe"}
    finally:
        conn.close()

@auth_routes.route("/login_user", methods=["POST"])
def login_user_route():
    data = request.json

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (data["username"],)
    )

    user = cursor.fetchone()
    conn.close()

    if not user:
        return {"success": False, "message": "Usuário não existe"}

    if data["password"] != user[0]:
        return {"success": False, "message": "Senha incorreta"}

    session["temp_user"] = data["username"]

    return {"success": True}
