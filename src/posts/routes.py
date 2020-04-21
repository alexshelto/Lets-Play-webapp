# posts Routes.py
# File is responsible for handling the requests to the url and loading the correct page
# Dealing with urls that have to do with creating/accessing posts
#




from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from src import db
from src.models import Post, Comment
from src.posts.forms import PostForm, Game_Choices #importing the post form and the available game choices
from src.posts.forms import AddCommentForm #importing the comment form 
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



@posts.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def comment_post(post_id):
    #post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    if form.validate_on_submit():
        #db.create_all()
        comment = Comment(body=form.body.data, article=post)
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added to the post", "success")
        return redirect(url_for("post", post_id=post.id))
    return render_template('post.html', title="Comment", form=form)



@posts.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def comment(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title="Comment", comment=comment)



# Route allows users to delete a post that they created
#
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required #need to be logged in to update a post
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
       abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required #need to be logged in to update a post
def delete_comment(post_id):
    post = Post.query.get_or_404(post_id)
    if comment.author != current_user:
       abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return redirect(url_for('main.home'))
    