from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database.models.medicinemodel import MedicineCategory
from config.database import engine

router = APIRouter(prefix="/medicine", tags=["Medicine"])

@router.get("/")
def GetAllMedicineCategory():
    db = Session(engine)
    query = db.query(MedicineCategory).all()
    response = {
        "status": "success",
        "data": query
    }
    return response


@router.get("/{id}")
def getMedicineCategoryid(id: int):
    db = Session(engine)

    query = db.query(MedicineCategory).where(MedicineCategory.id == id).first()

    response = {
        "status": "success",
        "data": query
    }

    return response


@router.post("/")
def createMedicineCategory(medicineCategory: MedicineCategory):
    db = Session(engine)
    get_medicineCategory = db.query(MedicineCategory).where(MedicineCategory.name == medicineCategory.name).first()

    if get_medicineCategory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MedicineCategory already exist")

    db_medicineCategory = MedicineCategory(
        name=medicineCategory.name, description=medicineCategory.description
    )
    db.add(db_medicineCategory)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.put("/{id}")
def updateMedicineCategory(id: int, medicineCategory: MedicineCategory):
    db = Session(engine)

    get_medicineCategory = db.query(MedicineCategory).where(MedicineCategory.id == medicineCategory.id).first()

    if not get_medicineCategory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MedicineCategory already exist")

    get_medicineCategory.name = medicineCategory.name
    get_medicineCategory.description = medicineCategory.description
    get_medicineCategory.pharmacy_id = medicineCategory.pharmacy_id

    db.commit()

    response = {
        "status": "success",
    }
    return response


@router.delete("/{id}")
def deleteMedicineCategory(id: int):
    db = Session(engine)
    get_medicineCategory = db.query(MedicineCategory).where(MedicineCategory.id == id).first()

    if not get_medicineCategory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MedicineCategory already exist")

    db.delete(get_medicineCategory)
    db.commit()

    response = {
        "status": "success",
    }
    return response