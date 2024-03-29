#here the parameters and their display in swagger is defined for the user, authentication and get_jobs operations. 
from flask_restx import Namespace, fields
from app.main.service.auth import AuthHelper

#all this data will be saved in an object _user
class UserDto:
    api = Namespace('User', 'User operations')
    user = api.model('user', {
        'id': fields.Integer(required=False, description='unique identifier'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'keyword': fields.String(required=True, description='Area of interest'),
        'location': fields.String(required=True, description='Location'),
        'full_time': fields.Boolean(default=True, description='Are you searching for full time job?')
    })
#data to be saved in the object _auth
class AuthDto:
    api = Namespace('Auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='Username'),
        'password': fields.String(required=True, description='The user password '),
    })

class JobDto:
    api = Namespace('Jobs', description='Search for Jobs')

        
