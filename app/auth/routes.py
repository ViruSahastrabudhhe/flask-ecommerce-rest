from datetime import datetime, timezone, timedelta

from . import (
    auth as auth_bp,
    db,
    User,
    RoleUser,
    Roles,
    jwt
)
from flask import (
    jsonify,
    abort,
    request
)
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    get_jwt_identity,
    unset_jwt_cookies,
    set_access_cookies,
    current_user
)
from flask_bcrypt import (
    generate_password_hash, 
    check_password_hash
)
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

@auth_bp.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

@jwt.user_identity_loader
def user_identity_lookup(user):
    founduser = db.session.execute(select(User).where(User.username==user)).scalar_one_or_none()
    return str(founduser.id)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.session.execute(select(User).where(User.id==identity)).scalar_one_or_none()

@auth_bp.post('/login')
def login():
    data = request.get_json()

    username=data['username']
    password=data['password']
    
    user=db.session.execute(select(User).where(User.username==username)).scalar_one_or_none()

    if username=="" or password=="":
        return jsonify(msg="Please input your credentials!"), 401
    if user is None:
        return jsonify(msg="User does not exist!"), 401
    if check_password_hash(user.password, password)==False:
        return jsonify(msg="Bad username or password!"), 401
    
    access_token = create_access_token(identity=username, additional_claims={"is_seller": False})
    response = jsonify(msg="Successfully logged in!", access_token=access_token)
    set_access_cookies(response, access_token)
    return response

@auth_bp.post('/logout')
@jwt_required()
def logout():
    response=jsonify(msg="Successfully logged out!") 
    unset_jwt_cookies(response)

    return response

@auth_bp.post('/register')
def register():
    data=request.get_json()

    try:
        hashed_password=generate_password_hash(data['password']).decode('utf-8')

        user=User(
            email=data['email'],
            username=data['username'],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return jsonify(msg="Successfully registered user!"), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify(msg="Email already exists!"), 400
    except:
        db.session.rollback()
        return jsonify(msg="An error occurred!"), 500
    
@auth_bp.get('/protected')
@jwt_required()
def protected():
    return jsonify(id=current_user.id), 200