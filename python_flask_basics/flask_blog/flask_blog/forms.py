from flask_wtf import FlaskForm

""" For profile pictures """
from flask_wtf.file import FileField, FileAllowed 

from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import HiddenInput
from flask_login import current_user

from flask_blog.models import User


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


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [ DataRequired(), Email() ] )
    password = PasswordField( 'Password', validators = [ DataRequired(), Length(min=5) ] )

    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class PostCreationForm(FlaskForm):
    title = StringField('Title', validators = [ DataRequired(), Length(min=5) ] )
    content = TextAreaField( 'Content', validators = [ DataRequired(), Length(max=1000) ] )

    submit = SubmitField('Create')

class PostChangeForm(PostCreationForm):
    id = IntegerField( HiddenInput() ) ### THIS ADDS THE ID OF THE REFERENCING POST AS HIDDEN FIELD
    submit = SubmitField('Save')
