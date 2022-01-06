from flask import Blueprint, jsonify
from sqlalchemy import select

from backend import db
from backend.models.group import Group

groups_bp = Blueprint("groups", __name__, url_prefix="/groups")


@groups_bp.route("", methods=["GET"])
def get_all_groups():
    # style 1.x
    # groups = Group.query.all()

    # style 2.0
    groups = db.session.scalars(select(Group)).all()
    return jsonify([{"name": g.name for g in groups}])
