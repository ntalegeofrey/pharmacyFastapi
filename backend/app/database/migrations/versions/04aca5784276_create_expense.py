"""Create Expense

Revision ID: 04aca5784276
Revises: 7b2c18bee298
Create Date: 2022-06-04 23:34:28.747742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04aca5784276'
down_revision = '7b2c18bee298'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "expenses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date", sa.DateTime, nullable=False),
        sa.Column("amount", sa.String(length=255), nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("pharmacy_id", sa.Integer, sa.ForeignKey("pharmacy.id")),
    )


def downgrade() -> None:
    op.drop_table("expenses")
