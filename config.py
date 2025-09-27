class Config:
    TESTING=False
    # secrets.token_urlsafe()
    # NOTE: this aint my secret key lol
    SECRET_KEY ='pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw'
    WTF_CSRF_SECRET_KEY='wtfsecretkey'
    # secrets.SystemRandom().getrandbits(128)
    # NOTE: this aint my password salt lol
    SECURITY_PASSWORD_SALT = '146585145368132386173505678016728509634'

    SECURITY_FLASH_MESSAGES = False
    SECURITY_URL_PREFIX = '/api/accounts'

    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    # SECURITY_UNIFIED_SIGNIN = True

    SECURITY_POST_CONFIRM_VIEW = "/confirmed"
    SECURITY_CONFIRM_ERROR_VIEW = "/confirm-error"
    SECURITY_RESET_VIEW = "/reset-password"
    SECURITY_RESET_ERROR_VIEW = "/reset-password-error"
    SECURITY_LOGIN_ERROR_VIEW = "/login-error"
    # SECURITY_POST_OAUTH_LOGIN_VIEW = "/post-oauth-login"
    SECURITY_REDIRECT_BEHAVIOR = "spa"

    # SECURITY_TWO_FACTOR_ENABLED_METHODS = ['email', 'authenticator']
    # SECURITY_TWO_FACTOR = True
    # SECURITY_TWO_FACTOR_RESCUE_MAIL = ''

    # SECURITY_TWO_FACTOR_ALWAYS_VALIDATE = False
    # SECURITY_TWO_FACTOR_LOGIN_VALIDITY = '1 week'

    # passlib.totp.generate_secret()
    # NOTE: this aint my totp secrets lol
    # SECURITY_TOTP_SECRETS = {'1': 'TjQ9Qa31VOrfEzuPy4VHQWPCTmRzCnFzMKLxXYiZu9B'}
    # SECURITY_TOTP_ISSUER = ''

    SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True

    SECURITY_CSRF_COOKIE_NAME = "XSRF-TOKEN"
    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_TIME_LIMIT = None

class DevelopmentConfig(Config):
    DEBUG=True
    DB_SERVER = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root@localhost/ecommerce'
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
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root@localhost/ecommerce'
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