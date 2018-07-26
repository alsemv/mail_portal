from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from src import db
from src.models.alerts.alert import Alert
from src.models.alerts.forms import AlertForm

alert_blueprint = Blueprint('alert', __name__,  url_prefix="/alert")


@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
@login_required
def edit(alert_id):
    alert = Alert().query.filter_by(id=alert_id).first()
    days = list(range(1, 366))
    form = AlertForm()

    if form.validate_on_submit():
        alert.reminder_interval = form.reminder_interval.data
        alert.update_interval = form.update_interval.data
        db.session.add(alert)
        db.session.commit()
        return redirect(url_for('alert.edit', alert_id=alert.id))
    return render_template('alert/edit.html', days=days, form=form, alert=alert)
