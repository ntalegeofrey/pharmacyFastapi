from fastapi import APIRouter
from dto.payschema import PaymentSchema
from .payservice import PayService
from models.paymentmodels import Payment


router = APIRouter(prefix="/payment", tags=["Payment"])


@router.get("/")
def getAll():
    return PayService.getAll()


@router.post("/")
def createPay(request: PaymentSchema):
    return PayService.createPay(request=request)


@router.post("/{id}")
def updatePay(id: int, request: PaymentSchema):
    return PayService.updatePay(id=id, request=request)


@router.delete("/{id}")
def deletePay(id: int):
    return PayService.deletePay(id=id)
