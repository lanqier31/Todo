from app import db

class Category(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    content = db.Column(db.String(400))

    def __init__(self,title,content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Category %r>' %(self.title)

