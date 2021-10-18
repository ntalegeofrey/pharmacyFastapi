from fastapi import APIRouter

from dto.expensesschema import ExpenseCategorySchema

from .exgroupservice import ExGroupService

router = APIRouter(prefix="/expense-group", tags=["ExpenseGroup"])


@router.get("/")
def getAll():
    return ExGroupService.getAll()


@router.post("/")
def createExGroup(request: ExpenseCategorySchema):
    return ExGroupService.createExGroup(request=request)


@router.post("/{id}")
def updateExGroup(id: int, request: ExpenseCategorySchema):
    return ExGroupService.updateExGroup(id=id, request=request)


@router.delete("/{id}")
def deleteExGroup(id: int):
    return ExGroupService.deleteExGroup(id=id)
