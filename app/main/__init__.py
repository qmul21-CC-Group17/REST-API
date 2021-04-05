from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import pymysql

#this line helps with an error
pymysql.install_as_MySQLdb()

from.config import Config
flask_bcrypt = Bcrypt() # for encryption of passwords
db = SQLAlchemy() # adapter for any database. takes care of the operations of the database

def create_app():
    """"Create app context"""
    app = Flask(__name__)
    app.config.from_object(Config) # config.py has all env variables like secret key and db urls etc
    # Initialise databse object
    db.init_app(app)
    flask_bcrypt.init_app(app) # starting point for the app. bcrypt searches for the secret key for the app. secret key used for password hashing

    return app
