from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from .config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.admin import admin_bp
    from .routes.student import student_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)

    return app
