from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    pwd = PasswordField("Password", validators=[DataRequired(),Length(8)])
    rembPwd = BooleanField('Remember me')
    submit = SubmitField('Login')
    