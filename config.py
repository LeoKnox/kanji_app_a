import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secrect_string"

    MONGODB_SETTINGS = { 'db' : 'kanji_app_db' }