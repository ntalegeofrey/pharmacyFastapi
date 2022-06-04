from datetime import datetime, timedelta
import logging
from jwt import PyJWTError
import jwt
from sqlmodel import Session
from database.models.usersmodels import User
from ..config.database import engine
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logging.info("Ini message".format(encoded_jwt))
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    db = Session(engine)
    try:
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception
        token_data = email
    except PyJWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == token_data).first()

    logging.info("Ini message".format(user))

    if not user:
        raise credentials_exception

    return user


def get_currentUser(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token=data, credentials_exception=credentials_exception)
