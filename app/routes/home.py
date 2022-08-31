from flask import Blueprint, render_template

# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later. This corresponds to using the Router middleware of Express.js.

bp = Blueprint('home', __name__, url_prefix='/')

# we add a @bp.route() decorator before the function to turn it into a route
@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')