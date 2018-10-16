from app import db

class Category(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True)
    level = db.Column(db.Integer)
    parent_ID = db.Column(db.String, db.ForeignKey('category.id'))

    def __init__(self,name,level):
        self.name = name
        self.level = level


    def __repr__(self):
        return '<Category %r>' %(self.name)


class Article(db.Model):
    __tablename__='articles'
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String)
    author = db.Column(db.String(10))
    createtime = db.Column(db.String())
    level = db.Column(db.Integer)
    parent_title = db.Column(db.String, db.ForeignKey('articles.title'))
    # parent = db.relationship('Article', remote_side=[id], backref='article', uselist=False)

    def __repr__(self):
        return '<Article %r>' %(self.title)

    def __init__(self,title,body,author, createtime, level,parent_title):
        self.title = title
        self.body = body
        self.author = author
        self.createtime = createtime
        self.level = level
        self.parent_title = parent_title

    def get_child(self, ptitle):
        children = Article.query.filter_by(parent_title=ptitle).all()
        childs=[]
        cd={}
        for p in children:
            cd['cname']= p.tiitle
            cd['cid'] = p.id
            childs.append(cd)
            cd={}
        return childs