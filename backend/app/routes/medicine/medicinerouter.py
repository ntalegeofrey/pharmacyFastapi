from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from dto.medicschema import MedicineSchema
from database.models.medicinemodel import Medicine
from config.database import engine

router = APIRouter(prefix="/medicine", tags=["Medicine"])

@router.get("/")
def GetAllMedicine():
    db = Session(engine)
    query = db.query(Medicine).all()
    response = {
        "status": "success",
        "data": query
    }
    return response

@router.get("/{id}")
def getMedicineid(id: int):
    db = Session(engine)

    query = db.query(Medicine).where(Medicine.id == id).first()

    response = {
        "status": "success",
        "data": query
    }

    return response


@router.post("/")
def createMedicine(medicine: MedicineSchema):
    db = Session(engine)
    get_medicine = db.query(Medicine).where(Medicine.name == medicine.name).first()

    if get_medicine:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Medicine already exist")

    db_medicine = Medicine(
        name=medicine.name, description=medicine.description
    )
    db.add(db_medicine)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.put("/{id}")
def updateMedicine(id: int, medicine: MedicineSchema):
    db = Session(engine)
    get_medicine = db.query(Medicine).where(Medicine.id == id).first()

    if get_medicine:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Medicine already exist")

    db_medicine = Medicine(
        name=medicine.name, description=medicine.description
    )
    db.add(db_medicine)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.delete("/{id}")
def deleteMedicine(id: int):
    db = Session(engine)
    get_medicine = db.query(Medicine).where(Medicine.id == id).first()

    if not get_medicine:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Medicine not found")

    db.delete(get_medicine)
    db.commit()

    response = {
        "status": "success",
    }

    return response
    