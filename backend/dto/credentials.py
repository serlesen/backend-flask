from marshmallow import Schema, fields, post_load

from backend.models.user import User


class CredentialsSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
