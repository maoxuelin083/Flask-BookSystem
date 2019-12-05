from flask_restful import Api

from book.views import BookResource

book_api = Api(prefix='/book')

book_api.add_resource(BookResource, '/')

