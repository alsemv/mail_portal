from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask_login import login_required, current_user
from src import db
from src.models.campaigns.campaign import Campaign
from src.models.recipients.forms import CreateRecipientForm
from src.models.recipients.recipient import Recipient
from src.models.users.user import User

recipient_blueprint = Blueprint('recipient', __name__, url_prefix="/recipient")


@recipient_blueprint.route('/list')
@login_required
def index():
    return render_template('recipients/index.html')


@recipient_blueprint.route('/json/<string:user_id>', methods=['GET'])
def all_recipients_json(user_id):
    user = User.query.filter_by(id=user_id).first()
    recipients = user.recipients
    recipients_list = [recipient.serialize() for recipient in recipients]

    return jsonify(data=recipients_list)


@recipient_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateRecipientForm()
    if form.validate_on_submit():
        recipient = Recipient()
        recipient.user_id = current_user.id
        recipient.name = form.name.data
        recipient.email = form.email.data
        recipient.state = form.state.data
        db.session.add(recipient)

        campaign = Campaign().query.one()
        campaign.recipients.append(recipient)
        db.session.add(campaign)

        db.session.commit()
        return redirect(url_for('recipient.index'))
    return render_template('recipients/create.html', form=form)


@recipient_blueprint.route('/edit/<string:recipient_id>', methods=['GET', 'POST'])
@login_required
def edit(recipient_id):
    form = CreateRecipientForm()
    recipient = Recipient.query.filter_by(id=recipient_id).first()
    if form.validate_on_submit():
        recipient.name = form.name.data
        recipient.email = form.email.data
        recipient.state = form.state.data
        db.session.add(recipient)
        db.session.commit()
        return redirect(url_for('recipient.index'))
    return render_template('recipients/edit.html', form=form, data=recipient)


@recipient_blueprint.route('/delete/<string:recipient_id>', methods=['GET', 'POST'])
@login_required
def delete(recipient_id):
    recipient = Recipient.query.filter_by(id=recipient_id).first()
    db.session.delete(recipient)
    db.session.commit()
    return redirect(url_for('recipient.index'))
