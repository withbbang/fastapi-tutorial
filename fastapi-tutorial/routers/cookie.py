from typing import Union
from fastapi import APIRouter, Cookie
from typing_extensions import Annotated

router = APIRouter(
    prefix="/router",
)

# 파라미터에 쿠키 설정시, 해당 값은 쿠키로 설정된다.
@router.get("/cookie")
async def cookie(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}