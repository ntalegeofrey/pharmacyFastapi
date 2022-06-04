"""Create Pharmacy

Revision ID: f0dfc15a7b17
Revises: 52995a5190df
Create Date: 2022-06-04 23:29:25.972731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0dfc15a7b17'
down_revision = '52995a5190df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "pharmacy",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("address", sa.String(length=255)),
        sa.Column("phone", sa.String(length=255)),
        sa.Column("email", sa.String(length=255), unique=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
    )


def downgrade() -> None:
    op.drop_table("pharmacy")
