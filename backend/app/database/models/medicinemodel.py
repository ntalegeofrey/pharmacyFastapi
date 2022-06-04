from typing import Optional
from sqlalchemy import table
from sqlmodel import Field, SQLModel

class Medicine(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    category: str
    price: str
    box: str
    s_price: str
    quantity: str
    generic: str
    company: str
    effects: str
    pharmacy_id: int = Field(default=None, foreign_key="pharmacy.id")

class MedicineCategory(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    category: str
    description: str
    pharmacy_id: int = Field(default=None, foreign_key="pharmacy.id")

