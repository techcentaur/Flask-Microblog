from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#a instance of flask
app = Flask(__name__)
#a instance of the class in config.py
app.config.from_object(Config)
#created objects of database aoos
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#Flask-login extension instance creation
login = LoginManager(app)
#flask-login can automatically redirect the user to login
#form, if not already logged-in, for this purpose, Flask-login
#needs to know what is the view function that handles logins.
login.login_view = 'login'

# routes - view functions; models - structure of the database
from app import routes, models