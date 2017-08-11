# -*-coding:utf-8-*-
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.User import User
from app.models.Category import Category
from app.models.Todo import Todo
import os ,json,sys
from app import app,db
from sqlalchemy import func
reload(sys)
sys.setdefaultencoding("utf-8")

@app.route('/show_entries')
def show_entries():
    category = Category.query.all()
    return render_template('show_entries.html',entries=category)


@app.route('/todo',methods=['GET','POST'])
def todo():
    todolists = []
    data = {}

    version = request.args.get('version')
    module = request.args.get('module')
    worktype = request.args.get('worktype')
    status = request.args.get('status')

    print version, module, worktype, status
    query = Todo.query
    if (version != "all") and (version is not None):
        query = query.filter_by(version=version)
    if (module != 'all') and (module is not None):
        query = query.filter_by(module=module)
    if (worktype != 'all') and (worktype is not None):
        query = query.filter_by(worktype=worktype)
    if (status != 'all') and (status is not None):
        query = query.filter_by(status=status)
    todolist = query.all()
    total = len(todolist)

    for todo in todolist:
        todolists.append(todo.to_dict())
    rows = json.dumps(todolists, ensure_ascii=False)
    data['total'] = total
    data['rows'] = rows
    # data = json.dumps(data)
    print rows
    return render_template('todo.html',rows=rows)


@app.route('/query_todo',methods=['GET','POST'])
def query_todo():
    try:
        todolists = []
        data = {}

        version = request.args.get('version')
        module = request.args.get('module')
        worktype = request.args.get('worktype')
        status = request.args.get('status')

        print version, module, worktype, status
        query = Todo.query
        if (version != "all") and (version is not None):
            query = query.filter_by(version=version)
        if (module != 'all') and (module is not None):
            query = query.filter_by(module=module)
        if (worktype != 'all') and (worktype is not None):
            query = query.filter_by(worktype=worktype)
        if (status != 'all') and (status is not None):
            query = query.filter_by(status=status)
        todolist = query.all()
        total = len(todolist)

        for todo in todolist:
            todolists.append(todo.to_dict())
        rows = json.dumps(todolists, ensure_ascii=False)
        data['total'] = total
        data['rows'] = rows
        data = json.dumps(data)
        print rows
        return rows
    except IOError:
        return "error"


@app.route('/add_todo',methods={'POST'})
def add_todo(charset='utf-8'):
    if not session.get('login_in'):
        abort(401)
    try:
        data = str(request.values)
        # print data
        project = request.form.get('project')
        version = request.form.get('version')
        worktype = request.form.get('worktype')
        module = request.form.get('module')
        title = request.form.get('title',"null")
        description = request.form.get('description')
        # developer = json.dumps(request.form.getlist('developer[]'))
        developer = map(int, request.form.getlist('developer[]'))
        developer=str(developer)
        # tester = json.dumps(request.form.getlist('tester[]'))
        tester = map(int, request.form.getlist('tester[]'))
        tester=str(tester)
        status = request.form.get('status')
        createtime = request.form.get('createtime')
        completetime = request.form.get('completetime')
        remarks = request.form.get('remarks')
        print tester
        todo = Todo(project,version,worktype,module,title,description,developer,tester,status,createtime,completetime,remarks)
        print todo
        db.session.add(todo)
        db.session.commit()
        flash('New todo was successfully posted')
        return redirect(url_for('todo'))
    except IOError:
        print IOError


@app.route('/edit_todo',methods=['GET','POST'])
def edit_todo():
    try:
        id = request.form.get("pk","null")
        field=request.form.get("name","null")
        value=request.form.get("value",'null')
        todo = Todo.query.get(id)
        if(field=='status'):
            todo.status=value
        elif(field=='developer'):

            developer = map(int, request.form.getlist('value[]'))
            developer = str(developer)
            todo.developer=developer
        elif(field=='tester'):
            tester=map(int,request.form.getlist('value[]'))
            tester=str(tester)
            todo.tester=tester
        elif(field=='remarks'):
            todo.remarks=value
        elif (field == 'description'):
            todo.description=value
        elif(field=='title'):
            todo.title=value
        elif(field=='module'):
            todo.module=value
        elif(field=='worktype'):
            todo.worktype=value
        todo.save()
        return 'success';
    except IOError:
        return "error"


@app.route('/delete_todo',methods=['GET','POST'])
def delete_todo():
    try:
        ids=map(int,request.form.getlist('ids[]'))
        print ids
        for id in ids:
            todo=Todo.query.get(id)
            db.session.delete(todo)
            db.session.commit()
        return 'success'
    except IOError:
        print IOError
        return 'error'





@app.route('/add',methods={'POST'})
def add_entry():
    if not session.get('login_in'):
        abort(401)
    title = request.form['title']
    content = request.form['text']
    category = Category(title,content)
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user =User.query.filter_by(username= request.form['username']).first()
        passwd = User.query.filter_by(password=request.form['password']).first()

        if user is None:
            error = 'Invaild username'
        elif passwd is None:
            error = 'Invaild password'
        else:
            session['login_in'] = True
            flash('You were logged in')
            return redirect(url_for('todo'))
    return render_template('login.html',error=error)


@app.route('/logout')
def logout():
    session.pop('login_in',None)
    flash('You were logged out')
    return redirect(url_for('todo'))










































