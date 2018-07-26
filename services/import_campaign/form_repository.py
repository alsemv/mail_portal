import datetime

from flask_login import current_user

from src import db
from src.models.forms.form import Form


class FormRepository(object):

    def add_form(self):
        form = Form()
        form.name = "form_{}".format(current_user.id)
        form.user_id = current_user.id
        form.date = datetime.datetime.now()
        db.session.add(form)
        db.session.commit()
        return form
