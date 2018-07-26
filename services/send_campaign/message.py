from src import app
from src.models.campaigns.campaign import Campaign
from src.models.recipients.recipient import Recipient


class Message(object):
    def __init__(self, campaign: Campaign, recipient: Recipient):
        self.campaign = campaign
        self.recipient = recipient

    def create_message_remind(self):
        return 'To fill the form, please click the link <a href="http://{server_name}/form/{campaign_id}/{recipient_id}">http://{server_name}/form/{campaign_id}/{recipient_id}</a>'\
            .format(campaign_id=self.campaign.id, recipient_id=self.recipient.id, server_name=app.config['SERVER_NAME'])

    def crate_subject_remind(self):
        return 'Fill the form'

    def create_message_update(self):
        return 'To update the form, please click the link <a href="http://{server_name}/form/{campaign_id}/{recipient_id}">http://{server_name}/form/{campaign_id}/{recipient_id}</a>'\
            .format(campaign_id=self.campaign.id, recipient_id=self.recipient.id, server_name=app.config['SERVER_NAME'])

    def crate_subject_update(self):
        return 'Update the form'


