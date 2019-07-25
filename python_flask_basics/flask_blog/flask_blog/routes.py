from flask import escape, request, render_template, url_for, flash, redirect

from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm, UserUpdateForm, PostCreationForm, PostChangeForm
from flask_blog.models import User, Post

from flask_login import login_user, logout_user, current_user, login_required

""" For profile pictures """
from PIL import Image ## resizing images

from datetime import datetime
import secrets
import os

"""date formatter"""
@app.template_filter('date_f')
def formatted_date(date):
    return date.strftime('%B, %d.%m.%Y - %H:%M')


@app.route('/')
@app.route('/home')
@app.route('/Home')
def posts_list():
    posts = Post.query.all()
    posts = sorted( posts, key = lambda p: p.date_changed, reverse= True )
    return render_template('home.html',posts=posts,dformat=formatted_date)

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
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))

    form = LoginForm()
    if form.validate_on_submit():
        """Just for testing the logon mechanism for now"""
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('posts_list'))
        flash(f'Wrong login data','danger')
    return render_template('login.html',title="Login", form=form)



""" account registering """
@app.route( '/register', methods=['GET','POST'] )
def register():
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
        
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html',title="Register",form=form)

""" User only areas """

""" User logout """
@app.route('/logout')
@login_required # this HAS TO COME AFTER the app.route decorator to work
def logout():
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

        # """create a hashed password"""
        # if not bcrypt.check_password_hash(current_user.password, form.password.data):
        #     hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #     current_user.password = hashed_pw

        db.session.commit()

        flash(f'User account successfully updated','success')

        return redirect(url_for('account'))

    return render_template('account_update.html',title="Account Update",form=form)

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

    return redirect(url_for('posts_list'))