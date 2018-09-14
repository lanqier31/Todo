# -*-coding:utf-8-*-
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from flask_login import login_required, login_user, logout_user, current_user
from app.models.Roles import Role
from app.models.User import User
from app.models.PermType import PermType
from app.models.Permission import Permission
import os ,json,sys
from app import app,db

from datetime import date,timedelta
from sqlalchemy import extract
reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/user',methods=['GET', 'POST'])
@login_required
def user():
    if current_user.Is_Admin:
        roles = Role.query.all()
        return render_template('setting/user.html', roles=roles)
    return render_template('setting/user.html', roles=roles)

@app.route('/getRoles')
def getRoles():
    rolelist=[]
    rolev={}
    roles = Role.query.all()
    for role in roles:
        rolev['value']=role.id
        rolev['text']=role.name
        rolelist.append(rolev)
        rolev={}
    return jsonify(rolelist)


@app.route('/edit_user',methods=['GET', 'POST'])
def edit_user():

        id = request.form.get("pk","null")

        field=request.form.get("name","null")
        user = User.query.get(id)
        for r in user.roles:
            print r
            user.roles.remove(r)
        db.session.commit()
        if(field == 'roles'):
            roles = request.form.getlist('value[]')
            for r in roles:
                role = Role.query.get(r)
                if not role in user.roles:
                    user.roles.append(role)
        db.session.commit()
        return 'success'


@app.route('/role')
@login_required
def role():
    permissions = Permission.query.all()
    roles = Role.query.all()

    return render_template('setting/Roles.html', permissions=permissions)


@app.route('/query_user',methods=['GET', 'POST'])
def query_user():
    try:
        users = []
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        userlist = User.query.all()
        total = len(userlist)
        for u in userlist:
            users.append(u.to_json())
        return jsonify({"total": total, 'rows': users[int(offset):(int(offset) + int(limit))]})

    except IOError:
        return "error"


@app.route('/query_developers',methods = ['GET','POST'])
def query_developers():
    try:
        develops =[]
        role =Role.query.get(2)    #查询开发的角色
        users = User.query.filter(User.roles.contains(role)).all()
        for user in users:
            develops.append(user.to_json())
        return develops
    except IOError:
        return "error"


@app.route('/developers',methods = ['GET','POST'])
def developers():
    try:
        develops =[]
        role =Role.query.get(2)    #查询开发的角色
        users = User.query.filter(User.roles.contains(role)).all()
        for user in users:
            develops.append(user.to_json())
        return jsonify(develops)
    except IOError:
        return "error"


@app.route('/testers',methods = ['GET','POST'])
def testers():
    try:
        tests =[]
        role =Role.query.get(3)    #查询开发的角色
        users = User.query.filter(User.roles.contains(role)).all()
        for user in users:
            tests.append(user.to_json())
        return jsonify(tests)
    except IOError:
        return "error"


@app.route('/query_testers',methods = ['GET','POST'])
def query_testers():
    try:
        testers =[]
        role = Role.query.get(3)  # 查询开发的角色
        users = User.query.filter(User.roles.contains(role)).all()
        for user in users:
            testers.append(user.to_json())
        return testers
    except IOError:
        return "error"


@app.route('/query_role', methods=['GET', 'POST'])
def query_role():
    try:
        roles = []
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        rolelist = Role.query.all()
        total = len(rolelist)
        for r in rolelist:
            roles.append(r.to_json())
        return jsonify({"total": total, 'rows': roles[int(offset):(int(offset) + int(limit))]})

    except IOError:
        return "error"


@app.route('/query_permission', methods=['GET', 'POST'])
def query_permission():
    try:
        permissions = []
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        plist = Permission.query.all()
        total = len(plist)
        for r in plist:
            permissions.append(r.to_json())
        return jsonify({"total": total, 'rows': permissions[int(offset):(int(offset) + int(limit))]})

    except IOError:
        return "error"


@app.route('/add_user',methods=['GET', 'POST'])
def add_user():
    try:
        username = request.form.get('username')
        loginname = request.form.get('loginname')
        password = request.form.get('password')
        roles = request.form.getlist('roles[]')
        active = int(request.form.get('active'))
        user = User(loginname,username,password,active)
        db.session.add(user)
        for r in roles:
            role = Role.query.get(r)
            user.roles.append(role)
        db.session.commit()
        flash('New user was successfully posted')
        return redirect(url_for('user'))
    except IOError:
        print IOError


