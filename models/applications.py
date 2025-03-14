from sqlalchemy.sql import func

from db import db


class ApplicationModel(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    job_title = db.Column(db.String, nullable=False)
    job_req = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    date_submitted = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=func.now(), nullable=False)

    company = db.relationship('Company', back_populates='applications')