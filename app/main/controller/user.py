from flask import request
from flask_restx import Resource

from app.main.dto import UserDto
from app.main.decorator import admin_token_required, login_required
from app.main.service.user import save_new_user, get_all_users, get_user_by_id, update_existing_user, delete_user_by_id
from app.main.service.auth import AuthHelper

api = UserDto.api
_user = UserDto.user

parser = api.parser()
parser.add_argument('username', location='json')
parser.add_argument('email', location='json')
parser.add_argument('password', location='json')
parser.add_argument('location', location='json')
parser.add_argument('full_time', location='json')
parser.add_argument('keyword', location='json')


auth_parser = api.parser()
auth_parser.add_argument('Authorization', location='headers')


@api.route('/')
class UserList(Resource):
    @api.doc('List users')
    @api.expect(auth_parser)
    @admin_token_required
    @api.marshal_with(_user, mask='id,username,email,location,keyword,full_time')
    def get(self):
        """List all users (Admin access required)"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Create new user"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.expect(auth_parser)
    @admin_token_required
    @api.marshal_with(_user, mask='id,username,email,location,keyword,full_time')
    @api.doc('Get user by ID (Admin access required)')
    def get(self, id):
        """"Get user by ID (Admin access required)"""
        
        user = get_user_by_id(id)
        if not user:
            api.abort(404)
        else:
            return user, 200

    @api.doc('Update user details')
    @api.expect(parser)
    @login_required
    def patch(self, id):
        """Update user details"""
        
        resp = AuthHelper.get_loged_in_user(request)
        if resp[0]['status'] == 'success':
            user_id = resp[0]['user_data']['user_id']
            if user_id == int(id):
                data = request.json
                return update_existing_user(data, user_id)
            else:
                return {
                    'status': 'fail',
                    'message': 'only logined user can update details'
                }, 401

    @api.expect(auth_parser)
    @admin_token_required
    @api.doc('Delete Account (Admin access required)')
    def delete(self, id):
        """Delete Account (Admin access required)"""
        resp = AuthHelper.get_loged_in_user(request)
        if resp[0]['status'] == 'success':
            user_id = resp[0]['user_data']['user_id']
            return delete_user_by_id(id)
        else:
            return {
                'status': 'fail',
                'message': 'only logged in user '
            }, 401
