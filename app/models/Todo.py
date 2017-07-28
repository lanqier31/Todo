from app import db
import sys

#
# reload(sys)
# sys.setdefaultencoding("utf-8")



class Todo(db.Model):
    __tablename__ = 'todolist'
    id=db.Column(db.Integer,primary_key=True)
    project = db.Column(db.String(36))
    version = db.Column(db.String(10))
    worktype = db.Column(db.String(10))
    module = db.Column(db.String(10))
    title =  db.Column(db.String(100))
    description = db.Column(db.String(500))
    developer = db.Column(db.String(36))
    tester = db.Column(db.String(36))
    status = db.Column(db.String(10))
    createtime = db.Column(db.String(16))
    completetime = db.Column(db.String(16))
    remarks = db.Column(db.String(100))

    def __init__(self,project,version,worktype,module,title,description,developer,tester,status,createtime,completetime,remarks):
        self.project = project
        self.version = version
        self.worktype = worktype
        self.module = module
        self.title = title
        self.description = description
        self.developer = developer
        self.tester = tester
        self.status = status
        self.createtime = createtime
        self.completetime = completetime
        self.remarks = remarks

    def __repr__(self):
        return '<Todo %r>' % self.title

    def to_dict(self):
        return {
            "id": self.id,
            "project": self.project,
            "version": self.version,
            "worktype": self.worktype,
            "module": self.module,
            "title": self.title,
            "description": self.description,
            "developer": self.developer,
            "tester": self.tester,
            "status":self.status,
            "createtime": self.createtime,
            "completetime":self.completetime,
            "remarks": self.remarks,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def query_row_id(self, rid):
        obj = self.filter_by(id=rid).first()
        return obj