import os
import uuid

def random():
        random = uuid.uuid4().hex
        print(random)
        return random

class Config:
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

        # https://www.base64encode.org/
        SECRET_KEY = os.environ.get('SECRET_KEY')
        JWT_ERROR_MESSAGE_KEY = 'message'

        JWT_BLACKLIST_ENABLED = True
        JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

        # JWT security options:
        JWT_COOKIE_SECURE = True
        JWT_TOKEN_LOCATION = ["headers", "cookies"]


