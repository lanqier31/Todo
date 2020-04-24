from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from flask_login import login_required, login_user, logout_user, current_user
from app.models.Roles import Role
from app.models.User import User
from app.models.PermType import PermType
from app.models.Permission import Permission
import os ,json,sys
from app import app,db


@app.route('/interfaceTest',methods=['GET', 'POST'])
def interfaceTest():
    return render_template('InterfaceTest/case_detail.html')


@app.route('/caselist',methods=['GET', 'POST'])
def caselist():
    return render_template('InterfaceTest/caselist.html')


@app.route('/reportlist',methods=['GET', 'POST'])
def reportlist():
    return render_template('InterfaceTest/reportlist.html')


@app.route('/query_interfaceTest',methods=['GET','POST'])
def query_interfaceTest():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    try:
        caselist = [
            {'apiID': u'01',
             'apiTitle': u'Login',
             'urlPath': u'http://192.168.10.120/Login',
             'method': u'GET',
             'params': u'',
             'headers': u'\u8d85\u58f0\u58f0\u50cf',
             'testresult': u'SUCCESS'},
            {'apiID': u'02',
             'apiTitle': u'Login',
             'urlPath': u'http://192.168.10.120/Login',
             'method': u'GET',
             'params': u'',
             'headers': u'\u8d85\u58f0\u58f0\u50cf',
             'testresult': u'SUCCESS'},
            {'apiID': u'03',
             'apiTitle': u'Login',
             'urlPath': u'http://192.168.10.120/Login',
             'method': u'GET',
             'params': u'',
             'headers': u'\u8d85\u58f0\u58f0\u50cf',
             'testresult': u'SUCCESS'},
            {'apiID': u'04',
             'apiTitle': u'Login',
             'urlPath': u'http://192.168.10.120/Login',
             'method': u'GET',
             'params': u'',
             'headers': u'\u8d85\u58f0\u58f0\u50cf',
             'testresult': u'SUCCESS'},
         ]
        total = len(caselist)
        return jsonify({"total":total,'rows': caselist[int(offset):(int(offset) + int(limit))]})
    except IOError:
        return "error"