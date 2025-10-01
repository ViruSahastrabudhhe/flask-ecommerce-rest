from . import (
    auth as auth_bp,
    db,
    User,
    login_manager
)
from flask import (
    jsonify,
    abort,
    request
)
from flask_login import (
    login_user,
    logout_user,
    login_required
)
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    unset_jwt_cookies
)
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

@login_manager.user_loader
def load_user(user_id):
    user=db.session.execute(select(User).where(User.id==user_id)).scalar()
    return user

@auth_bp.post('/login')
def login():
    data = request.get_json()

    username=data['username']
    password=data['password']
    
    user=db.session.execute(select(User).where(User.username==username)).scalar()

    if user is None or user.password!=password:
        return jsonify({
            'msg': 'Bad username or password',
            'result': False
        }), 401

    login_user(user)

    access_token = create_access_token(identity=username)
    return jsonify({
        'access_token': access_token,
        'msg': 'Successfully logged in!',
        'result': True
    }), 200

@auth_bp.post('/logout')
@login_required
def logout():
    logout_user()
    
    response=({'msg': "Successfully logged out!"})
    unset_jwt_cookies(response)

    return jsonify({
        'msg': response,
        'result': True
    }), 200

@auth_bp.post('/register')
def register():
    data=request.get_json()

    try:
        user=User(
            email=data['email'],
            username=data['username'],
            password=data['password']
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({
            'msg': 'Successfully registered user!',
            'result': True
        }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            'msg': 'Email already exists!',
            'result': False
        }), 400
    except:
        db.session.rollback()
        return jsonify({
            'msg': 'Error occurred!',
            'result': False
        }), 500