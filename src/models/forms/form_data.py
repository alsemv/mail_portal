import datetime
from src import db


class FormData(db.Model):
    __tablename__ = "form_data"
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipients.id'), index=True, nullable=False)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'), index=True, nullable=False)
    responsible = db.Column(db.String(255),  nullable=False)
    business_unit = db.Column(db.String(255),  nullable=False)
    product_per_year = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String,  nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return '<FormData %r>' % self.id

    def add(self, form, recipient_id, form_id):
        self.recipient_id = recipient_id
        self.form_id = form_id
        self.responsible = form.responsible.data
        self.business_unit = form.business_unit.data
        self.product_per_year = form.product_per_year.data
        self.address = form.address.data
        self.date = datetime.datetime.now()
        db.session.add(self)

    def update(self, form):
        self.responsible = form.responsible.data
        self.business_unit = form.business_unit.data
        self.product_per_year = form.product_per_year.data
        self.address = form.address.data
        self.date = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()
