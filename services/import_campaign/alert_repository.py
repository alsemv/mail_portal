from src import db
from src.models.alerts.alert import Alert


class AlertRepository(object):
    def __init__(self, campaign_id):
        self.campaign_id = campaign_id

    def add_alert(self):
        alert = Alert()
        alert.campaign_id = self.campaign_id
        alert.reminder_interval = 15
        alert.update_interval = 180
        db.session.add(alert)
        db.session.commit()