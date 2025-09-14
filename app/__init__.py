from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

db=SQLAlchemy()

#App and DB Setup
def create_app():
    app=Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///todo.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'my_jwt_secret_key')
    
    db.init_app(app)
    jwt = JWTManager(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app



