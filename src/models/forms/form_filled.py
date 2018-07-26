import datetime
from src import db


class FormFilled(db.Model):
    __tabelename__ = "form_filled"
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipients.id'), index=True, nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), index=True, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    def add(self, campaign_id, recipient_id):
        self.recipient_id = recipient_id
        self.campaign_id = campaign_id
        self.date = datetime.datetime.now()
        db.session.add(self)
