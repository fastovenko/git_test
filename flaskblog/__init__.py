from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '19a44ec19ea6f2c3bf8384d63a44f384'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# This must be placed over here (not in the top)
# otherwise 'the error of circular import' will be occurred
from flaskblog import views
