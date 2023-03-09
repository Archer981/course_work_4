from flask import request, abort
import jwt
from constants import SECRET, JWT_ALGO


def auth_required(func):
    def wrapper(self, *args, **kwargs):
        email = get_token()['email']
        return func(self, email, *args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        data = get_token()
        if data['role'] != 'admin':
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def get_token():
    if 'Authorization' not in request.headers:
        abort(401)
    data = request.headers['Authorization']
    token = data.split('Bearer ')[-1]
    try:
        decoded_token = jwt.decode(token, SECRET, algorithms=[JWT_ALGO])
    except:
        abort(401)
    return decoded_token
