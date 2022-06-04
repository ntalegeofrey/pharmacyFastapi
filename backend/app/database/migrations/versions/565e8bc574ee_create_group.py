"""Create Group

Revision ID: 565e8bc574ee
Revises: fbe1e59a96a9
Create Date: 2022-06-04 23:28:10.411877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565e8bc574ee'
down_revision = 'fbe1e59a96a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "group",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("description", sa.String(length=255)),
    )


def downgrade() -> None:
    op.drop_table("group")
