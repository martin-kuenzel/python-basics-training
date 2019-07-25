from flask import escape, request, render_template, url_for, flash, redirect

from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm, UserUpdateForm, PostCreationForm, PostChangeForm
from flask_blog.models import User, Post

from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
@app.route('/Home')
def posts_list():
    posts = Post.query.all()
    return render_template('home.html',posts=reversed(posts))

@app.route('/posts_detail/<int:id>')
def posts_detail(id):
    post_id = id
    post = Post.query.filter_by(id=post_id).first()

    if post is None: 
        flash(f'Post does not exist','info')
        return redirect(url_for('posts_list'))

    return render_template('posts_detail.html',post=post)

@app.route('/about')
def about():
    return render_template('about.html',title="About")



""" USER AUTH PAGES """

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
        
        """create the user in the database"""
        db.session.add(user)
        db.session.commit()
        
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html',title="Register",form=form)

""" account login """
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts_list'))
    form = LoginForm()
    if form.validate_on_submit():
        """Just for testing the logon mechanism for now"""
        user = User.query.filter_by(email=form.email.data).first()
        if not user is None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('posts_list'))
        flash(f'Wrong login data','danger')
    return render_template('login.html',title="Login", form=form)


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
    return render_template('account.html',title="Account")

""" User account update """
@app.route('/account_update', methods=['GET','POST'])
@login_required # this HAS TO COME AFTER the app.route decorator to work
def account_update():
    form = UserUpdateForm(obj=current_user)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = current_user

            """create a hashed password"""
            hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            
            """update the user in the database"""
            user.email = form.email.data
            user.username = form.username.data
            user.password = hashed_pw

            db.session.commit()

            flash(f'User account successfully updated','success')

            return redirect(url_for('posts_list'))

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
@app.route('/posts_change/<int:id>', methods=['GET','POST'])
@login_required
def posts_change(id):
    
    post = Post.query.filter_by(id=id).first()
    if post and current_user.id is post.user_id:
        form = PostChangeForm(obj=post)

        if request.method == 'POST':
            if form.validate_on_submit():
                post.title = form.title.data
                post.content = form.content.data

                db.session.commit()

                flash(f'Post changed','success')
                return redirect(url_for('posts_list'))

        return render_template('posts_change.html',title='Post update',form=form)

    # flash(f'Post does not exist','info')
    return redirect(url_for('posts_list'))


""" deletion of posts """
@app.route('/posts_delete/<int:id>', methods=['GET','POST'])
@login_required
def posts_delete(id):
    
    post = Post.query.filter_by(id=id).first()
    if post and current_user.id is post.user_id:

        if request.method == 'POST':
            
            db.session.delete(post)
            db.session.commit()

            flash(f'Post deleted','success')
            return redirect(url_for('posts_list'))

        return render_template('posts_delete.html',title='Post deletion',post=post)

    #flash(f'Post does not exist','info')
    return redirect(url_for('posts_list'))