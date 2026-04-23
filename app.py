from flask import Flask
from database import create_table

app = Flask(__name__)
create_table()

from auth.routes import auth_routes
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(debug=True)