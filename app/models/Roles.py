#coding:utf-8

from app import db
from flask_security import RoleMixin,UserMixin





#角色权限关联表
roles_permissions = db.Table('roles_permissions',
                             db.Column('role_id',db.Integer(),db.ForeignKey('role.id')),
                             db.Column('permission_ID',db.Integer,db.ForeignKey('permission.ID')))


class Role(db.Model,RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True)
    description = db.Column(db.String(255))
    permissions = db.relationship('Permission', secondary=roles_permissions, backref=db.backref('roles', lazy='dynamic'))

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __repr__(self):
        return '<Role %r>' % self.name

    def get_id(self):
        return str(self.id)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'permissions': self.get_permissions()
        }

    def get_permissions(self):
        permnames=[]
        if self.permissions:
            for perm in self.permissions:
                perm.to_json()
                permnames.append(perm.PermName)
        return permnames

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])





