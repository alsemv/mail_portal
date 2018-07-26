from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField, ValidationError
from src import User


class LoginForm(FlaskForm):
    username = StringField('email', validators=[validators.DataRequired(), validators.Length(1, 64)])
    password = PasswordField('password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Keep me logged in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        validators.DataRequired(), validators.Length(1, 64), validators.Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                 'Usernames must have only letters, '
                                                                                 'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        validators.DataRequired(), validators.EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[validators.DataRequired()])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
