from app import db
from flask_login import UserMixin
from datetime import datetime


class PermType(db.Model, UserMixin):
    __tablename__ = 'perm_type'
    ID = db.Column(db.String(36), primary_key=True)
    TypeName = db.Column(db.String(100))
    DESCRIPTION = db.Column(db.String(200))
    permissions = db.relationship('Permission',  backref='type', lazy='dynamic')

    def to_json(self):
        return {
            'id': self.ID,
            'typename': self.TypeName,
            'description': self.DESCRIPTION
        }

    def __repr__(self):
        return '<PermType %r>\n' % self.TypeName



