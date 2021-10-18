from fastapi import APIRouter

from dto.usersschema import UserGroupSchema

from .usergroupservice import UserGroupService


router = APIRouter(prefix="/users-group", tags=["UserGroup"])


@router.get("/")
def getAll():
    return UserGroupService.getAll()


@router.post("/")
def createUserGroup(request: UserGroupSchema):
    return UserGroupService.createusergroup(request=request)


@router.get("/{id}")
def showUserGroup(id: int):
    return UserGroupService.showusergroup(id=id)


@router.post("/{id}")
def updateUserGroup(id: int, request: UserGroupSchema):
    return UserGroupService.updateusergroup(id=id, request=request)


@router.delete("/{id}")
def deleteUserGroup(id: int):
    return UserGroupService.deleteusergroup(id=id)
