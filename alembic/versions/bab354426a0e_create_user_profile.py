"""create user profile

Revision ID: bab354426a0e
Revises: f5e2b6df626f
Create Date: 2022-09-20 22:28:25.639361

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
from backend.models import message_table_name, profile_table_name, user_table_name

revision = "bab354426a0e"
down_revision = "f5e2b6df626f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        profile_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("birth_date", sa.DateTime),
        sa.Column("job", sa.String(100)),
        sa.Column("user_id", sa.Integer),
    )
    op.create_foreign_key("fk_profile_user_id", profile_table_name, user_table_name, ["user_id"], ["id"])

    op.create_table(
        message_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("content", sa.Text, nullable=False),
        sa.Column("created", sa.DateTime(timezone=True)),
        sa.Column("user_id", sa.Integer, nullable=False),
    )
    op.create_foreign_key("fk_message_user_id", message_table_name, user_table_name, ["user_id"], ["id"])


def downgrade() -> None:
    op.drop_table(message_table_name)
    op.drop_table(profile_table_name)
