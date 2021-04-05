from app.main.controller.auth import api as auth_api
from app.main.controller.user import api as user_api
from app.main.controller.jobs import api as jobs_api
from flask import Blueprint
from flask_restx import Api #flask-restx is a wrapper around restful flask in order to support swagger ui

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Job search application', version=None)
# these are defined REST method routes. added to swagger so it knows how to display them.
"""Add routes"""
api.add_namespace(auth_api)
api.add_namespace(user_api)
api.add_namespace(jobs_api)
