from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class Books(BaseModelPrimaryKey):
    b_name = db.Column(db.String(32), nullable=False)
    b_author = db.Column(db.String(32), nullable=False)
    b_user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

