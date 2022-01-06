import jwt

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from sqlalchemy import select
from werkzeug.security import check_password_hash

from backend import db
from backend.models.user import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

secret_token = "mysecret"


@basic_auth.verify_password
def verify_basic_password(username, password):
    user = db.session.scalars(select(User).where(User.username == username)).one_or_none()
    if not user:
        return None

    if check_password_hash(user.password, password):
        return username


@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, secret_token, algorithms=["HS256"])
    except Exception as e:
        return None

    user = db.session.scalars(select(User).where(User.username == decoded_jwt["username"])).one_or_none()
    if user:
        return decoded_jwt["username"]
    return None

