"""create country table

Revision ID: 5d011ccf390c
Revises:
Create Date: 2022-09-20 21:29:50.338494

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
from backend.models import country_table_name

revision = "5d011ccf390c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        country_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("code", sa.String(2), unique=True, nullable=False),
        sa.Column("name", sa.String(50), unique=True, nullable=False),
    )


def downgrade() -> None:
    op.drop_table(country_table_name)
