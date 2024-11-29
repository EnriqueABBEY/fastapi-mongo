from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError
import jwt
from .models import (
    LoginResponseSchema,
    RegisterResponseSchema,
    UserCreateSchema,
    UserLoginSchema,
)
from .services import (
    ALGORITHM,
    SECRET_KEY,
    create_user,
    create_access_token,
    create_refresh_token,
    get_user,
    verify_password,
)

router = APIRouter()
OAUTH_SCHEME = HTTPBearer()


@router.post("/register", response_model=RegisterResponseSchema)
def register(user: UserCreateSchema):
    if get_user(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    create_user(user)
    return {
        "status": True,
    }


@router.post("/login", response_model=LoginResponseSchema)
async def login(body: UserLoginSchema):
    try:
        user = get_user(body.username)
        if not user or not verify_password(body.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        access_token = create_access_token(data={"sub": user.username})
        refresh_token = create_refresh_token(data={"sub": user.username})
        return {
            "user": user,
            "tokens": {
                "access_token": access_token,
                "token_type": "bearer",
                "refresh_token": refresh_token,
            },
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/me", response_model=UserCreateSchema)
def read_users_me(token: dict = Depends(OAUTH_SCHEME)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = get_user(username)
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user


@router.post("/logout")
def logout():
    # Logique pour gérer la déconnexion (par exemple, supprimer le refresh_token)
    return {"msg": "Déconnexion réussie"}
