from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service
from utils import auth_required

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self, email):
        user = user_service.get_one(email)
        result = UserSchema().dump(user)
        del result['password']
        return result, 200

    @auth_required
    def patch(self, email):
        req_json = request.json
        req_json['email'] = email
        user_service.update(req_json)
        return '', 204


@user_ns.route('/password/')
class UserPasswordView(Resource):
    @auth_required
    def put(self, email):
        req_json = request.json
        req_json['email'] = email
        user_service.update_password(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return '', 204
