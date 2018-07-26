import csv
import datetime
import io
from flask_login import current_user
from services.import_campaign.alert_repository import AlertRepository
from services.import_campaign.campaign_repository import CampaignRepository
from services.import_campaign.form_repository import FormRepository
from src import db
from src.models.recipients.recipient import Recipient


class ImportRecipients(object):
    def __init__(self, file):
        self.file = file
        self.campaign_recipient = []

    def add_recipients(self):

        form = FormRepository().add_form()
        campaign = CampaignRepository(form.id).add_campaign()
        AlertRepository(campaign.id).add_alert()

        file_contents = self.file.stream.read().decode("utf-8-sig", 'ignore')
        stream_f = io.StringIO(file_contents)
        reader = csv.reader(stream_f, delimiter=';')
        headers = next(reader)

        for item in reader:
            recipient = Recipient()
            recipient.user_id = current_user.id
            recipient.name = item[3]
            recipient.email = item[5]
            recipient.state = item[2]
            # recipient.last_send_date = datetime.datetime.now()
            db.session.add(recipient)

            self.campaign_recipient.append(recipient)

        db.session.commit()

        campaign.recipients.extend(self.campaign_recipient)
        db.session.add(campaign)
        db.session.commit()

        stream_f.seek(0)
