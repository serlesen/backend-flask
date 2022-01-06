from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema, SQLAlchemySchema
from sqlalchemy.orm import relationship

from backend import db
from backend.models import user_table_name, profile_table_name
from backend.models.country import Country


class User(db.Model):
    __tablename__ = user_table_name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    country_id = db.Column(db.Integer, db.ForeignKey(Country.id))

    country = relationship(Country.__name__)
    profile = relationship("Profile", uselist=False, back_populates="user")


class Profile(db.Model):
    __tablename__ = profile_table_name

    id = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.DateTime)
    job = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    user = relationship(User.__name__, uselist=False, back_populates="profile")


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    id = auto_field()
    username = auto_field()
    email = auto_field()


class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        include_relationships = True
        load_instance = True
