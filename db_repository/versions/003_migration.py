from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
articles = Table('articles', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=50)),
    Column('body', VARCHAR),
    Column('author', VARCHAR(length=10)),
    Column('createtime', VARCHAR),
    Column('category_id', INTEGER),
)

articles = Table('articles', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=50)),
    Column('body', String),
    Column('author', String(length=10)),
    Column('createtime', String),
    Column('category', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['articles'].columns['category_id'].drop()
    post_meta.tables['articles'].columns['category'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['articles'].columns['category_id'].create()
    post_meta.tables['articles'].columns['category'].drop()
