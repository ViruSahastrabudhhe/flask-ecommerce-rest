from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mailman import Mail

migrate=Migrate()
mail=Mail()
csrf=CSRFProtect()
security=Security()
mail=Mail()
login_manager=LoginManager()