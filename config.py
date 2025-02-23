import os
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask


# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class BaseConfig(object):

    def __init__(self, app: Flask):
        self.init_app(app)

    @classmethod
    def init_app(cls, app: Flask):
        app.config.from_object(cls)

    # # LOGGER
    LOGGING_PATH = '../logs'

    # TARGET API ENDPOINTS
    TARGET_API = os.environ.get('TARGET_API', 'http://localhost:10000')
