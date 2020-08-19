import os
import random
import re
import shutil
import string
import uuid

import fakeredis
from flask_redis import FlaskRedis
from sqlalchemy.exc import SQLAlchemyError


def create_dir_if_not_exists(output_dir):
    try:
        os.makedirs(output_dir)
        return output_dir
    except OSError:
        if not os.path.isdir(output_dir):
            raise

        return output_dir


def delete_file_if_exists(file):
    try:
        os.remove(file)
    except Exception:
        pass


def delete_dir_if_exists(folder):
    try:
        shutil.rmtree(folder)
    except Exception:
        pass


def datetime_to_filename(dt):
    return dt.strftime("%d%m%Y_%H%M%S%f")


def generate_random_hash():
    return str(uuid.uuid4().hex)


def generate_random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def db_connection_successful(db):
    """Checks if DB Connection is successful"""
    from flask import current_app

    try:
        db.session.execute('SELECT 1')
        db.session.commit()
        db.session.remove()
    except SQLAlchemyError as se:
        current_app.logger.error(str(se))
        return False
    return True


def get_valid_filename(s):
    s = str(s).strip().replace(" ", "_")
    return re.sub(r"(?u)[^-\w.]", "", s)


def init_celery(celery, app):
    celery.conf.broker_url = app.config["CELERY_BROKER_URL"]
    celery.conf.result_backend = app.config["CELERY_RESULT_BACKEND"]
    celery.conf.update(app.config)
    return celery


def init_redis(app):
    if app.config.get("TESTING"):
        redis_store = fakeredis.FakeStrictRedis()
    else:
        redis_store = FlaskRedis(
            host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"], db=0
        )
        redis_store.init_app(app)
    return redis_store
