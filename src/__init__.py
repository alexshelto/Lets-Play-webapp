

import os
from flask import Flask
from src.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Configuring FlaskApp from config.py file. allows multiple instances

    #Importing blueprint instances
    return app