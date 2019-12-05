from flask_restful import Api

from user.views import UserResource

user_api = Api(prefix='/user')

user_api.add_resource(UserResource, '/')

