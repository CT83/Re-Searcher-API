from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.api.search import SearchRes
from app.api.workers import Workers
from config import config
from shared.utils import init_celery, init_redis


def create_app(config_name):
    app = Flask(__name__, )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)

    api = Api(app)
    api.add_resource(SearchRes, "/search", )

    from shared.log_manager import LogManager
    app = LogManager().init_app(app)

    from shared.factories import client

    client = init_celery(celery=client, app=app)
    app.client = client

    app.redis_store = init_redis(app)

    return app
