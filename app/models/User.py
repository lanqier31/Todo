# -*-coding:utf-8 -*-
from app import db
from flask_security import UserMixin
from app import login_manager
import json
from flask import jsonify

#角色用户关联表
roles_users = db.Table('roles_users',
                       db.Column('user_id',db.Integer(),db.ForeignKey('user.id')),
                       db.Column('role_id',db.Integer(),db.ForeignKey('role.id')))


class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id=db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(10))
    username = db.Column(db.String(10))
    password= db.Column(db.String(16))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role',secondary=roles_users,backref=db.backref('users', lazy='dynamic'))

    def __init__(self,loginname,username,password,active,roles):
        self.loginname = loginname
        self.username = username
        self.password = password
        self.active = active
        self.roles = roles

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'loginname':self.loginname,
            'active':self.active,
            'roles':self.get_roles,
        }

    def get_roles(self):
        rolenames=[]
        if self.roles:
            for re in self.roles:
                re.to_json()
                rolenames.append(re.name)
        return rolenames

    @property
    def get_roles(self):
        roleids = []
        if self.roles:
            for role in self.roles:
                role.to_json()
                roleids.append(role.id)
        return roleids

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])

    def verify_password(self, password):
        if self.password == password:
            return True
        return False

    @property
    def Is_Admin(self):
        if 'Administrator' in self.roles:
            return True
        return False

    @property
    def permissions(self):
        permissions = []
        if self.roles:
            for role in self.roles:
                if role.get_permissionIds():
                    permissions +=role.get_permissionIds()
        return permissions

    # @property
    # def password_hash(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password_hash.setter
    # def password_hash(self, password):
    #     self.password = generate_password_hash(password)

    # def get_id(self):
    #     return unicode(self.id)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

