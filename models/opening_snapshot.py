from db import db


class OpeningSnapshot(db.Model):
    __tablename__ = 'opening_snapshot'

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    snapshot_date = db.Column(db.Date, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    new_york = db.Column(db.Integer, nullable=False)

    company = db.relationship('Company', back_populates='opening_snapshots')

    __table_args__ = (
        db.UniqueConstraint('company_id', 'snapshot_date', name='uq_company_date'),
    )
