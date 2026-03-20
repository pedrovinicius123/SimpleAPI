from flask import Flask
from .config import Config
from .routes.user import bp_user
from .extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(bp_user)

    with app.app_context():
        db.create_all()

    return app
