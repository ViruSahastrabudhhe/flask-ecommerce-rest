import datetime

from . import (
    products as products_bp,
    db,
    Product,
)
from flask import (
    jsonify,
    abort,
    request
)
from flask_login import (
    current_user,
    login_required
)
from flask_jwt_extended import (
    jwt_required
)
from sqlalchemy import select

@products_bp.get('/product/<int:product_id>')
def getProduct(product_id):
    product=db.session.execute(select(Product).where(Product.id==product_id)).scalar()

    try:
        return jsonify({
            "product": product
        })
    except:
        return "Error occurred", 500

@products_bp.post('/create')
def createProduct():
    try:
        data = request.get_json()

        product=Product(
            name=data['name'],
            price=data['price'],
            quantity=data['quantity'],
            description=data['description'],
            user_id=data['user_id']
        )

        db.session.add(product)
        db.session.commit()

        return jsonify({'result': True}), 201
    except:
        db.session.rollback()
        return "Error occurred", 500
    
@products_bp.delete('/delete/<int:product_id>')
def deleteProduct(product_id):
    product=db.session.execute(select(Product).where(Product.id==product_id)).scalar()
    
    try:
        db.session.delete(product)
        db.session.commit()

        return jsonify({'result': True}), 200
    except:
        db.session.rollback()
        return "Error occurred", 500
    
@products_bp.put('/edit/<int:product_id>')
def updateProduct(product_id):
    product=db.session.execute(select(Product).where(Product.id==product_id)).scalar()

    try:
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

        return jsonify({'result': True}), 200
    except:
        db.session.rollback()
        return "Error occurred", 500