import jwt
from flask import Blueprint, jsonify, request
from sqlalchemy import select
from werkzeug.security import check_password_hash

from backend import db
from backend.models.user import User
from backend.routes import secret_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    d = request.json
    if "username" not in d or "password" not in d:
        raise Exception("Unable to authenticate")

    user = db.session.scalars(select(User).where(User.username == d["username"])).one()
    if not check_password_hash(user.password, d["password"]):
        raise Exception("Invalid password")

    encoded_jwt = jwt.encode({"sub": user.id, "username": user.username}, secret_token, algorithm="HS256")
    return jsonify({"token": encoded_jwt})

