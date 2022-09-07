from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db

# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later. This corresponds to using the Router middleware of Express.js.

bp = Blueprint('home', __name__, url_prefix='/')

# we add a @bp.route() decorator before the function to turn it into a route
@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template(
    'homepage.html',
    posts=posts,
    loggedIn=session.get('loggedIn')
  ) 

@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')
  # if logged in, redirect to the dashboard page
  return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  # use the filter() method on the connection object to specify the SQL WHERE clause
  post = db.query(Post).filter(Post.id == id).one()

  # pass the single post object to the single-post.html template to render it
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )