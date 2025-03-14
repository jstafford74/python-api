from db import db


class OpeningModel(db.Model):
    __tablename__ = "openings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    new_york = db.Column(db.Integer, nullable=False)

    company = db.relationship('Company', back_populates='openings')
