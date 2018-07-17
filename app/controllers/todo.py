# -*-coding:utf-8-*-
from flask_login import login_required, login_user, logout_user, current_user
from flask import request,render_template,flash,escape,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.User import User
from app.models.Category import Category
from app.models.Todo import Todo
from app.models.Audit import Audit
from app.forms import LoginForm
import os ,json,sys
from app import app,db
from datetime import date,timedelta,datetime
from sqlalchemy import extract
reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/')
def root():
    return render_template('todo.html')


@app.route('/todo',methods=['GET','POST'])
def todo():
    return render_template('todo.html')


@app.route('/query_todo',methods=['GET','POST'])
def query_todo():
    try:
        todolists = []
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        version = request.args.get('version')
        module = request.args.get('module')
        worktype = request.args.get('worktype')
        status = request.args.get('status')
        time = request.args.get('createtime')
        developer =request.args.get('developer')
        tester= request.args.get('tester')
        searchText=request.args.get('searchText')

        # print searchText
        query = Todo.query
        if (version != "all") and (version is not None):
            query = query.filter_by(version=version)
        if (module != 'all') and (module is not None):
            query = query.filter_by(module=module)
        if (worktype != 'all') and (worktype is not None):
            query = query.filter_by(worktype=worktype)
        if (status != 'all') and (status is not None):
            query = query.filter_by(status=status)
        if (time == 'today'):
            today=date.today()
            query = query.filter_by(createtime=today)
        if (developer != 'all') and (developer is not None):
            developer = '%' + str(developer) + '%'
            query = query.filter(Todo.developer.ilike(developer))

        if (tester != 'all') and (tester is not None):
            tester = '%' + str(tester) + '%'
            query = query.filter(Todo.tester.ilike(tester))

        if (time =='thisyear'):
            year=date.today().year
            query = query.filter(extract('year', Todo.createtime)==year)
        if (time== 'thismonth'):
            year = date.today().year
            month= date.today().month
            query = query.filter(extract('year', Todo.createtime)==year).filter(extract('month', Todo.createtime)==month)
        if (time == 'thisweek'):
            today= date.today()
            weekday = date.today().isoweekday()
            monday = today-timedelta(days=weekday)
            query = query.filter(Todo.createtime.between(monday,today))
        if (time == 'last7day'):
            today = date.today()
            beginday = today - timedelta(7)
            query = query.filter(Todo.createtime.between(beginday, today))

        if(time == 'last30day'):
            today= date.today()
            beginday = today-timedelta(30)
            query = query.filter(Todo.createtime.between(beginday,today))


        if (searchText !=''):
            query = Todo.query.filter_by(id=searchText)
        todolist = query.all()
        total = len(todolist)

        for todo in todolist:
            todolists.append(todo.to_dict())

        return jsonify({"total":total,'rows': todolists[int(offset):(int(offset) + int(limit))]})

    except IOError:
        return "error"


@app.route('/add_todo',methods={'POST'})
def add_todo(charset='utf-8'):
    # if not session.get('login_in'):
    #     abort(401)
    if current_user.is_anonymous:
        return "nouser"
    if 2 not in current_user.permissions:
        return '8'

    try:
        data = str(request.values)
        # print data
        project = request.form.get('project')
        version = request.form.get('version')
        worktype = request.form.get('worktype')
        module = request.form.get('module')
        priority = request.form.get('priority')
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
        plantime = request.form.get('plantime')
        createUser = current_user.username
        completetime = request.form.get('completetime')
        remarks = request.form.get('remarks')
        todo = Todo(project,version,worktype,module,priority,title,description,developer,tester,status,createUser,createtime,plantime,completetime,remarks,updateTime=None,updateUser=None)
        db.session.add(todo)
        db.session.commit()
        flash('New todo was successfully posted')
        return redirect(url_for('todo'))
    except IOError:
        print IOError


@app.route('/edit_todo',methods=['GET','POST'])
def edit_todo():
    if current_user.is_anonymous:
        return "nouser"
    if 3 not in current_user.permissions:
        return 'notallowed'
    try:
        # data = request.values
        id = request.form.get("pk","null")
        field=request.form.get("name","null")

        oldValue = request.form.get("oldValue","null")
        value=request.form.get("value",'null')
        todo = Todo.query.get(id)
        if(field=='status'):
            todo.status=value
            if value=='Closed':
                if 10 not in current_user.permissions:
                    return 'notallowed'
            if value=='Completed':
                if 9 not in current_user.permissions:
                    return 'notallowed'
        elif(field=='developer'):
            oldValue = str(map(int, request.form.getlist('oldValue[]')))
            developer = map(int, request.form.getlist('value[]'))
            value = str(developer)
            todo.developer=value
        elif(field=='tester'):
            oldValue = str(map(int, request.form.getlist('oldValue[]')))
            tester=map(int,request.form.getlist('value[]'))
            value=str(tester)
            todo.tester=value
        elif(field=='remarks'):
            todo.remarks=value
        elif (field == 'description'):
            todo.description=value
        elif(field=='title'):
            todo.title=value
        elif(field=='module'):
            todo.module=value
        elif (field == 'priority'):
            todo.priority = value
        elif(field=='worktype'):
            todo.worktype=value
        elif(field=='plantime'):
            todo.plantime = value
        elif(field=='completetime'):
            todo.completetime=value
        todo.updateUser = current_user.username
        todo.updateTime = datetime.now()
        todo.save()
        audit = Audit(id, field, oldValue, value, current_user.username, datetime.now(), 'edit')
        audit.save()
        return value
    except IOError:
        return 'error'


@app.route('/delete_todo',methods=['GET','POST'])
def delete_todo():
    tet = current_user
    user = User.query.get(current_user.id)
    if 4 not in user.permissions():
        return '4'
    else:
        try:
            ids=map(int,request.form.getlist('ids[]'))
            # ides = request.form.getlist('ids[]')

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


@app.route('/login',methods=['GET','POST'])
def login():

    if request.method=='POST':
        form = LoginForm()
        if not form.validate_on_submit():
            user = User.query.filter_by(loginname = form.loginname.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for('todo'))
            else:
                flash('Loginname or Password is invalid','danger')
        else:
            flash('Loggin Failed','danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    # session.pop('login_in',None)
    logout_user()
    flash('You were logged out',"info")
    return redirect(url_for('todo'))





































