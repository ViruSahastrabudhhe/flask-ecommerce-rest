from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_mailman import Mail
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

migrate=Migrate()
mail=Mail()
csrf=CSRFProtect()
mail=Mail()
login_manager=LoginManager()
jwt=JWTManager()
bcrypt=Bcrypt()