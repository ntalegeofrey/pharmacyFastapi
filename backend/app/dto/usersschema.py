from typing import Optional, List
from pydantic import BaseModel
from .pharmacyschema import CreatePharmacy

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]


class UserList(BaseModel):
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]
    pharmacy = CreatePharmacy


class GroupSchema(BaseModel):
    name: str
    description: str


class UserGroupSchema(BaseModel):
    user_id: int
    group_id: int
