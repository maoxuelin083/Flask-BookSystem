from book.route import book_api
from user.route import user_api


def init_route(app):
    user_api.init_app(app)
    book_api.init_app(app)

