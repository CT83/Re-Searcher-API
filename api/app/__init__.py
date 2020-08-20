from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.api.search import SearchRes
from config import config
from models.utils import init_tables
from shared.utils import init_celery, init_redis


def create_app(config_name):
    app = Flask(__name__, )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)

    # Setup routes
    api = Api(app)
    api.add_resource(SearchRes, "/search", )

    # Setup logging
    from shared.log_manager import LogManager
    app = LogManager().init_app(app)

    # Setup Persistence
    from shared.factories import client
    app.client = init_celery(celery=client, app=app)
    app.redis_store = init_redis(app)
    init_tables(app)

    return app
