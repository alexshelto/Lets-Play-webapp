# Main Routes.py
# File is responsible for handling the requests to the url and loading the correct page
#
#
#
#



from flask import render_template, request, Blueprint, flash, redirect, url_for
from datetime import datetime
# querying
import sqlite3
from sqlite3 import Error



#Creating a blueprint instance
main = Blueprint('main', __name__)




@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')
