from extensions import db
from builtins import classmethod
#from models.perms import *

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    firstname = db.Column(db.String(80), nullable=True, unique=False)
    lastname = db.Column(db.String(80), nullable=True, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    #roles = db.relationship('Role', backref='user')
    roles = db.relationship('Role', backref='user', lazy=True)

    # https://docs.sqlalchemy.org/en/13/orm/loading_relationships.html
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # not yet used
    @property
    def data(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'roles': list(map(lambda k: {'id': k.id, 'name': k.name}, user.roles)),
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
