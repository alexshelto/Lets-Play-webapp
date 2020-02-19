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



