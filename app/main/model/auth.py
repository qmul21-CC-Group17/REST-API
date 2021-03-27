from .. import db
import datetime

class BlackListToken(db.Model):
    """"
    db to save invalid tokens
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
    
    @staticmethod
    def check_validity(auth_token):
        """"Check if auth_token has an entry in BlackListToken table"""
        is_listed = BlackListToken.query.filter_by(token=auth_token).first()
        if is_listed:
            return True
        return False
         