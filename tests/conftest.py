import pytest
from sqlalchemy import delete
from werkzeug.security import generate_password_hash

from backend import create_app, db, User, Country


@pytest.fixture(scope="session")
def flask_app():
    app = create_app()

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture(scope="session")
def app_with_db(flask_app):
    db.create_all()

    yield flask_app

    db.session.commit()
    db.drop_all()


@pytest.fixture
def app_with_data(app_with_db):
    country = Country()
    country.code = "FR"
    country.name = "France"
    db.session.add(country)

    user = User()
    user.username = "sergio"
    user.password = generate_password_hash("pass")
    user.email = "sergio@mail.com"
    db.session.add(user)

    db.session.commit()

    yield app_with_db

    db.session.execute(delete(User))
    db.session.execute(delete(Country))
    db.session.commit()
