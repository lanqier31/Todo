from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('permissioname', VARCHAR(length=36)),
    Column('url', VARCHAR(length=200)),
)

permission = Table('permission', post_meta,
    Column('ID', String(length=36), primary_key=True, nullable=False),
    Column('PermName', String(length=100)),
    Column('URL', String(length=200)),
    Column('DESCRIPTION', String(length=200)),
    Column('SEQ', Integer),
    Column('TARGET', String(length=100)),
    Column('CREATEDATETIME', DateTime),
    Column('UPDATEDATETIME', DateTime),
    Column('PermType_ID', String),
    Column('parent_ID', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['permission'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['permission'].drop()
