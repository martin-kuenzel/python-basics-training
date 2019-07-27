from flask import Blueprint

users = Blueprint( 'users', __name__ )

import os

from flask import escape, request, render_template, url_for, flash, redirect

from flask import current_app

from flask_blog import db, bcrypt

from ..models import User, Post
from .utils import save_profile_pic, send_verification_mail #, Message, os
from .forms import RegistrationForm, LoginForm, UserUpdateForm, PasswordResetRequestForm, PasswordResetForm

from flask_login import login_user, logout_user, current_user, login_required

""" account login """
@users.route('/account_login', methods=['GET','POST'])
def account_login():

    if current_user.is_authenticated:
        return redirect(url_for('posts.posts_list'))

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.active and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('posts.posts_list'))

        flash(f'Wrong login data','danger')

    return render_template('accounts/account_login.html',title="Login", form=form)

""" password resetting email link route """
@users.route( '/password_reset_confirm/<string:token>', methods=['GET','POST'] )
def password_reset_confirm(token):  
    
    if current_user.is_authenticated:
        return redirect(url_for('posts.posts_list'))
  
    form = PasswordResetForm()    
    user = User.confirm_usr_verify_token( token )

    if user and form.validate_on_submit():
        
        """create a hashed password"""
        if not bcrypt.check_password_hash(user.password, form.password.data):
            hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_pw

        db.session.commit()

        flash('Your password has been reset','success')
        return redirect(url_for('users.account_login'))
        
    return render_template('accounts/password_reset_confirm.html', title="Password reset confirmation", form=form)

""" password resetting requested route """
@users.route( '/password_reset_request', methods=['GET','POST'] )
def password_reset_request():

    if current_user.is_authenticated:
        return redirect(url_for('posts.posts_list'))

    form = PasswordResetRequestForm()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.validate_on_submit():

            """Send reset mail"""
            send_verification_mail( topic = 'Password reset', email_template = 'accounts/password_reset_email.html', link_route = 'users.password_reset_confirm', user = user )
            flash(f'An email has been sent to your email address', 'info')

        return redirect(url_for('users.account_login'))
        
    return render_template('accounts/password_reset_request.html',title="Reset Password", form = form)

""" account registering """
@users.route( '/account_register', methods=['GET','POST'] )
def account_register():
    if current_user.is_authenticated:
        return redirect(url_for('posts.posts_list'))

    form = RegistrationForm()
    if form.validate_on_submit():
        
        """create a hashed password"""
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        """create a user with the given data"""
        user = User( username=form.username.data, email=form.email.data, password=hashed_pw )

        """ add profile pic for new user"""
        if form.profile_pic.data:
            profile_pic = save_profile_pic(form.profile_pic.data)
            user.image_file = profile_pic
        
        """create the user in the database"""
        db.session.add(user)
        db.session.commit()

        """ Send activation mail """
        send_verification_mail( topic = 'Account activation', email_template = 'accounts/account_activate_email.html', link_route = 'users.account_activate_confirm', user = user )  
        logout_user() ## for some reason the user is logged in after this

        flash(f'An email with an activation link has been sent to you!', 'info')

        return redirect(url_for('users.account_login'))

    return render_template('accounts/account_register.html',title="Register account",form=form)

""" account activation confirmation route """
@users.route( '/account_activate_confirm/<string:token>', methods=['GET','POST'] )
def account_activate_confirm(token):
    if current_user.is_authenticated:
        return redirect(url_for('posts.posts_list'))

    user = User.confirm_usr_verify_token( token )
    if user:
        user.active = True
        db.session.commit()

        flash('Your account has been activated','success')

    return redirect(url_for('users.account_login'))

""" User only areas """

""" User account logout """
@users.route('/account_logout')
@login_required # this HAS TO COME AFTER the users.route decorator to work
def account_logout():
    logout_user()
    return redirect(url_for('posts.posts_list'))

""" User account overview """
@users.route('/account')
@login_required # this HAS TO COME AFTER the users.route decorator to work
def account():
    profile_pic = url_for('static', filename = 'profile_pics/' + current_user.image_file )
    return render_template('accounts/account.html',title="Account", profile_pic = profile_pic)

""" User account update """
@users.route('/account_update', methods=['GET','POST'])
@login_required # this HAS TO COME AFTER the users.route decorator to work
def account_update():
    form = UserUpdateForm(obj=current_user)
    if form.validate_on_submit():
        
        if form.profile_pic.data:
            profile_pic = save_profile_pic(form.profile_pic.data)

            """ if current profile pic is not the default pic, then delete current profile pic from system """
            if current_user.image_file != 'default.png': 
                profile_pic_old = os.path.join(current_app.root_path,'static','profile_pics',current_user.image_file)
                if os.path.exists(profile_pic_old):
                    os.remove( profile_pic_old )

            current_user.image_file = profile_pic
        
        """update the user in the database"""
        current_user.email = form.email.data
        current_user.username = form.username.data

        db.session.commit()

        flash(f'User account successfully updated','success')

        return redirect(url_for('users.account'))

    return render_template('accounts/account_update.html',title="Account Update",form=form)

""" deletion of accounts """
@users.route('/account_delete', methods=['GET','POST'])
@login_required
def account_delete():

    if request.method == 'POST':
    
        if current_user.image_file != 'default.png': 
            profile_pic = os.path.join(current_app.root_path,'static','profile_pics',current_user.image_file)
            if os.path.exists(profile_pic):
                os.remove( profile_pic )

        db.session.delete(current_user)
        db.session.commit()

        flash(f'Your account has been deleted','success')
        return redirect(url_for('posts.posts_list'))

    return render_template('accounts/account_delete.html',title='Account deletion')
