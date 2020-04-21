# posts/forms.py
# file creates all the input form for making a post 
#


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired



Game_Choices = [('al', 'Apex Legends'),('arma', 'Arma 3'),('bb', 'Baseball'),('bball', 'Basketball'),('bil', 'Billiards'),('bg', 'Board Games'),('cod', 'Call of Duty'),('csgo', 'Counter-Strike: Global Offensive'),('dayz', 'DayZ'),('dd', 'Dungeons & Dragons'),('db', 'Dodgeball'),('ft', 'Fortnite'),('fb', 'Football'),('gmod', 'Garry\'s Mod'),('ha', 'Halo'),('hi', 'Hiking'),('kb', 'Kickball'),('lol', 'League of Legends'),('mg', 'Misc. Games'),('rust', 'Rust'),('sb', 'Smash Brothers'),('val', 'Valorant'),('vol', 'Volleyball'),('wow', 'World of Warcraft')] 

class PostForm(FlaskForm):
    game = SelectField('Game',[DataRequired()], choices=Game_Choices)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class AddCommentForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')
