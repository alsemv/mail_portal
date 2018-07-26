from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


def integer_type_check(form, field):
    try:
        int(field.data)
    except Exception:
        raise ValidationError('This field must be integer type')


class AlertForm(FlaskForm):
    reminder_interval = StringField('reminder_interval', validators=[validators.DataRequired(), integer_type_check])
    update_interval = StringField('update_interval', validators=[validators.DataRequired(), integer_type_check])