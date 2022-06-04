from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database.models.accountantmodel import Accountant
from database.models.pharmacymodel import Pharmacy
from dto.accountantschema import AccountantSchema
from config.database import engine

router = APIRouter(prefix="/accountant", tags=["Accountant"])

@router.get("/")
def GetAllAccountant():
    db = Session(engine)
    query = db.query(Accountant).join(Pharmacy.id == Accountant.pharmacy_id).all()
    response = {
        "status": "success",
        "data": query
    }
    return response


@router.post("/")
def createAccountant(accountant: AccountantSchema):
    db = Session(engine)
    get_accountant = db.query(Accountant).where(Accountant.name == accountant.name).first()

    if get_accountant:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Accountant already exist")

    db_accountant = Accountant(
        name=accountant.name, address=accountant.address, phone=accountant.phone, img_url=accountant.img_url, ion_user_id=accountant.ion_user_id, pharmacy_id=accountant.pharmacy_id
    )
    db.add(db_accountant)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.put("/{id}")
def updateAccountant(id: int, accountant: AccountantSchema):
    db = Session(engine)
    db_id = db.query(Accountant).filter(Accountant.id == id).first()

    if not db_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Accountant not found")

    db_id.name = accountant.name
    db_id.address = accountant.address
    db_id.phone = accountant.phone
    db_id.img_url = accountant.img_url
    db_id.ion_user_id = accountant.ion_user_id
    db_id.pharmacy_id = accountant.pharmacy_id

    db.commit()

    response = {
        "status": "success",
        "data": db_id
    }

    return response


@router.delete("/{id}")
def deleteAccountant(id: int):
    db = Session(engine)
    db_id = db.query(Accountant).filter(Accountant.id == id).first()

    if not db_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Accountant not found")

    db.delete(db_id)
    db.commit()

    response = {
        "status": "success",
    }

    return response