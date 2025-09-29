import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    registry,
    mapped_column
)
from sqlalchemy import (
    ForeignKey,
    String,
    BIGINT,
    TEXT,
    TIMESTAMP,
    VARCHAR
)
from dataclasses import dataclass

mapper_registry = registry(
    type_annotation_map = {
        str: String()
        .with_variant(VARCHAR(255), "mysql"),
    }
)

class Base(DeclarativeBase):
    registry=mapper_registry

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

@dataclass
class Product(Base):
    __tablename__='products'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=lambda: datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
