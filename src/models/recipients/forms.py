from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CreateRecipientForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    email = StringField('email', validators=[validators.DataRequired(), validators.Regexp('^.+@[^.].*\.[a-z]{2,10}$', message='Invalid email address.')])
    state = StringField('state', validators=[validators.DataRequired()])