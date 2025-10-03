from flask import Blueprint
from app.models import (
    db,
    Product
)
from app.decorators import (
    seller_required
)

products=Blueprint('products', __name__)

from . import routes