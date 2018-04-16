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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['TestSuite'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['TestSuite'].drop()
