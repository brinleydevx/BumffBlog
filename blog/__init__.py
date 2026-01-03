from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app