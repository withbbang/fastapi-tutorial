from fastapi import APIRouter, Form
from typing_extensions import Annotated

router = APIRouter(
    prefix="/router",
)

# Tip: OAuth2를 사용하기 위해선 Form Field는 필수이다. (JSON X)
# 파라미터에 form 선언을 하지 않을 경우, fast api는 파라미터를 json 혹은 query 파라미터로 인식한다.
@router.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password": password}