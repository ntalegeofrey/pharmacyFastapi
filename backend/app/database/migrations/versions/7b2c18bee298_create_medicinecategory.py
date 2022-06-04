"""Create MedicineCategory

Revision ID: 7b2c18bee298
Revises: b7806a7bfcfa
Create Date: 2022-06-04 23:32:54.150450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b2c18bee298'
down_revision = 'b7806a7bfcfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "medicinecategory",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("category", sa.String(length=255)),
        sa.Column("description", sa.String(length=255)),
        sa.Column("pharmacy_id", sa.Integer, sa.ForeignKey("pharmacy.id")),
    )


def downgrade() -> None:
    op.drop_table("medicinecategory")
