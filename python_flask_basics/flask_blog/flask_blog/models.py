from datetime import datetime

from flask import current_app

from flask_blog import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

"""required by Extension login_manager"""
@login_manager.user_loader
def login_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Boolean(),nullable=False, default=False)
    
    """relationship for multiple posts from table:post"""
    posts = db.relationship('Post',cascade="all,delete",backref='author',lazy=True)

    """ 
    
    for activation/pw reset we need a security token 
    
    """

    """ this creates a security token 
        times out after 600 Seconds (15 mins)
    """
    def create_usr_verify_token(self,expires_secs=600):
        s = Serializer(current_app.config['SECRET_KEY'],expires_secs)
        return s.dumps({'user_id':self.id}).decode('utf-8')
    
    """ this checks security tokens against the app/db for users """
    @staticmethod
    def confirm_usr_verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try: 
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)



    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.email}, {self.image_file})'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_changed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    """Foreign Key to table:user, column:id"""
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f'Post({self.id},{self.user_id},{self.title},{self.date_created})'
