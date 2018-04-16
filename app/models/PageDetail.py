from app import db


class PageDetail(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    project = db.Column(db.String(36))
    version = db.Column(db.String(10))
    page_name = db.Column(db.String(50))
    resource_name = db.Column(db.String(100))
    resource_type = db.Column(db.String(10))
    resource_size = db.Column(db.INTEGER)
    resource_duration = db.Column(db.INTEGER)
    create_time = db.Column(db.String(16))

    def __init__(self,project,version,page_name,resource_name,resource_type,resource_size,resource_duration,create_time):
        self.project = project
        self.version = version
        self.page_name = page_name
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.resource_size = resource_size
        self.resource_duration = resource_duration
        self.create_time = create_time

    def __repr__(self):
        return '<PageDetail %r>' % self. page_name


