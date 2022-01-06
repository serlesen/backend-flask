from sqlalchemy import select, insert
from werkzeug.security import generate_password_hash

from backend import db
from backend.models.user import User
from backend.routes import basic_auth, token_auth

from flask import Blueprint, jsonify, request, Response

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@token_auth.login_required
def get_all_users():
    # style 1.X
    # all_users = User.query.all()

    # style 2.0
    users = db.session.scalars(select(User)).all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])


@users_bp.route("", methods=["POST"])
def create_user():
    d = request.json

    # style 1.X
    # u = User()
    # u.username = d["username"]
    # u.email = d["email"]
    # u.password = generate_password_hash(d["password"])
    # db.session.add(u)

    # style 2.0
    db.session.execute(
        insert(User).values(username=d["username"], email=d["email"], password=generate_password_hash(d["password"])))
    db.session.commit()

    return Response(status=204)

@users_bp.route("/<user_id>")
@token_auth.login_required
def get_user(user_id):
    # style 1.X
    # u = User.query.filter(User.id == user_id).one()

    # style 2.0
    user = db.session.scalars(select(User).where(User.id == user_id)).one()
    return jsonify({"id": user.id, "username": user.username})
