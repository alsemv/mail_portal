from src import db
from src.models.recipients.recipient import Recipient
from src.models.alerts.alert import Alert

campaigns_recipients = db.Table('campaigns_recipients',
    db.Column('campaign_id', db.Integer, db.ForeignKey('campaigns.id'), index=True, primary_key=True),
    db.Column('recipient_id', db.Integer, db.ForeignKey('recipients.id'), index=True, primary_key=True)
)


class Campaign(db.Model):
    __tablename__ = "campaigns"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, nullable=False)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'), index=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    unique_opens = db.Column(db.Integer)
    recipients = db.relationship('Recipient', secondary=campaigns_recipients, lazy='dynamic', backref=db.backref('campaigns', lazy='dynamic'))
    alert = db.relationship("Alert", backref='campaign', lazy=True, uselist=False)
    date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return '<Campaign %r>' % self.name