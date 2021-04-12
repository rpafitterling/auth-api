from config import Config
from extensions import db
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models.user import *
from models.perms import *

from utils import hash_password

# minimal setup for DB actions only
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
roles=[
    {'id': 10, 'roleName': 'NOT_LOGGED_IN', 'level': 10},
    ]

perms = (
    'PERM1',
    'PERM2',


users = [
    {
        'username': 'test',
        'email': 'email',
        'no_hash_password': 'test'
    }
]

for user in users:
    username=user.get('username')
    email=user.get('email')
    no_hash_password=user.get('no_hash_password')
    db.session.add(
        User(
            username=username, email=email, password=hash_password(no_hash_password),
            roles=[] 
        )
    )
db.session.commit()

for name in perms:
    db.session.add(
        PermNames(name=name)
        )

db.session.commit()

for item in roles:
    db.session.add(
        RoleNames(
            id=item.get('id'),
            name=item.get('roleName'),
            level=item.get('level')
            )
        )

db.session.commit()

# TODO user seed daten mit default perm groups








