from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
TestSuite = Table('TestSuite', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('projectname', String(length=30)),
    Column('testsuitename', String(length=80)),
    Column('subsuite', String(length=80)),
    Column('totalcase', INTEGER),
    Column('passedcase', INTEGER),
    Column('failedcase', INTEGER),
    Column('duration', String(length=50)),
)

articles = Table('articles', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=50)),
    Column('body', String),
    Column('author', String(length=10)),
    Column('createtime', String),
    Column('category', String),
)

page_detail = Table('page_detail', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('project', String(length=36)),
    Column('version', String(length=10)),
    Column('page_name', String(length=50)),
    Column('resource_name', String(length=100)),
    Column('resource_type', String(length=10)),
    Column('resource_size', INTEGER),
    Column('resource_duration', INTEGER),
    Column('create_time', String(length=16)),
)

role = Table('role', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('description', String(length=255)),
)

roles_users = Table('roles_users', post_meta,
    Column('user_id', Integer),
    Column('role_id', Integer),
)

web_load = Table('web_load', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('project', String(length=36)),
    Column('version', String(length=10)),
    Column('page_name', String(length=50)),
    Column('url', String(length=100)),
    Column('dns', INTEGER),
    Column('request', INTEGER),
    Column('dom_parser', INTEGER),
    Column('dom_ready', INTEGER),
    Column('load_event', INTEGER),
    Column('whitewait', INTEGER),
    Column('loadall', INTEGER),
    Column('create_time', String(length=16)),
)

category = Table('category', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=20)),
    Column('content', VARCHAR(length=400)),
)

category = Table('category', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
)

todolist = Table('todolist', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('project', String(length=36)),
    Column('version', String(length=10)),
    Column('worktype', String(length=10)),
    Column('module', String(length=10)),
    Column('priority', String(length=6)),
    Column('title', String(length=100)),
    Column('description', String(length=500)),
    Column('developer', String(length=36)),
    Column('tester', String(length=36)),
    Column('status', String(length=10)),
    Column('createtime', String(length=16)),
    Column('plantime', String(length=16)),
    Column('completetime', String(length=16)),
    Column('remarks', String(length=100)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=10)),
    Column('password', String(length=16)),
    Column('active', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['TestSuite'].create()
    post_meta.tables['articles'].create()
    post_meta.tables['page_detail'].create()
    post_meta.tables['role'].create()
    post_meta.tables['roles_users'].create()
    post_meta.tables['web_load'].create()
    pre_meta.tables['category'].columns['content'].drop()
    pre_meta.tables['category'].columns['title'].drop()
    post_meta.tables['category'].columns['name'].create()
    post_meta.tables['todolist'].columns['priority'].create()
    post_meta.tables['user'].columns['active'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['TestSuite'].drop()
    post_meta.tables['articles'].drop()
    post_meta.tables['page_detail'].drop()
    post_meta.tables['role'].drop()
    post_meta.tables['roles_users'].drop()
    post_meta.tables['web_load'].drop()
    pre_meta.tables['category'].columns['content'].create()
    pre_meta.tables['category'].columns['title'].create()
    post_meta.tables['category'].columns['name'].drop()
    post_meta.tables['todolist'].columns['priority'].drop()
    post_meta.tables['user'].columns['active'].drop()
