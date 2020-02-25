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
from src.posts.forms import PostForm, Game_Choices #importing the post form and the available game choices 
# querying
import sqlite3
from sqlite3 import Error


#Creating a blueprint instance
posts = Blueprint('posts', __name__)



@posts.route("/post/new", methods=['GET','POST'])
@login_required #user must be loged in to post
def new_post():
    #Creating list of available games to make a post for:
    form = PostForm()
    


    if request.method == 'POST' and form.validate():
        # 
        # Retrieves the value for game selected creates a new post form
        # Add and commit new post form to database

        game = dict(form.game.choices).get(form.game.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user, game=game)
        #Commit the post to the post db
        db.session.add(post)
        db.session.commit()
        
        flash('Your post has been created', 'success')
        return redirect(url_for('main.home'))

    return render_template('create_post.html', title='New Post', form=form, legend="New Post", games=Game_Choices) #removed games=game_display








@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
