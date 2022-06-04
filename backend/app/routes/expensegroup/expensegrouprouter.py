from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database.models.expensemodel import Expense
from dto.expensesschema import ExpenseCategorySchema
from config.database import engine

router = APIRouter(prefix="/expensegroup", tags=["ExpenseGroup"])

@router.get("/")
def GetAllExpenseGroup():
    db = Session(engine)
    query = db.query(Expense).all()
    response = {
        "status": "success",
        "data": query
    }
    return response


@router.post("/")
def createExpenseGroup(expense: ExpenseCategorySchema):
    db = Session(engine)
    get_expense = db.query(Expense).where(Expense.name == expense.name).first()

    if get_expense:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expense already exist")

    db_expense = Expense(
        name=expense.name, description=expense.description
    )
    db.add(db_expense)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.put("/{id}")
def updateExpenseGroup(id: int, expense: ExpenseCategorySchema):
    db = Session(engine)
    db_id = db.query(Expense).filter(Expense.id == id).first()

    if not db_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expense not found")

    db_id.category = expense.category
    db_id.date = expense.date
    db_id.amount = expense.amount
    db_id.user_id = expense.user_id
    db_id.pharmacy_id = expense.pharmacy_id

    db.commit()

    response = {
        "status": "success",
        "data": db_id
    }

    return response

@router.delete("/{id}")
def deleteExpenseGroup(id: int):
    db = Session(engine)
    db_id = db.query(Expense).filter(Expense.id == id).first()

    if not db_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expense not found")

    db.delete(db_id)
    db.commit()

    response = {
        "status": "success",
    }

    return response