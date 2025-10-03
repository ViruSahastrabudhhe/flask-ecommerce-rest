from flask import Blueprint
from app.models import (
    db,
    User,
    RoleUser,
    Roles
)
from app.extensions import (
    jwt,
)

auth = Blueprint('auth', __name__)

from . import routes