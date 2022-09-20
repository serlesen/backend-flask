"""create user tables

Revision ID: f5e2b6df626f
Revises: 5d011ccf390c
Create Date: 2022-09-20 21:33:49.765415

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
from backend.models import country_table_name, user_table_name

revision = "f5e2b6df626f"
down_revision = "5d011ccf390c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        user_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(80), unique=True, nullable=False),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("email", sa.String(120), unique=True, nullable=False),
        sa.Column("country_id", sa.Integer),
    )
    op.create_foreign_key("fk_user_country_id", user_table_name, country_table_name, ["country_id"], ["id"])


def downgrade() -> None:
    op.drop_table(user_table_name)
