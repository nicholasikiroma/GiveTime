#!/usr/bin/python3
"""Base Flask Application for GiveTime"""
from flask import Flask, render_template
from flask_login import LoginManager
from models.modified_schema import db
from auth import nonprofit_bp
from auth import volunteer_bp
import os


base_dir = os.path.dirname(os.path.realpath(__file__))
app = Flask('__name__')
app.register_blueprint(nonprofit_bp)
app.register_blueprint(volunteer_bp)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, 'givetime.db')


db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)


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


if __name__ == "__main__":
    app.run(debug=True)
