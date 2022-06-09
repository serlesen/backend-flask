import logging

import jwt
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from sqlalchemy import select
from werkzeug.security import check_password_hash

from backend import db
from backend.models.user import User

LOGGER = logging.getLogger(__name__)
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

secret_token = "mysecret"


@basic_auth.verify_password
def verify_basic_password(username, password):
    user = db.session.scalars(select(User).where(User.username == username)).one_or_none()
    if not user:
        return None

    if check_password_hash(user.password, password):
        return user
    LOGGER.warning(f"User {username} not correctly authenticated")


@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, secret_token, algorithms=["HS256"])
    except Exception:
        LOGGER.exception("Unable to decode JWT")
        return None

    username = decoded_jwt["username"]
    user = db.session.scalars(select(User).where(User.username == username)).one_or_none()
    if user:
        return user
    LOGGER.error(f"Unknown user {username}")
    return None
