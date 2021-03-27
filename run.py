from app.main import create_app
from app.main import db

from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from app.main.model.user import User
from app.main.model.auth import BlackListToken

app = create_app()
app.register_blueprint(blueprint)
migrate = Migrate(app, db)
Migrate(app, db)

def run():
    app.run()

if __name__ == '__main__':
    run()


