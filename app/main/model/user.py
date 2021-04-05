# db queries defined for the operations on USER table in MYSQL database using SQLAlchemy

from .. import db, flask_bcrypt
from app.main.model.auth import BlackListToken
from app.main.config import secret_key
import jwt

import datetime


class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(50), unique=True)
    keyword = db.Column(db.String(50))
    full_time = db.Column(db.Boolean, nullable=False, default=False)
    location = db.Column(db.String(50))
    password_hash = db.Column(db.String(100))

    def __init__(self, email, username, password, full_time=True, location=None, keyword=None):
        self.email = email
        self.username = username
        self.password_hash = flask_bcrypt.generate_password_hash(
            password).decode('utf-8')
        self.registered_on = datetime.datetime.utcnow()
        self.full_time = full_time
        self.keyword = keyword
        self.location = location

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def generate_auth_token(id_):
        """
          Generate an auth token
        """

        try: # checks if the tokens are valid because its making note of the time of login
            payload = {
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow()+datetime.timedelta(days=1, seconds=5),
                'sub': id_
            }
    
            return jwt.encode(
             payload,
             secret_key, 
             algorithm='HS256' # hash algorithm applied for auth token
            )
            

        except Exception as e:
            print(e)
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decode auth token
        """
        try:
            payload = jwt.decode(auth_token, secret_key, algorithms=["HS256"])
            is_listed = BlackListToken.check_validity(auth_token)
            if is_listed:
                return 'Invalid token, please login again'
            else:
                return payload['sub']
        
        except jwt.ExpiredSignatureError:
            return 'Token expired, please login again'
        
        except jwt.InvalidTokenError as e:
            print(e)
            return 'Invalid token, Please login again'
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
# all these functions are defined under db.user 
