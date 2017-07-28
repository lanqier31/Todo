from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from app.models.User import User
from app.models.Todo import Todo
import os
from app import app,db


@app.route('/todo',methods=['GET','POST'])
def todo():
    todolist = todo.query.all()
    print todolist
    return render_template('todo.html', entries=todolist)


@app.route('/add',methods={'POST'})
def add_todo():
    if not session.get('login_in'):
        abort(401)
    project = request.form['project']
    version = request.form['version']
    worktype = request.form['worktype']
    title = request.form['title']
    description = request.form['description']
    developer = request.form['developer']
    tester = request.form['tester']
    status = request.form['status']
    createtime = request.form['createtime']
    completetime = request.form['completetime']
    remarks = request.form['remarks']
    atodo = todo(project,version,worktype,title,description,developer,tester,status,createtime,completetime,remarks)
    db.session.add(atodo)
    db.session.commit()
    flash('New todo was successfully posted')
    return redirect(url_for('todo'))