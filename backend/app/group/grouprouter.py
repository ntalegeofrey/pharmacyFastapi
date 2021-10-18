from fastapi import APIRouter

from dto.usersschema import GroupSchema
from .groupservice import GroupService

router = APIRouter(prefix="/groups", tags=["Groups"])

@router.get("/")
def GetAllGroup():
    return GroupService.getAll()

@router.post("/")
def createGroup(request: GroupSchema):
    return GroupService.creategroup(request=request)


@router.put("/{id}")
def updateGroup(id: int, request: GroupSchema):
    return GroupService.updateGroup(id=id,request=request)


@router.delete("/{id}")
def deleteGroup(id: int):
    return GroupService.deleteGroup(id=id)
