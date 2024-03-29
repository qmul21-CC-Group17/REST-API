#defining endpoints for auth i.e. login and logout methods

from app.main.service.auth import AuthHelper
from app.main.decorator import login_required
from app.main.dto import AuthDto
from flask_restx import Resource
from flask import request


api = AuthDto.api
user_auth = AuthDto.user_auth
parser = api.parser()

@api.doc('Login user')
@api.route('/login') # linked to /login function
class UserLogin(Resource): #set of end points used to update the entries in the table
    """"
    User login
    """
    @api.doc('User login')
    @api.expect(user_auth, validate=True) # checking if the parameters are passed
    def post(self):
        """Login user by generating JWT token"""
        data = request.json
        return AuthHelper.login_user(data)


parser.add_argument('Authorization', location='headers')
@api.route('/logout')
@api.doc('Logout user')
@api.expect(parser)
class UserLogout(Resource):
    """
    User logout user
    """
    @api.doc('Logout User')
    def post(self):
        """Logout User by balcklisting JWT token"""
        auth_token = request.headers.get('Authorization')
        return AuthHelper.logout_user(auth_token)

    



