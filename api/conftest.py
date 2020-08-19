import os
import sys

import pytest

sys.path.append(os.getcwd())

@pytest.fixture
def config():
    return "testing"


@pytest.fixture
def app():
    from app import create_app
    from shared.utils import create_dir_if_not_exists

    create_dir_if_not_exists("temp")
    app = create_app("testing")

    with app.app_context():
        # from shared.factories import db
        #
        # db.create_all()

        yield app
        # try:
        #     db.drop_all()
        # except:
        #     pass


def cleanup_dirs_and_db():
    try:
        import shutil

        shutil.rmtree("temp")
    except:
        pass
