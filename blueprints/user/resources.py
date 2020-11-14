from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
from datetime import datetime
from .model import User
from blueprints import db, app
from flask_orator import  jsonify

bp_user = Blueprint('User', __name__)
api = Api(bp_user)

class UserResource(Resource) :
    def __init__(self) :
        pass

    def get(self) :
        users = User.all()
    
        app.logger.debug('DEBUG : %s', users)
        return jsonify(users)


api.add_resource(UserResource, '', '')
