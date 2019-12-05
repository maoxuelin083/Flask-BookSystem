import uuid

from flask_restful import Resource, reqparse, marshal

from FlaskProject.extendsions import cache
from book.models import Books
from common.fields_templates import book_fields
from common.time import TIMEOUT
from .models import Users


class UserResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("action", required=True)
    parser.add_argument("token")
    parser.add_argument("username")
    parser.add_argument("password")


    def get(self):
        # action = request.args.get("action")
        args = self.parser.parse_args()
        action = args.action
        if action == "register":
            return self.do_register()
        elif action == "login":
            return self.do_login()
        elif action == "token":
            return self.do_token()
        else:
            data = {
                "msg": "Unknow Access",
                "status": 400
            }
            return data

    def do_register(self):
        args = self.parser.parse_args()
        username = args.username
        password = args.password
        user = Users()
        user.username = username
        user.password = password
        if not user.save():
            data = {
                "msg": "save error",
                "status": 400
            }
            return data
        data = {
            "msg": "save success",
            "status": 200
        }
        return data


    def do_login(self):
        args = self.parser.parse_args()
        username = args.username
        password = args.password
        user = Users.query.filter_by(username=username).first()
        print(user)
        if not user:
            data = {
                "msg": "no users",
                "status": 400
            }
            return data
        token = uuid.uuid4().hex
        cache.set(token, user.id, TIMEOUT)
        data = {
            "msg": "login success",
            "status": 200,
            "data": {
                "token": token
            }
        }
        return data


    def do_token(self):
        args = self.parser.parse_args()
        token = args.token
        id = cache.get(token)
        print(id)
        user = Users.query.filter_by(id=id).first()
        if not user:
            data = {
                "msg": "not find",
                "status": 404
            }
            return data
        books = Books.query.filter_by(id=user.id).all()
        data = {
            "msg": "find success",
            "status": 200,
            "data": marshal(books, book_fields)
        }
        return data













