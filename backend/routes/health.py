from flask import Blueprint

from backend.decorators import timed_windowed

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
@timed_windowed(60)
def health_check():
    return "ok"
