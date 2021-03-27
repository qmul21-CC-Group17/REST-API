import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'super_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


secret_key = Config.SECRET_KEY
