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


