from FlaskProject.extendsions import db


class BaseModels(db.Model):
    __abstract__ = True
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        return True


class BaseModelPrimaryKey(BaseModels):
    __abstract__ =True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)



