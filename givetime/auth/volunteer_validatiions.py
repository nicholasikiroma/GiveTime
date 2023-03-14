#!/usr/bin/python3
"""Handles form validations for volunteer authentication"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class VolunteerSignUpForm(FlaskForm):
    """Defines Validators for nonprofit sign-up form"""
    first_name = StringField(label='First Name', validators=
                           [InputRequired(message="Field cannot be blank")])

    last_name = StringField(label='Last Name', validators=
                           [InputRequired(message="Field cannot be blank")])

    email = StringField(label='Email Address',
                        validators=[InputRequired(message="email name should not be blank"),
                                    Length(max=45, message="Email should have less than 45 characters")])

    password = PasswordField(label='Password', validators=
                             [InputRequired(message="Password should not be left blank"),
                              Length(max=10, message="Password too long")])
    
    skills = TextAreaField(lable='Skill',
                                validators=[InputRequired(message='Provide short description of your NGO')])


    city = StringField(label='City', validators=[InputRequired(message='Provide city')])

    state = StringField(label='State', validators=[InputRequired(message='Provide city')])


    phone = IntegerField(lable='Description',
                                validators=[InputRequired(message='Enter a valid phone number'),
                                            Length(max=11, min=11)])


    confirm_password = PasswordField(label='Confirm Password', validators=
                             [InputRequired(message="Password should not be left blank"),
                              Length(max=10, message="Password too long"),
                              EqualTo('password', message="Passwords do not match")])

    submit = SubmitField(label= 'Create Account')



class VolunteerLoginForm(FlaskForm):
    """Defines validators for user login form"""
    password = PasswordField(label='Password',
                             validators=[InputRequired(message='Password cannot be blank'),
                                         Length(max=10, message=('Password should be less than 10 characters'))])
    
    submit = SubmitField(label= 'Sign Up')

    email = StringField(label='Email Address', validators=
                           [InputRequired(message="email name should not be blank"),
                            Length(max=45, message="Email should have less than 45 characters")])
