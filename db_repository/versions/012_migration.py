from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
perm_type = Table('perm_type', post_meta,
    Column('ID', String(length=36), primary_key=True, nullable=False),
    Column('TypeName', String(length=100)),
    Column('DESCRIPTION', String(length=200)),
)

permission = Table('permission', post_meta,
    Column('ID', Integer, primary_key=True, nullable=False),
    Column('PermName', String(length=100)),
    Column('URL', String(length=200)),
    Column('DESCRIPTION', String(length=200)),
    Column('SEQ', Integer),
    Column('TARGET', String(length=100)),
    Column('PermType_ID', String),
    Column('parent_ID', String),
)

roles_permissions = Table('roles_permissions', post_meta,
    Column('role_id', Integer),
    Column('permission_ID', Integer),
)

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
    Column('createUser', String(length=10)),
    Column('createtime', String(length=16)),
    Column('plantime', String(length=16)),
    Column('completetime', String(length=16)),
    Column('remarks', String(length=100)),
    Column('updateTime', String(length=16)),
    Column('updateUser', String(length=10)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('loginname', String(length=10)),
    Column('username', String(length=10)),
    Column('password', String(length=16)),
    Column('active', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['perm_type'].create()
    post_meta.tables['permission'].create()
    post_meta.tables['roles_permissions'].create()
    post_meta.tables['subtodos'].create()
    post_meta.tables['todolist'].columns['createUser'].create()
    post_meta.tables['todolist'].columns['updateTime'].create()
    post_meta.tables['todolist'].columns['updateUser'].create()
    post_meta.tables['user'].columns['loginname'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['perm_type'].drop()
    post_meta.tables['permission'].drop()
    post_meta.tables['roles_permissions'].drop()
    post_meta.tables['subtodos'].drop()
    post_meta.tables['todolist'].columns['createUser'].drop()
    post_meta.tables['todolist'].columns['updateTime'].drop()
    post_meta.tables['todolist'].columns['updateUser'].drop()
    post_meta.tables['user'].columns['loginname'].drop()
