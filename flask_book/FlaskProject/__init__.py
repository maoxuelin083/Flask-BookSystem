from flask import Flask

from FlaskProject.config import FlaskConfig
from FlaskProject.extendsions import init_extendsions
from FlaskProject.route import init_route


def create_app():

    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    app.config.from_object(FlaskConfig)

    init_extendsions(app)

    init_route(app)

    return app





