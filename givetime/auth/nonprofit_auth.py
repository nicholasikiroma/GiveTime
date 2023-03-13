#!/usr/bin/python3
"""Blueprint for Nonprofit authentication"""
from flask import Blueprint, render_template, flash, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from nonprofit_validations import NonprofitLoginForm, NonprofitSignUpForm
from app import db


nonprofit_bp = Blueprint('nonprofit_auth',
                         __name__, url_prefix='/auth/nonprofit')


@nonprofit_bp.route('/register')
def nonprofit_reg():
    """Renders registraton page for nonprofit"""
    form = NonprofitSignUpForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # checks if username exists in database
        check_username = Users.query.filter_by(username=username).first()
        if check_username:
            flash(f'{username} already exists....try something different.')
            return redirect(url_for('sign_up'))
        
        # checks if email address exists in database
        check_email = Users.query.filter_by(email=email).first()
        if check_email:
            flash(f'User with {email} already exists....try something different.')
            return redirect(url_for('sign_up'))

        password_hash = generate_password_hash(password)
        new_user = Users(username=username,
                         email=email,
                         password_hash=password_hash)

        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('login'))


    return render_template('nonprofit_auth.html')


@nonprofit_bp.route('/login')
def nonprofit_login():
    """Renders registraton page for nonprofit"""
    form = NonprofitLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_email = Users.query.filter_by(email=email).first()
        if user_email and check_password_hash(user_email.password_hash, password):
            login_user(user_email)
            return redirect(url_for('index'))
        else:
            flash('email/password Incorrect')
            return redirect(url_for('login'))


    return render_template('nonprofit_auth.html', form=form)