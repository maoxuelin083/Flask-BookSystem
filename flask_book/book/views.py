from flask_restful import Resource, reqparse, marshal

from FlaskProject.extendsions import cache
from common.fields_templates import book_fields
from .models import Books


class BookResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("action", required=True)
    parser.add_argument("b_name")
    parser.add_argument("b_author")
    parser.add_argument("token")

    def get(self):
        args = self.parser.parse_args()
        action = args.action
        if action == "add":
            return self.do_add()
        elif action == "get":
            return self.get_book()
        else:
            data = {
                "msg": "unknow Access",
                "status": 400
            }
            return data


    def do_add(self):
        args = self.parser.parse_args()
        b_name = args.b_name
        b_author = args.b_author
        token = args.token
        id = cache.get(token)
        book = Books()
        book.b_name = b_name
        book.b_author = b_author
        book.b_user_id = id
        if not book.save():
            data = {
                "msg": "save error",
                "status": 404
            }
            return data
        data = {
            "msg": "save success",
            "status": 200,
        }
        return data


    def get_book(self):
        args = self.parser.parse_args()
        token = args.get("token")
        id = cache.get(token)
        # print(id)
        books = Books.query.filter_by(b_user_id=id).all()
        # print(books)
        if not books:
            data = {
                "msg": "no books",
                "status": 400
            }
            return data
        data = {
            "msg": "find success",
            "status": 200,
            "data": marshal(books, book_fields)
        }
        return data




