from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from .model import User
from blueprints import db, app
from flask_orator import  jsonify
import hashlib
from helper.encryption import Encryption

bp_user = Blueprint('User', __name__)
api = Api(bp_user)

class UserResource(Resource) :
    def __init__(self) :
        pass

    def get(self, id) :
        user = User.find(id)    
        app.logger.debug('DEBUG : %s', user)
        return jsonify(user)

    def post(self) :
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('email', location='json', required=True)       

        data = parser.parse_args()

        password_hash = Encryption.generatePassword(data['password'])
        
        try:
            user = User()
            user.name = data['name']
            user.password = password_hash
            user.email = data['email']
            user.role = 'user'
            user.save()

            app.logger.debug('DEBUG : %s', user)

            return jsonify(user)
        except Exception as e :
            app.logger.debug('DEBUG : %s', 'EROR'+str(e))
            result = {}
            result['msg'] = str(e)
            return jsonify(result)

class UserResourceList(Resource) :
    def __init__(self) :
        pass

    def get(self) :
        users = User.all()

        app.logger.debug('DEBUG : %s', users)

        return jsonify(users)




api.add_resource(UserResourceList, '/list', '')
api.add_resource(UserResource, '', '/<id>')
