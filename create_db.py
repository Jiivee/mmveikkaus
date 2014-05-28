from app import db
import os
_basedir = os.path.abspath(os.path.dirname(__file__))
os.remove(os.path.join(_basedir, 'app.db'))
db.create_all()
