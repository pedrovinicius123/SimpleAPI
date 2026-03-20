from flask import Flask
from .config import Config
from .routes.messages import bp_message
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(bp_message)

    with app.app_context():
        db.create_all()

    return app
