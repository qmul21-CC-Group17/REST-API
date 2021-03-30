from app.main.model.user import User
from app.main.service.blacklist import save_token


class AuthHelper:
    """"
    class to manage user session
    """

    @staticmethod
    def login_user(data):
        """
        Generates auth token based on passing username and password
        """
        try:
            user = User.query.filter_by(username=data['username']).first()
            if user and user.check_password(data['password']):
                auth_token = user.generate_auth_token(user.id)
                if auth_token:
                    return {
                        'status': 'success',
                        'message': 'logged in successfully',
                        'Auth': auth_token
                    }, 200
            else:
                return {
                    'status': 'fail',
                    'message': 'username or password did not match'
                }, 401
        except Exception as e:
            print(e)
            return {
                'status': 'fail',
                'message': 'Try again'
            }, 500

    @staticmethod
    def logout_user(data):
        """Add auth_token to BlackListTable on logout"""
        if data:
            auth_token = data.split(' ')[1]
        else:
            auth_token = None

        if auth_token:
            resp = User.decode_auth_token(auth_token)
            print(type(resp))
            if isinstance(resp, int):
                return save_token(auth_token)
            else:
                return {
                    'status': 'fail',
                    'message': resp
                }, 401

        else:
            return {
                'status': 'fail',
                'status': 'provide a valid token'
            }, 403

    @staticmethod
    def get_loged_in_user(request):
        """ Get the user from the auth token"""
        
        auth_token = request.headers.get('authorization')
        
        if auth_token:
            auth_token = auth_token.split(' ')[1]
            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, int):
                user = User.query.filter_by(id=resp).first()
                if user:
                    return {
                        'status': 'success',
                        'user_data': {
                            'user_id': user.id,
                            'username': user.username,
                            'is_admin': user.is_admin,
                            'email': user.email,
                            'full_time': user.full_time,
                            'location': user.location,
                            'keyword': user.keyword
                        }
                    }, 200
                else:
                    return {
                        'status': 'fail',
                        'message': 'user not found'
                    }, 404
            else:
                return {
                    'status': 'fail',
                    'message': resp
                }, 401
        return {
            'status': 'fail',
            'message': 'provide valid token'
        }, 401
        
