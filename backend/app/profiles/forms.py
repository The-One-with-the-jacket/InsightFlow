from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class EditProfileForm(FlaskForm):
    bio = TextAreaField('Bio', validators=[Length(max=500)])
    avatar_url = StringField('Avatar URL', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Update Profile')
