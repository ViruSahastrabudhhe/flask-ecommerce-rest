import os

from flask import Flask
from .models import (
    db,
    Role
)
from .extensions import (
    migrate, 
    csrf, 
    mail, 
    jwt,
    bcrypt
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
    jwt.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()
        # db.session.add(Role(name="seller"))
        # db.session.add(Role(name="buyer"))
        # db.session.add(Role(name="admin"))
        # db.session.commit()

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/accounts')
    from .products import products as products_bp
    app.register_blueprint(products_bp, url_prefix='/api/products')
    from .seller import seller as seller_bp
    app.register_blueprint(seller_bp, url_prefix='/api/seller')

    return app