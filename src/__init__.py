from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config.Dev')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from src.models.users.user import User
from src.models.users import user
from src.models.recipients import recipient
from src.models.forms import form
from src.models.forms import form_data
from src.models.forms import form_filled
from src.models.campaigns import campaign
from src.models.alerts import alert
import src.widgets


@app.route('/')
def main():
    return redirect(url_for('recipient.index'))

