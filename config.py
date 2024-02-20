import os
import redis
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
    Set the config variables for the flask app
    using Environment variables where available.
    Otherwise create the config variable if not done already.
    
    '''
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Ideas make great oranges'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False

    REDIS_URI = os.environ.get("REDIS_URI")
    SESSION_TYPE = "redis"
    print(REDIS_URI)
    SESSION_REDIS = redis.from_url("redis://default:16NT4bXOr6bNff0vRr8ftjvK4ZF3eNk6@redis-19920.c284.us-east1-2.gce.cloud.redislabs.com:19920")

    DREAMOBJECTS_SECRET_KEY=os.getenv('DREAMOBJECTS_SECRET_KEY')
    DREAMOBJECTS_KEY = os.getenv('DREAMOBJECTS_KEY')

    





