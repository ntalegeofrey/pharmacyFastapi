from config.database import engine
from models.expensesmodels import ExpenseCategory
from sqlmodel import Session

from dto.expensesschema import ExpenseCategorySchema


class ExGroupService:
    def getAll():
        db = Session(engine)
        return db.query(ExpenseCategory).all()

    def createExGroup(request: ExpenseCategorySchema):
        db = Session(engine)

        db_create = ExpenseCategory(
            category=request.category, description=request.description
        )

        db.add(db_create)
        db.commit()

        return "Create Expense Category"

    def updateExGroup(id: int, request: ExpenseCategorySchema):
        db = Session(engine)
        db_id = db.query(ExpenseCategory).filter(ExpenseCategory.id == id).first()

        db_id.category = request.category
        db_id.description = request.description

        db.commit()

        return "Update Expense Category"


    def deleteExGroup(id: int):
        db = Session(engine)
        db_id = db.query(ExpenseCategory).filter(ExpenseCategory.id == id).first()

        db.delete(db_id)
        db.commit()

        return "Delete Expense Category"

