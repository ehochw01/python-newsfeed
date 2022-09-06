from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# flask creates a new context every time a server request is made. When the request ends, the context is removed from the app. These temporary contexts provide global variables, like the g object, that can be shared across modules as long as the context is still active.
from flask import g

load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
    # creates any tables that Base mapped in a class that inherits Base (i.e. User)
    Base.metadata.create_all(engine)
    # The close_db() function won't run automatically. We need to tell Flask to run it whenever a context is destroyed.
    app.teardown_appcontext(close_db)

# The get_db() function now saves the current connection on the g object, if it's not already there. Then it returns the connection from the g object instead of creating a new Session instance each time.
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db

def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()

# def get_db():
#     # Whenever this function is called, it returns a new session-connection object. 
#     return Session()