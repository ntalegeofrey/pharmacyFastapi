from pydantic import BaseModel


class AccountantSchema(BaseModel):
    img_url: str
    name: str
    address: str
    phone: str
    ion_user_id: int
    pharmacy_id: int
