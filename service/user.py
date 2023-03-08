from flask import abort
import hashlib
import base64

from constants import HASH_ALGO, PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, email):
        return self.dao.get_one(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        email = user_d.get('email')
        password = user_d.get('password')
        if not email or not password:
            abort(401)
        user_data = self.dao.get_one(email)
        if user_data:
            abort(401)
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, username):
        user_data = self.get_one(username)
        uid = user_data.get('id')
        self.dao.delete(uid)

    def get_hash(self, password):
        return base64.b64encode(
            hashlib.pbkdf2_hmac(
                HASH_ALGO,
                password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )
