import hashlib
import base64
import hmac
import datetime
import calendar
import jwt
from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_ALGO, HASH_ALGO, SECRET


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def user_authorization(self, user_data):
        username = user_data.get('username')
        password = user_data.get('password')
        if not username or not password:
            print('No data')
            return 401
        user_data = self.dao.get_one(username)
        if not user_data:
            print('No user')
            return 401
        if not self.password_compare(password, user_data.password):
            print('Incorrect password')
            return 401
        return self.get_tokens({'username': username, 'role': user_data.role})

    def get_tokens(self, token_data):
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token_data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(token_data, SECRET, algorithm=JWT_ALGO)
        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        token_data['exp'] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(token_data, SECRET, algorithm=JWT_ALGO)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def refresh_token_verification(self, old_refresh_token):
        if not old_refresh_token:
            return '', 401
        try:
            token_data = jwt.decode(old_refresh_token, SECRET, algorithms=[JWT_ALGO])
        except:
            return '', 401
        return self.get_tokens(token_data)

    def password_compare(self, password, user_password):
        password = hashlib.pbkdf2_hmac(
            HASH_ALGO,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        user_password = base64.b64decode(user_password)
        return hmac.compare_digest(password, user_password)
