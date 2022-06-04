"""Create UserGroup

Revision ID: 52995a5190df
Revises: 565e8bc574ee
Create Date: 2022-06-04 23:28:41.292861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52995a5190df'
down_revision = '565e8bc574ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "usergroup",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("group_id", sa.Integer, sa.ForeignKey("group.id")),
    )


def downgrade() -> None:
    op.drop_table("usergroup")
