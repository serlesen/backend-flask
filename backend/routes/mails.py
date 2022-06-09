from flask import Blueprint, render_template
from sqlalchemy import select

from backend import db
from backend.models.message import Message, MessageSchema
from backend.routes import token_auth

mails_bp = Blueprint("mails", __name__)
message_schema = MessageSchema()


@mails_bp.route("/mails/summary", methods=["GET"])
@token_auth.login_required  # type: ignore
def summary_mail():

    navigation_items = [
        {"url": "localhost:5000/messages", "label": "Home"},
        {"url": "localhost:5000/groups", "label": "Groups"},
        {"url": "localhost:5000/users", "label": "Users"},
    ]

    current_user = token_auth.current_user()
    messages = db.session.scalars(
        select(Message).where(Message.user_id == current_user.id).order_by(Message.created)
    ).all()

    return render_template(
        "summary_mail.html.jinja",
        title="Summary",
        description="Summary of the last week",
        user=current_user,
        navigation_items=navigation_items,
        messages=message_schema.dump(messages, many=True),
    )
