#!flask/bin/python
# -*-coding:utf-8 -*-

import os

from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy

from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)                          #创建数据库实例

lm=LoginManager()
lm.init_app(app)
lm.login_view='login'
oid=OpenID(app,os.path.join(basedir,'tmp'))

from app.models import User,Category,Todo
from app.controllers import blog_message,frontPerform
