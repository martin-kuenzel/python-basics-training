from flask_wtf import FlaskForm

""" For profile pictures """
from flask_wtf.file import FileField, FileAllowed 

from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask_login import current_user

from flask_blog.models import User

""" the creation of new users form """
class RegistrationForm(FlaskForm):
    username = StringField( 'Username', validators = [ DataRequired(), Length(min=5,max=20) ] )
    email = StringField('Email', validators = [ DataRequired(), Email() ] )
    profile_pic = FileField('Update profile picture', validators = [FileAllowed(['jpg','png','jpeg'])])

    password = PasswordField( 'Password', validators = [ DataRequired(), Length(min=5) ] )
    confirm_password = PasswordField( 'Confirm Password', validators = [ DataRequired(), Length(min=5), EqualTo('password') ] )

    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user is None:
            raise ValidationError('Username is already taken')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user is None:
            raise ValidationError('Email already exists')

""" the updating of existing users form  """
class UserUpdateForm(RegistrationForm):
    password = None
    confirm_password = None
    submit = SubmitField('Save')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user is None and not user.username is current_user.username:
            raise ValidationError('Username is already taken')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user is None and not user.email is current_user.email:
            raise ValidationError('Email already exists')


""" the logging in for existing users form """
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [ DataRequired(), Email() ] )
    password = PasswordField( 'Password', validators = [ DataRequired(), Length(min=5) ] )

    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


""" the forgot password form """
class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators = [ DataRequired(), Email() ] )
    submit = SubmitField('Reset')

""" the updating password form (only reachable via received email) """
class PasswordResetForm(RegistrationForm):
    username = None
    email = None
    profile_pic = None
    submit = SubmitField('Save')