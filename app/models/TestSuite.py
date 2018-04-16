from app import db


class TestSuite(db.Model):
    __tablename__ = 'TestSuite'
    id=db.Column(db.Integer,primary_key=True)
    projectname = db.Column(db.String(30))
    testsuitename = db.Column(db.String(80))
    subsuite = db.Column(db.String(80))
    totalcase = db.Column(db.INTEGER)
    passedcase = db.Column(db.INTEGER)
    failedcase = db.Column(db.INTEGER)
    duration = db.Column(db.String(50))

    def __init__(self,projectname,testsuitename,subsuite,totalcase,passedcase,failedcase,duration):
        self.projectname = projectname
        self.testsuitename = testsuitename
        self.subsuite = subsuite
        self.totalcase = totalcase
        self.passedcase = passedcase
        self.failedcase = failedcase
        self.duration = duration

    def __repr__(self):
        return '<TestSuite %r>' %(self.testsuitename)