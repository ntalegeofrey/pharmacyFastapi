"""Create User

Revision ID: fbe1e59a96a9
Revises: 
Create Date: 2022-06-04 23:26:40.845663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbe1e59a96a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("email", sa.String(length=255), unique=True),
        sa.Column("password", sa.String(length=255)),
        sa.Column("address", sa.String(length=255)),
        sa.Column("phone", sa.String(length=255)),

    )


def downgrade() -> None:
    op.drop_table("user")
