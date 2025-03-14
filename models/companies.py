from sqlalchemy.sql import func

from db import db


class CompanyModel(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String, nullable=False)
    workday_url = db.Column(db.String)
    equity_ticker = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    opening_snapshots = db.relationship('OpeningSnapshot', back_populates='company')
    applications = db.relationship('Application', back_populates='company', cascade='all, delete-orphan')