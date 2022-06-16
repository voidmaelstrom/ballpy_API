# config                    
from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    # Database connection configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from flask_migrate import Migrate

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # register reptile blueprint
    from . import reptile
    app.register_blueprint(reptile.bp)

    # return the app 
    return app