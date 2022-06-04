from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database.models.pharmacymodel import Pharmacy, User
from dto.pharmacyschema import PharmacySchema
from config.database import engine

router = APIRouter(prefix="/pharmacy", tags=["Pharmacy"])

@router.get("/")
def GetAllPharmacy():
    db = Session(engine)
    query = db.query(Pharmacy).join(User, Pharmacy.user_id == User.id).all()
    response = {
        "status": "success",
        "data": query
    }
    return response

@router.get("/{id}")
def getPharmacyid(id: int):
    db = Session(engine)

    query = db.query(Pharmacy).where(Pharmacy.id == id).all()

    response = {
        "status": "success",
        "data": query
    }

    return response

@router.post("/")
def createPharmacy(pharmacy: PharmacySchema):
    db = Session(engine)
    get_pharmacy = db.query(Pharmacy).filter(Pharmacy.name == pharmacy.name).first()
    

    if get_pharmacy:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pharmacy already exist")

    db_pharmacy = Pharmacy(
        name=pharmacy.name, address=pharmacy.address, phone=pharmacy.phone,email=pharmacy.email,user_id=pharmacy.user_id
    )
    db.add(db_pharmacy)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.put("/{id}")
def updatePharmacy(id: int, pharmacy: PharmacySchema):
    db = Session(engine)
    get_pharmacy = db.query(Pharmacy).where(Pharmacy.id == id).first()

    if not get_pharmacy:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pharmacy not found exist")

    get_pharmacy.name = pharmacy.name
    get_pharmacy.address = pharmacy.address
    get_pharmacy.phone = pharmacy.phone
    get_pharmacy.email = pharmacy.email

    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.delete("/{id}")
def deletePharmacy(id: int):
    db = Session(engine)
    get_pharmacy = db.query(Pharmacy).where(Pharmacy.id == id).first()

    if not get_pharmacy:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pharmacy not found exist")

    db.delete(get_pharmacy)

    response = {
        "status": "success",
    }

    return response