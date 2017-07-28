from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
todolist = Table('todolist', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('project', String(length=36)),
    Column('version', String(length=10)),
    Column('worktype', String(length=10)),
    Column('module', String(length=10)),
    Column('title', String(length=100)),
    Column('description', String(length=500)),
    Column('developer', String(length=36)),
    Column('tester', String(length=36)),
    Column('status', String(length=10)),
    Column('createtime', DateTime),
    Column('completetime', DateTime),
    Column('remarks', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['todolist'].columns['module'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['todolist'].columns['module'].drop()
