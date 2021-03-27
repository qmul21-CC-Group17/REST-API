from app.main.controller.auth import api as auth_api
from app.main.controller.user import api as user_api
from app.main.controller.jobs import api as jobs_api
from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Job search application', version=None)

"""Add routes"""
api.add_namespace(auth_api)
api.add_namespace(user_api)
api.add_namespace(jobs_api)
