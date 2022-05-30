from email.mime import image
from flask import render_template, url_for, request, flash, redirect, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
from flaskblog.posts.utils import save_picture
import urllib.request
import os
from werkzeug.utils import secure_filename
from PIL import Image
from flask import current_app
import secrets


posts = Blueprint('posts', __name__)

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if image := form.image.data:
            if image and allowed_file(image.filename):
                random_hex = secrets.token_hex(8)
                _, f_ext = os.path.splitext(image.filename)
                picture_fn = random_hex + f_ext
                picture_path = os.path.join(
                    current_app.root_path, 'static/uploads/posts', picture_fn)
                output_size = (500,300)
                i = Image.open(image)
                i.thumbnail(output_size)
                i.save(picture_path)
            else:
                flash('Allowed image types are - png, jpg, jpeg, gif', 'danger')
        else:
            flash('No image selected', 'danger')
            return redirect(request.url)
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user, image=picture_fn)
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('posts/create_post.html', legend='New post', title='Create new post', form=form)


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():

        if form.image.data:
            prev_picture = os.path.join(
                posts.root_path, 'static/uploads/posts', post.image)
            if os.path.exists(prev_picture):
                os.remove(prev_picture)
            if image := form.image.data:
                if image and allowed_file(image.filename):
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(image.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(
                        current_app.root_path, 'static/uploads/posts', picture_fn)
                    output_size = (400, 300)
                    i = Image.open(image)
                    i.thumbnail(output_size)
                    i.save(picture_path)
                else:
                    flash('Allowed image types are - png, jpg, jpeg, gif', 'danger')
            else:
                flash('No image selected', 'danger')
                return redirect(request.url)
            post.image = picture_fn
        post.title = form.title.data
        post.content = form.content.data
        # post.image = form.image.data
        db.session.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.image.data = post.image
    return render_template('posts/create_post.html', title='Update post', legend=f'Update {post.title}', form=form, post=post)


@posts.route('/post/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted!', 'success')
    return redirect(url_for('main.home'))
