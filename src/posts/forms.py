# posts/forms.py
# file creates all the input form for making a post 
#


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

# class PostForm(FlaskForm):
#         title = StringField('Title', validators=[DataRequired()])
#         content = TextAreaField('Content', validators=[DataRequired()])
#         submit = SubmitField('Post')