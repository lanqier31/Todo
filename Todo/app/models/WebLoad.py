from app import db


class WebLoad(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    project = db.Column(db.String(36))
    version = db.Column(db.String(10))
    page_name = db.Column(db.String(50))
    url = db.Column(db.String(100))
    dns = db.Column(db.INTEGER)
    request = db.Column(db.INTEGER)
    dom_parser = db.Column(db.INTEGER)
    dom_ready = db.Column(db.INTEGER)
    load_event = db.Column(db.INTEGER)
    whitewait = db.Column(db.INTEGER)
    loadall = db.Column(db.INTEGER)
    create_time = db.Column(db.String(16))


    def __init__(self,project,version,page_name,url,dns,request,dom_parser,dom_ready,load_event,whitewait,loadall,create_time):

        self.project = project
        self.version = version
        self.page_name = page_name
        self.url = url
        self.dns = dns
        self.request = request
        self.dom_parser = dom_parser
        self.dom_ready = dom_ready
        self.load_event = load_event
        self.whitewait = whitewait
        self.loadall = loadall
        self.create_time = create_time

    def __repr__(self):
        return '<WebLoad %r>' % (self.project)

    def to_dict(self):
        return {
            "id": self.id,
            "project": self.project,
            "version": self.version,
            "page_name": self.page_name,
            "url": self.url,
            "dns": self.dns,
            "request": self.request,
            "dom_parser": self.dom_parser,
            "dom_ready": self.dom_ready,
            "load_event":self.load_event,
            "whitewait": self.whitewait,
            "loadall": self.loadall,
            "create_time": self.create_time,
        }