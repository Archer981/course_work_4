from flask import request
from flask_restx import Namespace, Resource
from implemented import auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        user_data = request.json
        return auth_service.user_authorization(user_data)

    def put(self):
        tokens = request.json
        refresh_token = tokens.get('refresh_token')
        return auth_service.refresh_token_verification(refresh_token)
