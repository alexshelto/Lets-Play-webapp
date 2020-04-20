# users/utils.py file
# file holds some functions dealing with users accounts
# saving user images and downscaling the size & sending reset emails for passwords
#



import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from src import mail


#logic to save a users picture:
def save_picture(form_picture):
    #randomize a name for an image so no conflicting file names:
    random_hex_name = secrets.token_hex(8) #8 bytes of randomized hex:
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex_name + f_ext #combining names for the picture file name
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn) #joining filename in apps root path directory with static profile pics folder for save location
    #image resizing using pillow module:
    output_size = (250,250)
    newImage = Image.open(form_picture)
    newImage.thumbnail(output_size)
    newImage.save(picture_path)
    #end resize logic
    return picture_fn


##sending a reset email: 
def send_reset_email(user):
    #grab token
    token = user.get_reset_token()
    msg = Message('Lets Play | Password Reset Request',sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True) }
\n\nIf you did not make this request then ignore this email and check your account for security measures
'''
    mail.send(msg)#sending the mail using the mail app instance from init.py
