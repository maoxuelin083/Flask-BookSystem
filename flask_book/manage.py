from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from FlaskProject import create_app

app = create_app()

manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
