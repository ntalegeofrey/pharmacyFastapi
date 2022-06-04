"""Create Account

Revision ID: d0b6b496ba5b
Revises: fbfa1475f816
Create Date: 2022-06-04 23:37:10.699769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0b6b496ba5b'
down_revision = 'fbfa1475f816'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "accountant",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("img_url", sa.String(length=255)),
        sa.Column("name", sa.String(length=255)),
        sa.Column("address", sa.String(length=255)),
        sa.Column("phone", sa.String(length=255)),
        sa.Column("ion_user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("pharmacy_id", sa.Integer, sa.ForeignKey("pharmacy.id")),
    )


def downgrade() -> None:
    op.drop_table("accountant")
