from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from backend import db
from backend.models import country_table_name


class Country(db.Model):
    __tablename__ = country_table_name

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)


class CountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        include_relationships = True
        load_instance = True
