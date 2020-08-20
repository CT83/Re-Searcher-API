import os

from shared.utils import generate_random_string

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True

    AZURE_BING_KEY = os.environ.get('AZURE_BING_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    CONFIG_NAME = "development"
    DEBUG = True

    # Database
    DB_URL = os.environ['DB_URL']

    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PORT = os.environ['REDIS_PORT']
    REDIS_URL = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)

    CELERY_BROKER_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    CELERY_RESULT_BACKEND = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)


class TestingConfig(Config):
    CONFIG_NAME = "testing"
    TESTING = True
    DB_FILE_NAME = 'temp/test_{}.db'.format(generate_random_string())
    DB_URL = 'sqlite:///' + os.path.join(basedir, DB_FILE_NAME)
    APP_NAME = os.environ.get('APP_NAME')
    RQ_CONNECTION_CLASS = 'fakeredis.FakeStrictRedis'
    CELERY_BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'
    CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'


class ProductionConfig(Config):
    CONFIG_NAME = "production"
    # Database
    DB_URL = os.environ['DB_URL']

    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PORT = os.environ['REDIS_PORT']
    REDIS_URL = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)

    CELERY_BROKER_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    CELERY_RESULT_BACKEND = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
