#
#
#
#
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from src import db, bcrypt
from src.models import User, Post
from src.users.forms import RegistrationForm, LoginForm
from src.users.utils import save_picture

#creatiing blueprint instance:
users = Blueprint('users', __name__)



@users.route('/register', methods=['GET', 'POST'])
def register():
    #if user is authenticated bring them to sign in:
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    #else creating a registration form object to gather the 'User' model data:
    form = RegistrationForm()
    
    #Checking for user validation. validate_on_submit is a function from wtf_forms & flask
    if form.validate_on_submit():
        #first hash the users password using bcrypt module
        #then load the neccesary form entries into the db model for user
        #Use syntax: form.name.data to pull the var 'name's data
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        #Creating User db object
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw, zipcode=form.zipcode.data)

        #Adding & commiting new change(addition) to the database named 'db'
        db.session.add(user)
        db.session.commit()

        flash('Account has been created! Procede to log in', 'success')

    #If form validated and user made -> send to login. Else -> render register page again
        return redirect(url_for('users.login')) 
    return render_template('register.html', title='Register', form=form)



@users.route('/login',methods=['GET', 'POST'])
def login():
    #If current user is authenticated. route them to the home page
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    #Else: Create a login form to acquire login information

    #Creating login form
    form = LoginForm()

    #Checking if user validated and sent the form
    if form.validate_on_submit():

        #logging in a user with an email
        #1.) Query the User Table of the database. search by username. will check if the account has the same password
        #2.) decrypt the password

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if user exists and password is valid with database:
            #logs in user and gives remember option form
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')#grabs page user was previously on
            return redirect(next_page) if next_page else redirect(url_for('main.home')) #returns user to original page if not put them to the home page
            
        else:#if login was not sucsessful: send flash message
            flash('Login unsucsessful. Check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))





#TODO: make posts query from newest to oldest instead of oldest to newest 
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    page = request.args.get('page',1, type=int)
    posts = Post.query.filter_by(user_id=current_user.id).paginate(page=page,per_page=5)##posts per page:
    return render_template("account.html", posts=posts)






##user post page route
## This is where we can create a profile page
@users.route("/user/<string:username>")
def user_page(username):
    page = request.args.get('page',1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page,per_page=10)##posts per page:
    return render_template('user_page.html',posts=posts, user=user)