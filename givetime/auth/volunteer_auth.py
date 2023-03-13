#!/usr/bin/python3
"""Blueprint for volunteer authentication"""
from flask import Blueprint, render_template
from volunteer_validatiions import VolunteerLoginForm, VolunteerSignUpForm


volunteer_bp = Blueprint('volunteer_auth',
                         __name__, url_prefix='/auth/volunteer')


@volunteer_bp.route('/register')
def volunteer_reg():
    """Renders registraton page for nonprofit"""
    form = VolunteerSignUpForm()

    return render_template('nonprofit_auth.html', form=form)


@volunteer_bp.route('/login')
def voluneer_login():
    """Renders registraton page for nonprofit"""
    form = VolunteerLoginForm()

    return render_template('nonprofit_auth.html', form=form)
