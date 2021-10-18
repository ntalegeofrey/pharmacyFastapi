from pydantic import BaseModel


class CreatePharmacy(BaseModel):
    name: str
    email: str
    password: str
    address: str
    phone: str

