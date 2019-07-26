from flask import escape, request, render_template, url_for, flash, redirect

from flask_blog import app, db, bcrypt, mail
from flask_blog.forms import RegistrationForm, LoginForm, UserUpdateForm, PasswordResetRequestForm, PasswordResetForm, PostCreationForm, PostChangeForm
from flask_blog.models import User, Post

from flask_login import login_user, logout_user, current_user, login_required

from sqlalchemy import desc

""" For profile pictures """
from PIL import Image ## resizing images

""" For Emails Password reset / Account activation"""
from flask_mail import Message

""" For pagination of posts """
from flask_paginate import Pagination

from datetime import datetime
import secrets
import os

""" date formatter """
@app.template_filter('date_f')
def formatted_date(date):
    return date.strftime('%B, %d.%m.%Y - %H:%M')

""" for pagination in posts listing """
def get_posts( offset=0, per_page=5, posts=list(range(5)) ):
    return posts[offset: offset + per_page]


@app.route('/')
@app.route('/home')
@app.route('/Home')
def posts_list():
    
    posts = db.session.query(Post).order_by(desc(Post.date_changed))

    """ FILTERING BY user_id """
    user_id = request.args.get( 'user_id', type=int, default=0 )
    user = User.query.get( user_id ) ## get parameter &user_id=<int>, defaults to 0 (NONE)
    
    if user:
        posts = posts.filter_by( author = user )
    if user_id and not user:
        flash("No user with such id exists", 'info')

    """ PAGINATION """
    per_page = 3 ## show <int> entries per page
    page = int( request.args.get('page', type=int, default=1) ) ## get parameter &page=<int>, defaults to 1 (first page)
    pagination = Pagination( page=page, per_page=per_page, total=posts.count(), record_name='posts', css_framework='bootstrap4') ## the pagination html objects
    
    posts = posts.paginate(page=page, per_page=per_page)
    return render_template('home.html', posts=posts.items, pagination=pagination, title="Posts" )

@app.route('/posts_detail/<int:post_id>')
def posts_detail(post_id):
    post = Post.query.get(post_id)

    if post is None: 
        flash(f'Post does not exist','info')
        return redirect(url_for('posts_list'))

    return render_template('posts_detail.html',post=post,dformat=formatted_date)

@app.route('/about')
def about():
    return render_template('about.html',title="About")

""" USER AUTH PAGES """

""" User profile picture uploading """
def save_profile_pic(form_picture):
    _, fileext = os.path.splitext(form_picture.filename) ## using _ for the filename because its not needed

    """ resize images to a unified size """
    output_size = (64,64)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    rand = secrets.token_hex(16)
    save_name = f'{rand}{fileext}'
    profile_pic_path = os.path.join( app.root_path, 'static/profile_pics', save_name)
    i.save(profile_pic_path)

    return save_name

""" account login """
@app.route('/account_login', methods=['GET','POST'])
def account_login():

    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))

    form = LoginForm()
    if form.validate_on_submit():

        """Just for testing the logon mechanism for now"""
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.active and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('posts_list'))

        flash(f'Wrong login data','danger')

    return render_template('account_login.html',title="Login", form=form)

""" password resetting email link route """
@app.route( '/password_reset_confirm/<string:token>', methods=['GET','POST'] )
def password_reset_confirm(token):  
    
    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))
  
    form = PasswordResetForm()    
    user = User.confirm_usr_verify_token( token )

    if user and form.validate_on_submit():
        
        """create a hashed password"""
        if not bcrypt.check_password_hash(user.password, form.password.data):
            hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_pw

        db.session.commit()

        flash('Your password has been reset','success')
        return redirect(url_for('account_login'))
        
    return render_template('password_reset_confirm.html', title="Password reset confirmation", form=form)

""" password resetting requested route """
@app.route( '/password_reset_request', methods=['GET','POST'] )
def password_reset_request():

    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))

    form = PasswordResetRequestForm()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.validate_on_submit():

            """Send reset mail"""
            email = Message('Password reset', sender=os.environ.get('EMAIL_ACCOUNT'), recipients = [user.email])
            reset_link = url_for( 'password_reset_confirm', user_id = user.id, token=user.create_usr_verify_token(), _external=True )
            email.html = render_template('password_reset_email.html', reset_link = reset_link, user = user)
            mail.send(email)

            flash(f'An email has been sent to your email address', 'info')

        return redirect(url_for('account_login'))
        
    return render_template('password_reset_request.html',title="Reset Password", form = form)

