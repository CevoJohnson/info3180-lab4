from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed



class PhotoForm(FlaskForm):
    imageFile = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'Appropriate Images Only'])])