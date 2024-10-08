from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

pdb = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object("app.config.PostgresqlConfig")
    authorizations = {
        "apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}
    }
    api = Api(app, security="apikey", authorizations=authorizations)

    pdb.init_app(app)
    migrate.init_app(app, pdb)

    with app.app_context():
        from app.resources.User import api_users
        from app.resources.Customer import api_customer
        from app.resources.DeviceType import api_device_type
        from app.resources.CustomerDevice import api_customer_device
        from app.resources.Logger import api_logger

        api.add_namespace(api_users)
        api.add_namespace(api_customer)
        api.add_namespace(api_device_type)
        api.add_namespace(api_customer_device)
        api.add_namespace(api_logger)

    return app
