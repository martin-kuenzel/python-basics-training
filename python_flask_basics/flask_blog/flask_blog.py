from flask import Flask, escape, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') #'b680f9c461dca3d215fca7e59a4838b1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    
    """relationship for multiple posts from table:post"""
    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.email}, {self.image_file})'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    """Foreign Key to table:user, column:id"""
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f'Post({self.id},{self.user_id},{self.title},{self.date_created})'


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

## to run in python directly
if __name__ == '__main__':
    app.run(debug=True)