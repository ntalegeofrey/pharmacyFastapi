from fastapi import APIRouter
from dto.expensesschema import ExpensesSchema
from .expensesservice import ExpensesService


router = APIRouter(prefix="/expense", tags=["Expenses"])


@router.get("/")
def getAll():
    return ExpensesService.getAllExpenses()


@router.post("/")
def createExpense(request: ExpensesSchema):
    return ExpensesService.createExpense(request=request)


@router.post("/{id}")
def updateExpense(id: int, request: ExpensesSchema):
    return ExpensesService.updateExpense(id=id, request=request)


@router.delete("/{id}")
def deleteExpense(id: int):
    return ExpensesService.deleteExpense(id=id)
