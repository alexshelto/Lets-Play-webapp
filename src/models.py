# Models.py
# File holds the table models for the databases used in this webapp
# The classes are the databases
# USER and POST tables



#TODO: Post model, game id. it will be chosen from select list not inputted
#TODO: __repr__ functions for both models need to be tailored to sites idea once at that stage
#If name is optional. remove nullable from User class for 'first_name' and 'last_name'




from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from src import db, login_manager
from flask_login import UserMixin

#manages login sessions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



#User database model:
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)                                #Each user is given a unique id number
    first_name = db.Column(db.String(30),  nullable=False)                
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)            #Each user will be able to create a unique username of length 20
    email = db.Column(db.String(120), unique=True, nullable=False)              #Every user will need to register with an email address (maybe?)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')#Each user has a profile pic. uploaded or default
    password = db.Column(db.String(64), nullable=False)                         #Users will have a password of up to size 64 chars
    posts = db.relationship('Post', backref='author', lazy=True)                #Posts from users will be associated with them? (maybe?)

    #User class methods:
    ############################################################################
    #Reset token class method
    @staticmethod #not taking selt in methodS
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    #how User is represented
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    ############################################################################

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(100),nullable=False ) #Change to entered from menu on form
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #How Post is displayed
    def __repr__(self):
        return f"Post('{self.game}', '{self.date_posted}')"