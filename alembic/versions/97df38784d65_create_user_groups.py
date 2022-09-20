"""create user groups

Revision ID: 97df38784d65
Revises: f5e2b6df626f
Create Date: 2022-09-20 22:26:43.095951

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
from backend.models import group_table_name, user_table_name

revision = "97df38784d65"
down_revision = "f5e2b6df626f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        group_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(20), unique=True, nullable=False),
    )

    op.create_table(
        "users_to_groups_assocation",
        sa.Column("user_id", sa.Integer, primary_key=True),
        sa.Column("group_id", sa.Integer, primary_key=True),
    )
    op.create_foreign_key(
        "fk_users_to_groups_assocation_user_id", "users_to_groups_assocation", user_table_name, ["user_id"], ["id"]
    )
    op.create_foreign_key(
        "fk_users_to_groups_assocation_group_id", "users_to_groups_assocation", group_table_name, ["group_id"], ["id"]
    )


def downgrade() -> None:
    op.drop_table("users_to_groups_assocation")
    op.drop_table(group_table_name)
