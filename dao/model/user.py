from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    pk = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    favorite_genre = db.Column(db.Integer())

class UserSchema(Schema):
    pk = fields.Integer()
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.Integer()
