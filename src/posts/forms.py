# posts/forms.py
# file creates all the input form for making a post 
#


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired




Game_Choices = [('bball', 'Basketball'), ('cod', 'Call of Duty'), ('dd', 'Dungeons & Dragons'), ('vol', 'Volleyball'), ('fb', 'Football'), ('ha', 'Halo'), ('ft', 'Fortnite'), ('al', 'Apex Legends'), ('sb', 'Smash Brothers'), ('bb', 'Baseball'), ('bg', 'Board Games'), ('mg', 'Misc. Games')]


class PostForm(FlaskForm):
    game = SelectField('Game',[DataRequired()], choices=Game_Choices)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

# class PostForm(FlaskForm):
#         title = StringField('Title', validators=[DataRequired()])
#         content = TextAreaField('Content', validators=[DataRequired()])
#         submit = SubmitField('Post')