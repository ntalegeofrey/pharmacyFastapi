from fastapi import APIRouter
from dto.medicschema import MedicineSchema

from .medicservice import MedicService


router = APIRouter(prefix="/medicine", tags=["Medcine"])


@router.get("/")
def getAll():
    return MedicService.getAll()


@router.post("/")
def createMedicine(request: MedicineSchema):
    return MedicService.createMedic(request=request)


@router.post("/{id}")
def updateMedicine(id: int, request: MedicineSchema):
    return MedicService.updateMedic(id=id, request=request)


@router.delete("/{id}")
def deleteMedicine(id: int):
    return MedicService.deleteMedic(id=id)
