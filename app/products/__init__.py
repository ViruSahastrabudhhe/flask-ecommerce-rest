from flask import Blueprint
from app.models import (
    db,
    Product
)

products=Blueprint('products', __name__)

from . import routes