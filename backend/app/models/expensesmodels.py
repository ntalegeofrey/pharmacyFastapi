from typing import Optional
from sqlalchemy.sql.expression import table
from sqlmodel import Field, SQLModel


class Expenses(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    date: str
    amount: str
    user_id: int
    pharmacy_id: int


class ExpenseCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    description: str
