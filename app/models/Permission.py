from app import db
from flask_login import UserMixin
from datetime import datetime
from flask import jsonify


class Permission(db.Model, UserMixin):
    __tablename__ = 'permission'
    ID = db.Column(db.Integer, primary_key=True)
    PermName = db.Column(db.String(100))
    URL = db.Column(db.String(200))
    DESCRIPTION = db.Column(db.String(200))
    SEQ = db.Column(db.Integer)
    TARGET = db.Column(db.String(100))
    PermType_ID = db.Column(db.String, db.ForeignKey('perm_type.ID'))
    parent_ID = db.Column(db.String, db.ForeignKey('permission.ID'))
    parent = db.relationship('Permission', remote_side=[ID], backref='Permission', uselist=False)

    def get_id(self):
        return str(self.ID)

    def to_json(self):
        return {
            'id': self.ID,
            'permName': self.PermName,
            'url': self.URL,
            'description': self.DESCRIPTION,
            'seq': self.SEQ,
            'target': self.TARGET,
            'pid': self.get_pid(),
            'PermType': self.get_type_json()
        }

    def to_menu_json(self):
        return {
            'id': self.ID,
            'pid': self.get_pid(),
            'state': 'open',
            'checked': False,
            'attributes': {
                'target': self.TARGET,
                'url': self.URL
            },
            'text': self.PermName
        }

    def get_pid(self):
        if self.parent:
            return self.parent.PermName
        return ''

    def get_child(self, pid):
        children = Permission.query.filter_by(parent_ID=pid).all()
        childs=[]
        cd={}
        for p in children:
            cd['cname']= p.PermName
            cd['cid'] = p.ID
            childs.append(cd)
            cd={}
        return childs

    def get_type_json(self):
        if self.type:
            return self.type.to_json()
        return {}

    def __repr__(self):
        return '<Permission permName:%r url:%r >\n' %(self.PermName, self.URL)

    def __init__(self, PermName, URL, PermType_ID,parent_ID,DESCRIPTION):
        self.PermName = PermName
        self.URL = URL
        self.PermType_ID = PermType_ID
        self.parent_ID = parent_ID
        self.DESCRIPTION = DESCRIPTION