from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import pymysql

#this line helps with an error
pymysql.install_as_MySQLdb()

from.config import Config
flask_bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app():
    """"Create app context"""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
