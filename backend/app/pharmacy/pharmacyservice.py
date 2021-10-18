from models.usersmodels import User
from sqlmodel import Session
from config.database import engine
from models.pharmacymodels import Pharmacy
from dto.pharmacyschema import CreatePharmacy


class PharmacyService:
    def getAll():
        db = Session(engine)

        return db.query(Pharmacy).all()

    def createpharmacy(current_user: User, pharmacy: CreatePharmacy):
        db = Session(engine)
        db_user = db.query(User).filter(User.email == current_user.email).first()

        db_create = Pharmacy(
            name=pharmacy.name,
            email=pharmacy.email,
            password=pharmacy.password,
            address=pharmacy.address,
            phone=pharmacy.phone
        )
        print(db_user)
        db_create.users = db_user
        db.add(db_create)
        db.commit()

        return db_create


