#!/usr/bin/python3
"""Base Flask Application for GiveTime"""
from flask import Flask, render_template
import os


def create_app():

    app = Flask('__name__')
    base_dir = os.path.dirname(os.path.realpath(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        base_dir, 'givetime.db')

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

    db.init_app(app)


    @app.route('/')
    def index():
        """Renders template for home page"""
        return render_template('index.html')


    @app.route('/explore')
    def explore():
        """Renders the html template for the explore page"""
        return render_template('explore.html')


    @app.route('/about')
    def about():
        return render_template('about.html')
    
    from givetime.auth.nonprofit_auth import nonprofit_bp
    from givetime.auth.volunteer_auth import volunteer_bp

    app.register_blueprint(nonprofit_bp)
    app.register_blueprint(volunteer_bp)

    return app
