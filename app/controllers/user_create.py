from app import app,db
from app.models.Roles import Role,User
from flask_security import SQLAlchemyUserDatastore,Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
# db.create_all()


admin = user_datastore.create_user(username='weir', password='admin',active=True)
user_datastore.create_role(name='User', description='Generic user role')

admin_role = user_datastore.create_role(name='Admin', description='Admin user role')

user_datastore.add_role_to_user(admin, admin_role)
db.session.commit()