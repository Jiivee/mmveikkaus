import os

_basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'For your eyes only'
CSRF_ENABLED = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

if 'DATABASE_URL' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
