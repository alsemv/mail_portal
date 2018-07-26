from src.models.campaigns.campaign import Campaign
from src.models.users.user import User


class CampaignRepository(object):
    def __init__(self, campaign: Campaign, user: User):
        self.campaign = campaign
        self.user = user

    def user_campaigns(self):
        campaigns = self.campaign.query.filter_by(user_id=self.user.id).all()
        return campaigns
