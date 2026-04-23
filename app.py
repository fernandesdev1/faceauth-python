from flask import Flask
from database import create_table
import os

app = Flask(__name__)
create_table()

app.secret_key = os.getenv("SECRET_KEY", "dev_key")

from auth.routes import auth_routes
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(debug=True)