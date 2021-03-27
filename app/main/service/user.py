from app.main.model.user import User
from app.main import db

import uuid


def save_new_user(data):
    user_exist = User.query.filter_by(username=data['username']).first(
    ) or User.query.filter_by(email=data['email']).first()

    if user_exist:
        return {
            'status': 'fail',
            'message': "User already exist, please login or register"
        }, 409
    
    user = User(
        username=data['username'],
        email=data['email'],
        password = data['password'],
        full_time=data['full_time'],
        location=data['location'],
        keyword = data['keyword']
    )
    save_user(user)
    return {
            'status': 'success',
            'message': "please login with your email id and password"
        }, 201

def update_existing_user(data, id):
    if 'username' in data:
        user_exist=User.query.filter_by(username=data['username']).first()
        if user_exist:
            return {
            'status': 'fail',
            'message': "Username already exist, please try different username"
        }, 409
    
    if 'email' in data:
        user_exist=User.query.filter_by(email=data['email']).first()
        if user_exist:
            return {
            'status': 'fail',
            'message': "email id already exist, please try different username"
        }, 409
    
    return update_user(data, id)


def save_user(user):
    db.session.add(user)
    db.session.commit()

def update_user(data, id):
    user = User.query.get(id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.add(user)
    db.session.commit()
    return {
                    'status': 'success',
                    'message': 'Details updated successfully'
                }, 200

def get_all_users():
    return User.query.all()

def get_user_by_id(id_):
    return User.query.get(id_)

def delete_user_by_id(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {
            'status': 'success',
            'message': 'Deleted successfully'
        }, 200
    else:
        return {
            'status': 'fail',
            'message': 'User not found'
        }, 400


    
    
