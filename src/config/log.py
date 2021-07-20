import os
import sys

from dotenv import load_dotenv
from loguru import logger


class Config(object):
    DEBUG = False
    TESTING = False
    LOGURU_SETTINGS = {}
    LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "log")


class ProdConfig(Config):
    LOGURU_SETTINGS = {
        "handlers": [
            dict(sink=sys.stderr, format="[{time}] {message}"),
            dict(sink=os.path.join(Config.LOG_PATH, "app.log"), enqueue=True, serialize=True, retention="10 days", rotation="1 day"),
        ],
        "levels": []
    }


class DevConfig(Config):
    DEBUG = True
    LOGURU_SETTINGS = {
        "handlers": [
            dict(sink=sys.stdout, format="[{time}] {message}"),
        ],
        "levels": []
    }


load_dotenv()
ENV = os.getenv('ENV', 'dev')
if ENV == "prod":
    config = ProdConfig()
else:
    config = DevConfig()

logger.configure(**config.LOGURU_SETTINGS)