@app.route('/delete_user',methods=['GET','POST'])
def delete_user():

    try:
        ids=map(int,request.form.getlist('ids[]'))
        # ides = request.form.getlist('ids[]')
        for id in ids:
            u=User.query.get(id)
            db.session.delete(u)
            db.session.commit()
        return 'success'
    except IOError:
        print IOError
        return 'error'



@app.route('/add_role',methods=['GET', 'POST'])
def add_role():
    try:

        name = request.form.get('name')
        description = request.form.get('description')
        role = Role(name,description)
        db.session.add(role)
        db.session.commit()
        flash('New todo was successfully posted')
        return redirect(url_for('role'))
    except IOError:
        print IOError


@app.route('/delete_role',methods=['GET','POST'])
def delete_role():

    try:
        ids=map(int,request.form.getlist('ids[]'))
        # ides = request.form.getlist('ids[]')
        for id in ids:
            role=Role.query.get(id)
            db.session.delete(role)
            db.session.commit()
        return 'success'
    except IOError:
        print IOError
        return 'error'

@app.route('/show_Fun', methods=['POST'])
def show_Fun():
    role_id = map(int, request.form.getlist('role_id[]'))
    role_id = int(role_id[0])
    ids=[]
    role_permissions = Role.query.filter_by(id=role_id).first().permissions
    for perm in role_permissions:
        ids.append(perm.ID)
    result = jsonify({'role_id':role_id,'ids':ids})
    return result


@app.route('/show_permissionTree', methods=['GET', 'POST'])
def show_permissionTree():
    data = []
    chs= []
    parents= Permission.query.filter_by(PermType_ID=1)   #查询所有的菜单项
    #列出每个菜单项对应的子功能
    for p in parents:
        da = {"text": p.PermName,"id":p.ID,"nodeId":p.ID}
        children = p.get_child(p.ID)

        if children:
            for child in children:
                chs.append({"text": child['cname'],"id":child['cid'],"nodeId":child['cid']})
                da['nodes']=chs
            chs = []
        data.append(da)
        # print data
    return jsonify(data)


@app.route('/grant_Fun', methods=['GET','POST'])
def grant_Fun():
    role_id = request.form.get('roleId')
    permissions_ids = map(int, request.form.getlist('permIds[]'))
    role = Role.query.filter_by(id=role_id).first()

    for per in role.permissions:
        role.permissions.remove(per)       #delete all permissions in role
        db.session.commit()
        role = Role.query.filter_by(id=role_id).first()
    # print role.permissions   # IT should be [] ，however it has error
    for id in permissions_ids:
        perm=Permission.query.filter_by(ID=id).first()
        if not perm in role.permissions:
            role.permissions .append(perm)
    db.session.commit()
    return jsonify({'success': True})


# @app.route('/delete_role', methods=['POST'])
# def delete_role():
#     role = Role.query.get(request.form.get('id'))
#     if role:
#         db.session.delete(role)
#     return jsonify({'success': True})


@app.route('/permission')
@login_required
def permission():
    permTypes = PermType.query.all()
    parennts = Permission.query.filter_by(PermType_ID=1).all()
    return render_template('setting/Permission.html', permTypes=permTypes, parents=parennts)


@app.route('/add_permission',methods=['GET', 'POST'])
def add_permission():
    try:

        permName = request.form.get('permissioname')
        url = request.form.get('url')
        permtype = request.form.get('permType')
        pid = request.form.get('parent')
        description = request.form.get('description')

        perm = Permission(permName,url,permtype,pid,description)
        db.session.add(perm)
        db.session.commit()
        flash('New todo was successfully posted')
        return redirect(url_for('permission'))
    except IOError:
        print IOError


@app.route('/delete_permission',methods=['GET','POST'])
def delete_permission():

    try:
        ids=map(int,request.form.getlist('ids[]'))
        # ides = request.form.getlist('ids[]')
        for id in ids:
            perm=Permission.query.get(id)
            db.session.delete(perm)
            db.session.commit()
        return 'success'
    except IOError:
        print IOError
        return 'error'








