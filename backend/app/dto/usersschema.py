from typing import Optional, List
from pydantic import BaseModel
from .pharmacyschema import PharmacySchema

class UserSchema(BaseModel):
    id: Optional[int]
    name: str
    email: str
    is_active: Optional[bool]
    is_staff: Optional[bool]

class UserCreateDto(UserSchema):
    password: str


class UserList(UserSchema):
    pharmacy = PharmacySchema


class GroupSchema(BaseModel):
    name: str
    description: str


class UserGroupSchema(BaseModel):
    user_id: int
    group_id: int
