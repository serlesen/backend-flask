from flask import Flask
from werkzeug.security import generate_password_hash

from backend.extensions import db
from backend.routes.groups import groups_bp
from backend.routes.health import health_bp
from backend.routes.auth import auth_bp
from backend.routes.errors import error_bp
from backend.routes.users import users_bp

from sqlalchemy import insert, select

from backend.models.country import Country
from backend.models.group import Group
from backend.models.message import Message
from backend.models.user import User, Profile


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sergio:my-password@localhost:5432/backenddb"

    db.app = app
    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(groups_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)

    return app


def feed_db():
    nb_countries = db.session.scalar(select(db.func.count(Country.id)))
    if nb_countries > 0:
        return

    db.session.execute(insert(Country).values(code="ES", name="Spain"))

    country = db.session.scalars(select(Country).where(Country.name == "Spain")).one()
    db.session.execute(insert(User).values(
        username="sergio",
        email="sergio@mail.com",
        password=generate_password_hash("my-password"),
        country_id=country.id))
    db.session.execute(insert(User).values(
        username="john",
        email="john@mail.com",
        password=generate_password_hash("his-password"),
        country_id=country.id))

    user = db.session.scalars(select(User).where(User.username == "sergio")).one()
    db.session.execute(insert(Message).values(content="This is my first post", user_id=user.id))
    db.session.execute(insert(Message).values(content="This is my second post", user_id=user.id))

    db.session.execute(insert(Profile).values(job="developer", user_id=user.id))

    db.session.execute(insert(Group).values(name="Art"))
    db.session.execute(insert(Group).values(name="Cars"))

    group = db.session.scalars(select(Group).where(Group.name == "Cars")).one()

    user.groups = [group]
    db.session.commit()
