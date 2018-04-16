from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
articles = Table('articles', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=50)),
    Column('body', String),
    Column('author', String(length=10)),
    Column('createtime', String),
    Column('category_id', Integer),
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['articles'].create()
    pre_meta.tables['category'].columns['content'].drop()
    pre_meta.tables['category'].columns['title'].drop()
    post_meta.tables['category'].columns['name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['articles'].drop()
    pre_meta.tables['category'].columns['content'].create()
    pre_meta.tables['category'].columns['title'].create()
    post_meta.tables['category'].columns['name'].drop()
