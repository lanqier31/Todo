# -*-coding:utf-8-*-
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
# from app.models.Roles import Role,User
from app.models.Category import Category,Article
from app.models.Todo import Todo
import os ,json,sys
from app import app,db
import HTMLParser
from datetime import date,timedelta
from sqlalchemy import extract
reload(sys)
sys.setdefaultencoding("utf-8")