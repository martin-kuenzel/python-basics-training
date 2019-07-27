from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

""" the configurations for the application """
from flask_blog.config import Config

""" DATABASE SETUP """
db = SQLAlchemy()

"""for password hashing, we use flask-bcrypt"""
bcrypt = Bcrypt()

"""login manager from flask-login"""
login_manager = LoginManager()
login_manager.login_view = 'users.account_login'
login_manager.login_message_category = 'info'

""" setting up a mail object"""
mail = Mail()

""" to create multiple instances of our app """
def create_app( config_class = Config ):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flask_blog.users.routes import users
    app.register_blueprint(users)

    from flask_blog.posts.routes import posts
    app.register_blueprint(posts)

    from flask_blog.root.routes import root
    app.register_blueprint(root)

    from flask_blog.errors.routes import errors
    app.register_blueprint(errors)

    """ date formatter """
    @app.template_filter('date_f')
    def formatted_date(date):
        return date.strftime('%B, %d.%m.%Y - %H:%M')

    return app