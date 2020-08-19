import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.api.workers import Workers
from config import config
from shared.utils import db_connection_successful, init_celery, init_redis


def create_app(config_name, managing=False):
    app = Flask(__name__, )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)

    api = Api(app)
    api.add_resource(
        Workers, "/workers", "/workers/<int:index>",
    )

    # Database
    from shared.factories import db

    db.app = app
    db.init_app(app)
    with app.app_context():
        if not db_connection_successful(db):
            exit(1)

    from shared.log_manager import LogManager
    app = LogManager().init_app(app)

    from shared.factories import client
    from app.cron import scheduler_start

    client = init_celery(celery=client, app=app)
    app.client = client

    app.redis_store = init_redis(app)

    if (
            not app.config.get("TESTING")
            and not managing
            and not os.environ.get("DONT_RUN_SCHEDULAR")
    ):
        from app.cron import init_cron

        init_cron(app, config_name=config_name)

    return app
