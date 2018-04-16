from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
permission = Table('permission', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('permissioname', String(length=36)),
    Column('url', String(length=200)),
    Column('description', String(length=200)),
)

roles_permissions = Table('roles_permissions', post_meta,
    Column('role_id', Integer),
    Column('permission_id', Integer),
)

role = Table('role', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=20)),
    Column('description', VARCHAR(length=255)),
    Column('permission', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['permission'].create()
    post_meta.tables['roles_permissions'].create()
    pre_meta.tables['role'].columns['permission'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['permission'].drop()
    post_meta.tables['roles_permissions'].drop()
    pre_meta.tables['role'].columns['permission'].create()
