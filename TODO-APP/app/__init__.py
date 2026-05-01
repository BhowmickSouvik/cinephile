from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os

# create database object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    os.makedirs(app.instance_path,exist_ok=True)

    app.permanent_session_lifetime = timedelta(days=30)
    app.config['SECRET_KEY'] = 'sou2007'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'todo.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app