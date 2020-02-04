# users/forms.py
# file creates all the input form for user registration and account details
# allong with methods of validating and reseting user email/pictures/etc
#
#


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


pass
