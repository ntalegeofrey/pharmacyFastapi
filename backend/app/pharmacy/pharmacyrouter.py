from fastapi import APIRouter, Depends

from dto.pharmacyschema import CreatePharmacy
from .pharmacyservice import PharmacyService
from models.usersmodels import User
from config.token import get_currentUser


router = APIRouter(prefix="/pharmacy", tags=["Pharmacy"])

@router.get("/")
def getAll():
    return PharmacyService.getAll()


@router.post('/')
def createPharmacy(pharmacy: CreatePharmacy,current_user: User = Depends(get_currentUser)):
    return PharmacyService.createpharmacy(current_user=current_user, pharmacy=pharmacy)