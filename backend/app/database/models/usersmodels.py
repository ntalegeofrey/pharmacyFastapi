from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel
from sqlmodel.main import Relationship

if TYPE_CHECKING:
    from .pharmacymodel import Pharmacy


class Group(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: str
    user_group: Optional["UserGroup"] = Relationship(back_populates="group")


class UserGroup(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    group_id: int = Field(default=None, foreign_key="group.id")
    group: Optional["Group"] = Relationship(back_populates="user_group")

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]
    pharmacy: List["Pharmacy"] = Relationship(back_populates="user")

