
import logging
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Response
from database.models.usersmodels import User
from dto.usersschema import UserCreateDto
from app.utils.token import get_currentUser
from sqlmodel import Session
from config.database import engine
from app.utils.hashing import Hashing

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def getMe(current_user: User = Depends(get_currentUser)):
    current_user.password = None
    response = {
        "status": "success",
        "data": current_user
    }
    logging.error("user: %s", current_user)

    return response

@router.get("/")
def GetAllUser():
    db = Session(engine)
    return db.query(User).all()

@router.get("/{email}")
def getEmail(email: str):
    db = Session(engine)
    user = db.query(User).where(User.email == email).first()
    
    response = {
        "status": "success",
        "data": user
    }

    return response


@router.get("/{id}")
def getUserid(id: int):
    db = Session(engine)

    query = db.query(User).where(User.id == id).all()

    response = {
        "status": "success",
        "data": query
    }

    return response


@router.post("/")
def createUser(user: UserCreateDto):
    db = Session(engine)
    get_email = db.query(User).where(User.email == user.email).first()

    if get_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exist")

    db_user = User(
            name=user.name, email=user.email, password=Hashing.bcrypt(user.password), is_active=user.is_active, is_staff=user.is_staff
    )
    db.add(db_user)
    db.commit()

    return Response(status_code=status.HTTP_201_CREATED, content="User created")


@router.put("/{id}")
def updateUser(id: int, user: UserCreateDto):
    db = Session(engine)
    get_email = db.query(User).where(User.email == user.email).first()

    if get_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exist")

    db_user = db.query(User).where(User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db_user.name = user.name
    db_user.email = user.email
    db_user.password = Hashing.bcrypt(user.password)
    db_user.is_active = user.is_active
    db_user.is_staff = user.is_staff

    db.commit()

    return Response(status_code=status.HTTP_200_OK, content="User updated")

@router.delete("/{id}")
def deleteUser(id: int):
    db = Session(engine)
    db_user = db.query(User).where(User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(db_user)
    db.commit()

    return Response(status_code=status.HTTP_200_OK, content="User deleted")



    