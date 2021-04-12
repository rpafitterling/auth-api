from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.perms import Role
from models.user import User
from flask_jwt_extended import jwt_required

class RoleResource(Resource):

    @jwt_required
    def get(self, roleId):
        role = Role.get_by_id(roleId)

        data = {'id': role.id, 'name': role.name, 'permissions': list(map(lambda k: k.name, role.permissions))}

        return data, HTTPStatus.OK
            

class UserRoleListResource(Resource):

    @jwt_required
    def put(self, userId):
        json_data = request.get_json()
        name = json_data["name"]
        user = User.get_by_id(userId)

        if (Role.get_by_rolename(name=name) == None):
            role = Role(name=name)
            user.roles.append(role)
                
        user.save()

        data = {'roles': [
            list(map(lambda k: {'id': k.id, 'name': k.name}, user.roles))
        ]}

        return data, HTTPStatus.CREATED
            



class DefaultRoleResource(Resource):

    @jwt_required
    def get(self):
        role = Role.get_by_id(1)
        if (role == None):
            return HTTPStatus.NOT_FOUND

        data = {'id': role.id, 'name': role.name, 'permissions': list(map(lambda k: k.name, role.permissions))}

        return data, HTTPStatus.OK
            

class RoleListResource(Resource):
    
    @jwt_required
    def get(self):
        roles = Role.query.all()

        data = {'roles': [
            list(map(
                lambda k: {
                    'id': k.id, 'name': k.name,
                    'perms': [list(map(lambda m: m.name, k.permissions))]
                    }, roles
                ))
        ]}

        return data, HTTPStatus.CREATED
            
    @jwt_required
    def post(self):
        data = request.get_json();
        role = Role(name = data['name']);
        role.save();

        data = role;

        return data, HTTPStatus.CREATED


