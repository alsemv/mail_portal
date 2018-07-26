from src import db


class Alert(db.Model):
    __tablename__ = "alerts"
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), index=True, nullable=False)
    reminder_interval = db.Column(db.Integer, default=15, nullable=False)
    update_interval = db.Column(db.Integer, default=180, nullable=False)