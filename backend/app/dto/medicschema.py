from pydantic import BaseModel


class MedicineSchema(BaseModel):
    name: str
    category: str
    price: str
    box: str
    s_price: str
    quantity: str
    generic: str
    company: str
    effects: str
    e_date: str
    pharmacy_id: int
