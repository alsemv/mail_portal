from flask import Blueprint, render_template, flash
from flask_login import login_required
from services.import_campaign.import_recipients import ImportRecipients
from src.models.campaigns.forms import ImportForm

campaign_blueprint = Blueprint('campaign', __name__, url_prefix='/campaign')


@campaign_blueprint.route('import', methods=['GET', 'POST'])
@login_required
def recipient_import():
    form = ImportForm()
    if form.validate_on_submit():
        file = form.file.data
        imp_recip = ImportRecipients(file)
        imp_recip.add_recipients()
        flash('You are successfully imported recipients', 'success_import')
    return render_template('campaign/import.html', form=form)