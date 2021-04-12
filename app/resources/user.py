from http import HTTPStatus
from utils import hash_password

from flask import request, jsonify
from flask_restful import Resource

from flask_jwt_extended import get_jwt_identity, jwt_required

from models.user import User
from models.perms import Role

from schemas.user import UserSchema

user_schema = UserSchema()
#user_public_schema = UserSchema(exclude=('email', )

class UserListResource(Resource):

    ## TODO @jwt_required
    def post(self):
        json_data = request.get_json()

        #data, errors = user_schema.load(data=json_data)
        username = json_data.get('username')
        email = json_data.get('email')
        no_hash_password = json_data.get('password')

        if User.get_by_username(username):
            return {'message': 'username used already'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(email):
            return {'message': 'email used already'}, HTTPStatus.BAD_REQUEST

        user = User(username=username, email=email, password=hash_password(no_hash_password) )

        user.save()

        data = {'id': user.id, 'username': user.username, 'email': user.email}

        return data, HTTPStatus.CREATED

class UserResource(Resource):

    # WARNING potential security risc without authorization
    @jwt_required
    def get(self, userId):
        # user we are
        user = User.get_by_id(id=get_jwt_identity())
    
        if not user:
            return HTTPStatus.FORBIDDEN

        # user we want
        user = User.get_by_id(userId)
        
        perms = []
        for each in user.roles:
            role = Role.get_by_rolename(each.name)
            perms = perms + role.permissions # merge list

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'roles': list(map(lambda k: {'id': k.id, 'name': k.name}, user.roles)),
            'perms': list(map(lambda k: {'id': k.id, 'name': k.name}, perms)),
            }

        return data, HTTPStatus.OK

