"""Defines form for creating volunteering opportunities.

   Requires:
   -Flaskform
   -WTForms
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired


class OpportunitiesForm(FlaskForm):
    """Defines form fields and a validators"""
    title = StringField(label='Title of Opportunity',
                        validators=[InputRequired(message='Title cannot be left blanks')])

    status = SelectField(label='Status',
                         choices=['open', 'closed'],
                         validate_choice=True)

    categories = SelectField(label='Categories', coerce=str)

    description = TextAreaField(label='Description',
                                validators=[InputRequired("Briefly explain the details of your project")])

    location = StringField(label='Location',
                           validators=[InputRequired(message='Location cannot be left blanks')])
