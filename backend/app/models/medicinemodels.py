from typing import Optional
from sqlmodel import Field, SQLModel

class Medicine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    price: str
    box: str
    s_price: str
    quantity: str
    generic: str
    company: str
    effects: str
    e_date: str
    created_at: str
    pharmacy_id: int

class MedicineCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    description: str
    pharmacy_id: int
