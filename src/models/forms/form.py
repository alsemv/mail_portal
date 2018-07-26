from src import db


class Form(db.Model):
    __tablename__ = "forms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    form_data = db.relationship("FormData", backref='form', lazy=True)
    campaigns = db.relationship("Campaign", backref='form', lazy=True)

    def __repr__(self):
        return '<Form %r>' % self.name