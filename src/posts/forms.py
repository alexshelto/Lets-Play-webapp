# posts/forms.py
# file creates all the input form for making a post 
#


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired



Game_Choices = [('al', 'Apex Legends'),('bb', 'Baseball'),('bball', 'Basketball'),('bg', 'Board Games'),('cod', 'Call of Duty'), ('dd', 'Dungeons & Dragons'),('ft', 'Fortnite'), ('fb', 'Football'),('ha', 'Halo'),('mg', 'Misc. Games'), ('sb', 'Smash Brothers'),('vol', 'Volleyball')] 

class PostForm(FlaskForm):
    game = SelectField('Game',[DataRequired()], choices=Game_Choices)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