""" account registering """
@app.route( '/account_register', methods=['GET','POST'] )
def account_register():
    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))

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
        email = Message('Account activation', sender=os.environ.get('EMAIL_ACCOUNT'), recipients = [user.email])
        activation_link = url_for( 'account_activate_confirm', user_id = user.id, token=user.create_usr_verify_token(), _external=True )
        email.html = render_template('account_activate_email.html', activation_link = activation_link)
        mail.send(email)
        
        logout_user() ## for some reason the user is logged in after this

        flash(f'An email with an activation link has been sent to you!', 'info')

        return redirect(url_for('account_login'))

    return render_template('account_register.html',title="Register account",form=form)

""" account activation confirmation route """
@app.route( '/account_activate_confirm/<string:token>', methods=['GET','POST'] )
def account_activate_confirm(token):
    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))

    user = User.confirm_usr_verify_token( token )
    if user:
        user.active = True
        db.session.commit()

        flash('Your account has been activated','success')

    return redirect(url_for('account_login'))

""" User only areas """

""" User account logout """
@app.route('/account_logout')
@login_required # this HAS TO COME AFTER the app.route decorator to work
def account_logout():
    logout_user()
    return redirect(url_for('posts_list'))

""" User account overview """
@app.route('/account')
@login_required # this HAS TO COME AFTER the app.route decorator to work
def account():
    profile_pic = url_for('static', filename = 'profile_pics/' + current_user.image_file )
    return render_template('account.html',title="Account", profile_pic = profile_pic)

""" User account update """
@app.route('/account_update', methods=['GET','POST'])
@login_required # this HAS TO COME AFTER the app.route decorator to work
def account_update():
    form = UserUpdateForm(obj=current_user)
    if form.validate_on_submit():
        
        if form.profile_pic.data:
            profile_pic = save_profile_pic(form.profile_pic.data)

            """ if current profile pic is not the default pic, then delete current profile pic from system """
            if current_user.image_file != 'default.png': 
                profile_pic_old = os.path.join(app.root_path,'static','profile_pics',current_user.image_file)
                os.remove( profile_pic_old )

            current_user.image_file = profile_pic
        
        """update the user in the database"""
        current_user.email = form.email.data
        current_user.username = form.username.data

        db.session.commit()

        flash(f'User account successfully updated','success')

        return redirect(url_for('account'))

    return render_template('account_update.html',title="Account Update",form=form)

""" deletion of accounts """
@app.route('/account_delete', methods=['GET','POST'])
@login_required
def account_delete():

    if request.method == 'POST':
    
        if current_user.image_file != 'default.png': 
            profile_pic = os.path.join(app.root_path,'static','profile_pics',current_user.image_file)
            os.remove( profile_pic )

        db.session.delete(current_user)
        db.session.commit()

        flash(f'Your account has been deleted','success')
        return redirect(url_for('posts_list'))

    return render_template('account_delete.html',title='Account deletion')

""" creation of posts """
@app.route('/posts_create', methods=['GET','POST'])
@login_required
def posts_create():
    form = PostCreationForm()
    if form.validate_on_submit():
        post = Post(user_id=current_user.id, title=form.title.data,content=form.content.data)
        db.session.add(post)
        db.session.commit()

        flash(f'Post created','success')
        return redirect(url_for('posts_list'))

    return render_template('posts_create.html',title='Post creation',form=form)

""" changing of posts """
@app.route('/posts_change/<int:post_id>', methods=['GET','POST'])
@login_required
def posts_change(post_id):
    
    post = Post.query.get(post_id)

    if post and current_user == post.author:
        form = PostChangeForm(obj=post)

        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            post.date_changed = datetime.utcnow()

            db.session.commit()

            flash(f'Post changed','success')
            return redirect(url_for('posts_list'))

        return render_template('posts_change.html',title='Post update',form=form)

    return redirect(url_for('posts_list'))


""" deletion of posts """
@app.route('/posts_delete/<int:post_id>', methods=['GET','POST'])
@login_required
def posts_delete(post_id):
    
    post = Post.query.get(post_id)

    if post and current_user == post.author:
        if request.method == 'POST':
        
            db.session.delete(post)
            db.session.commit()

            flash(f'Post deleted','success')
            return redirect(url_for('posts_list'))

    return render_template('posts_delete.html',title='Post deletion',post=post)