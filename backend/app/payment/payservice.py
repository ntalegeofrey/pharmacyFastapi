from config.database import engine
from sqlmodel import Session
from models.paymentmodels import Payment
from dto.payschema import PaymentSchema

#


class PayService:
    def getAll():
        db = Session(engine)
        return db.query(Payment).all()

    def createPay(request: PaymentSchema):
        db = Session(engine)
        db_create = Payment(
            category=request.category,
            client_id=request.client_id,
            doctor=request.doctor,
            date=request.date,
            amount=request.amount,
            vat=request.vat,
            x_ray=request.x_ray,
            flat=request.flat,
            discount=request.discount,
            flat_discount=request.discount,
            gross_total=request.gross_total,
            hospital_amount=request.hospital_amount,
            doctor_amount=request.doctor_amount,
            category_amount=request.category_amount,
            category_name=request.category_name,
            amount_received=request.amount_received,
            status=request.status,
            pharmacy_id=request.pharmacy_id,
        )

        db.add(db_create)
        db.commit()

        return "Create"

    def updatePay(id: int, request: PaymentSchema):
        db = Session(engine)

        db_id = db.query(Payment).filter(Payment.id == id).first()

        db_id.category = request.category
        db_id.client_id = request.client_id
        db_id.doctor = request.doctor
        db_id.date = request.date
        db_id.amount = request.amount
        db_id.vat = request.vat
        db_id.x_ray = request.x_ray
        db_id.flat = request.flat
        db_id.discount = request.discount
        db_id.flat_discount = request.discount
        db_id.gross_total = request.gross_total
        db_id.hospital_amount = request.hospital_amount
        db_id.doctor_amount = request.doctor_amount
        db_id.category_amount = request.category_amount
        db_id.category_name = request.category_name
        db_id.amount_received = request.amount_received
        db_id.status = request.status
        db_id.pharmacy_id = request.pharmacy_id

        db.commit()

        return "Update"

    def deletePay(id: int):
        db = Session(engine)

        db_id = db.query(Payment).filter(Payment.id == id).first()

        db.delete(db_id)

        return "Delete Payment"
