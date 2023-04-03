#!/usr/bin/python3
"""Blueprint for volunteer authentication"""
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


volunteer_bp = Blueprint('volunteer_auth',
                         __name__, url_prefix='/auth/volunteer')


@volunteer_bp.route('/register', methods=['POST', 'GET'])
def volunteer_reg():
    """Renders registraton page for nonprofit"""
    from givetime.auth.volunteer_validatiions import VolunteerSignUpForm

    form = VolunteerSignUpForm()

    if request.method == 'POST' and form.validate_on_submit():
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        skill = request.form.get('skill')
        location = request.form.get('location')

        from givetime.modified_model import Volunteer
        check_email = Volunteer.query.filter_by(email=email).first()
        if check_email:
            flash(f'Volunteer with {email} already exists....try something different.')
            return redirect(url_for('volunteer_auth.volunteer_reg'))

        try:
            password_hash = generate_password_hash(password)
            Volunteer.create(first_name=first_name, email=email,
                             password=password_hash, last_name=last_name,
                             skill=skill, location=location)

            flash('Account created successfully!')

            return redirect(url_for('index'))

        except Exception as err:
            print(f"Error: {err}")
    return render_template('auth/signup.html', form=form)


@volunteer_bp.route('/login', methods=['POST', 'GET'])
def volunteer_login():
    """Renders registraton page for nonprofit"""
    from givetime.auth.volunteer_validatiions import VolunteerLoginForm
    form = VolunteerLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')

        from givetime.modified_model import Volunteer

        user_email = Volunteer.query.filter_by(email=email).first()
        if user_email and check_password_hash(user_email.password, password):
            login_user(user_email)
            return redirect(url_for('index'))
        else:
            flash('Email/Password Incorrect')
            return redirect(url_for('volunteer_auth.volunteer_login'))

    return render_template('auth/login.html', form=form)


@volunteer_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
