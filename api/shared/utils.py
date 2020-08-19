import os
import random
import re
import shutil
import string
import uuid

import fakeredis
import requests
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


def generate_random_image():
    """Generates random images, using a randomly generated numpy array - used in tests"""
    import numpy as np

    rgb = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)
    return rgb


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


def _add_worker(host, port, gpus, name, secret_token, desc):
    from models.worker import Worker
    from shared.factories import db

    w = Worker(host=host, port=port, gpus=gpus, name=name, secret_token=secret_token, description=desc)
    db.session.add(w)
    db.session.commit()
    print("Added {}".format(str(w)))


def get_valid_filename(s):
    s = str(s).strip().replace(" ", "_")
    return re.sub(r"(?u)[^-\w.]", "", s)


def download_file(url, download_path):
    r = requests.get(url, timeout=5)
    if r.status_code == 200:
        open(download_path, "wb").write(r.content)
        return download_path


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


def add_architectures_and_backbones():
    from shared.factories import db
    from models.architectures_backbones import ArchitectureTypes, BackboneTypes

    data = {
        "DetectNet_V2": [
            "ResNet10",
            "ResNet18",
            "ResNet34",
            "ResNet50",
            "ResNet101",
            "VGG 16",
            "VGG 19",
            "GoogleNet",
            "MobileNet V1",
            "MobileNet V2",
            "SqueezeNet",
            "DarkNet 19",
            "DarkNet 53",
        ],
        "FasterRCNN": [
            "ResNet10",
            "ResNet18",
            "ResNet34",
            "ResNet50",
            "ResNet101",
            "VGG 16",
            "VGG 19",
            "GoogleNet",
            "MobileNet V1",
            "MobileNet V2",
            "DarkNet 19",
            "DarkNet 53",
        ],
        "SSD": [
            "ResNet10",
            "ResNet18",
            "ResNet34",
            "ResNet50",
            "ResNet101",
            "VGG 16",
            "VGG 19",
            "GoogleNet",
            "MobileNet V1",
            "MobileNet V2",
            "SqueezeNet",
            "DarkNet 19",
            "DarkNet 53",
        ],
        "YOLOV3": [
            "ResNet10",
            "ResNet18",
            "ResNet34",
            "ResNet50",
            "ResNet101",
            "VGG 16",
            "VGG 19",
            "GoogleNet",
            "MobileNet V1",
            "MobileNet V2",
            "SqueezeNet",
            "DarkNet 19",
            "DarkNet 53",
        ],
        "RetinaNet": [
            "ResNet10",
            "ResNet18",
            "ResNet34",
            "ResNet50",
            "ResNet101",
            "VGG 16",
            "VGG 19",
            "GoogleNet",
            "MobileNet V1",
            "MobileNet V2",
            "SqueezeNet",
            "DarkNet 19",
            "DarkNet 53",
        ],
        "DSSD": [
            "ResNet10",
            "ResNet18",
            "ResNet34",
            "ResNet50",
            "ResNet101",
            "VGG 16",
            "VGG 19",
            "GoogleNet",
            "MobileNet V1",
            "MobileNet V2",
            "SqueezeNet",
            "DarkNet 19",
            "DarkNet 53",
        ],
    }

    archs = data.keys()
    for arch in archs:
        new_arch = ArchitectureTypes(name=arch)
        db.session.add(new_arch)
        db.session.commit()

        for backbone in data[arch]:
            new_backbone = BackboneTypes.query.filter_by(name=backbone).first()
            if not new_backbone:
                new_backbone = BackboneTypes(name=backbone)
                db.session.add(new_backbone)
                db.session.commit()

            new_arch.back_bone.append(new_backbone)
            db.session.commit()

    print("created architectures and backbones")
