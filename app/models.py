import datetime

from flask_sqlalchemy import SQLAlchemy
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
    VARCHAR
)
from flask_login import UserMixin
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

class User(Base, UserMixin):
    __tablename__='user'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=lambda: datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
 
class Role(Base):
    __tablename__='role'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str]

class RoleUser(Base):
    __tablename__='roles_users'

    id: Mapped[str] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))

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
