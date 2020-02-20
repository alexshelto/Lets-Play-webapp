# posts Routes.py
# File is responsible for handling the requests to the url and loading the correct page
# Dealing with urls that have to do with creating/accessing posts
#
#
#



from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

from src import db
from src.models import Post
from src.posts.forms import PostForm
# querying
import sqlite3
from sqlite3 import Error



#Creating a blueprint instance
posts = Blueprint('posts', __name__)



@posts.route("/post/new", methods=['GET','POST'])
@login_required #user must be loged in to post
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend="New Post")



@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
