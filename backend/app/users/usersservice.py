
from models.pharmacymodels import Pharmacy
from config.database import engine

from models.usersmodels import User
from sqlmodel import Session
from dto.usersschema import RegisterUser, UserList


from config.hashing import Hashing


class UserService:
    def get_user(email: str):
        db = Session(engine)
        return db.query(User).filter(User.email == email).first()

    def getAll():
        db = Session(engine)
        return db.query(User).all()

    def getById(id: int):
        db = Session(engine)
        db_userid = db.query(User).filter(User.id == id).first()
        db.commit()
        
        db_pharmacy = db.query(Pharmacy).filter(Pharmacy.users_id == id).all()
        
        list_us = {
            "name": db_userid.name,
            "email": db_userid.email,
            "password": db_userid.password,
            "is_active": db_userid.is_active,
            "is_staff": db_userid.is_staff,
            "pharmacy": db_pharmacy
        }



        return list_us


    def create_user(user: RegisterUser):
        db = Session(engine)
        db_user = User(
            name=user.name, email=user.email, password=Hashing.bcrypt(user.password)
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return db_user
