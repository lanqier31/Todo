from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length


class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(1, 32)])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('Login')



