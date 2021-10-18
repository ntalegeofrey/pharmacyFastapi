from sqlmodel import Session
from config.database import engine
from dto.medicschema import MedicineSchema
from models.medicinemodels import Medicine
from datetime import datetime


class MedicService:
    def getAll():
        db = Session(engine)

        return db.query(Medicine).all()

    def createMedic(request: MedicineSchema):
        db = Session(engine)

        db_create = Medicine(
            name=request.name,
            category=request.category,
            price=request.price,
            box=request.box,
            s_price=request.s_price,
            quantity=request.quantity,
            generic=request.generic,
            company=request.company,
            effects=request.effects,
            e_date=request.e_date,
            created_at=datetime.now(),
            pharmacy_id=request.pharmacy_id,
        )

        db.add(db_create)
        db.commit()

        return "Create Medic"

    def updateMedic(id: int, request: MedicineSchema):
        db = Session(engine)
        db_id = db.query(Medicine).filter(Medicine.id == id).first()

        db_id.name = request.name
        db_id.category = request.category
        db_id.price = request.price
        db_id.box = request.box
        db_id.s_price = request.s_price
        db_id.quantity = request.quantity
        db_id.generic = request.generic
        db_id.company = request.company
        db_id.effects = request.effects
        db_id.e_date = request.e_date
        db_id.created_at = datetime.now()
        db_id.pharmacy_id = request.pharmacy_id

        db.commit()

        return "Update Medic"

    def deleteMedic(id: int):
        db = Session(engine)
        db_id = db.query(Medicine).filter(Medicine.id == id).first()

        db.delete(db_id)
        db.commit()

        return "Delete Medic"
