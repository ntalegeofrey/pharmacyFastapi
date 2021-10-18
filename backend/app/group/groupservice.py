from dto.usersschema import GroupSchema
from models.usersmodels import Group
from config.database import engine
from sqlmodel import Session
from models.usersmodels import Group

class GroupService:
    def getAll():
        db = Session(engine)
        return db.query(Group).all()

    def creategroup(request: GroupSchema):
        db = Session(engine)
        group_create = Group(name=request.name,description=request.description)

        db.add(group_create)
        db.commit()


        return "Bisa"

    def updateGroup(id: int, request: GroupSchema):
        db = Session(engine)
        db_groupid = db.query(Group).filter(Group.id == id).first()

        db_groupid.name = request.name
        db_groupid.description = request.description

        db.commit()

        return "Update"

    def deleteGroup(id: int):
        db = Session(engine)
        db_groupid = db.query(Group).filter(Group.id == id).first()
        db.delete(db_groupid)

        return "Delete"


