from flask import Flask

from backend.routes.errors import error_bp
from backend.routes.health import health_bp
from backend.routes.users import users_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app

