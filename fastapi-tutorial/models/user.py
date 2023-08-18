from typing import Union
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str