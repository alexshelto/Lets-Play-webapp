#
#
#
#
#
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from src import db, bcrypt
from src.models import User
from src.users.forms import RegistrationForm, LoginForm
from src.users.utils import save_picture

#creatiing blueprint instance:
users = Blueprint('users', __name__)



@users.route('/register', methods=['GET', 'POST'])
def register():
    #If the current user is already signed in -> redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    #Create a registrationForm object.
    form = RegistrationForm()
    if form.validate_on_submit():#must hash password if user submission is approved:
        hased_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #decode in utf8 to turn into string
        #Creating a user instance from the models.py, with username email and hashed password.
        user = User(username=form.username.data, email=form.email.data,password=hased_password)
        #adding / commiting user into database
        db.session.add(user)
        db.session.commit()##adding user to database:
        flash('Account has been created! Procede to log in', 'success')
        return redirect(url_for('users.login'))#redirect user to home page
    return render_template('register.html', title='Register', form=form)




@users.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        #logging in a user with an email

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if user exists and password is valid with database:
            login_user(user,remember=form.remember.data)#logs in user and gives remember option form
            next_page = request.args.get('next')#grabs page user was previously on
            return redirect(next_page) if next_page else redirect(url_for('main.home')) #returns user to original page if not put them to the home page
            
        else:#if login was not sucsessful: send flash message
            flash('Login unsucsessful. Check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
