from datetime import timedelta
from fastapi import APIRouter
from .models import UserCreateScema
from .services import create_user

router = APIRouter()


@router.post("/register", response_model=UserCreateScema)
def register_user(user: UserCreateScema):
    create_user(user)
    return user