from services.send_campaign.campaign_repository import CampaignRepository
from services.send_campaign.schedule import Schedule
from services.send_campaign.user_repository import UserRepository
from src.models.campaigns.campaign import Campaign
from src.models.forms.form_filled import FormFilled
from src.models.users.user import User

users = UserRepository(User())
users_list = users.users_list()

for user in users_list:
    campaign_repo = CampaignRepository(Campaign(), user)
    campaigns = campaign_repo.user_campaigns()
    for campaign in campaigns:
        schedule = Schedule(campaign, FormFilled())
        schedule.check_and_send_remind()
        schedule.check_and_send_update()
