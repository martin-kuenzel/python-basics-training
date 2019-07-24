from flask import escape, request, render_template, url_for, flash, redirect

from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        "author": "Mike Miller",
        "title" : "First Post",
        "content": "Post Content",
        "date_created": "10/10/1924"
    },
    {
        "author": "Mike Miller",
        "title" : "Second Post",
        "content": "Post Content",
        "date_created": "15/10/1954"
    }
]

@app.route('/')
@app.route('/home')
@app.route('/Home')
def posts_list():
    posts = Post.query.all()
    return render_template('home.html',posts=posts)

@app.route('/posts_detail')
def posts_detail():
    post_id = int(request.args.get("id"))
    post = Post.query.filter_by(id=post_id).first()
    print(post)

    if post is None: 
        return f'''post with this id does not exist<br><a href="{url_for('posts_list')}">back to main</a>'''

    return render_template('posts_detail.html',post=post)

@app.route('/about')
def about():
    return render_template('about.html',title="About")

""" USER AUTH PAGES """
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('posts_list'))

""" User only area """
@app.route('/account')
@login_required # this HAS TO COME AFTER the app.route decorator to work
def account():
    return render_template('account.html',title="Account")
