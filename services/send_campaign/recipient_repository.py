from src.models.campaigns.campaign import Campaign
from src.models.forms.form_filled import FormFilled
from src.models.recipients.recipient import Recipient


class RecipientRepository(object):
    def __init__(self, recipient: Recipient, campaign: Campaign, form_filled: FormFilled):
        self.recipient = recipient
        self.campaign = campaign
        self.form_filled = form_filled

    def all_recipients(self):
        return self.campaign.recipients.all()

    def recipients_to_remind(self):
        all_recipients = self.all_recipients()
        recipients_filled_form = self.recipient_submitted_form()

        all_recipients_set = set(all_recipients)
        recipients_filled_form_set = set(recipients_filled_form)

        recipients_to_remind = list(all_recipients_set.difference(recipients_filled_form_set))
        return recipients_to_remind

    def recipient_submitted_form(self):
        filled_form = self.form_filled.query.filter_by(campaign_id=self.campaign.id).all()
        recipients_filled_form_id = [recipient.recipient_id for recipient in filled_form]
        recipients_filled_form = Recipient.query.filter(Recipient.id.in_(recipients_filled_form_id)).all()
        return recipients_filled_form
