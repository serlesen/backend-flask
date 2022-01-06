from marshmallow import Schema, fields, post_load, validates, ValidationError
import re

from backend.models.user import User


class UserCreationSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)

    @validates("password")
    def validates_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must longer than 8")
        if not any(char.isupper() for char in value):
            raise ValidationError("Password must contain upper case")
        if not any(char.islower() for char in value):
            raise ValidationError("Password must contain lower case")

    @validates("email")
    def validates_email(self, value):
        if not re.match("[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError("Invalid email format")

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)