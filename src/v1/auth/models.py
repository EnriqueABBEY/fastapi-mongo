from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str


class UserInDb(User):
    password: str


class TokenData(BaseModel):
    username: str = None
    _id: str = None


# validations schemas
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class UserCreateSchema(User):
    password: str


class UserLoginSchema(BaseModel):
    username: str
    password: str


class LoginResponseSchema(BaseModel):
    user: User
    tokens: TokenResponse
    
class RegisterResponseSchema(BaseModel):
    status: bool
