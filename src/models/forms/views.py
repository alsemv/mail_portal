from flask import Blueprint, render_template, redirect, url_for
import src.models.forms.decorators as form_decorators
from src import db
from src.models.campaigns.campaign import Campaign
from src.models.forms.form_data import FormData
from src.models.forms.form_filled import FormFilled
from src.models.forms.forms import RecipientForm

form_blueprint = Blueprint('form', __name__, url_prefix='/form')

#check if recipient have permission to open this form


@form_blueprint.route('/<string:campaign_id>/<string:recipient_id>', methods=['GET'])
@form_decorators.check_campaign
def campaign_form(campaign_id, recipient_id):
    form = RecipientForm()

    campaign = Campaign.query.get(campaign_id)
    form_id = campaign.form.id
    form_filled = db.session.query(FormData).filter(FormData.form_id.like(form_id),
                                                  FormData.recipient_id.like(recipient_id)).first()
    if not form_filled:
        return render_template('forms/index.html', form=form, campaign_id=campaign_id, recipient_id=recipient_id)
    else:
        data_recipient_filled = FormData.query.filter_by(recipient_id=recipient_id).first()
        return render_template('forms/edit.html', form=form, campaign_id=campaign_id, recipient_id=recipient_id, data=data_recipient_filled)


@form_blueprint.route('/store/<string:campaign_id>/<string:recipient_id>', methods=['POST'])
def store_form_data(campaign_id, recipient_id):
    form = RecipientForm()
    campaign = Campaign.query.get(campaign_id)
    form_id = campaign.form.id

    if form.validate_on_submit():

        form_data = FormData()
        form_data.add(form, recipient_id, form_id)
        form_filled = FormFilled()
        form_filled.add(campaign_id, recipient_id)
        db.session.commit()

        return redirect(url_for('form.submit_success'))
    else:
        errors = form.errors.items()
        return render_template('forms/index.html', form=form, errors=errors, campaign_id=campaign_id, recipient_id=recipient_id)


@form_blueprint.route('/update/<string:recipient_id>', methods=['POST'])
def update_form_data(recipient_id):
    form = RecipientForm()

    if form.validate_on_submit():
        form_data = FormData().query.filter_by(recipient_id=recipient_id).first()
        form_data.update(form)
        return redirect(url_for('form.submit_success'))
    else:
        data_recipient_filled = FormData.query.filter_by(recipient_id=recipient_id).first()
        errors = form.errors.items()
        return render_template('forms/edit.html', form=form, errors=errors, recipient_id=recipient_id, data=data_recipient_filled)


@form_blueprint.route('/success')
def submit_success():
    return render_template('form_submitted.html')
