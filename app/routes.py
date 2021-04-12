from flask_restful import Api

from resources.test import ApiTestResource
from resources.token import TokenResource, RefreshTokenResource, RevokeTokenResource

from resources.test_auth import ApiTestAuthResource

from resources.user import UserListResource
from resources.user import UserResource
from resources.roles import RoleResource
from resources.roles import UserRoleListResource
from resources.roles import RoleListResource
from resources.roles import DefaultRoleResource
from resources.me import MeResource

from resources.permissions import PermissionResource

def register_basic_resources(app):
    api = Api(app)

    api.add_resource(TokenResource,'/api/v1'+ '/auth')
    api.add_resource(RevokeTokenResource,'/api/v1'+ '/revoke')
    api.add_resource(RefreshTokenResource,'/api/v1'+ '/refresh')

    api.add_resource(ApiTestResource, '/api/v1' + '/status')
    api.add_resource(ApiTestAuthResource,'/api/v1'+ '/auth_test')


def register_app_specific_resources(app):
    api = Api(app)

    # https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html

    api.add_resource(UserListResource,'/api/v1/users/', methods = ['POST'])
    #
    
    api.add_resource(MeResource,'/api/v1/me', methods = ['GET'])
    
    api.add_resource(UserResource,'/api/v1/users/<int:userId>', methods = ['GET'])
    api.add_resource(UserRoleListResource,'/api/v1/users/<int:userId>/roles', methods = ['PUT'])

    api.add_resource(RoleResource,'/api/v1/roles/<int:roleId>', methods = ['GET'])
    api.add_resource(RoleListResource,'/api/v1/roles/', methods = ['POST', 'GET'])
    
    api.add_resource(DefaultRoleResource,'/api/v1/roles/default', methods = ['GET'])
    api.add_resource(PermissionResource,'/api/v1/roles/<int:roleId>/permissions', methods = ['PUT', 'DELETE'])


    # TODO
    # get permissionNames
    
    # TODO
    #api.add_resource(PermCreateResource,'/api/v1/users/<int:userId>/perms', methods = ['POST'])
    #api.add_resource(PermUpdateResource,'/api/v1/users/<int:userId>/perms', methods = ['PUT'])


