from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import validators


class ImportForm(FlaskForm):
    file = FileField(validators=[validators.DataRequired(), FileRequired(), FileAllowed(['csv'])])