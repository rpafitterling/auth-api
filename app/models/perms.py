from extensions import db
from builtins import classmethod


## helper table many to many
rolePerms = db.Table('roles_perms',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('perm_id', db.Integer, db.ForeignKey('perms.id'), primary_key=True)
)

class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)

    # Is exactly a value from RoleNames TODO relation
    name = db.Column(db.String(80), nullable=False, unique=True)

    permissions = db.relationship('Permission', secondary=rolePerms, lazy='subquery',
        backref=db.backref('roles', lazy=False))

    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

# FIXME   
#    @property
#    def data(self):
#        return {
#       }

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_rolename(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


class Permission(db.Model):
    __tablename__ = 'perms'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(80), nullable=False, unique=True)
    
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

class Operations(db.Model):
    __tablename__ = 'operations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Enum("read", "write", "create", "delete"), name="name")

    def save(self):
        db.session.add(self)
        db.session.commit()


class RoleNames(db.Model):
    __tablename__ = 'role_names'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    level = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

class PermNames(db.Model):
    __tablename__ = 'perm_names'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


