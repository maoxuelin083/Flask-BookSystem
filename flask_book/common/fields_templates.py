from flask_restful import fields

book_fields = {
    "name": fields.String(attribute="b_name"),
    "author": fields.String(attribute="b_author"),
}