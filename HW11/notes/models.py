from app import db
from datetime import datetime


class ContactBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<ContactBook %r>' % self.id