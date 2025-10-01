class Config:
    TESTING=False
    # secrets.token_urlsafe()
    SECRET_KEY ='pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw'
    WTF_CSRF_SECRET_KEY='wtfsecretkey'
    JWT_SECRET_KEY = 'jwtsecretkey'

    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_TIME_LIMIT = None

class DevelopmentConfig(Config):
    DEBUG=True
    DB_SERVER = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root@localhost/3e_ecommerce_rest'
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
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root@localhost/3e_ecommerce_rest'
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