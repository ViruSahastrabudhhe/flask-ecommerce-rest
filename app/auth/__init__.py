from flask import Blueprint
from app.models import (
    db,
    User
)
from app.extensions import login_manager

auth = Blueprint('auth', __name__)

from . import routes