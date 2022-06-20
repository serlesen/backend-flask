from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy.orm import relationship

from backend import db
from backend.models import message_table_name
from backend.models.user import User


class Message(db.Model):
    __tablename__ = message_table_name

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)  # type: ignore

    user = relationship(User.__name__, backref="messages", cascade="all")


class MessageSchema(SQLAlchemySchema):
    class Meta:
        model = Message
        include_relationships = True
        load_instance = True

    id = auto_field()
    content = auto_field()
    author = fields.Method("serialize_user")
    date = fields.Method("serialize_date")

    def serialize_date(self, message):
        return message.created.strftime("%Y-%m-%d %H:%M:%S")

    def serialize_user(self, message):
        return {"url": f"localhost:5000/users/{message.user.id}", "label": f"{message.user.username}"}
