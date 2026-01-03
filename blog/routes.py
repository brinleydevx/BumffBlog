from crypt import methods

from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.utils import redirect
from . import db

from .models import Post
from .forms import PostForm

main = Blueprint("main", __name__)

@main.route("/")
def home():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template('home.html', posts=posts)

@main.route("/create", methods=["GET", "POST"])
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post)
        db.session.commit()

        flash("Post created successfully!", "success")
        return redirect(url_for("main.home"))
    return render_template("create.html", form=form)

@main.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post)
