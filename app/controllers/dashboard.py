# -*-coding:utf-8-*-
from flask_login import login_required, login_user, logout_user, current_user
from flask import request,render_template,flash,escape,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.User import User
from app.models.Category import Category
from app.models.Todo import Todo
from app.models.Audit import Audit
from app.controllers import setting
from app.forms import LoginForm
import os ,json,sys
from app import app,db
from datetime import date,timedelta,datetime
from sqlalchemy import extract
reload(sys)
sys.setdefaultencoding('utf8')


@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    try:
        statics = {}
        statics['sum'] =len( Todo.query.all())
        statics['unresolves'] = len(Todo.query.filter_by(status='Unresolved').all())
        statics['completes'] = len(Todo.query.filter_by(status='Completed').all())
        statics['closeds']  = len(Todo.query.filter_by(status='Closed').all())
        statics['bugs'] = len(Todo.query.filter_by(worktype ='bug').all())
        statics['requests'] = len (Todo.query.filter(Todo.worktype !='bug').all())
        # statics = jsonify(statics)
        return render_template('dashboard.html',statics = statics)
    except IOError:
        return "error"