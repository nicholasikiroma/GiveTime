#!/usr/bin/python3
"""Handles form validations for nonprofit authentication"""
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, TextAreaField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class NonprofitSignUpForm(FlaskForm):
    """Defines Validators for nonprofit sign-up form"""
    name = StringField(label='Organisation Name',
                       validators=[InputRequired(message="Organisation name cannot be blank")])

    email = EmailField(label='Email Address',
                       validators=[InputRequired(message="email name should not be blank"),
                                   Length(max=45, message="Email should have less than 45 characters")])

    password = PasswordField(label='Password',
                             validators=[InputRequired(message="Password should not be left blank"),
                                         Length(min=7, message="Password too short")])

    description = TextAreaField(label='Description',
                                validators=[InputRequired(message='Provide short description of your NGO')])

    website = URLField(label='Website URL')

    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[InputRequired(
                                         message="Password should not be left blank"),
                                         Length(
                                             max=10, message="Password too long"),
                                         EqualTo('password', message="Passwords do not match")])


class NonprofitLoginForm(FlaskForm):
    """Defines validators for user login form"""
    password = PasswordField(label='Password',
                             validators=[InputRequired(message='Password cannot be blank'),
                                         Length(max=10, message=('Password should be less than 10 characters'))])

    submit = SubmitField(label='Sign Up')

    email = StringField(label='Email Address',
                        validators=[InputRequired(message="email name should not be blank"),
                                    Length(max=45, message="Email should have less than 45 characters")])
