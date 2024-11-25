from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
login = LoginManager()
mail = Mail()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.chat import chat as chat_blueprint
    app.register_blueprint(chat_blueprint, url_prefix='/chat')

    from app.profiles import profiles as profiles_blueprint
    app.register_blueprint(profiles_blueprint, url_prefix='/profiles')

    from app.groups import groups as groups_blueprint
    app.register_blueprint(groups_blueprint, url_prefix='/groups')

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
