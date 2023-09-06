from typing import Any, List, Union
from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/router",
)

class ResponseModel(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

# 응답 모델 지정하는 법 1
@router.post("/first-response-model")
async def create_item(response: ResponseModel) -> ResponseModel:
    return response
@router.get("/first-response-model")
async def read_items() -> List[ResponseModel]:
    return [
        ResponseModel(name="Portal Gun", price=42.0),
        ResponseModel(name="Plumbus", price=32.0),
    ]

# 응답 모델 지정하는 법 2
@router.post("/second-response-model", response_model=ResponseModel)
async def create_item(response: ResponseModel) -> Any:
    return response
@router.get("/second-response-model")
async def read_items() -> Any:
    return [
        ResponseModel(name="Portal Gun", price=42.0),
        ResponseModel(name="Plumbus", price=32.0),
    ]


# input, output 파라미터가 동일한 변수를 참조하더라도, 응답 모델이 다르면 해당 모델에 따른다.
@router.post("/response-model/user", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

# 하위의 경우 input 파라미터는 BaseUser + UserInIn 이다.
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
class UserInIn(BaseUser):
    password: str
@router.post("/response-model/user/test")
async def create_user(user: UserInIn) -> BaseUser:
    return user


# 원칙상 fast api에선 응답값을 Union으로 Response와 다른 모델을 함께 묶으면 안 된다.
# @router.get("/portal")
# async def get_portal(teleport: bool = False) -> Union[Response, dict]:
#     if teleport:
#         return RedirectResponse(url="https://www.google.com")
#     return {"message": "Here's your interdimensional portal."}
# Union으로 Response와 다른 모델을 함께 묶으려면 데코레이터에 response_model=None를 추가해야한다.
@router.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="https://www.google.com")
    return {"message": "Here's your interdimensional portal."}
# Union으로 Response와 다른 모델을 함께 묶으려면 데코레이터에 response_model=None를 추가해야한다.
@router.post("/portal", response_model=None)
async def get_portal(user: BaseUser, teleport: bool = False) -> Union[Response, BaseUser]:
    if teleport:
        return RedirectResponse(url="https://www.google.com")
    return user

