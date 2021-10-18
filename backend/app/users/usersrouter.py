from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.usersmodels import User
from dto.usersschema import RegisterUser
from .usersservice import UserService
from config.token import get_currentUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/')
def GetAllUser():
    return UserService.getAll()

@router.post("/")
def createUser(user: RegisterUser):
    return UserService.create_user(user)

@router.get('/{id}')
def getUserid(id: int):
    return UserService.getById(id=id)

@router.get("/me")
def getMe(current_user: User = Depends(get_currentUser)):
    return current_user
