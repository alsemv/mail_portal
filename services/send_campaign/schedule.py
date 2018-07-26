from dateutil.relativedelta import relativedelta
from datetime import datetime
from services.send_campaign.message import Message
from services.send_campaign.recipient_repository import RecipientRepository
from services.send_campaign.sender import Sender
from src import db
from src.models.campaigns.campaign import Campaign
from src.models.forms.form_filled import FormFilled
from src.models.recipients.recipient import Recipient


class Schedule(object):
    def __init__(self, campaign: Campaign, form_filled: FormFilled()):
        self.campaign = campaign
        self.form_filled = form_filled
        self.recipient_repo = RecipientRepository(Recipient(), self.campaign, self.form_filled)

    def reminder_period(self):
        return self.campaign.alert.reminder_interval

    def update_period(self):
        return self.campaign.alert.update_interval

    def get_remind_date(self):
        date = datetime.today() - relativedelta(days=self.reminder_period())
        return date.strftime("%Y/%m/%d")

    def get_update_data(self):
        date = datetime.today() - relativedelta(days=self.update_period())
        return date.strftime("%Y/%m/%d")

    def check_and_send_remind(self):
        recipients_to_remind = self.recipient_repo.recipients_to_remind()
        for recipient in recipients_to_remind:
            if self.get_remind_date() == recipient.last_send_date.strftime("%Y/%m/%d"):
                message = Message(self.campaign, recipient)
                Sender.send_email(recipient.email, message.crate_subject_remind(), message.create_message_remind())
                recipient.last_send_date = datetime.now()
                db.session.add(recipient)
        db.session.commit()

    def check_and_send_update(self):
        recipients_submitted_form = self.recipient_repo.recipient_submitted_form()
        for recipient in recipients_submitted_form:
            form_filled = self.form_filled.query.filter_by(recipient_id=recipient.id).filter_by(campaign_id=self.campaign.id).first()
            if self.get_update_data() == form_filled.date.strftime("%Y/%m/%d"):
                message = Message(self.campaign, recipient)
                Sender.send_email(recipient.email, message.crate_subject_update(), message.create_message_update())
                recipient.last_send_date = datetime.now()
                db.session.add(recipient)
                form_filled.date = datetime.now()
                db.session.add(form_filled)
        db.session.commit()

    def send_first_email(self):
        recipients_list = self.campaign.recipients.filter(Recipient.last_send_date == None).all()

        for recipient in recipients_list:
            message = Message(self.campaign, recipient)
            Sender.send_email(recipient.email, message.crate_subject_remind(), message.create_message_remind())
            recipient.last_send_date = datetime.now()
            db.session.add(recipient)
        db.session.commit()
