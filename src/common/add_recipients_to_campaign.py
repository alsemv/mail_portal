from src import db
from src.models.recipients.recipient import Recipient
from src.models.campaigns.campaign import Campaign

#recipients = db.session.query(Recipient).filter(Recipient.id.in_((10003, 10004))).all()
recipients = db.session.query(Recipient).filter(Recipient.id.in_(list(range(1, 101)))).all()
campaign = Campaign.query.get(2)
campaign.recipients.extend(recipients)
db.session.add(campaign)
db.session.commit()