import os

from flask import Flask
from .models import db, User, Role
from .extensions import (
    migrate, 
    csrf, 
    security, 
    mail, 
    login_manager, 
    SQLAlchemyUserDatastore
)
from instance.config import config

def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config['development'])
    else:
        # load the test config if passed in
        app.config.from_object(config['testing'])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    user_datastore=SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    return app