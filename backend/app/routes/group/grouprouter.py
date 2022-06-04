
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database.models.usersmodels import Group
from dto.usersschema import GroupSchema
from config.database import engine

router = APIRouter(prefix="/group", tags=["Group"])


@router.get("/")
def GetAllGroup():
    db = Session(engine)
    query = db.query(Group).all()
    response = {
        "status": "success",
        "data": query
    }
    return response


@router.get("/{id}")
def getGroupid(id: int):
    db = Session(engine)

    query = db.query(Group).where(Group.id == id).all()

    response = {
        "status": "success",
        "data": query
    }

    return response

@router.post("/")
def createGroup(group: GroupSchema):
    db = Session(engine)
    get_group = db.query(Group).where(Group.name == group.name).first()

    if get_group:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group already exist")

    db_group = Group(
        name=group.name, description=group.description
    )
    db.add(db_group)
    db.commit()

    response = {
        "status": "success",
    }

    return response


@router.put("/{id}")
def updateGroup(id: int, group: GroupSchema):
    db = Session(engine)
    get_group = db.query(Group).where(Group.id == id).first()

    if not get_group:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group not found")

    get_group.name = group.name
    get_group.description = group.description
    db.commit()

    response = {
        "status": "success",
        "data": get_group
    }

    return response

@router.delete("/{id}")
def deleteGroup(id: int):
    db = Session(engine)
    get_group = db.query(Group).where(Group.id == id).first()

    if not get_group:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group not found")

    db.delete(get_group)
    db.commit()
    return Response(status_code=status.HTTP_200_OK, content="Group deleted")