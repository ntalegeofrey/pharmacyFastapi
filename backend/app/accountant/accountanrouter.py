from fastapi import APIRouter

from models.accountantmodels import Accountant
from dto.accountantschema import AccountantSchema

from .accountantservice import AccountantService

router = APIRouter(prefix="/accountant", tags=["Accountant"])


@router.get("/")
def getAllAccountant():
    return AccountantService.getAll()


@router.post("/")
def createAccountant(request: AccountantSchema):
    return AccountantService.createaccountant(request=request)


@router.post('/{id}')
def updateAccountant(id: int, request: AccountantSchema):
    return AccountantService.updateaccountant(id=id,request=request)


@router.delete("/{id}")
def deleteAccountant(id: int):
    return AccountantService.deleteaccountant(id=id)