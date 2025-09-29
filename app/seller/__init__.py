from flask import Blueprint
from app.models import (
    db, 
    Product
)

seller=Blueprint('seller', __name__)

from . import routes