#!/usr/bin/python3
"""Blueprint for Nonprofit authentication"""
from flask import Blueprint, render_template


nonprofit_bp = Blueprint('nonprofit_auth',
                         __name__, url_prefix='/auth/nonprofit')


@nonprofit_bp.route('/register')
def nonprofit_reg():
    """Renders registraton page for nonprofit"""
    return render_template('nonprofit_auth.html')


@nonprofit_bp.route('/login')
def nonprofit_login():
    """Renders registraton page for nonprofit"""
    return render_template('nonprofit_auth.html')
