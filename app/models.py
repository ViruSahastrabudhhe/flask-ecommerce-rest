import datetime
from enum import Enum

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
    VARCHAR,
    select
)
from dataclasses import dataclass

class Roles(Enum):
    ADMIN=1
    BUYER=2
    SELLER=3

mapper_registry = registry(
    type_annotation_map = {
        str: String()
        .with_variant(VARCHAR(255), "mysql"),
    }
)

class Base(DeclarativeBase):
    registry=mapper_registry

db=SQLAlchemy(model_class=Base)

class User(Base):
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
