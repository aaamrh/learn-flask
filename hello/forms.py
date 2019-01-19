from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_ckeditor import CKEditorField


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message='必填')])
    pwd = PasswordField("Password", validators=[DataRequired(message='必填'),Length(8)])
    rembPwd = BooleanField('Remember me')
    submit = SubmitField('Login')

class UploadForm(FlaskForm):
    photo = FileField('上传图片', validators=[FileRequired()])
    submit = SubmitField()

class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('body', validators=[DataRequired()])
    submit = SubmitField('publish')