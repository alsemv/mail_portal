from functools import wraps
from flask import render_template
from src.models.campaigns.campaign import Campaign
from src.models.recipients.recipient import Recipient


def check_campaign(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        campaign_id = kwargs['campaign_id']
        recipient_id = kwargs['recipient_id']

        if Campaign.query.get(campaign_id) is not None and Recipient.query.get(recipient_id) is not None:
            return func(*args, **kwargs)
        return render_template('404.html'), 404
    return decorated_function

