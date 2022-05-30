from email.mime import image
from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField,  TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), Length(min=2, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')
