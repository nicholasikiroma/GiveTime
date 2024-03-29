#!/usr/bin/python3
"""Handles form validations for volunteer authentication"""
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class VolunteerSignUpForm(FlaskForm):
    """Defines Validators for nonprofit sign-up form"""
    first_name = StringField(label='First Name',
                             validators=[InputRequired(message="Field cannot be blank")])

    last_name = StringField(label='Last Name',
                            validators=[InputRequired(message="Field cannot be blank")])

    email = EmailField(label='Email Address',
                       validators=[InputRequired(message="email name should not be blank"),
                                                          Length(max=45, message="Email should have less than 45 characters")])

    password = PasswordField(label='Password',
                             validators=[InputRequired(message="Password should not be left blank"),
                                                           Length(max=40, message="Password too long")])

    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[InputRequired(message="Password should not be left blank"),
                                                                           Length(max=40, message="Password too long"),
        EqualTo('password', message="Passwords do not match")])

    skill = StringField(label='Skill',
                        validators=[InputRequired(message='Skill cannot be left blank')])

    location = StringField(label='Location', validators=[
                           InputRequired(message='Provide state of residence')])


class VolunteerLoginForm(FlaskForm):
    """Defines validators for user login form"""
    password = PasswordField(label='Password',
                             validators=[InputRequired(message='Password cannot be blank'),
                                         Length(max=10, message=('Password should be less than 10 characters'))])

    email = StringField(label='Email Address',
                        validators=[InputRequired(message="email name should not be blank"),
                                                           Length(max=45, message="Email should have less than 45 characters")])
