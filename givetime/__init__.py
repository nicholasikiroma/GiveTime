#!/usr/bin/python3
"""Base Flask Application for GiveTime"""
from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()


db = SQLAlchemy()


def create_app():

    app = Flask('__name__', template_folder='givetime/templates', static_folder='givetime/static')
    base_dir = os.path.dirname(os.path.realpath(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        base_dir, 'givetimeStorage.db')
    app.secret_key = '8745f7abde63c4ba78c4d60c863ded4eaf4bdf239dc3d2c866364629ab07f73b'

    db.init_app(app)
    login_manager.init_app(app)


    @app.route('/')
    def index():
        """Renders template for home page"""
        return render_template('index.html')


    @app.route('/registration')
    def register():
        """Renders the html template for the explore page"""
        return render_template('registration.html')


    @app.route('/about')
    def about():
        return render_template('about.html')
    
    
    @app.route('/nonprofit/dashboard')
    def dashboard():
        return "Nonprofit dashboard"


    from givetime.auth.nonprofit_auth import nonprofit_bp
    from givetime.auth.volunteer_auth import volunteer_bp

    app.register_blueprint(nonprofit_bp)
    app.register_blueprint(volunteer_bp)


    from givetime import modified_model
    with app.app_context():
        db.create_all()

    return app
