from sqlmodel import Session
from config.database import engine
from models.expensesmodels import Expenses
from dto.expensesschema import ExpensesSchema


class ExpensesService:
    def getAllExpenses():
        db = Session(engine)

        return db.query(Expenses).all()

    def createExpense(request: ExpensesSchema):
        db = Session(engine)
        db_cr = Expenses(
            category=request.category,
            date=request.date,
            amount=request.amount,
            user_id=request.user_id,
            pharmacy_id=request.pharmacy_id,
        )

        db.add(db_cr)
        db.commit()

        return "Bisa"

    def updateExpense(id: int, request: ExpensesSchema):
        db = Session(engine)
        db_id = db.query(Expenses).filter(Expenses.id == id).first()

        db_id.category = request.category
        db_id.date = request.date
        db_id.amount = request.amount
        db_id.user_id = request.user_id
        db_id.pharmacy_id = request.pharmacy_id

        db.commit()

        return "Update Expense"

    def deleteExpense(id: int):
        db = Session(engine)
        db_id = db.query(Expenses).filter(Expenses.id == id).first()

        db.delete(db_id)

        return "Delete Expense"

