import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '19a44ec19ea6f2c3bf8384d63a44f384'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# The name of the view (route) to redirect to when the user needs to log in.
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# This string must be placed over here (not in the top)
# otherwise 'the error of circular import' will be occurred.
from flaskblog import views
