from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_security.models import fsqla_v3 as fsqla

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
fsqla.FsModels.set_db_info(db)

class Role(Base, fsqla.FsRoleMixin):
    __tablename__='role'
    pass

class User(Base, fsqla.FsUserMixin):
    __tablename__='user'
    pass

class WebAuthn(Base, fsqla.FsWebAuthnMixin):
    __tablename__='webauthn_credentials'
    pass