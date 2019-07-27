from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

from wtforms.widgets import HiddenInput ## this is needed for updating existing posts

""" the creation of a new post form """
class PostCreationForm(FlaskForm):
    title = StringField('Title', validators = [ DataRequired(), Length(min=5) ] )
    content = TextAreaField( 'Content', validators = [ DataRequired(), Length(max=10000) ] )

    submit = SubmitField('Create')

""" the updating of an existing post form """
class PostChangeForm(PostCreationForm):
    id = IntegerField( HiddenInput() ) ### THIS ADDS THE ID OF THE REFERENCING POST AS HIDDEN FIELD
    submit = SubmitField('Save')
