from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from src.database import get_database

from .models import UserCreateScema

SECRET_KEY = "1222122020393894847484940200293984932029383845765749430"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 60

db = get_database()
users_collection = db["users"]


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(username: str) -> UserCreateScema:
    user_data = users_collection.find_one({"username": username})
    if user_data:
        return UserCreateScema(**user_data)
    return None


def create_user(user: UserCreateScema):
    users_collection.insert_one(user.dict())
