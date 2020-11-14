from blueprints import db
from flask_restful import fields


class User(db.Model) :
    __fillable__ = ['name', 'email', 'role']

    def __repr__(self) :
        return '<User %r>' % self.name