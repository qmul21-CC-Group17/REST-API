import os

base_dir = os.path.abspath(os.path.dirname(__file__)) #absolute base directory path

#create config object
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'super_secret_key')
    # format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
    SQLALCHEMY_DATABASE_URI = 'mysql://group17Admin:Group17Password@group17-githubjobs.cbgj5urfzqbw.us-east-1.rds.amazonaws.com:3306/JobSearchAPI'
    # Uncomment the line below if you want to work with a local DB
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


secret_key = Config.SECRET_KEY
