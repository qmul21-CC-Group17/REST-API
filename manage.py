from app.main import create_app
from app.main import db

from app import blueprint
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main.model.user import User
from app.main.model.auth import BlackListToken

app = create_app('dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()
    #run()


