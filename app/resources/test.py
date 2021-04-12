from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
from utils import hash_password

class ApiTestResource(Resource):
        def get(self):
            data = {'data': {'success': True}}
            return data, HTTPStatus.OK



