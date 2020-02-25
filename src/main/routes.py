# Main Routes.py
# File is responsible for handling the requests to the url and loading the correct page
#
#
#
#
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import login_user, current_user, logout_user, login_required
from src import db, bcrypt
from src.models import Post, User
from src.posts.forms import PostForm
from src.users.forms import LoginForm
from datetime import datetime
# querying
import sqlite3
from sqlite3 import Error



#Creating a blueprint instance
main = Blueprint('main', __name__)





@main.route('/', methods=["GET","POST"])
def landing_page():
    # the first page a user will see if they are not logged in already
    # The html will display a cover page for first time visitors with an option to sign in or register
    # Creates a login form in case user logs into page, or has links to register

    #If user is logged in -> redirect them to their content page
    if (current_user.is_authenticated):
        return redirect(url_for('main.home'))

    # User is not signed in -> login post logic
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if user exists and password is valid with database:
            #logs in user and gives remember option form
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')#grabs page user was previously on
            return redirect(next_page) if next_page else redirect(url_for('main.home')) #returns user to original page if not put them to the home page
            
        else:#if login was not sucsessful: send flash message
            flash('Login unsucsessful. Check username and password', 'danger')
            return redirect("login.html", title='Login', form=form)


    return render_template('landing_page.html', form=form)
    
    






@main.route('/home')
@login_required
def home():
    # If user is not logged in, send them to the login page
    # else show the home content
    #

    if not (current_user.is_authenticated):
        return redirect(url_for('user.login'))

    page = request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)##posts per page:
    return render_template('home.html',posts=posts)


@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')