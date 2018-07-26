from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


def integer_type_check(form, field):
    try:
        int(field.data)
    except Exception:
        raise ValidationError('This field must be integer type')


class RecipientForm(FlaskForm):
    responsible = StringField('responsible', validators=[validators.DataRequired()])
    business_unit = StringField('business_unit', validators=[validators.DataRequired()])
    product_per_year = StringField('product_per_year', validators=[validators.DataRequired(), integer_type_check])
    address = StringField('address', validators=[validators.DataRequired()])
