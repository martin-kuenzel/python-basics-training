from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') #'b680f9c461dca3d215fca7e59a4838b1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

"""for password hashing, we use flask-bcrypt"""
bcrypt = Bcrypt(app)

"""login manager from flask-login"""
login_manager = LoginManager(app)
login_manager.login_view = '/login'
login_manager.login_message_category = 'info'

from flask_blog import routes