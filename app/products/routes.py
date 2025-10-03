import datetime

from . import (
    products as products_bp,
    db,
    Product,
    seller_required
)
from flask import (
    jsonify,
    abort,
    request
)
from flask_jwt_extended import (
    jwt_required,
    current_user
)
from sqlalchemy import select

@products_bp.get('/product/<int:product_id>')
def getProduct(product_id):
    product=db.session.execute(select(Product).where(Product.id==product_id)).scalar_one_or_none()

    try:
        return jsonify(product=product)
    except:
        return jsonify(msg="Error occurred!"), 500

@products_bp.post('/create')
@jwt_required()
@seller_required()
def createProduct():
    try:
        data = request.get_json()

        product=Product(
            name=data['name'],
            price=data['price'],
            quantity=data['quantity'],
            description=data['description'],
            user_id=current_user.id
        )

        db.session.add(product)
        db.session.commit()

        return jsonify(msg="Succesfully created product!"), 201
    except:
        db.session.rollback()
        return jsonify(msg="Error occurred!"), 500
    
@products_bp.delete('/delete/<int:product_id>')
@jwt_required()
def deleteProduct(product_id):
    product=db.session.execute(select(Product).where(Product.id==product_id)).scalar_one_or_none()
    
    try:
        if product.user_id!=current_user.id:
            return jsonify(msg="Unauthorized request!"), 403
        
        db.session.delete(product)
        db.session.commit()

        return jsonify(msg="Successfully deleted product!"), 200
    except:
        db.session.rollback()
        return jsonify(msg="Error occurred!"), 500
    
@products_bp.put('/edit/<int:product_id>')
@jwt_required()
def updateProduct(product_id):
    product=db.session.execute(select(Product).where(Product.id==product_id)).scalar_one_or_none()

    try:
        if product.user_id!=current_user.id:
            return jsonify(msg="Unauthorized request!"), 403
        
        data = request.get_json()

        if not (data['name'] == ''):
            product.name=data['name']
        if data['price'] is not None:
            product.price=data['price']
        if data['quantity'] is not None:
            product.quantity=data['quantity']
        if not (data['description'] == ''):
            product.description=data['description']

        product.updated_at=datetime.datetime.now()

        db.session.commit()

        return jsonify(msg="Succesfully updated product!"), 201
    except:
        db.session.rollback()
        return jsonify(msg="Error occurred!"), 500