
import os

from flask import render_template, url_for
from flask import current_app

from flask_blog import mail

""" For Emails Password reset / Account activation"""
import secrets
from flask_mail import Message

""" For profile pictures """
from PIL import Image ## preprocessing images

""" User profile picture uploading """
def save_profile_pic(form_picture):
    _, fileext = os.path.splitext(form_picture.filename) ## using _ for the filename because its not needed anywhere

    """ resize images to a unified size """
    output_size = (120,120)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    rand = secrets.token_hex(16)
    save_name = f'{rand}{fileext}'
    profile_pic_path = os.path.join( current_app.root_path, 'static/profile_pics', save_name)
    i.save(profile_pic_path)

    return save_name

""" send emails with verification token links for variable topics """
def send_verification_mail( topic, email_template, link_route, user = None ):
    if not user is None:
        try:
            email = Message( topic, sender=os.environ.get('EMAIL_ACCOUNT'), recipients = [user.email])
            link_route = url_for( link_route, user_id = user.id, token=user.create_usr_verify_token(), _external=True )
            print(link_route)

            email.html = render_template(email_template, link_route = link_route, user = user)
            mail.send(email)
        except Exception as E:
            raise E 
    return True

        
