#!/usr/bin/python3
"""Blueprint for Nonprofit authentication"""
from flask import Blueprint, render_template, flash, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from givetime.auth.nonprofit_validations import NonprofitLoginForm, NonprofitSignUpForm
from flask_login import login_user, logout_user


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
        description = request.form.get('description')
        website_url = request.form.get('website')
 #       city = request.form.get('city')
#        state = request.form.get('state')
        # Implement AJAX Verification of CAC num
        status = request.form.get('cac_num')
#        phone_no = request.form.get('phone')
        address = request.form.get('address')

        # checks if username exists in database
        from givetime.modified_model import Nonprofit
        check_username = Nonprofit.query.filter_by(name=name).first()
        if check_username:
            flash(f'{name} already exists....try something different.')
            return redirect(url_for('sign_up', form=form))

        # checks if email address exists in database
        check_email = Nonprofit.query.filter_by(email=email).first()
        if check_email:
            flash(
                f'Nonprofit with {email} already exists....try something different.')
            return redirect(url_for('sign_up'))

        password_hash = generate_password_hash(password)

        Nonprofit.create(name=name, email=email,
                         password=password_hash, description=description,
                         website=website_url)
    
        flash('Account created successfully!')
        return redirect(url_for('login'))

    return render_template('auth/signup_nonprofit.html', form=form)


from givetime import login_manager

@login_manager.user_loader
@nonprofit_bp.route('/login')
def nonprofit_login():
    """Renders registraton page for nonprofit"""
    form = NonprofitLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')

        from givetime.modified_model import Nonprofit
        user_email = Nonprofit.query.filter_by(email=email).first()
        if user_email and check_password_hash(user_email.password_hash, password):
            login_user(user_email)
            return redirect(url_for('index'))
        else:
            flash('email/password Incorrect')
            return redirect(url_for('nonprofit_login'))

    return render_template('auth/nonprofit_signup.html', form=form)


@nonprofit_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
