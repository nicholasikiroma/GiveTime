#!/usr/bin/python3
"""Blueprint for volunteer authentication"""
from app import db
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from auth.volunteer_validatiions import VolunteerLoginForm, VolunteerSignUpForm
from models.modified_schema import Volunteer
from werkzeug.security import generate_password_hash, check_password_hash


volunteer_bp = Blueprint('volunteer_auth',
                         __name__, url_prefix='/auth/volunteer')



@volunteer_bp.route('/register')
def volunteer_reg():
    """Renders registraton page for nonprofit"""
    form = VolunteerSignUpForm()

    if request.method == 'POST' and form.validate_on_submit():
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        city = request.form.get('city')
        state = request.form.get('state')     
        phone_no = request.form.get('phone')
        address = request.form.get('address')
        skill = request.form.get('skills')

        # checks if email address exists in database
        check_email = Volunteer.query.filter_by(email=email).first()
        if check_email:
            flash(f'Nonprofit with {email} already exists....try something different.')
            return redirect(url_for('sign_up'))

        password_hash = generate_password_hash(password)
        new_nonprofit = Volunteer(first_name=first_name, last_name=last_name,
                                  email=email,password_hash=password_hash, city=city,
                                  phone=phone_no, address=address, state=state,
                                  skill=skill)

        db.session.add(new_nonprofit)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('login'))
    return render_template('nonprofit_auth.html', form=form)


@volunteer_bp.route('/login')
def voluneer_login():
    """Renders registraton page for nonprofit"""
    form = VolunteerLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_email = Volunteer.query.filter_by(email=email).first()
        if user_email and check_password_hash(user_email.password_hash, password):
            login_user(user_email)
            return redirect(url_for('index'))
        else:
            flash('email/password Incorrect')
            return redirect(url_for('login'))

    return render_template('nonprofit_auth.html', form=form)


@volunteer_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))