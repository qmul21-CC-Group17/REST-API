from app.main.model.auth import BlackListToken
from app.main import db

def save_token(auth_token):
    try:
        bl_token = BlackListToken(auth_token)
        db.session.add(bl_token)
        db.session.commit()
        return {
            'status': 'success',
            'message': 'user logged out successfully'
        }
    except Exception as e:
        print(e)
        return {
            'status': 'fail',
            'message': e
        }, 500
    