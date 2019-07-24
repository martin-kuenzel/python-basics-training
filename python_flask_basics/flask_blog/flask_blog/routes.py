from flask import escape, request, render_template, url_for, flash, redirect

from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

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
    return render_template('home.html',posts=posts)

@app.route('/posts_detail')
def posts_detail():
    post_id = int(request.args.get("id"))
    if posts[post_id] is None: 
        return f'post with this id does not exist'
    return render_template('posts_detail.html',post=posts[post_id])

@app.route('/about')
def about():
    return render_template('about.html',title="About")

## USER AUTH PAGES
@app.route( '/register', methods=['GET','POST'] )
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('posts_list'))
    return render_template('register.html',title="Register",form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        """Just for testing the logon mechanism for now"""
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in', 'success')
            return redirect(url_for('posts_list'))
        else:
            flash(f'Wrong login data','danger')
    return render_template('login.html',title="Login", form=form)

###
