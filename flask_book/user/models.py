from werkzeug.security import generate_password_hash, check_password_hash

from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class Users(BaseModelPrimaryKey):
    username = db.Column(db.String(32), nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)


    @property
    def password(self):
        raise Exception("保存密码异常")

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self._password, pwd)

