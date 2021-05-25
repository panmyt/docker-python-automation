import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'default')

# MySQL configuration options.
# User connecting to database.
MYSQL_DB_USER = os.environ.get('MYSQL_DB_USER', 'root')
# Mysql user password.
MYSQL_DB_PASSWORD = os.environ.get('DB_PASSWORD', 'root')
# Mysql database host.
MYSQL_DB_HOST = os.environ.get('DB_HOST', 'localhost:3306')
# Mysql database name.
MYSQL_DB_NAME = os.environ.get('DB_NAME', 'myapp')
#MYSQL_DB_PORT = '3306'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(
    MYSQL_DB_USER, MYSQL_DB_PASSWORD, MYSQL_DB_HOST, MYSQL_DB_NAME)

# Redis configuration options.
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

# Listening options.
LISTENING_HOST = os.environ.get('LISTENING_HOST', '172.22.0.3')
LISTENING_PORT = os.environ.get('LISTENING_PORT', '5000')
