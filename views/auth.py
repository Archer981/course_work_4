from flask import request
from flask_restx import Namespace, Resource
from implemented import auth_service, user_service


auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        user_data = request.json
        user_service.create(user_data)
        return 'User created', 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    def post(self):
        user_data = request.json
        return auth_service.user_authorization(user_data)

    def put(self):
        tokens = request.json
        access_token = tokens.get('access_token')
        refresh_token = tokens.get('refresh_token')
        return auth_service.tokens_verification(access_token, refresh_token)
