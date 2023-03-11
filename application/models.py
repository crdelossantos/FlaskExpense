from application import db
from datetime import datetime
import enum


class IncomeExpenses(db.Model):
    __tablename__ = "IncomeExpenses"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), default = 'expense', nullable=False)
    category = db.Column(db.String(30), nullable=False, default='Cafe')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    





