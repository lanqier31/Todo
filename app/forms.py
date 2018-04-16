from flask_wtf  import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length


class LoginForm(Form):
    username = StringField('username',validators=[DataRequired(),Length(1, 32)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')



