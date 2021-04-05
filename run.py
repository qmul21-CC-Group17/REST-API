from app.main import create_app
from app.main import db
import OpenSSL
from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from app.main.model.user import User
from app.main.model.auth import BlackListToken

app = create_app()
app.register_blueprint(blueprint) #registering all the endpoints, and to display in swagger
migrate = Migrate(app, db) # Identifies what db it is and creates tables: creates a migrate folder with the db properties. run only first time.
Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
