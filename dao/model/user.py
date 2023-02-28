from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(db.String(50))

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    role = fields.String()
