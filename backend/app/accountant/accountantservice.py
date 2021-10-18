from sqlmodel import Session
from config.database import engine
from models.accountantmodels import Accountant
from dto.accountantschema import AccountantSchema


class AccountantService:
    def getAll():
        db = Session(engine)
        return db.query(Accountant).all()

    def createaccountant(request: AccountantSchema):
        db = Session(engine)
        db_create = Accountant(
            img_url=request.img_url,
            name=request.name,
            address=request.address,
            phone=request.phone,
            ion_user_id=request.ion_user_id,
            pharmacy_id=request.pharmacy_id,
        )

        db.add(db_create)

        db.commit()

        return "Bisa"

    def updateaccountant(id: int, request: AccountantSchema):
        db = Session(engine)
        db_id = db.query(Accountant).filter(Accountant.id == id).first()

        db_id.img_url = request.img_url
        db_id.name = request.name
        db_id.address = request.address
        db_id.phone = request.phone
        db_id.ion_user_id = request.ion_user_id
        db_id.pharmacy_id = request.pharmacy_id

        db.commit(db_id)

        return "Update"

    
    def deleteaccountant(id: int):
        db = Session(engine)
        db_id = db.query(Accountant).filter(Accountant.id == id).first()

        db.delete(db_id)

        db.commit()

        return "Delete"

