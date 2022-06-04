from sqlmodel import create_engine
from sqlmodel.main import SQLModel



SQLALCHAMY_DATABASE_URL = "sqlite:///./pharmacy.db"
engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def create_table():
    SQLModel.metadata.create_all(engine)
