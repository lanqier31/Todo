# -*-coding:utf-8 -*-
from app import db
from flask_security import UserMixin
from app import login_manager

#角色用户关联表
roles_users = db.Table('roles_users',
                       db.Column('user_id',db.Integer(),db.ForeignKey('user.id')),
                       db.Column('role_id',db.Integer(),db.ForeignKey('role.id')))

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10))
    password= db.Column(db.String(16))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role',secondary=roles_users,backref=db.backref('users', lazy='dynamic'))

    def __init__(self,username,password,active):
        self.username = username
        self.password = password
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'roles': self.get_roles()
        }

    def get_roles(self):
        roleids = []
        if self.roles:
            for role in self.roles:
                role.to_json()
                roleids.append(role.id)
        return roleids

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))