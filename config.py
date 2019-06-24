import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wont-tell-you'

    """change the secret_key value"""