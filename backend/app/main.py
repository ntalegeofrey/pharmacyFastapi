import uvicorn
from fastapi import FastAPI
from config.database import create_table
from routes.users import usersroutes
from routes.auth import authrouter
from routes.group import grouprouter
from routes.usergroup import usergrouprouter
from routes.pharmacy import pharmacyrouter
from routes.medicine import medicinerouter
from routes.medicinecategory import medicategory
from routes.accountant import accountantrouter


app = FastAPI()


@app.on_event("startup")
async def table_all():
    create_table()


@app.get("/")
def Hello():
    return "Hello"

app.include_router(authrouter.router)
app.include_router(usersroutes.router)
app.include_router(grouprouter.router)
app.include_router(usergrouprouter.router)
app.include_router(pharmacyrouter.router)
app.include_router(medicinerouter.router)
app.include_router(medicategory.router)
app.include_router(accountantrouter.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)