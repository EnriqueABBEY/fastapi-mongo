from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


#validations schemas
class UserCreateScema(User):
    password: str