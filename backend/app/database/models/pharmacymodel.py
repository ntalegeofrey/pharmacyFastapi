from typing import Optional
from sqlmodel import SQLModel
from sqlmodel.main import Field, Relationship
from .usersmodels import User

class Pharmacy(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    address: str
    phone: str
    email: str
    user_id: int = Field(default=None, foreign_key="user.id")
    users: Optional[User] = Relationship(back_populates="pharmacy")