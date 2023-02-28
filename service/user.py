from utils import get_hash
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, username):
        return self.dao.get_one(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d['password'] = get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, username):
        user_data = self.get_one(username)
        uid = user_data.get('id')
        self.dao.delete(uid)
