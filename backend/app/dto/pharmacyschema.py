from pydantic import BaseModel


class PharmacySchema(BaseModel):
    name: str
    email: str
    password: str
    address: str
    phone: str
    user_id: int

