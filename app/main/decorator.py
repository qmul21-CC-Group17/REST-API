#this file defines the messages to display when invalid logins and tokens are encountered in the app
from flask import request
from functools import wraps
from app.main.service.auth import AuthHelper


def login_required(func):
    """Check if the valid auth token is passed in the authorization header"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, status = AuthHelper.get_loged_in_user(request)
        if status == 200:
            if data.get('user_data'):
                return func(*args, **kwargs)
        return data, status
    
    return wrapper

def admin_token_required(func):
    """Check if auth token in the headers belongs to admin"""
    
    @wraps(func)
    def decorated(*args, **kwargs):

        data, status_code = AuthHelper.get_loged_in_user(request)
        
        if status_code != 200:
            return data, status_code

        is_admin = data['user_data'].get('is_admin')
        if not is_admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return func(*args, **kwargs)

    return decorated
