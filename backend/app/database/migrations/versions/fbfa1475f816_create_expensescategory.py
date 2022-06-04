"""Create ExpensesCategory

Revision ID: fbfa1475f816
Revises: 04aca5784276
Create Date: 2022-06-04 23:34:36.083245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbfa1475f816'
down_revision = '04aca5784276'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Table(
        "expensecategory",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("category", sa.String(length=255)),
        sa.Column("description", sa.String(length=255)),
    )


def downgrade() -> None:
    op.drop_table("expensecategory")
