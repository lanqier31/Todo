from app import db

class Category(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True)


    def __init__(self,name):
        self.name = name


    def __repr__(self):
        return '<Category %r>' %(self.name)


class Article(db.Model):
    __tablename__='articles'
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String)
    author = db.Column(db.String(10))
    createtime = db.Column(db.String())
    category = db.Column(db.String())

    def __repr__(self):
        return '<Article %r>' %(self.title)

    def __init__(self,category,title,body,author,createtime):
        self.category = category
        self.title = title
        self.body = body
        self.author = author
        self.createtime = createtime

