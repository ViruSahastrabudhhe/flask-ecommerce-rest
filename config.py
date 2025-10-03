from datetime import timedelta

class Config:
    TESTING=False
    # secrets.token_urlsafe()
    SECRET_KEY ='supersecretkey'
    WTF_CSRF_SECRET_KEY='wtfsecretkey'
    JWT_SECRET_KEY = 'jwtsecretkey'

    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_TIME_LIMIT = None

    JWT_TOKEN_LOCATION = ["headers", "cookies", "json", "query_string"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG=True
    DB_SERVER = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root@localhost/ecommerce_rest'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
    }

    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # insert ur own here
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class TestingConfig(Config):
    TESTING=True
    DEBUG=False
    DB_SERVER = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root@localhost/ecommerce_rest'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
    }

    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # insert ur own here
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    
    'default': DevelopmentConfig
}