from typing import Optional
from sqlmodel import SQLModel, Field


class Settings(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    system_vendor: str
    title: str
    address: str
    phone: str
    email: str
    facebook_id: str
    curreny: str
    discount: str
    vat: str
    codec_username: str
    codec_purchase_code: str
    pharmacy_id: int
