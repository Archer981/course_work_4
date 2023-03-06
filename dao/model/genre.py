from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    pk = fields.Int()
    name = fields.Str()
