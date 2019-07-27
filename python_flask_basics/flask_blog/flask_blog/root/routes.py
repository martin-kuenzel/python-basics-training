from flask import Blueprint

root = Blueprint('root',__name__)

from flask import escape, request, render_template, url_for, flash, redirect
from flask import current_app

from flask_blog import db
from flask_blog.models import User, Post

from sqlalchemy import desc

from datetime import datetime
import secrets
import os

@root.route('/about')
def about():
    return render_template('about.html',title="About")
