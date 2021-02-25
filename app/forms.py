from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed



class PhotoForm(FlaskForm):
    imageFile = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Appropriate Images Only'])])