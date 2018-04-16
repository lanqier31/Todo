from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
subtodos = Table('subtodos', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('patientid', Integer),
    Column('subtitle', String(length=100)),
    Column('description', String(length=500)),
    Column('developer', String(length=36)),
    Column('tester', String(length=36)),
    Column('status', String(length=10)),
    Column('createtime', String(length=16)),
    Column('plantime', String(length=16)),
    Column('completetime', String(length=16)),
    Column('remarks', String(length=100)),
)

role = Table('role', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('description', String(length=255)),
    Column('permission', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['subtodos'].create()
    post_meta.tables['role'].columns['permission'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['subtodos'].drop()
    post_meta.tables['role'].columns['permission'].drop()
