#!/usr/bin/python3
"""Blueprint for Nonprofit authentication"""
from flask import Blueprint, render_template, flash, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from auth.nonprofit_validations import NonprofitLoginForm, NonprofitSignUpForm
from models.modified_schema import Nonprofit
from flask_login import login_user, logout_user
from auth import db

nonprofit_bp = Blueprint('nonprofit_auth',
                         __name__, url_prefix='/auth/nonprofit')


@nonprofit_bp.route('/register', methods=['Post', 'GET'])
def nonprofit_reg():
    """Renders registraton page for nonprofit"""
    form = NonprofitSignUpForm()

    if request.method == 'POST' and form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        bio = request.form.get('description')
        website_url = request.form.get('website')
        city = request.form.get('city')
        state = request.form.get('state')     
        status = request.form.get('cac_num') # Implement AJAX Verification of CAC num
        phone_no = request.form.get('phone')
        address = request.form.get('address')

        # checks if username exists in database
        check_username = Nonprofit.query.filter_by(name=name).first()
        if check_username:
            flash(f'{name} already exists....try something different.')
            return redirect(url_for('sign_up', form=form))
        

        # checks if email address exists in database
        check_email = Nonprofit.query.filter_by(email=email).first()
        if check_email:
            flash(f'Nonprofit with {email} already exists....try something different.')
            return redirect(url_for('sign_up'))

        password_hash = generate_password_hash(password)
        new_nonprofit = Nonprofit(name=name,
                         email=email,
                         password_hash=password_hash, description=bio,
                         city=city, phone=phone_no, address=address,
                         state=state, verificaton_status=status,
                         website=website_url)

        db.session.add(new_nonprofit)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('login'))

    return render_template('nonprofit_auth.html', form=form)


@nonprofit_bp.route('/login')
def nonprofit_login():
    """Renders registraton page for nonprofit"""
    form = NonprofitLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_email = Nonprofit.query.filter_by(email=email).first()
        if user_email and check_password_hash(user_email.password_hash, password):
            login_user(user_email)
            return redirect(url_for('index'))
        else:
            flash('email/password Incorrect')
            return redirect(url_for('login'))


    return render_template('nonprofit_auth.html', form=form)


@nonprofit_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))