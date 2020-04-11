import os

class Config(object):
    SECRET_KEY = os.envrion.get('SECRET_KEY') or "secrect_string"