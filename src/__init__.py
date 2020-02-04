# init.py file
# file gathers all of the templates and forms to create the flask application
# the function of this file is called in the exported flask app file: run.py
#

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from src.config import Config




db = SQLAlchemy() #initializing db
bcrypt = Bcrypt()#initialiaing hashing
login_manager = LoginManager()#login manager so users can log in
login_manager.login_view = 'users.login' ##passing in function name of route if user isnt logged in
login_manager.login_message_category = 'warning' #warning = yellow color


mail = Mail() #initialize






def create_app():
    #Configuring Flask application
    app = Flask(__name__)
    app.config.from_object(Config)

    #Initializing dependencies
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #Importing blueprint instances
    from src.main.routes import main
    from src.posts.routes import posts
    from src.users.routes import users
    from src.errors.handlers import errors #instance of errors blueprint. similar for the rest of the imports

    #registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app
