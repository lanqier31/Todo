#!flask/bin/python
# -*-coding:utf-8 -*-

import os

from flask import Flask
from flask_login import LoginManager
# from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy

from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app,use_native_unicode='utf8')                          #创建数据库实例

login_manager=LoginManager()
app.config['SECRET_KEY']='234324234'
login_manager.session_protection = "basic"
login_manager.init_app(app)
login_manager.login_view='login'
# oid=OpenID(app,os.path.join(basedir,'tmp'))

from app.models import Category,Todo,WebLoad,PageDetail,TestSuite,Roles,PermType,Permission,User,Audit
from app.controllers import todo,frontPerform,knowledge,setting,Items
