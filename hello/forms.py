from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message='必填')])
    pwd = PasswordField("Password", validators=[DataRequired(message='必填'),Length(8)])
    rembPwd = BooleanField('Remember me')
    submit = SubmitField('Login')

class UploadForm(FlaskForm):
    photo = FileField('上传图片', validators=[FileRequired(), FileAllowed(['jpg','png'], message='只能上传jpg,png格式的')])
    