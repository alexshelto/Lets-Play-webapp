# Main Routes.py
# File is responsible for handling the requests to the url and loading the correct page
#
#
#
#
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from src import db
from src.models import Post
from src.posts.forms import PostForm
from datetime import datetime
# querying
import sqlite3
from sqlite3 import Error



#Creating a blueprint instance
main = Blueprint('main', __name__)



@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)##posts per page:
    return render_template('home.html',posts=posts)
    # return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')