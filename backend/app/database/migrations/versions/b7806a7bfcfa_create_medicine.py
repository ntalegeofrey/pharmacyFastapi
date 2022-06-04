"""Create Medicine

Revision ID: b7806a7bfcfa
Revises: f0dfc15a7b17
Create Date: 2022-06-04 23:30:30.099956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7806a7bfcfa'
down_revision = 'f0dfc15a7b17'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "medicine",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("category", sa.String(length=255)),
        sa.Column("price", sa.String(length=255)),
        sa.Column("box", sa.String(length=255)),
        sa.Column("s_price", sa.String(length=255)),
        sa.Column("quantity", sa.String(length=255)),
        sa.Column("generic", sa.String(length=255)),
        sa.Column("company", sa.String(length=255)),
        sa.Column("effects", sa.String(length=255)),
        sa.Column("pharmacy_id", sa.Integer, sa.ForeignKey("pharmacy.id")),
    )


def downgrade() -> None:
    op.drop_table("medicine")
