from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
from utils import hash_password
from flask_jwt_extended import jwt_required, get_jwt_identity

class ApiTestAuthResource(Resource):
   
    @jwt_required
    def get(self):
        user = User.get_by_id(id=get_jwt_identity())

        user_data = {
            'id': user.id,
            'email': user.email,
            'username': user.username
        }
        
        data = {'data': {'user': user_data}}
        return data, HTTPStatus.OK




