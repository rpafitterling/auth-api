#!/usr/local/bin/python3

import sys
# TODO https://github.com/flasgger/flasgger
from flask import Flask, request
from flask_restful import Resource
from flask_migrate import Migrate
from flask_cors import CORS

#from resources.token import (black_list)
from config import Config
from extensions import db, jwt

# flask migrate uses this block to determine changes
from models.perms import *
from models.user import *

# alternatively flask will pick it up here, but ONLY linked ones
from routes import *

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    register_extensions(app)
    
    register_basic_resources(app)
    register_app_specific_resources(app)

    list_routes(app)

    CORS(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db,compare_type=True)
    jwt.init_app(app)

def list_routes(app):
    routes = []
    print("")
    for i in app.url_map.iter_rules():
        print(i.rule, i.methods)
    print("")

if __name__ == '__main__':
    app = create_app()
    port = 8080

    if len(sys.argv) >= 2:
        if sys.argv[1]:
            port = sys.argv[1] # overwrite port if given

    app.run(host='0.0.0.0', debug=True, port=port)

