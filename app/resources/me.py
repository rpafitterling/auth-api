from http import HTTPStatus
from utils import hash_password

from flask import request, jsonify
from flask_restful import Resource

from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional

from models.user import User
from models.perms import Role

from schemas.user import UserSchema

class MeResource(Resource):

    @jwt_optional
    def get(self):
        user = User.get_by_id(id=get_jwt_identity())

        if not user:
            # ADD default role(s) Role.get_defaults()
            #role = Role.get_by_id(1)
            defaultRole = Role.get_by_rolename('NOT_LOGGED_IN')
            if (defaultRole == None):
                return HTTPStatus.NOT_FOUND
            
            data = {
                'username': 'guest',
                'email': '',
                'roles': [ {'id': defaultRole.id, 'name': defaultRole.name}],
                'perms': list(map(lambda k: k.name, defaultRole.permissions))
                }
            return data, HTTPStatus.OK

        perms = []
        for each in user.roles:
            role = Role.get_by_rolename(each.name)
            perms = perms + role.permissions # merge list

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'roles': list(map(lambda k: {'id': k.id, 'name': k.name}, user.roles)),
            #'perms': list(map(lambda k: {'id': k.id, 'name': k.name}, perms)),
            'perms': list(map(lambda k: k.name, perms)),
            }

        return data, HTTPStatus.OK

