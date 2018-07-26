from src import db


class Recipient(db.Model):
    __tablename__ = 'recipients'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    last_send_date = db.Column(db.DateTime())
    form_data = db.relationship("FormData", backref='recipient', lazy=True)

    def __repr__(self):
        return '<Recipient %r>' % self.name

    def serialize(self):
       return {
           'id': self.id,
           'email': self.email,
           'name': self.name,
           'user_name': self.user.username,
           'state': self.state,
           'last_send_date': self.last_send_date
       }