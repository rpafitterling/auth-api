from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.perms import Permission
from models.perms import PermNames
from models.perms import Role
from models.user import User
from flask_jwt_extended import jwt_required

# TODO rename -> RolePermissionList
class PermissionResource(Resource):

        @jwt_required
        def put(self, roleId):
            json_data = request.get_json()
            name = json_data.get('name')

            perm = Permission.get_by_name(name = name)
            if (perm == None):
                perm = Permission(name=name)

            role = Role.get_by_id(roleId)
            if (role == None):
                return HTTPStatus.NOT_FOUND

            role.permissions.append(perm)
            role.save()

            data = {'id': role.id, 'name': role.name, 'permissions': list(map(lambda k: k.name, role.permissions))}

            return data, HTTPStatus.OK
            


        @jwt_required
        def delete(self, roleId):
            json_data = request.get_json()
            name = json_data.get('name')

            perm = Permission.get_by_name(name = name)
            if (perm == None):
                return HTTPStatus.NOT_FOUND

            role = Role.get_by_id(roleId)
            if (role == None):
                return HTTPStatus.NOT_FOUND

            if (role.permissions.count(perm)):
                role.permissions.remove(perm)
                role.save()

            data = {'id': role.id, 'name': role.name, 'permissions': list(map(lambda k: k.name, role.permissions))}

            return data, HTTPStatus.OK
            

