from app import db


class Audit(db.Model):
    __tablename__ = 'audit'
    ID = db.Column(db.Integer,primary_key=True)
    editId = db.Column(db.String(36))
    editField = db.Column(db.String(36))
    oldValue = db.Column(db.String(500))
    newValue = db.Column(db.String(500))
    editUser = db.Column(db.String(50))
    editTime = db.Column(db.DATETIME)
    auditType = db.Column(db.String(10))

    def __init__(self, editId, editField,oldValue,newValue,editUser,editTime,auditType):
        self.editId = editId
        self.editField = editField
        self.oldValue = oldValue
        self.newValue = newValue
        self.editUser = editUser
        self.editTime = editTime
        self.auditType = auditType

    def to_json(self):
        return {
            'editId': self.editId,
            'editField': self.editField,
            'oldValue': self.oldValue,
            'newValue': self.newValue,
            'editUser': self.editUser,
            'editTime': self.editTime,
            'auditType': self.auditType,
        }

    def __repr__(self):
        return '<Audit %r>\n' % self.editId

    def save(self):
        db.session.add(self)
        db.session.commit()