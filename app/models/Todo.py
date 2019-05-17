# -*- coding: utf-8 -*-：
from app import db
from datetime import datetime
import sys


reload(sys)
sys.setdefaultencoding("utf-8")



class Todo(db.Model):
    __tablename__ = 'todolist'
    id=db.Column(db.Integer,primary_key=True)
    project = db.Column(db.String(36))
    version = db.Column(db.String(10))
    worktype = db.Column(db.String(10))
    module = db.Column(db.String(10))
    priority = db.Column(db.String(6))
    title =  db.Column(db.String(100))
    description = db.Column(db.String(500))
    developer = db.Column(db.String(36))
    tester = db.Column(db.String(36))
    status = db.Column(db.String(10))
    createUser = db.Column(db.String(10))
    createtime = db.Column(db.String(16))
    plantime = db.Column(db.String(16))
    completetime = db.Column(db.String(16))
    remarks = db.Column(db.String(100))
    updateTime = db.Column(db.String(16))
    updateUser = db.Column(db.String(10))

    def __init__(self,project,version,worktype,module,priority,title,description,developer,tester,status,
                 createUser,createtime,plantime,completetime,remarks,updateTime,updateUser):
        self.project = project
        self.version = version
        self.worktype = worktype
        self.module = module
        self.priority = priority
        self.title = title
        self.description = description
        self.developer = developer
        self.tester = tester
        self.status = status
        self.createUser = createUser
        self.createtime = createtime
        self.plantime=plantime
        self.completetime = completetime
        self.remarks = remarks
        self.updateTime = updateTime
        self.updateUser = updateUser

    def __repr__(self):
        return '<Todo %r>' % self.title

    def to_dict(self):
        return {
            "id": self.id,
            "project": self.project,
            "version": self.version,
            "worktype": self.worktype,
            "module": self.module,
            "priority":self.priority,
            "title": self.title,
            "description": self.description,
            "developer": self.developer,
            "tester": self.tester,
            "status":self.status,
            "createUser":self.createUser,
            "createtime": self.createtime,
            "plantime": self.plantime,
            "completetime": self.completetime,
            "remarks": self.remarks,
            "updateTime":self.updateTime,
            "updateUser":self.updateUser
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

class subTodo(db.Model):
    __tablename__ = 'subtodos'
    id = db.Column(db.Integer, primary_key=True)
    patientid = db.Column(db.Integer)
    subtitle = db.Column(db.String(100))
    description = db.Column(db.String(500))
    developer = db.Column(db.String(36))
    tester = db.Column(db.String(36))
    status = db.Column(db.String(10))
    createtime = db.Column(db.String(16))
    plantime = db.Column(db.String(16))
    completetime = db.Column(db.String(16))
    remarks = db.Column(db.String(100))

    def __init__(self,patientid,subtitle,description,developer,tester,status,createtime,plantime,completetime,remarks):

        self.patientid = patientid
        self.subtitle = subtitle
        self.description = description
        self.developer = developer
        self.tester = tester
        self.status = status
        self.createtime = createtime
        self.plantime=plantime
        self.completetime = completetime
        self.remarks = remarks

    def __repr__(self):
        return '<subTodo %r>' % self.subtitle

    def to_dict(self):
        return {
            "id": self.id,
            "patientid":self.patientid,
            "subtitle": self.subtitle,
            "description": self.description,
            "developer": self.developer,
            "tester": self.tester,
            "status":self.status,
            "createtime": self.createtime,
            "plantime": self.plantime,
            "completetime": self.completetime,
            "remarks": self.remarks
        }