from fastapi import FastAPI
from config.database import create_table
from users import usersrouter
from auth import authrouter
from pharmacy import pharmacyrouter
from group import grouprouter
from usergroup import usergrouprouter
from accountant import accountanrouter
from expenses import expensesrouter
from expensegroup import exgrouprouter
from medicine import medicrouter
from payment import payrouter

app = FastAPI()


@app.on_event("startup")
async def table_all():
    create_table()


@app.get("/")
def Hello():
    return "Hello"


app.include_router(usersrouter.router)
app.include_router(authrouter.router)

app.include_router(pharmacyrouter.router)

app.include_router(grouprouter.router)

app.include_router(usergrouprouter.router)

app.include_router(accountanrouter.router)
app.include_router(expensesrouter.router)
app.include_router(exgrouprouter.router)
app.include_router(medicrouter.router)

app.include_router(payrouter.router)