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
from src.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
            validators=[DataRequired(), Length(min = 4, max=18)])##sets validators for username length
    email = StringField('Email',
            validators=[DataRequired(),Email()])

    zipcode = StringField('Zipcode',
            validators=[DataRequired(), Length(min=5, max=5)]) #Sets all zipcodes to be of length 5 only

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
             validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')
    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user: #if user found with same email throw error
                    raise ValidationError('Email has already been taken, please choose a different one')


    def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user: #if user found, throw an error:
                raise ValidationError('Username has already been taken, please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    ##secure cookie
