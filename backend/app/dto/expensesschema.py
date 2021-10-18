from pydantic import BaseModel


class ExpensesSchema(BaseModel):
    category: str
    date: str
    amount: str
    user_id: int
    pharmacy_id: int


class ExpenseCategorySchema(BaseModel):
    category: str
    description: str
