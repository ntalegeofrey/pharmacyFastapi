from models.usersmodels import UserGroup, Group, User
from sqlmodel import Session
from config.database import engine
from dto.usersschema import UserGroupSchema


class UserGroupService:
    def getAll():
        db = Session(engine)

        return db.query(UserGroup).all()

    def createusergroup(request: UserGroupSchema):
        db = Session(engine)
        db_group = db.query(Group).filter(Group.id == request.group_id).first()
        db_user = db.query(Group).filter(User.id == request.user_id).first()

        db_create = UserGroup(user_id=db_user.id, group_id=db_group.id)
        db.add(db_create)
        db.commit()

        return "Bisa coy"

    def showusergroup(id: int):
        db = Session(engine)
        db_usergroup = db.query(UserGroup).filter(UserGroup.id == id).first()
        db_group = db.query(Group).filter(Group.id == db_usergroup.group_id).all()
        db_user = db.query(User).filter(User.id == db_usergroup.user_id).all()

        res = {"group": db_group, "users": db_user}

        return res

    def updateusergroup(id: int, request: UserGroupSchema):
        db = Session(engine)
        db_usergroup = db.query(UserGroup).filter(UserGroup.id == id).first()
        db_group = db.query(Group).filter(Group.id == request.group_id).first()
        db_user = db.query(Group).filter(User.id == request.user_id).first()

        db_usergroup.user_id = db_user.id
        db_usergroup.group_id = db_group.id

        db.commit()

        return "Update"

    def deleteusergroup(id: int):
        db = Session(engine)
        db_usergroup = db.query(UserGroup).filter(UserGroup.id == id).first()

        db.delete(db_usergroup)

        db.commit()

        return "Delete user group"
