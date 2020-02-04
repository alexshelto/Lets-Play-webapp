# posts Routes.py
# File is responsible for handling the requests to the url and loading the correct page
# Dealing with urls that have to do with creating/accessing posts
#
#
#



from flask import render_template, request, Blueprint, flash, redirect, url_for
from datetime import datetime
# querying
import sqlite3
from sqlite3 import Error



#Creating a blueprint instance
posts = Blueprint('posts', __name__)

@posts.route('/posts/new')
def new_post():
    return render_template('create_post.html')
