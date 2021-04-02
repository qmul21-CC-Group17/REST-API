from app.main import create_app
from app.main import db
import OpenSSL
from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from app.main.model.user import User
from app.main.model.auth import BlackListToken

app = create_app()
app.register_blueprint(blueprint)
migrate = Migrate(app, db)
Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, ssl_context='adhoc')
