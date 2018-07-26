import datetime
from flask_login import current_user
from src import db
from src.models.campaigns.campaign import Campaign


class CampaignRepository(object):
    def __init__(self, form_id):
        self.form_id = form_id

    def add_campaign(self):
        campaign = Campaign()
        campaign.user_id = current_user.id
        campaign.form_id = self.form_id
        campaign.name = 'campaign_{}'.format(current_user.id)
        campaign.date = datetime.datetime.now()
        db.session.add(campaign)
        db.session.commit()
        return campaign
