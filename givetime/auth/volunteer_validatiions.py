#!/usr/bin/python3
"""Handles form validations for volunteer authentication"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class VolunteerSignUpForm(FlaskForm):
    """Defines Validators for nonprofit sign-up form"""
    name = StringField(label='Organisation Name', validators=
                           [InputRequired(message="Organisation name cannot be blank"),
                            Length(min=5,max=50)])

    email = StringField(label='Email Address',
                        validators=[InputRequired(message="email name should not be blank"),
                                    Length(max=45, message="Email should have less than 45 characters")])

    password = PasswordField(label='Password', validators=
                             [InputRequired(message="Password should not be left blank"),
                              Length(max=10, message="Password too long")])
    
    skills = TextAreaField(lable='Skill',
                                validators=[InputRequired(message='Provide short description of your NGO')])
    

    website = StringField(label='Website URL')

    city = StringField(label='City', validators=[InputRequired(message='Provide city')])

    state = StringField(label='State', validators=[InputRequired(message='Provide city')])



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
