from flask import Blueprint

posts = Blueprint( 'posts', __name__ )

from flask import escape, request, render_template, url_for, flash, redirect

from flask import current_app

from flask_blog import db, bcrypt, mail

from ..models import User, Post
from .forms import PostCreationForm, PostChangeForm

from flask_login import login_user, logout_user, current_user, login_required

from sqlalchemy import desc

from datetime import datetime

""" For pagination of posts """
from flask_paginate import Pagination

@posts.route('/posts_detail/<int:post_id>')
def posts_detail(post_id):
    post = Post.query.get(post_id)
    user_id = request.args.get( 'user_id', type=int )

    if post is None: 
        flash(f'Post does not exist','info')
        return redirect(url_for('posts.posts_list'))

    return render_template('posts/posts_detail.html',post=post, user_id = user_id, title="Post details" )

""" creation of posts """
@posts.route('/posts_create', methods=['GET','POST'])
@login_required
def posts_create():
    form = PostCreationForm()
    if form.validate_on_submit():
        post = Post(user_id=current_user.id, title=form.title.data,content=form.content.data)
        db.session.add(post)
        db.session.commit()

        flash(f'Post created','success')
        return redirect(url_for('posts.posts_list'))

    return render_template('posts/posts_create.html',title='Post creation',form=form)

""" changing of posts """
@posts.route('/posts_change/<int:post_id>', methods=['GET','POST'])
@login_required
def posts_change(post_id):
    
    post = Post.query.get(post_id)

    if post and current_user == post.author:
        form = PostChangeForm(obj=post)

        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            post.date_changed = datetime.utcnow()

            db.session.commit()

            flash(f'Post changed','success')
            return redirect(url_for('posts.posts_list'))

        return render_template('posts/posts_change.html',title='Post update',form=form)

    return redirect(url_for('posts.posts_list'))


""" deletion of posts """
@posts.route('/posts_delete/<int:post_id>', methods=['GET','POST'])
@login_required
def posts_delete(post_id):
    
    post = Post.query.get(post_id)

    if post and current_user == post.author:
        if request.method == 'POST':
        
            db.session.delete(post)
            db.session.commit()

            flash(f'Post deleted','success')
            return redirect(url_for('posts.posts_list'))

    return render_template('posts/posts_delete.html',title='Post deletion',post=post)


@posts.route('/')
@posts.route('/home')
@posts.route('/Home')
def posts_list():
    
    posts = db.session.query(Post).order_by(desc(Post.date_changed))

    """ FILTERING BY user_id """
    user_id = request.args.get( 'user_id', type=int, default=0 )
    user = User.query.get( user_id ) ## get parameter &user_id=<int>, defaults to 0 (NONE)
    if user_id and not user:
        flash("No user with such id exists", 'info')
    elif user:
        posts = posts.filter_by( author = user )

    """ PAGINATION """
    per_page = 3 ## show <int> entries per page
    page = int( request.args.get('page', type=int, default=1) ) ## get parameter &page=<int>, defaults to 1 (first page)
    pagination = Pagination( page=page, per_page=per_page, total=posts.count(), record_name='posts', css_framework='bootstrap4') ## the pagination html objects
    
    posts = posts.paginate(page=page, per_page=per_page)
    return render_template('home.html', posts=posts.items, pagination=pagination, user=user, title="Posts" )