from . import (
    seller as seller_bp,
    db,
    Product
)
from flask import (
    jsonify,
    request
)
from sqlalchemy import select

@seller_bp.get('/products/<int:user_id>')
def getSellerProducts(user_id):
    products=db.session.execute(select(Product).where(Product.user_id==user_id)).scalars()
    
    try:
        return jsonify({
            "products": [p for p in products]
        }), 200
    except:
        return "Error occurred", 500