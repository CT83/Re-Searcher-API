import os

from shared.utils import generate_random_hash

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    CONFIG_NAME = "development"
    DEBUG = True
    # Database
    DBUSER = os.environ.get('POSTGRES_USER')
    DBPASS = os.environ['POSTGRES_PASSWORD']
    DBHOST = os.environ['DBHOST']
    DBPORT = os.environ['DBPORT']
    DBNAME = os.environ['POSTGRES_DB']

    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=DBUSER,
            passwd=DBPASS,
            host=DBHOST,
            port=DBPORT,
            db=DBNAME)

    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PORT = os.environ['REDIS_PORT']
    REDIS_URL = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)

    CELERY_BROKER_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    CELERY_RESULT_BACKEND = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)


class TestingConfig(Config):
    CONFIG_NAME = "testing"
    TESTING = True
    DB_FILE_NAME = 'temp/test_{}.db'.format(generate_random_hash())
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, DB_FILE_NAME)
    APP_NAME = os.environ.get('APP_NAME')
    RQ_CONNECTION_CLASS = 'fakeredis.FakeStrictRedis'
    CELERY_BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'
    CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'


class ProductionConfig(Config):
    CONFIG_NAME = "production"
    # Database
    DBUSER = os.environ.get('POSTGRES_USER')
    DBPASS = os.environ['POSTGRES_PASSWORD']
    DBHOST = os.environ['DBHOST']
    DBPORT = os.environ['DBPORT']
    DBNAME = os.environ['POSTGRES_DB']

    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=DBUSER,
            passwd=DBPASS,
            host=DBHOST,
            port=DBPORT,
            db=DBNAME)
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
