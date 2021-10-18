
from typing import Optional
from sqlmodel import SQLModel
from sqlmodel.main import Field, Relationship
from .usersmodels import User


class Pharmacy(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    address: str
    phone: str
    users_id: Optional[int] = Field(default=None, foreign_key="user.id")
    users: Optional[User] = Relationship(back_populates="pharmacy") 