from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel
from sqlmodel.main import Relationship

if TYPE_CHECKING:
    from .pharmacymodels import Pharmacy


class Group(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: str
    group_user: Optional["UserGroup"] = Relationship(back_populates="group")


class UserGroup(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="usergroup")
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")
    group: Optional["Group"] = Relationship(back_populates="group_user")

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]
    pharmacy: List["Pharmacy"] = Relationship(back_populates="users")
    usergroup: List["UserGroup"] = Relationship(back_populates="user")



# from sqlalchemy import Column, Integer, String, ForeignKey
# from config.database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)
