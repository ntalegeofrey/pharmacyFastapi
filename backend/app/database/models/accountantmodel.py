from typing import Optional
from sqlmodel import SQLModel, Field


class Accountant(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    img_url: str
    name: str
    address: str
    phone: str
    ion_user_id: int
    pharmacy_id: int