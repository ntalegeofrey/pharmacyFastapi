from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database.models.usersmodels import User, UserGroup, Group
from config.database import engine
from dto.usersschema import UserGroupSchema

router = APIRouter(prefix="/usergroup", tags=["UserGroup"])


@router.get("/")
def GetAllUserGroup():
    db = Session(engine)
    query = db.query(UserGroup).join(User, UserGroup.user_id == User.id).join(Group, UserGroup.group_id == Group.id).all()
    response = {
        "status": "success",
        "data": query
    }
    return response

@router.post("/")
def createUserGroup(userGroup: UserGroupSchema):
    db = Session(engine)

    get_Group = db.query(Group).where(Group.id == userGroup.group_id).first()
    if not get_Group:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group not found")

    get_userGroup = db.query(User).filter(User.id == userGroup.user_id).first()

    if not get_userGroup:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist")

    db_userGroup = UserGroup(
        user_id=userGroup.user_id, group_id=userGroup.group_id
    )
    db.add(db_userGroup)
    db.commit()

    response = {
        "status": "success",
    }

    return response

@router.get("/{id}")
def getUserGroupid(id: int):
    db = Session(engine)

    query = db.query(UserGroup).where(UserGroup.id == id).all()

    if not query:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="UserGroup not found")

    response = {
        "status": "success",
        "data": query
    }

    return response


@router.put("/{id}")
def updateUserGroup(id: int, userGroup: UserGroupSchema):
    db = Session(engine)
    get_userGroup = db.query(UserGroup).where(UserGroup.id == id).first()

    if not get_userGroup:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="UserGroup not found")

    get_userGroup.user_id = userGroup.user_id
    get_userGroup.group_id = userGroup.group_id

    response = {
        "status": "success",
        "data": get_userGroup
    }

    return response

@router.delete("/{id}")
def deleteUserGroup(id: int):
    db = Session(engine)
    get_userGroup = db.query(UserGroup).where(UserGroup.id == id).first()

    if not get_userGroup:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="UserGroup not found")

    db.delete(get_userGroup)
    db.commit()

    response = {
        "status": "success",
    }

    return response